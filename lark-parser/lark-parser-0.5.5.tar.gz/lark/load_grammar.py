"Parses and creates Grammar objects"

import os.path
from itertools import chain
import re
from ast import literal_eval
from copy import deepcopy

from .lexer import Token, UnexpectedInput

from .parse_tree_builder import ParseTreeBuilder
from .parser_frontends import LALR
from .parsers.lalr_parser import UnexpectedToken
from .common import is_terminal, GrammarError, LexerConf, ParserConf, PatternStr, PatternRE, TokenDef
from .grammar import RuleOptions, Rule

from .tree import Tree as T, Transformer, InlineTransformer, Visitor

__path__ = os.path.dirname(__file__)
IMPORT_PATHS = [os.path.join(__path__, 'grammars')]

_RE_FLAGS = 'imslux'

_TOKEN_NAMES = {
    '.' : 'DOT',
    ',' : 'COMMA',
    ':' : 'COLON',
    ';' : 'SEMICOLON',
    '+' : 'PLUS',
    '-' : 'MINUS',
    '*' : 'STAR',
    '/' : 'SLASH',
    '\\' : 'BACKSLASH',
    '|' : 'VBAR',
    '?' : 'QMARK',
    '!' : 'BANG',
    '@' : 'AT',
    '#' : 'HASH',
    '$' : 'DOLLAR',
    '%' : 'PERCENT',
    '^' : 'CIRCUMFLEX',
    '&' : 'AMPERSAND',
    '_' : 'UNDERSCORE',
    '<' : 'LESSTHAN',
    '>' : 'MORETHAN',
    '=' : 'EQUAL',
    '"' : 'DBLQUOTE',
    '\'' : 'QUOTE',
    '`' : 'BACKQUOTE',
    '~' : 'TILDE',
    '(' : 'LPAR',
    ')' : 'RPAR',
    '{' : 'LBRACE',
    '}' : 'RBRACE',
    '[' : 'LSQB',
    ']' : 'RSQB',
    '\n' : 'NEWLINE',
    '\r\n' : 'CRLF',
    '\t' : 'TAB',
    ' ' : 'SPACE',
}

# Grammar Parser
TOKENS = {
    '_LPAR': r'\(',
    '_RPAR': r'\)',
    '_LBRA': r'\[',
    '_RBRA': r'\]',
    'OP': '[+*][?]?|[?](?![a-z])',
    '_COLON': ':',
    '_OR': r'\|',
    '_DOT': r'\.',
    'TILDE': '~',
    'RULE': '!?[_?]?[a-z][_a-z0-9]*',
    'TOKEN': '_?[A-Z][_A-Z0-9]*',
    'STRING': r'"(\\"|\\\\|[^"\n])*?"i?',
    'REGEXP': r'/(?!/)(\\/|\\\\|[^/\n])*?/[%s]*' % _RE_FLAGS,
    '_NL': r'(\r?\n)+\s*',
    'WS': r'[ \t]+',
    'COMMENT': r'//[^\n]*',
    '_TO': '->',
    '_IGNORE': r'%ignore',
    '_IMPORT': r'%import',
    'NUMBER': r'\d+',
}

RULES = {
    'start': ['_list'],
    '_list':  ['_item', '_list _item'],
    '_item':  ['rule', 'token', 'statement', '_NL'],

    'rule': ['RULE _COLON expansions _NL',
             'RULE _DOT NUMBER _COLON expansions _NL'],
    'expansions': ['alias',
                   'expansions _OR alias',
                   'expansions _NL _OR alias'],

    '?alias':     ['expansion _TO RULE', 'expansion'],
    'expansion': ['_expansion'],

    '_expansion': ['', '_expansion expr'],

    '?expr': ['atom',
              'atom OP',
              'atom TILDE NUMBER',
              'atom TILDE NUMBER _DOT _DOT NUMBER',
              ],

    '?atom': ['_LPAR expansions _RPAR',
             'maybe',
             'name',
             'literal',
             'range'],

    '?name': ['RULE', 'TOKEN'],

    'maybe': ['_LBRA expansions _RBRA'],
    'range': ['STRING _DOT _DOT STRING'],

    'token': ['TOKEN _COLON expansions _NL',
              'TOKEN _DOT NUMBER _COLON expansions _NL'],
    'statement': ['ignore', 'import'],
    'ignore': ['_IGNORE expansions _NL'],
    'import': ['_IMPORT import_args _NL',
               '_IMPORT import_args _TO TOKEN'],
    'import_args': ['_import_args'],
    '_import_args': ['name', '_import_args _DOT name'],

    'literal': ['REGEXP', 'STRING'],
}


class EBNF_to_BNF(InlineTransformer):
    def __init__(self):
        self.new_rules = []
        self.rules_by_expr = {}
        self.prefix = 'anon'
        self.i = 0
        self.rule_options = None

    def _add_recurse_rule(self, type_, expr):
        if expr in self.rules_by_expr:
            return self.rules_by_expr[expr]

        new_name = '__%s_%s_%d' % (self.prefix, type_, self.i)
        self.i += 1
        t = Token('RULE', new_name, -1)
        tree = T('expansions', [T('expansion', [expr]), T('expansion', [t, expr])])
        self.new_rules.append((new_name, tree, self.rule_options))
        self.rules_by_expr[expr] = t
        return t

    def expr(self, rule, op, *args):
        if op.value == '?':
            return T('expansions', [rule, T('expansion', [])])
        elif op.value == '+':
            # a : b c+ d
            #   -->
            # a : b _c d
            # _c : _c c | c;
            return self._add_recurse_rule('plus', rule)
        elif op.value == '*':
            # a : b c* d
            #   -->
            # a : b _c? d
            # _c : _c c | c;
            new_name = self._add_recurse_rule('star', rule)
            return T('expansions', [new_name, T('expansion', [])])
        elif op.value == '~':
            if len(args) == 1:
                mn = mx = int(args[0])
            else:
                mn, mx = map(int, args)
                if mx < mn:
                    raise GrammarError("Bad Range for %s (%d..%d isn't allowed)" % (rule, mn, mx))
            return T('expansions', [T('expansion', [rule] * n) for n in range(mn, mx+1)])
        assert False, op


class SimplifyRule_Visitor(Visitor):

    @staticmethod
    def _flatten(tree):
        while True:
            to_expand = [i for i, child in enumerate(tree.children)
                         if isinstance(child, T) and child.data == tree.data]
            if not to_expand:
                break
            tree.expand_kids_by_index(*to_expand)

    def expansion(self, tree):
        # rules_list unpacking
        # a : b (c|d) e
        #  -->
        # a : b c e | b d e
        #
        # In AST terms:
        # expansion(b, expansions(c, d), e)
        #   -->
        # expansions( expansion(b, c, e), expansion(b, d, e) )

        while True:
            self._flatten(tree)

            for i, child in enumerate(tree.children):
                if isinstance(child, T) and child.data == 'expansions':
                    tree.data = 'expansions'
                    tree.children = [self.visit(T('expansion', [option if i==j else other
                                                                for j, other in enumerate(tree.children)]))
                                     for option in set(child.children)]
                    break
            else:
                break

    def alias(self, tree):
        rule, alias_name = tree.children
        if rule.data == 'expansions':
            aliases = []
            for child in tree.children[0].children:
                aliases.append(T('alias', [child, alias_name]))
            tree.data = 'expansions'
            tree.children = aliases

    def expansions(self, tree):
        self._flatten(tree)
        tree.children = list(set(tree.children))


class RuleTreeToText(Transformer):
    def expansions(self, x):
        return x
    def expansion(self, symbols):
        return [sym.value for sym in symbols], None
    def alias(self, x):
        (expansion, _alias), alias = x
        assert _alias is None, (alias, expansion, '-', _alias)
        return expansion, alias.value


class CanonizeTree(InlineTransformer):
    def maybe(self, expr):
        return T('expr', [expr, Token('OP', '?', -1)])

    def tokenmods(self, *args):
        if len(args) == 1:
            return list(args)
        tokenmods, value = args
        return tokenmods + [value]

class ExtractAnonTokens(InlineTransformer):
    "Create a unique list of anonymous tokens. Attempt to give meaningful names to them when we add them"

    def __init__(self, tokens):
        self.tokens = tokens
        self.token_set = {td.name for td in self.tokens}
        self.token_reverse = {td.pattern: td for td in tokens}
        self.i = 0


    def pattern(self, p):
        value = p.value
        if p in self.token_reverse and p.flags != self.token_reverse[p].pattern.flags:
            raise GrammarError(u'Conflicting flags for the same terminal: %s' % p)

        if isinstance(p, PatternStr):
            try:
                # If already defined, use the user-defined token name
                token_name = self.token_reverse[p].name
            except KeyError:
                # Try to assign an indicative anon-token name, otherwise use a numbered name
                try:
                    token_name = _TOKEN_NAMES[value]
                except KeyError:
                    if value.isalnum() and value[0].isalpha() and ('__'+value.upper()) not in self.token_set:
                        token_name = '%s%d' % (value.upper(), self.i)
                        try:
                            # Make sure we don't have unicode in our token names
                            token_name.encode('ascii')
                        except UnicodeEncodeError:
                            token_name = 'ANONSTR_%d' % self.i
                    else:
                        token_name = 'ANONSTR_%d' % self.i
                    self.i += 1

                token_name = '__' + token_name

        elif isinstance(p, PatternRE):
            if p in self.token_reverse: # Kind of a wierd placement.name
                token_name = self.token_reverse[p].name
            else:
                token_name = 'ANONRE_%d' % self.i
                self.i += 1
        else:
            assert False, p

        if token_name not in self.token_set:
            assert p not in self.token_reverse
            self.token_set.add(token_name)
            tokendef = TokenDef(token_name, p)
            self.token_reverse[p] = tokendef
            self.tokens.append(tokendef)

        return Token('TOKEN', token_name, -1)


def _rfind(s, choices):
    return max(s.rfind(c) for c in choices)



def _fix_escaping(s):
    w = ''
    i = iter(s)
    for n in i:
        w += n
        if n == '\\':
            n2 = next(i)
            if n2 == '\\':
                w += '\\\\'
            elif n2 not in 'unftr':
                w += '\\'
            w += n2
    w = w.replace('\\"', '"').replace("'", "\\'")

    to_eval = "u'''%s'''" % w
    try:
        s = literal_eval(to_eval)
    except SyntaxError as e:
        raise ValueError(s, e)

    return s


def _literal_to_pattern(literal):
    v = literal.value
    flag_start = _rfind(v, '/"')+1
    assert flag_start > 0
    flags = v[flag_start:]
    assert all(f in _RE_FLAGS for f in flags), flags

    v = v[:flag_start]
    assert v[0] == v[-1] and v[0] in '"/'
    x = v[1:-1]

    s = _fix_escaping(x)

    if v[0] == '"':
        s = s.replace('\\\\', '\\')

    return { 'STRING': PatternStr,
             'REGEXP': PatternRE }[literal.type](s, flags)


class PrepareLiterals(InlineTransformer):
    def literal(self, literal):
        return T('pattern', [_literal_to_pattern(literal)])

    def range(self, start, end):
        assert start.type == end.type == 'STRING'
        start = start.value[1:-1]
        end = end.value[1:-1]
        assert len(start) == len(end) == 1, (start, end, len(start), len(end))
        regexp = '[%s-%s]' % (start, end)
        return T('pattern', [PatternRE(regexp)])

class SplitLiterals(InlineTransformer):
    def pattern(self, p):
        if isinstance(p, PatternStr) and len(p.value)>1:
            return T('expansion', [T('pattern', [PatternStr(ch, flags=p.flags)]) for ch in p.value])
        return T('pattern', [p])

class TokenTreeToPattern(Transformer):
    def pattern(self, ps):
        p ,= ps
        return p

    def expansion(self, items):
        if len(items) == 1:
            return items[0]
        if len({i.flags for i in items}) > 1:
            raise GrammarError("Lark doesn't support joining tokens with conflicting flags!")
        return PatternRE(''.join(i.to_regexp() for i in items), items[0].flags)

    def expansions(self, exps):
        if len(exps) == 1:
            return exps[0]
        if len({i.flags for i in exps}) > 1:
            raise GrammarError("Lark doesn't support joining tokens with conflicting flags!")
        return PatternRE('(?:%s)' % ('|'.join(i.to_regexp() for i in exps)), exps[0].flags)

    def expr(self, args):
        inner, op = args[:2]
        if op == '~':
            if len(args) == 3:
                op = "{%d}" % int(args[2])
            else:
                mn, mx = map(int, args[2:])
                if mx < mn:
                    raise GrammarError("Bad Range for %s (%d..%d isn't allowed)" % (inner, mn, mx))
                op = "{%d,%d}" % (mn, mx)
        else:
            assert len(args) == 2
        return PatternRE('(?:%s)%s' % (inner.to_regexp(), op), inner.flags)


def _interleave(l, item):
    for e in l:
        yield e
        if isinstance(e, T):
            if e.data in ('literal', 'range'):
                yield item
        elif is_terminal(e):
            yield item

def _choice_of_rules(rules):
    return T('expansions', [T('expansion', [Token('RULE', name)]) for name in rules])

class Grammar:
    def __init__(self, rule_defs, token_defs, ignore):
        self.token_defs = token_defs
        self.rule_defs = rule_defs
        self.ignore = ignore

    def _prepare_scanless_grammar(self, start):
        # XXX Pretty hacky! There should be a better way to write this method..

        rule_defs = deepcopy(self.rule_defs)
        term_defs = self.token_defs

        # Implement the "%ignore" feature without a lexer..
        terms_to_ignore = {name:'__'+name for name in self.ignore}
        if terms_to_ignore:
            assert set(terms_to_ignore) <= {name for name, _t in term_defs}

            term_defs = [(terms_to_ignore.get(name,name),t) for name,t in term_defs]
            expr = Token('RULE', '__ignore')
            for r, tree, _o in rule_defs:
                for exp in tree.find_data('expansion'):
                    exp.children = list(_interleave(exp.children, expr))
                    if r == start:
                        exp.children = [expr] + exp.children
                for exp in tree.find_data('expr'):
                    exp.children[0] = T('expansion', list(_interleave(exp.children[:1], expr)))

            _ignore_tree = T('expr', [_choice_of_rules(terms_to_ignore.values()), Token('OP', '?')])
            rule_defs.append(('__ignore', _ignore_tree, None))

        # Convert all tokens to rules
        new_terminal_names = {name: '__token_'+name for name, _t in term_defs}

        for name, tree, options in rule_defs:
            for exp in chain( tree.find_data('expansion'), tree.find_data('expr') ):
                for i, sym in enumerate(exp.children):
                    if sym in new_terminal_names:
                        exp.children[i] = Token(sym.type, new_terminal_names[sym])

        for name, (tree, priority) in term_defs:   # TODO transfer priority to rule?
            if name.startswith('_'):
                options = RuleOptions(filter_out=True, priority=-priority)
            else:
                options = RuleOptions(keep_all_tokens=True, create_token=name, priority=-priority)

            name = new_terminal_names[name]
            inner_name = name + '_inner'
            rule_defs.append((name, _choice_of_rules([inner_name]), None))
            rule_defs.append((inner_name, tree, options))

        return [], rule_defs


    def compile(self, lexer=False, start=None):
        if not lexer:
            token_defs, rule_defs = self._prepare_scanless_grammar(start)
        else:
            token_defs = list(self.token_defs)
            rule_defs = self.rule_defs

        # =================
        #  Compile Tokens
        # =================

        # Convert token-trees to strings/regexps
        transformer = PrepareLiterals() * TokenTreeToPattern()
        tokens = [TokenDef(name, transformer.transform(token_tree), priority)
                  for name, (token_tree, priority) in token_defs]

        # =================
        #  Compile Rules
        # =================

        # 1. Pre-process terminals
        transformer = PrepareLiterals()
        if not lexer:
            transformer *= SplitLiterals()
        transformer *= ExtractAnonTokens(tokens)   # Adds to tokens

        # 2. Convert EBNF to BNF (and apply step 1)
        ebnf_to_bnf = EBNF_to_BNF()
        rules = []
        for name, rule_tree, options in rule_defs:
            ebnf_to_bnf.rule_options = RuleOptions(keep_all_tokens=True) if options and options.keep_all_tokens else None
            tree = transformer.transform(rule_tree)
            rules.append((name, ebnf_to_bnf.transform(tree), options))
        rules += ebnf_to_bnf.new_rules

        assert len(rules) == len({name for name, _t, _o in rules}), "Whoops, name collision"

        # 3. Compile tree to Rule objects
        rule_tree_to_text = RuleTreeToText()

        simplify_rule = SimplifyRule_Visitor()
        compiled_rules = []
        for name, tree, options in rules:
            simplify_rule.visit(tree)
            expansions = rule_tree_to_text.transform(tree)

            for expansion, alias in expansions:
                if alias and name.startswith('_'):
                    raise Exception("Rule %s is marked for expansion (it starts with an underscore) and isn't allowed to have aliases (alias=%s)" % (name, alias))

                rule = Rule(name, expansion, alias, options)
                compiled_rules.append(rule)

        return tokens, compiled_rules, self.ignore



_imported_grammars = {}
def import_grammar(grammar_path):
    if grammar_path not in _imported_grammars:
        for import_path in IMPORT_PATHS:
            with open(os.path.join(import_path, grammar_path)) as f:
                text = f.read()
            grammar = load_grammar(text, grammar_path)
            _imported_grammars[grammar_path] = grammar

    return _imported_grammars[grammar_path]


def resolve_token_references(token_defs):
    # TODO Cycles detection
    # TODO Solve with transitive closure (maybe)

    token_dict = {k:t for k, (t,_p) in token_defs}
    assert len(token_dict) == len(token_defs), "Same name defined twice?"

    while True:
        changed = False
        for name, (token_tree, _p) in token_defs:
            for exp in chain(token_tree.find_data('expansion'), token_tree.find_data('expr')):
                for i, item in enumerate(exp.children):
                    if isinstance(item, Token):
                        if item.type == 'RULE':
                            raise GrammarError("Rules aren't allowed inside tokens (%s in %s)" % (item, name))
                        if item.type == 'TOKEN':
                            exp.children[i] = token_dict[item]
                            changed = True
        if not changed:
            break

def options_from_rule(name, *x):
    if len(x) > 1:
        priority, expansions = x
        priority = int(priority)
    else:
        expansions ,= x
        priority = None

    keep_all_tokens = name.startswith('!')
    name = name.lstrip('!')
    expand1 = name.startswith('?')
    name = name.lstrip('?')

    return name, expansions, RuleOptions(keep_all_tokens, expand1, priority=priority)

class GrammarLoader:
    def __init__(self):
        tokens = [TokenDef(name, PatternRE(value)) for name, value in TOKENS.items()]

        rules = [options_from_rule(name, x) for name, x in RULES.items()]
        rules = [Rule(r, x.split(), None, o) for r, xs, o in rules for x in xs]
        callback = ParseTreeBuilder(rules, T).create_callback()
        lexer_conf = LexerConf(tokens, ['WS', 'COMMENT'])

        parser_conf = ParserConf(rules, callback, 'start')
        self.parser = LALR(lexer_conf, parser_conf)

        self.canonize_tree = CanonizeTree()

    def load_grammar(self, grammar_text, name='<?>'):
        "Parse grammar_text, verify, and create Grammar object. Display nice messages on error."

        try:
            tree = self.canonize_tree.transform( self.parser.parse(grammar_text+'\n') )
        except UnexpectedInput as e:
            raise GrammarError("Unexpected input %r at line %d column %d in %s" % (e.context, e.line, e.column, name))
        except UnexpectedToken as e:
            if e.expected == ['_COLON']:
                raise GrammarError("Missing colon at line %s column %s" % (e.line, e.column))
            elif e.expected == ['RULE']:
                raise GrammarError("Missing alias at line %s column %s" % (e.line, e.column))
            elif 'STRING' in e.expected:
                raise GrammarError("Expecting a value at line %s column %s" % (e.line, e.column))
            elif e.expected == ['_OR']:
                raise GrammarError("Newline without starting a new option (Expecting '|') at line %s column %s" % (e.line, e.column))
            raise

        # Extract grammar items

        token_defs = [c.children for c in tree.children if c.data=='token']
        rule_defs = [c.children for c in tree.children if c.data=='rule']
        statements = [c.children for c in tree.children if c.data=='statement']
        assert len(token_defs) + len(rule_defs) + len(statements) == len(tree.children)

        token_defs = [td if len(td)==3 else (td[0], 1, td[1]) for td in token_defs]

        token_defs = [(name.value, (t, int(p))) for name, p, t in token_defs]

        # Execute statements
        ignore = []
        for (stmt,) in statements:
            if stmt.data == 'ignore':
                t ,= stmt.children
                ignore.append(t)
            elif stmt.data == 'import':
                dotted_path = stmt.children[0].children
                name = stmt.children[1] if len(stmt.children)>1 else dotted_path[-1]
                grammar_path = os.path.join(*dotted_path[:-1]) + '.g'
                g = import_grammar(grammar_path)
                token_options = dict(g.token_defs)[dotted_path[-1]]
                assert isinstance(token_options, tuple) and len(token_options)==2
                token_defs.append([name.value, token_options])
            else:
                assert False, stmt


        # Verify correctness 1
        for name, _ in token_defs:
            if name.startswith('__'):
                raise GrammarError('Names starting with double-underscore are reserved (Error at %s)' % name)

        # Handle ignore tokens
        # XXX A slightly hacky solution. Recognition of %ignore TOKEN as separate comes from the lexer's
        #     inability to handle duplicate tokens (two names, one value)
        ignore_names = []
        for t in ignore:
            if t.data=='expansions' and len(t.children) == 1:
                t2 ,= t.children
                if t2.data=='expansion' and len(t2.children) == 1:
                    item ,= t2.children
                    if isinstance(item, Token) and item.type == 'TOKEN':
                        ignore_names.append(item.value)
                        continue

            name = '__IGNORE_%d'% len(ignore_names)
            ignore_names.append(name)
            token_defs.append((name, (t, 0)))

        # Verify correctness 2
        token_names = set()
        for name, _ in token_defs:
            if name in token_names:
                raise GrammarError("Token '%s' defined more than once" % name)
            token_names.add(name)

        if set(ignore_names) > token_names:
            raise GrammarError("Tokens %s were marked to ignore but were not defined!" % (set(ignore_names) - token_names))

        # Resolve token references
        resolve_token_references(token_defs)

        rules = [options_from_rule(*x) for x in rule_defs]

        rule_names = set()
        for name, _x, _o in rules:
            if name.startswith('__'):
                raise GrammarError('Names starting with double-underscore are reserved (Error at %s)' % name)
            if name in rule_names:
                raise GrammarError("Rule '%s' defined more than once" % name)
            rule_names.add(name)

        for name, expansions, _o in rules:
            used_symbols = {t for x in expansions.find_data('expansion')
                              for t in x.scan_values(lambda t: t.type in ('RULE', 'TOKEN'))}
            for sym in used_symbols:
                if is_terminal(sym):
                    if sym not in token_names:
                        raise GrammarError("Token '%s' used but not defined (in rule %s)" % (sym, name))
                else:
                    if sym not in rule_names:
                        raise GrammarError("Rule '%s' used but not defined (in rule %s)" % (sym, name))

        # TODO don't include unused tokens, they can only cause trouble!

        return Grammar(rules, token_defs, ignore_names)



load_grammar = GrammarLoader().load_grammar
