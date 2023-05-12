from .util_constants import TxFields, GlobalFields

TXN_VAR_NAME = "TXN"
SUBTXN_NAME = "SUB.TXN"
GLOBAL_VAR_NAME = "GLOBAL"

def ITXN(_code_gen, arg: str):
    if arg.isnumeric():
        arg = TxFields[int(arg)]
    _code_gen.stack_push("%s[field: %s, gi: %d, ai: %d]" %(TXN_VAR_NAME, arg, 0, 0))

def TXN(_code_gen, arg: str):
    if arg.isnumeric():
        arg = TxFields[int(arg)]
    
    gi = _code_gen.get_ctx_full_name("groupIndex")
    _code_gen.stack_push("%s[field: %s, gi: %s, ai: %s]" %(TXN_VAR_NAME, arg, gi, 0))
    
def TXNA(_code_gen, arg: str):
    arg = arg.split()
    assert(len(arg) >= 2)
    
    field = arg[0]
    idx = arg[1]

    assert(idx.isnumeric())
    if field.isnumeric():
        field = TxFields[int(field)]

    gi = _code_gen.get_ctx_full_name("groupIndex")
    _code_gen.stack_push("%s[field: %s, gi: %s, ai: %s]" %(TXN_VAR_NAME, field, gi, idx))

def TXNAS(_code_gen, arg: str):
    field = arg
    idx = _code_gen.stack_pop()

    if field.isnumeric():
        field = TxFields[int(field)]
    
    gi = _code_gen.get_ctx_full_name("groupIndex")
    _code_gen.stack_push("%s[field: %s, gi: %s, ai: %s]" %(TXN_VAR_NAME, field, gi, idx))

def GLOBAL(_code_gen, arg:str):
    if arg.isnumeric():
        arg = GlobalFields[int(arg)]

    _code_gen.stack_push("%s[%s]" %(GLOBAL_VAR_NAME, arg))


### ITXN ###

def ITXN_BEGIN(_code_gen, _):
    _code_gen.add_code("\nITXN_BEGIN()")
    _code_gen.new_itxn()
    _code_gen.record_itxn()

def ITXN_FIELD(_code_gen, arg: str):
    if arg.isnumeric():
        arg = TxFields[int(arg)]
        SUBTXN_NAME
    sv = _code_gen.stack_pop()

    _code_gen.add_code(f"{SUBTXN_NAME}[{_code_gen.get_now_itxn()}].{arg} = {sv}")

def ITXN_SUBMIT(_code_gen, arg: str):
    start = _code_gen.get_recorded_itxn()
    end = _code_gen.get_now_itxn()

    tmp = ", ".join(map(str,list(range(start, end+1))))
    _code_gen.add_code("\nITXN_SUBMIT([%s])\n" % tmp)



### GTXN ###

def GTXNS(_code_gen, arg:str):
    if arg.isnumeric():
        arg = TxFields[int(arg)]
    gi = _code_gen.stack_pop()
    _code_gen.stack_push("%s[%s, gi: %s]" %(TXN_VAR_NAME, arg, gi))
    

def GTXN(_code_gen, arg: str):
    assert(len(arg.split()) == 2)

    gi, field = arg.split()
    assert(gi.isnumeric())

    if field.isnumeric():
        field = TxFields[int(arg)]
        
    _code_gen.stack_push("%s[field: %s, gi: %s, ai: %s]" %(TXN_VAR_NAME, field, gi, 0))


def GTXNA(_code_gen, arg: str):
    assert(len(arg.split()) == 3)

    gi, field, ai = arg.split()
    assert(gi.isnumeric() and ai.isnumeric())

    if field.isnumeric():
        field = TxFields[int(arg)]
        
    _code_gen.stack_push("%s[field: %s, gi: %s, ai: %s]" %(TXN_VAR_NAME, field, gi, ai))


def GTXNSA(_code_gen, arg:str):
    assert(len(arg.split()) == 2)

    field, ai = arg.split()
    assert(ai.isnumeric())

    if field.isnumeric():
        field = TxFields[int(arg)]

    gi = _code_gen.stack_pop()
    _code_gen.stack_push("%s[field: %s, gi: %s, ai: %s]" %(TXN_VAR_NAME, field, gi, ai))