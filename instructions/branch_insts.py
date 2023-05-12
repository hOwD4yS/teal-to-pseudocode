def BNZ(_code_gen, label: str):
    ele = _code_gen.stack_pop()
    code = "if %s:\n\t goto %s\n" % (ele, label)
    _code_gen.add_code(code)

def BZ(_code_gen, label: str):
    ele = _code_gen.stack_pop()
    code = "if !%s:\n\t goto %s\n" % (ele, label)
    _code_gen.add_code(code)

def B(_code_gen, label: str):
    code = "goto %s\n" % (label)
    _code_gen.add_code(code)

def CALLSUB(_code_gen, label: str):
    varname = _code_gen.get_new_var()
    code = "%s = call_internal(to: %s)\n" % (varname, label)
    _code_gen.add_code(code)
    _code_gen.stack_push(varname)

def RETSUB(_code_gen, _):
    ele = _code_gen.stack_pop()
    _code_gen.add_code("RETSUB(DATA: %s)\n" % ele)

def RETURN(_code_gen, _):
    ele = _code_gen.stack_pop()
    _code_gen.add_code("RETURN %s // END PROGRAM\n" % ele)