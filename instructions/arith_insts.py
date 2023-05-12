def op_2(_code_gen, op):
    arg1 = _code_gen.stack_pop()
    arg2 = _code_gen.stack_pop()
    
    _code_gen.stack_push("(%s %s %s)" % (arg2, op, arg1))

def NOT(_code_gen, _):
    arg1 = _code_gen.stack_pop()
    _code_gen.stack_push("!%s" % (arg1))

    
def SQRT(_code_gen, _):
    arg1 = _code_gen.stack_pop()
    _code_gen.stack_push("sqrt(%s)" % (arg1))

ADD = lambda c,_: op_2(c, "+")
SUB = lambda c,_: op_2(c, "-")
DIV = lambda c,_: op_2(c, "/")
MUL = lambda c,_: op_2(c, "*")
MOD = lambda c,_: op_2(c, "%")
AND = lambda c,_: op_2(c, "&")
OR = lambda c,_: op_2(c, "|")
XOR = lambda c,_: op_2(c, "^")
INVERT = lambda c,_: op_2(c, "~")
EXP = lambda c,_: op_2(c, "**")
SHL = lambda c,_: op_2(c, "<<")
SHR = lambda c,_: op_2(c, ">>")


### B ###

def b_op_2(_code_gen, op):
    arg1 = _code_gen.stack_pop()
    arg2 = _code_gen.stack_pop()   
    _code_gen.stack_push("%s(%s, %s)" % (op, arg2, arg1))

    
def BSQRT(_code_gen, _):
    arg1 = _code_gen.stack_pop()
    _code_gen.stack_push("bsqrt(%s)" % (arg1))

def BZERO(_code_gen, _):
    arg1 = _code_gen.stack_pop()
    varname = _code_gen.get_new_var()
    _code_gen.add_code("%s = [0] * %s" %(varname, arg1))
    _code_gen.stack_push(varname)


BADD = lambda c,_: b_op_2(c, "BinAdd")
BSUB = lambda c,_: b_op_2(c, "BinSub")
BDIV = lambda c,_: b_op_2(c, "BinDiv")
BMUL = lambda c,_: b_op_2(c, "BinMul")
BMOD = lambda c,_: b_op_2(c, "BinMod")
BAND = lambda c,_: b_op_2(c, "BinAnd")
BOR = lambda c,_: b_op_2(c, "BinOr")
BXOR = lambda c,_: b_op_2(c, "BinXor")
BINVERT = lambda c,_: b_op_2(c, "BinInv")
BEXP = lambda c,_: b_op_2(c, "BinAddExp")

### W ###

def MULW(_code_gen, _):
    arg1 = _code_gen.stack_pop()
    arg2 = _code_gen.stack_pop()

    var1 = _code_gen.get_new_var()
    _code_gen.add_code("%s = Mul64(%s * %s)" % (var1, arg1, arg2))

    _code_gen.stack_push("%s.high" % (var1))
    _code_gen.stack_push("%s.low" % (var1))

def DIVW(_code_gen, _):
    low = _code_gen.stack_pop()
    high = _code_gen.stack_pop()
    y = _code_gen.stack_pop()

    var1 = _code_gen.get_new_var()
    _code_gen.add_code("%s = Div64((high: %s, low: %s), %s)" % (var1, high, low, y))
    _code_gen.stack_push(var1)

def DIVMODW(_code_gen, _):
    v_low = _code_gen.stack_pop()
    v_high = _code_gen.stack_pop()

    k_low = _code_gen.stack_pop()
    k_high = _code_gen.stack_pop()

    var1 = _code_gen.get_new_var()
    _code_gen.add_code("%s = DivMod64((high: %s, low: %s), (high: %s, low: %s))" % (var1, v_high, v_low, k_high, k_low))

    _code_gen.stack_push("%s.hiQuo" % var1)
    _code_gen.stack_push("%s.loQuo" % var1)
    _code_gen.stack_push("%s.hiRem" % var1)
    _code_gen.stack_push("%s.loRem" % var1)