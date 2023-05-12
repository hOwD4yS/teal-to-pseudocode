def ERR(_code_gen, _):
    _code_gen.add_code("\nERR // PROGRAM REVERT\n")

def ASSERT(_code_gen, _):
    arg = _code_gen.stack_pop()
    _code_gen.add_code("assert(%s)" % arg)

def BTOI(_code_gen, _):
    arg = _code_gen.stack_pop()
    _code_gen.stack_push("BTOI(%s)" % arg)

def ITOB(_code_gen, _):
    arg = _code_gen.stack_pop()
    _code_gen.stack_push("ITOB(%s)" % arg)

def LEN(_code_gen, _):
    arg = _code_gen.stack_pop()
    _code_gen.stack_push("LEN(%s)" % arg)

def SUBSTRING(_code_gen, arg: str):
    assert(len(arg.split()) == 2)
    
    start, end = arg.split()
    ele = _code_gen.stack_pop()
    _code_gen.stack_push("%s[%s:%s]" % (ele, start, end))

def SUBSTRING3(_code_gen, _):
    end = _code_gen.stack_pop()
    start = _code_gen.stack_pop()
    ele = _code_gen.stack_pop()
    _code_gen.stack_push("%s[%s:%s]" % (ele, start, end))

def LOG(_code_gen, _):
    arg = _code_gen.stack_pop()
    _code_gen.stack_push("LOG(%s)" % arg)

def BALANCE(_code_gen, _):
    addr = "accountref(%s)" % _code_gen.stack_pop()
    _code_gen.stack_push("%s.balance" % addr)

def MIN_BALANCE(_code_gen, _):
    addr = "accountref(%s)" % _code_gen.stack_pop()
    _code_gen.stack_push("%s.min_balance" % addr)

### STACK ###
def POP(_code_gen, _):
    _code_gen.stack_pop()

def SWAP(_code_gen, _):
    a = _code_gen.stack_pop()
    b = _code_gen.stack_pop()

    _code_gen.stack_push(a)
    _code_gen.stack_push(b)

def DUP(_code_gen, _):
    _code_gen.stack_push(_code_gen.stack[-1])

def DUP2(_code_gen, _):
    _code_gen.stack_push(_code_gen.stack[-2])

def SELECT(_code_gen, _):
    a = _code_gen.stack_pop()
    b = _code_gen.stack_pop()
    c = _code_gen.stack_pop()
    varname = _code_gen.get_new_var()

    _code_gen.add_code("if %s" % (a))
    _code_gen.add_code("%s = %s" % (varname, b))
    _code_gen.add_code("else")
    _code_gen.add_code("%s = %s\n" % (varname, c))    

    _code_gen.stack_push(varname)    

def CONCAT(_code_gen, _):
    a = _code_gen.stack_pop()
    b = _code_gen.stack_pop()

    _code_gen.stack_push("CONCAT(%s,%s)" % (a,b))    