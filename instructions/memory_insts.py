from .util_constants import AppParamsFields, AssetParamsFields, AssetHoldingFields

### GLOBAL ###

def APP_GLOBAL_PUT(_code_gen, _):
    sv = _code_gen.stack_pop()
    key = "string(%s)" % _code_gen.stack_pop()

    appid = _code_gen.get_ctx_full_name("appID")
    setglobal = _code_gen.get_ctx_full_name("SetGlobal")
    _code_gen.add_code("%s(appID: %s, key: %s, val: %s)" % (setglobal, appid, key, sv))

def APP_GLOBAL_GET(_code_gen, _):
    key = "string(%s)" % _code_gen.stack_pop()
    appid = _code_gen.get_ctx_full_name("appID")
    getglobal = _code_gen.get_ctx_full_name("GetGlobal")
    _code_gen.stack_push("%s(appID: %s, key: %s)" % (getglobal, appid, key))

def APP_GLOBAL_GET_EX(_code_gen, _):
    key = "string(%s)" % _code_gen.stack_pop()
    appid =  _code_gen.stack_pop()
    getglobal = _code_gen.get_ctx_full_name("GetGlobal")
    _code_gen.stack_push("%s(appID: %s, key: %s)" % (getglobal, appid, key))

def APP_GLOBAL_DEL(_code_gen, _):
    key = "string(%s)" % _code_gen.stack_pop()
    appid = _code_gen.get_ctx_full_name("appID")
    delglobal = _code_gen.get_ctx_full_name("DelGlobal")
    _code_gen.stack_push("%s(appID: %s, key: %s)" % (delglobal, appid, key))


### LOCAL ###

def APP_LOCAL_PUT(_code_gen, _):
    sv = _code_gen.stack_pop()
    key = "string(%s)" % _code_gen.stack_pop()
    addr = "accoutmutref(%s)" % _code_gen.stack_pop()

    appid = _code_gen.get_ctx_full_name("appID")
    setlocal = _code_gen.get_ctx_full_name("SetLocal")
    _code_gen.add_code("%s(appID: %s, addr: %s, key: %s, val: %s)" % (setlocal, appid, addr, key, sv))


def APP_LOCAL_GET(_code_gen, _):
    key = "string(%s)" % _code_gen.stack_pop()
    addr = "accountref(%s)" % _code_gen.stack_pop()

    appid = _code_gen.get_ctx_full_name("appID")
    getlocal = _code_gen.get_ctx_full_name("GetLocal")
    _code_gen.stack_push("%s(appID: %s, addr: %s, key: %s)" % (getlocal, appid, addr, key))


def APP_LOCAL_GET_EX(_code_gen, _):
    key = "string(%s)" % _code_gen.stack_pop()
    appid =  _code_gen.stack_pop()
    addr = "accountref(%s)" % _code_gen.stack_pop()

    getlocal = _code_gen.get_ctx_full_name("GetLocal")
    _code_gen.stack_push("%s(appID: %s, addr: %s, key: %s)" % (getlocal, appid, addr, key))

def APP_LOCAL_DEL(_code_gen, _):
    key = "string(%s)" % _code_gen.stack_pop()
    addr = "accoutmutref(%s)" % _code_gen.stack_pop()
    appid = _code_gen.get_ctx_full_name("appID")
    getlocal = _code_gen.get_ctx_full_name("DelLocal")
    _code_gen.stack_push("%s(appID: %s, addr :%s, key: %s)" % (getlocal, appid, addr, key))


### PARAMS ###

def APP_PARAMS_GET(_code_gen, arg: str):
    if arg.isnumeric():
        arg = AppParamsFields[int(arg)]
    appid =  _code_gen.stack_pop()
    
    appparams = _code_gen.get_ctx_full_name("AppParam")
    _code_gen.stack_push("%s(appID: %s, field: %s)" % (appparams, appid, arg))

def ASSET_HOLDING_GET(_code_gen, arg: str):
    if arg.isnumeric():
        arg = AssetHoldingFields[int(arg)]

    asaid = _code_gen.stack_pop()
    addr = "accountref(%s)" % _code_gen.stack_pop()
    assetParams = _code_gen.get_ctx_full_name("AssetHoldings")
    _code_gen.stack_push("%s(asaID: %s, addr: %s)" % (assetParams, asaid, addr))


def ASSET_PARAMS_GET(_code_gen, arg: str):
    if arg.isnumeric():
        arg = AssetParamsFields[int(arg)]
    asaid =  _code_gen.stack_pop()
    
    assetParams = _code_gen.get_ctx_full_name("AssetParam")
    _code_gen.stack_push("%s(asaID: %s, field: %s)" % (assetParams, asaid, arg))

## SCRATCH ##

def STORE(_code_gen, arg: str):
    assert(arg.isnumeric())

    key = int(arg)
    value = _code_gen.stack_pop()
    scratch = _code_gen.get_ctx_full_name("SCRATCH")
    _code_gen.add_code("%s[%d] =  %s" % (scratch, key, value))

def LOAD(_code_gen, arg: str):
    assert(arg.isnumeric())

    key = int(arg)
    scratch = _code_gen.get_ctx_full_name("SCRATCH")
    _code_gen.stack_push("%s[%d]" % (scratch, key))