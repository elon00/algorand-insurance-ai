# PyTeal / Algorand AVM Micro-Insurance Contract
from pyteal import *

def approval_program():
    on_creation = Seq([
        App.globalPut(Bytes("oracle"), Txn.sender()),
        App.globalPut(Bytes("total_policies"), Int(0)),
        App.globalPut(Bytes("total_claims_paid"), Int(0)),
        Approve()
    ])

    underwrite = Seq([
        Assert(Gtxn[0].type_enum() == TxnType.Payment),
        Assert(Gtxn[0].amount() >= Int(10000)), # Min 0.01 ALGO
        App.globalPut(
            Bytes("total_policies"),
            App.globalGet(Bytes("total_policies")) + Int(1)
        ),
        Approve()
    ])

    payout_claim = Seq([
        Assert(Txn.sender() == App.globalGet(Bytes("oracle"))),
        App.globalPut(
            Bytes("total_claims_paid"),
            App.globalGet(Bytes("total_claims_paid")) + Int(1)
        ),
        Approve()
    ])

    return Cond(
        [Txn.application_id() == Int(0), on_creation],
        [Txn.on_completion() == OnComplete.NoOp, underwrite],
        [Txn.on_completion() == OnComplete.OptIn, payout_claim]
    )

def clear_state_program():
    return Approve()

if __name__ == "__main__":
    print(compileTeal(approval_program(), Mode.Application, version=8))
