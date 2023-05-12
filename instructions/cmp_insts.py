def CMP(_code_gen, sign):
    arg1 = _code_gen.stack_pop()
    arg2 = _code_gen.stack_pop()
    _code_gen.stack_push("(%s %s %s)" % (arg1, sign, arg2))

LT = lambda c, _: CMP(c, "<")
GT = lambda c, _: CMP(c, ">")
LE = lambda c, _: CMP(c, "<=")
GE = lambda c, _: CMP(c, ">=")
NE = lambda c, _: CMP(c, "!=")
EQ = lambda c, _: CMP(c, "==")
OR = lambda c, _: CMP(c, "||")
AND = lambda c, _: CMP(c, "&&")

##CMP
def BCMP(_code_gen, sign):
    arg1 = _code_gen.stack_pop()
    arg2 = _code_gen.stack_pop()
    _code_gen.stack_push("%s(%s, %s)" % (sign, arg1, arg2))

BLT = lambda c, _: BCMP(c, "BIN<")
BGT = lambda c, _: BCMP(c, "BIN>")
BLE = lambda c, _: BCMP(c, "BIN<=")
BGE = lambda c, _: BCMP(c, "BIN>=")
BNE = lambda c, _: BCMP(c, "BIN!=")
BEQ = lambda c, _: BCMP(c, "BIN==")
BOR = lambda c, _: BCMP(c, "BIN||")
BAND = lambda c, _: BCMP(c, "BIN&&")