# teal-to-pseudocode (This project has been stopped)
# Some Instructions are not implemented.

# Test 
## Teal File: https://github.com/Folks-Finance/folks-finance-contracts/blob/main/contracts/v1/algo_governance/algo_governance_approval_program.teal
## The result after running program
```go
#pragma version 5

if ((int)NoOp == TXN[field: OnCompletion, gi: CTX.groupIndex, ai: 0]):
	 goto main_l6

if ((int)OptIn == TXN[field: OnCompletion, gi: CTX.groupIndex, ai: 0]):
	 goto main_l5

if ((int)CloseOut == TXN[field: OnCompletion, gi: CTX.groupIndex, ai: 0]):
	 goto main_l4


ERR // PROGRAM REVERT

// ./example.teal:15
main_l4: // it is possible for stack to be confused
assert((GLOBAL[ZeroAddress] == TXN[field: CloseRemainderTo, gi: CTX.groupIndex, ai: 0]))
assert((GLOBAL[ZeroAddress] == TXN[field: RekeyTo, gi: CTX.groupIndex, ai: 0]))
assert((0 == CTX.GetLocal(appID: CTX.appID, addr: accountref(0), key: string((byte)"committed"))))
goto main_l32

// ./example.teal:32
main_l5: // it is possible for stack to be confused
assert((GLOBAL[ZeroAddress] == TXN[field: CloseRemainderTo, gi: CTX.groupIndex, ai: 0]))
assert((GLOBAL[ZeroAddress] == TXN[field: RekeyTo, gi: CTX.groupIndex, ai: 0]))
CTX.SetLocal(appID: CTX.appID, addr: accoutmutref(0), key: string((byte)"committed"), val: 0)
goto main_l32

// ./example.teal:47
main_l6: // it is possible for stack to be confused
if (0 == TXN[field: ApplicationID, gi: CTX.groupIndex, ai: 0]):
	 goto main_l31

if ((byte)"s" == TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 0]):
	 goto main_l30

if ((byte)"ur" == TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 0]):
	 goto main_l29

if ((byte)"m" == TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 0]):
	 goto main_l26

if ((byte)"um" == TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 0]):
	 goto main_l25

if ((byte)"b" == TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 0]):
	 goto main_l24

if ((byte)"cr" == TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 0]):
	 goto main_l23

if ((byte)"g" == TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 0]):
	 goto main_l22

if ((byte)"ca" == TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 0]):
	 goto main_l18

if ((byte)"p" == TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 0]):
	 goto main_l17


ERR // PROGRAM REVERT

// ./example.teal:89
main_l17: // it is possible for stack to be confused
assert((1 == GLOBAL[GroupSize]))
var_0 = call_internal(to: sub1)

assert(var_0)
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"is_minting_paused"), val: (0 > BTOI(TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 1])))
goto main_l32

// ./example.teal:104
main_l18: // it is possible for stack to be confused
assert((2 == GLOBAL[GroupSize]))
var_1 = call_internal(to: sub1)

assert(var_1)
var_2 = call_internal(to: sub0)

if !CTX.GetGlobal(appID: CTX.appID, key: string((byte)"can_claim_rewards")):
	 goto main_l21

// ./example.teal:123
main_l20: // it is possible for stack to be confused
var_3 = call_internal(to: sub3)

assert(var_3)
assert((CTX.GetGlobal(appID: CTX.appID, key: string((byte)"period_end")) >= GLOBAL[LatestTimestamp]))
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"total_commitment_abandoned"), val: 0)
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"can_claim_rewards"), val: 1)
goto main_l32

// ./example.teal:140
main_l21: // it is possible for stack to be confused
var_4 = call_internal(to: sub0)

goto main_l20

// ./example.teal:156
main_l22: // it is possible for stack to be confused
assert((2 == GLOBAL[GroupSize]))
var_5 = call_internal(to: sub1)

assert(var_5)
assert((1 == TXN[field: NumAccounts, gi: 0, ai: 0]))
var_6 = call_internal(to: sub3)

assert(var_6)
goto main_l32

// ./example.teal:173
main_l23: // it is possible for stack to be confused
assert((2 == GLOBAL[GroupSize]))
var_7 = call_internal(to: sub2)

assert(var_7)
var_8 = call_internal(to: sub0)

var_9 = call_internal(to: sub3)

assert(var_9)
assert(CTX.GetGlobal(appID: CTX.appID, key: string((byte)"can_claim_rewards")))
goto main_l32

// ./example.teal:205
main_l24: // it is possible for stack to be confused
assert((3 == GLOBAL[GroupSize]))
var_10 = call_internal(to: sub2)

assert(var_10)
var_11 = call_internal(to: sub3)

assert(var_11)
var_12 = call_internal(to: sub4)

assert(var_12)
assert((CTX.GetGlobal(appID: CTX.appID, key: string((byte)"period_end")) > GLOBAL[LatestTimestamp]))
goto main_l32

// ./example.teal:225
main_l25: // it is possible for stack to be confused
assert((3 == GLOBAL[GroupSize]))
var_13 = call_internal(to: sub2)

assert(var_13)
var_14 = call_internal(to: sub3)

assert(var_14)
var_15 = call_internal(to: sub4)

assert(var_15)
assert((CTX.GetGlobal(appID: CTX.appID, key: string((byte)"commit_end")) < GLOBAL[LatestTimestamp]))
assert((TXN[field: AssetAmount, gi: 2, ai: 0] >= CTX.GetLocal(appID: CTX.appID, addr: accountref(0), key: string((byte)"committed"))))
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"total_commitment"), val: (CTX.GetGlobal(appID: CTX.appID, key: string((byte)"total_commitment")) - TXN[field: AssetAmount, gi: 2, ai: 0]))
CTX.SetLocal(appID: CTX.appID, addr: accoutmutref(0), key: string((byte)"committed"), val: (CTX.GetLocal(appID: CTX.appID, addr: accountref(0), key: string((byte)"committed")) - TXN[field: AssetAmount, gi: 2, ai: 0]))
goto main_l32

// ./example.teal:265
main_l26: // it is possible for stack to be confused
assert((2 == GLOBAL[GroupSize]))
var_16 = call_internal(to: sub2)

assert(var_16)
assert(((GLOBAL[ZeroAddress] == TXN[field: RekeyTo, gi: 1, ai: 0]) && ((GLOBAL[ZeroAddress] == TXN[field: CloseRemainderTo, gi: 1, ai: 0]) && ((CTX.GetGlobal(appID: CTX.appID, key: string((byte)"governance_contract_account_addr")) == TXN[field: Receiver, gi: 1, ai: 0]) && ((TXN[field: Sender, gi: 0, ai: 0] == TXN[field: Sender, gi: 1, ai: 0]) && ((int)pay == TXN[field: TypeEnum, gi: 1, ai: 0]))))))

ITXN_BEGIN()

//NEW Inner Txn [1]
SUB.TXN[1].TypeEnum = (int)axfer
SUB.TXN[1].XferAsset = CTX.GetGlobal(appID: CTX.appID, key: string((byte)"g_algo_id"))
SUB.TXN[1].Sender = GLOBAL[CurrentApplicationAddress]
SUB.TXN[1].AssetReceiver = TXN[field: Sender, gi: 1, ai: 0]
SUB.TXN[1].AssetAmount = TXN[field: Amount, gi: 1, ai: 0]
SUB.TXN[1].Fee = 0

ITXN_SUBMIT([1])

assert(!CTX.GetGlobal(appID: CTX.appID, key: string((byte)"is_minting_paused")))
if (CTX.GetGlobal(appID: CTX.appID, key: string((byte)"commit_end")) < GLOBAL[LatestTimestamp]):
	 goto main_l28

// ./example.teal:317
main_l27: // it is possible for stack to be confused
goto main_l32

// ./example.teal:320
main_l28: // it is possible for stack to be confused
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"total_commitment"), val: (CTX.GetGlobal(appID: CTX.appID, key: string((byte)"total_commitment")) + TXN[field: Amount, gi: 1, ai: 0]))
CTX.SetLocal(appID: CTX.appID, addr: accoutmutref(0), key: string((byte)"committed"), val: (CTX.GetLocal(appID: CTX.appID, addr: accountref(0), key: string((byte)"committed")) + TXN[field: Amount, gi: 1, ai: 0]))
goto main_l27

// ./example.teal:336
main_l29: // it is possible for stack to be confused
assert((1 == GLOBAL[GroupSize]))
var_17 = call_internal(to: sub1)

assert(var_17)
assert((2 == TXN[field: NumAppArgs, gi: CTX.groupIndex, ai: 0]))
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"rewards_per_algo"), val: BTOI(TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 1]))
goto main_l32

// ./example.teal:353
main_l30: // it is possible for stack to be confused
assert((1 == GLOBAL[GroupSize]))
var_18 = call_internal(to: sub1)

assert(var_18)
CTX.SCRATCH[0] =  CTX.GetGlobal(appID: 0, key: string((byte)"g_algo_id"))
CTX.SCRATCH[1] =  1
assert(!CTX.SCRATCH[1])
assert((1 == TXN[field: NumAccounts, gi: CTX.groupIndex, ai: 0]))
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"governance_contract_account_addr"), val: TXN[field: Accounts, gi: CTX.groupIndex, ai: 1])

ITXN_BEGIN()

//NEW Inner Txn [2]
SUB.TXN[2].TypeEnum = (int)acfg
SUB.TXN[2].ConfigAssetName = (byte)"Governance Algo 3"
SUB.TXN[2].ConfigAssetUnitName = (byte)"gALGO3"
SUB.TXN[2].ConfigAssetTotal = 10000000000000000
SUB.TXN[2].ConfigAssetDecimals = 6
SUB.TXN[2].ConfigAssetReserve = GLOBAL[CurrentApplicationAddress]
SUB.TXN[2].Fee = 0

ITXN_SUBMIT([2])

CTX.SetGlobal(appID: CTX.appID, key: string((byte)"g_algo_id"), val: TXN[field: CreatedAssetID, gi: 0, ai: 0])
goto main_l32

// ./example.teal:396
main_l31: // it is possible for stack to be confused
assert((1 == GLOBAL[GroupSize]))
assert((3 == TXN[field: NumAppArgs, gi: CTX.groupIndex, ai: 0]))
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"commit_end"), val: BTOI(TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 0]))
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"period_end"), val: BTOI(TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 1]))
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"fee"), val: BTOI(TXN[field: ApplicationArgs, gi: CTX.groupIndex, ai: 2]))
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"rewards_per_algo"), val: 0)
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"can_claim_rewards"), val: 0)
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"total_commitment"), val: 0)
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"total_commitment_abandoned"), val: 0)
CTX.SetGlobal(appID: CTX.appID, key: string((byte)"is_minting_paused"), val: 0)
assert((CTX.GetGlobal(appID: CTX.appID, key: string((byte)"commit_end")) < GLOBAL[LatestTimestamp]))
assert((CTX.GetGlobal(appID: CTX.appID, key: string((byte)"period_end")) < CTX.GetGlobal(appID: CTX.appID, key: string((byte)"commit_end"))))
assert((1000 <= CTX.GetGlobal(appID: CTX.appID, key: string((byte)"fee"))))
// ./example.teal:449
main_l32: // it is possible for stack to be confused
RETURN 1 // END PROGRAM

// ./example.teal:451
sub0: // it is possible for stack to be confused
CTX.SCRATCH[4] =  1
CTX.SCRATCH[3] =  1
CTX.SCRATCH[2] =  1
var_19 = Mul64(CTX.SCRATCH[3] * CTX.SCRATCH[2])
var_20 = DivMod64((0,(10 ** CTX.SCRATCH[4])), (var_19.high,var_19.low))
assert(!var_20.hiQuo)
RETSUB(DATA: var_20.loQuo)

// ./example.teal:469
sub1: // it is possible for stack to be confused
RETSUB(DATA: ((GLOBAL[ZeroAddress] == TXN[field: RekeyTo, gi: CTX.groupIndex, ai: 0]) && ((GLOBAL[ZeroAddress] == TXN[field: CloseRemainderTo, gi: CTX.groupIndex, ai: 0]) && ((addr)PMYQRSLECSJHPJC6POYFSVKF223IY7BTFZ2CPRQRR4HC4U334PTJT2LVJE == TXN[field: Sender, gi: CTX.groupIndex, ai: 0]))))

// ./example.teal:482
sub2: // it is possible for stack to be confused
RETSUB(DATA: ((GLOBAL[ZeroAddress] == TXN[field: RekeyTo, gi: 0, ai: 0]) && ((GLOBAL[ZeroAddress] == TXN[field: CloseRemainderTo, gi: 0, ai: 0]) && (0 == TXN[field: GroupIndex, gi: CTX.groupIndex, ai: 0]))))

// ./example.teal:495
sub3: // it is possible for stack to be confused
CTX.SCRATCH[6] =  TXN[field: AssetAmount, gi: 2, ai: 0]
CTX.SCRATCH[5] =  TXN[field: Sender, gi: 0, ai: 0]
RETSUB(DATA: ((GLOBAL[ZeroAddress] == TXN[field: RekeyTo, gi: 1, ai: 0]) && ((GLOBAL[ZeroAddress] == TXN[field: CloseRemainderTo, gi: 1, ai: 0]) && ((CTX.SCRATCH[6] == TXN[field: Amount, gi: 1, ai: 0]) && ((CTX.SCRATCH[5] == TXN[field: Receiver, gi: 1, ai: 0]) && ((CTX.GetGlobal(appID: CTX.appID, key: string((byte)"governance_contract_account_addr")) == TXN[field: Sender, gi: 1, ai: 0]) && ((int)pay == TXN[field: TypeEnum, gi: 1, ai: 0])))))))

// ./example.teal:523
sub4: // it is possible for stack to be confused
RETSUB(DATA: ((GLOBAL[ZeroAddress] == TXN[field: RekeyTo, gi: 2, ai: 0]) && ((GLOBAL[ZeroAddress] == TXN[field: CloseRemainderTo, gi: 2, ai: 0]) && ((GLOBAL[ZeroAddress] == TXN[field: AssetCloseTo, gi: 2, ai: 0]) && ((GLOBAL[CurrentApplicationAddress] == TXN[field: AssetReceiver, gi: 2, ai: 0]) && ((TXN[field: Sender, gi: 0, ai: 0] == TXN[field: Sender, gi: 2, ai: 0]) && ((CTX.GetGlobal(appID: CTX.appID, key: string((byte)"g_algo_id")) == TXN[field: XferAsset, gi: 2, ai: 0]) && ((int)axfer == TXN[field: TypeEnum, gi: 2, ai: 0]))))))))
```

