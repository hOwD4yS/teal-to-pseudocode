def INTCBLOCK(_code_gen, arg: str):
    _code_gen.add_ctx_var("intc", "[" + ",".join(arg.split(" ")) + "]")

def BYTECBLOCK(_code_gen, arg: str):
    _code_gen.add_ctx_var("bytec", "[" + ",".join(arg.split(" ")) + "]")

def INTC(_code_gen, arg: str):
    intc = _code_gen.get_ctx_full_name("intc")

    assert(arg.isnumeric())
    _code_gen.stack_push("%s[%s]" %(intc, arg))

def BYTEC(_code_gen, arg: str):
    intc = _code_gen.get_ctx_full_name("bytec")
    assert(arg.isnumeric())
    _code_gen.stack_push("%s[%s]" %(intc, arg))


## GET ##
def GETBYTE(_code_gen, arg: str):
    idx = _code_gen.stack_pop()
    target = _code_gen.stack_pop()

    _code_gen.stack_push("(int)((bytes)%s)[%s]" %(target, idx))

def SETBYTE(_code_gen, arg: str):
    value = _code_gen.stack_pop()
    sidx = _code_gen.stack_pop()
    target = _code_gen.stack_pop()

    varname = _code_gen.get_new_var()
    _code_gen.add_code("%s = %s" % (varname, target))
    _code_gen.add_code("%s[%s] = BYTE(%s)" % (varname, sidx, value))
    _code_gen.stack_push(varname)

def GETBIT(_code_gen, arg: str):
    idx = _code_gen.stack_pop()
    target = _code_gen.stack_pop()
    _code_gen.stack_push("((bits)%s)[%s]" %(target, idx))

def SETBIT(_code_gen, arg: str):
    value = _code_gen.stack_pop()
    sidx = _code_gen.stack_pop()
    target = _code_gen.stack_pop()

    varname = _code_gen.get_new_var()
    _code_gen.add_code("%s = (bits)%s" % (varname, target))
    _code_gen.add_code("%s[%s] = BIT(%s)" % (varname, sidx, value))

    _code_gen.stack_push(varname)


## OTHERS ##
def INT(_code_gen, arg: str):
    if arg.isnumeric():
        _code_gen.stack_push("%s" % arg)
    else:
        _code_gen.stack_push("(int)%s" % arg)

def BYTE(_code_gen, arg: str):
    _code_gen.stack_push("(byte)%s" % arg)

def ADDR(_code_gen, arg: str):
    _code_gen.stack_push("(addr)%s" % arg)


### PUSH ###

def PUSHBYTES(_code_gen, arg: str):
    _code_gen.stack_push(arg)

def PUSHINT(_code_gen, arg: str):
    assert(arg.isnumeric())
    _code_gen.stack_push(arg)


## EXTRACT ##

def EXTRACT(_code_gen, arg: str):
    assert(len(arg.split()) == 2)
    
    ele = _code_gen.stack_pop()
    start, length = arg.split()
    assert(start.isnumeric() and length.isnumeric())

    if length == '0':
        end = ""
    else:
        end = str(int(start) + int(length))
    
    _code_gen.stack_push("%s[%s:%s]" % (ele, start, end))


def EXTRACT3(_code_gen, arg: str):
    length = _code_gen.stack_pop()
    start = _code_gen.stack_pop()
    byte = _code_gen.stack_pop()

    if length == '0':
        end = ""
    elif start.isnumeric() and length.isnumeric():
        end = int(start) + int(length)
    else:
        end = start + "+" + length
    
    _code_gen.stack_push("%s[%s:%s]" % (byte, start, end))


def EXTRACT_UINTN(_code_gen, length):
    start = _code_gen.stack_pop()
    byte = _code_gen.stack_pop()

    if length == '0':
        end = ""
    elif start.isnumeric():
        end = int(start) + int(start)
    else:
        end = start + "+" + str(length)
    
    _code_gen.stack_push("%s[%s:%s]" % (byte, start, end))


EXTRACT_UINT16 = lambda x, _: EXTRACT_UINTN(x, 2)
EXTRACT_UINT32 = lambda x, _: EXTRACT_UINTN(x, 4)
EXTRACT_UINT64 = lambda x, _: EXTRACT_UINTN(x, 8)


### REPLACE ###

def REPLACE2(_code_gen, arg: str):
    assert(arg.isnumeric())

    replacement = _code_gen.stack_pop()
    original = _code_gen.stack_pop()
    start = int(arg)

    end = "len(%s)" % replacement

    varname = _code_gen.get_new_var()
    _code_gen.add_code("%s = %s" % (varname, original))
    _code_gen.add_code("%s[%d:%s] = %s" % (varname, start, str(start)+"+"+end, replacement))
    _code_gen.stack_push(varname)

def REPLACE3(_code_gen, _):
    replacement = _code_gen.stack_pop()
    start = _code_gen.stack_pop()
    original = _code_gen.stack_pop()

    end = "len(%s)" % replacement

    varname = _code_gen.get_new_var()
    _code_gen.add_code("%s = %s" % (varname, original))
    _code_gen.add_code("%s[%s:%s] = %s" % (varname, start, start+"+"+end, replacement))
    _code_gen.stack_push(varname)