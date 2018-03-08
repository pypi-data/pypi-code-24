"Converts between Lark and Nearley grammars. Work in progress!"

import os.path
import sys
import codecs


from lark import Lark, InlineTransformer

nearley_grammar = r"""
    start: (ruledef|directive)+

    directive: "@" NAME (STRING|NAME)
             | "@" JS  -> js_code
    ruledef: NAME "->" expansions
           | NAME REGEXP "->" expansions -> macro
    expansions: expansion ("|" expansion)*

    expansion: expr+ js

    ?expr: item [":" /[+*?]/]

    ?item: rule|string|regexp
         | "(" expansions ")"

    rule: NAME
    string: STRING
    regexp: REGEXP
    JS: /{%.*?%}/s
    js: JS?

    NAME: /[a-zA-Z_$]\w*/
    COMMENT: /#[^\n]*/
    REGEXP: /\[.*?\]/
    STRING: /".*?"/

    %import common.WS
    %ignore WS
    %ignore COMMENT

    """

nearley_grammar_parser = Lark(nearley_grammar, parser='earley', lexer='standard')

def _get_rulename(name):
    name = {'_': '_ws_maybe', '__':'_ws'}.get(name, name)
    return 'n_' + name.replace('$', '__DOLLAR__').lower()

class NearleyToLark(InlineTransformer):
    def __init__(self):
        self._count = 0
        self.extra_rules = {}
        self.extra_rules_rev = {}
        self.alias_js_code = {}

    def _new_function(self, code):
        name = 'alias_%d' % self._count
        self._count += 1

        self.alias_js_code[name] = code
        return name

    def _extra_rule(self, rule):
        if rule in self.extra_rules_rev:
            return self.extra_rules_rev[rule]

        name = 'xrule_%d' % len(self.extra_rules)
        assert name not in self.extra_rules
        self.extra_rules[name] = rule
        self.extra_rules_rev[rule] = name
        return name

    def rule(self, name):
        return _get_rulename(name)

    def ruledef(self, name, exps):
        return '!%s: %s' % (_get_rulename(name), exps)

    def expr(self, item, op):
        rule = '(%s)%s' % (item, op)
        return self._extra_rule(rule)

    def regexp(self, r):
        return '/%s/' % r

    def string(self, s):
        return self._extra_rule(s)

    def expansion(self, *x):
        x, js = x[:-1], x[-1]
        if js.children:
            js_code ,= js.children
            js_code = js_code[2:-2]
            alias = '-> ' + self._new_function(js_code)
        else:
            alias = ''
        return ' '.join(x) + alias

    def expansions(self, *x):
        return '%s' % ('\n    |'.join(x))

    def start(self, *rules):
        return '\n'.join(filter(None, rules))

def _nearley_to_lark(g, builtin_path, n2l, js_code, folder_path, includes):
    rule_defs = []

    tree = nearley_grammar_parser.parse(g)
    for statement in tree.children:
        if statement.data == 'directive':
            directive, arg = statement.children
            if directive in ('builtin', 'include'):
                folder = builtin_path if directive == 'builtin' else folder_path
                path = os.path.join(folder, arg[1:-1])
                if path not in includes:
                    includes.add(path)
                    with codecs.open(path, encoding='utf8') as f:
                        text = f.read()
                    rule_defs += _nearley_to_lark(text, builtin_path, n2l, js_code, os.path.abspath(os.path.dirname(path)), includes)
            else:
                assert False, directive
        elif statement.data == 'js_code':
            code ,= statement.children
            code = code[2:-2]
            js_code.append(code)
        elif statement.data == 'macro':
            pass    # TODO Add support for macros!
        elif statement.data == 'ruledef':
            rule_defs.append( n2l.transform(statement) )
        else:
            raise Exception("Unknown statement: %s" % statement)

    return rule_defs


def create_code_for_nearley_grammar(g, start, builtin_path, folder_path):
    import js2py

    emit_code = []
    def emit(x=None):
        if x:
            emit_code.append(x)
        emit_code.append('\n')

    js_code = ['function id(x) {return x[0];}']
    n2l = NearleyToLark()
    rule_defs = _nearley_to_lark(g, builtin_path, n2l, js_code, folder_path, set())
    lark_g = '\n'.join(rule_defs)
    lark_g += '\n'+'\n'.join('!%s: %s' % item for item in n2l.extra_rules.items())

    emit('from lark import Lark, Transformer')
    emit()
    emit('grammar = ' + repr(lark_g))
    emit()

    for alias, code in n2l.alias_js_code.items():
        js_code.append('%s = (%s);' % (alias, code))

    emit(js2py.translate_js('\n'.join(js_code)))
    emit('class TransformNearley(Transformer):')
    for alias in n2l.alias_js_code:
        emit("    %s = var.get('%s').to_python()" % (alias, alias))
    emit("    __default__ = lambda self, n, c: c if c else None")

    emit()
    emit('parser = Lark(grammar, start="n_%s")' % start)
    emit('def parse(text):')
    emit('    return TransformNearley().transform(parser.parse(text))')

    return ''.join(emit_code)

def main(fn, start, nearley_lib):
    with codecs.open(fn, encoding='utf8') as f:
        grammar = f.read()
    return create_code_for_nearley_grammar(grammar, start, os.path.join(nearley_lib, 'builtin'), os.path.abspath(os.path.dirname(fn)))


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Reads Nearley grammar (with js functions) outputs an equivalent lark parser.")
        print("Usage: %s <nearley_grammar_path> <start_rule> <nearley_lib_path>" % sys.argv[0])
        sys.exit(1)

    fn, start, nearley_lib = sys.argv[1:]

    print(main(fn, start, nearley_lib))
