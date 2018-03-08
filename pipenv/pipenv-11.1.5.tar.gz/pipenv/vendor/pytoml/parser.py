import string, re, sys, datetime
from .core import TomlError

if sys.version_info[0] == 2:
    _chr = unichr
else:
    _chr = chr

def load(fin, translate=lambda t, x, v: v):
    return loads(fin.read(), translate=translate, filename=getattr(fin, 'name', repr(fin)))

def loads(s, filename='<string>', translate=lambda t, x, v: v):
    if isinstance(s, bytes):
        s = s.decode('utf-8')

    s = s.replace('\r\n', '\n')

    root = {}
    tables = {}
    scope = root

    src = _Source(s, filename=filename)
    ast = _p_toml(src)

    def error(msg):
        raise TomlError(msg, pos[0], pos[1], filename)

    def process_value(v):
        kind, text, value, pos = v
        if kind == 'str' and value.startswith('\n'):
            value = value[1:]
        if kind == 'array':
            if value and any(k != value[0][0] for k, t, v, p in value[1:]):
                error('array-type-mismatch')
            value = [process_value(item) for item in value]
        elif kind == 'table':
            value = dict([(k, process_value(value[k])) for k in value])
        return translate(kind, text, value)

    for kind, value, pos in ast:
        if kind == 'kv':
            k, v = value
            if k in scope:
                error('duplicate_keys. Key "{0}" was used more than once.'.format(k))
            scope[k] = process_value(v)
        else:
            is_table_array = (kind == 'table_array')
            cur = tables
            for name in value[:-1]:
                if isinstance(cur.get(name), list):
                    d, cur = cur[name][-1]
                else:
                    d, cur = cur.setdefault(name, (None, {}))

            scope = {}
            name = value[-1]
            if name not in cur:
                if is_table_array:
                    cur[name] = [(scope, {})]
                else:
                    cur[name] = (scope, {})
            elif isinstance(cur[name], list):
                if not is_table_array:
                    error('table_type_mismatch')
                cur[name].append((scope, {}))
            else:
                if is_table_array:
                    error('table_type_mismatch')
                old_scope, next_table = cur[name]
                if old_scope is not None:
                    error('duplicate_tables')
                cur[name] = (scope, next_table)

    def merge_tables(scope, tables):
        if scope is None:
            scope = {}
        for k in tables:
            if k in scope:
                error('key_table_conflict')
            v = tables[k]
            if isinstance(v, list):
                scope[k] = [merge_tables(sc, tbl) for sc, tbl in v]
            else:
                scope[k] = merge_tables(v[0], v[1])
        return scope

    return merge_tables(root, tables)

class _Source:
    def __init__(self, s, filename=None):
        self.s = s
        self._pos = (1, 1)
        self._last = None
        self._filename = filename
        self.backtrack_stack = []

    def last(self):
        return self._last

    def pos(self):
        return self._pos

    def fail(self):
        return self._expect(None)

    def consume_dot(self):
        if self.s:
            self._last = self.s[0]
            self.s = self[1:]
            self._advance(self._last)
            return self._last
        return None

    def expect_dot(self):
        return self._expect(self.consume_dot())

    def consume_eof(self):
        if not self.s:
            self._last = ''
            return True
        return False

    def expect_eof(self):
        return self._expect(self.consume_eof())

    def consume(self, s):
        if self.s.startswith(s):
            self.s = self.s[len(s):]
            self._last = s
            self._advance(s)
            return True
        return False

    def expect(self, s):
        return self._expect(self.consume(s))

    def consume_re(self, re):
        m = re.match(self.s)
        if m:
            self.s = self.s[len(m.group(0)):]
            self._last = m
            self._advance(m.group(0))
            return m
        return None

    def expect_re(self, re):
        return self._expect(self.consume_re(re))

    def __enter__(self):
        self.backtrack_stack.append((self.s, self._pos))

    def __exit__(self, type, value, traceback):
        if type is None:
            self.backtrack_stack.pop()
        else:
            self.s, self._pos = self.backtrack_stack.pop()
        return type == TomlError

    def commit(self):
        self.backtrack_stack[-1] = (self.s, self._pos)

    def _expect(self, r):
        if not r:
            raise TomlError('msg', self._pos[0], self._pos[1], self._filename)
        return r

    def _advance(self, s):
        suffix_pos = s.rfind('\n')
        if suffix_pos == -1:
            self._pos = (self._pos[0], self._pos[1] + len(s))
        else:
            self._pos = (self._pos[0] + s.count('\n'), len(s) - suffix_pos)

_ews_re = re.compile(r'(?:[ \t]|#[^\n]*\n|#[^\n]*\Z|\n)*')
def _p_ews(s):
    s.expect_re(_ews_re)

_ws_re = re.compile(r'[ \t]*')
def _p_ws(s):
    s.expect_re(_ws_re)

_escapes = { 'b': '\b', 'n': '\n', 'r': '\r', 't': '\t', '"': '"', '\'': '\'',
    '\\': '\\', '/': '/', 'f': '\f' }

_basicstr_re = re.compile(r'[^"\\\000-\037]*')
_short_uni_re = re.compile(r'u([0-9a-fA-F]{4})')
_long_uni_re = re.compile(r'U([0-9a-fA-F]{8})')
_escapes_re = re.compile('[bnrt"\'\\\\/f]')
_newline_esc_re = re.compile('\n[ \t\n]*')
def _p_basicstr_content(s, content=_basicstr_re):
    res = []
    while True:
        res.append(s.expect_re(content).group(0))
        if not s.consume('\\'):
            break
        if s.consume_re(_newline_esc_re):
            pass
        elif s.consume_re(_short_uni_re) or s.consume_re(_long_uni_re):
            res.append(_chr(int(s.last().group(1), 16)))
        else:
            s.expect_re(_escapes_re)
            res.append(_escapes[s.last().group(0)])
    return ''.join(res)

_key_re = re.compile(r'[0-9a-zA-Z-_]+')
def _p_key(s):
    with s:
        s.expect('"')
        r = _p_basicstr_content(s, _basicstr_re)
        s.expect('"')
        return r
    if s.consume('\''):
        if s.consume('\'\''):
            r = s.expect_re(_litstr_ml_re).group(0)
            s.expect('\'\'\'')
        else:
            r = s.expect_re(_litstr_re).group(0)
            s.expect('\'')
        return r
    return s.expect_re(_key_re).group(0)

_float_re = re.compile(r'[+-]?(?:0|[1-9](?:_?\d)*)(?:\.\d(?:_?\d)*)?(?:[eE][+-]?(?:\d(?:_?\d)*))?')
_datetime_re = re.compile(r'(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})(\.\d+)?(?:Z|([+-]\d{2}):(\d{2}))')

_basicstr_ml_re = re.compile(r'(?:(?:|"|"")[^"\\\000-\011\013-\037])*')
_litstr_re = re.compile(r"[^'\000-\037]*")
_litstr_ml_re = re.compile(r"(?:(?:|'|'')(?:[^'\000-\011\013-\037]))*")
def _p_value(s):
    pos = s.pos()

    if s.consume('true'):
        return 'bool', s.last(), True, pos
    if s.consume('false'):
        return 'bool', s.last(), False, pos

    if s.consume('"'):
        if s.consume('""'):
            r = _p_basicstr_content(s, _basicstr_ml_re)
            s.expect('"""')
        else:
            r = _p_basicstr_content(s, _basicstr_re)
            s.expect('"')
        return 'str', r, r, pos

    if s.consume('\''):
        if s.consume('\'\''):
            r = s.expect_re(_litstr_ml_re).group(0)
            s.expect('\'\'\'')
        else:
            r = s.expect_re(_litstr_re).group(0)
            s.expect('\'')
        return 'str', r, r, pos

    if s.consume_re(_datetime_re):
        m = s.last()
        s0 = m.group(0)
        r = map(int, m.groups()[:6])
        if m.group(7):
            micro = float(m.group(7))
        else:
            micro = 0

        if m.group(8):
            g = int(m.group(8), 10) * 60 + int(m.group(9), 10)
            tz = _TimeZone(datetime.timedelta(0, g * 60))
        else:
            tz = _TimeZone(datetime.timedelta(0, 0))

        y, m, d, H, M, S = r
        dt = datetime.datetime(y, m, d, H, M, S, int(micro * 1000000), tz)
        return 'datetime', s0, dt, pos

    if s.consume_re(_float_re):
        m = s.last().group(0)
        r = m.replace('_','')
        if '.' in m or 'e' in m or 'E' in m:
            return 'float', m, float(r), pos
        else:
            return 'int', m, int(r, 10), pos

    if s.consume('['):
        items = []
        with s:
            while True:
                _p_ews(s)
                items.append(_p_value(s))
                s.commit()
                _p_ews(s)
                s.expect(',')
                s.commit()
        _p_ews(s)
        s.expect(']')
        return 'array', None, items, pos

    if s.consume('{'):
        _p_ws(s)
        items = {}
        if not s.consume('}'):
            k = _p_key(s)
            _p_ws(s)
            s.expect('=')
            _p_ws(s)
            items[k] = _p_value(s)
            _p_ws(s)
            while s.consume(','):
                _p_ws(s)
                k = _p_key(s)
                _p_ws(s)
                s.expect('=')
                _p_ws(s)
                items[k] = _p_value(s)
                _p_ws(s)
            s.expect('}')
        return 'table', None, items, pos

    s.fail()

def _p_stmt(s):
    pos = s.pos()
    if s.consume(   '['):
        is_array = s.consume('[')
        _p_ws(s)
        keys = [_p_key(s)]
        _p_ws(s)
        while s.consume('.'):
            _p_ws(s)
            keys.append(_p_key(s))
            _p_ws(s)
        s.expect(']')
        if is_array:
            s.expect(']')
        return 'table_array' if is_array else 'table', keys, pos

    key = _p_key(s)
    _p_ws(s)
    s.expect('=')
    _p_ws(s)
    value = _p_value(s)
    return 'kv', (key, value), pos

_stmtsep_re = re.compile(r'(?:[ \t]*(?:#[^\n]*)?\n)+[ \t]*')
def _p_toml(s):
    stmts = []
    _p_ews(s)
    with s:
        stmts.append(_p_stmt(s))
        while True:
            s.commit()
            s.expect_re(_stmtsep_re)
            stmts.append(_p_stmt(s))
    _p_ews(s)
    s.expect_eof()
    return stmts

class _TimeZone(datetime.tzinfo):
    def __init__(self, offset):
        self._offset = offset

    def utcoffset(self, dt):
        return self._offset

    def dst(self, dt):
        return None

    def tzname(self, dt):
        m = self._offset.total_seconds() // 60
        if m < 0:
            res = '-'
            m = -m
        else:
            res = '+'
        h = m // 60
        m = m - h * 60
        return '{}{:.02}{:.02}'.format(res, h, m)
