from scripts.helpful_script import LOCAL_BLOCKCAHIN_ENVIRONMENTS, get_account
from scripts.deploy import deploy_fund_me
import pytest
from brownie import network, accounts, exceptions

from brownie import network
def test_can_fund_and_withdraw():
    account=get_account()
    fund_me=deploy_fund_me()
    entrance__fee=fund_me.getEntranceFee()+100
    tx=fund_me.fund({"from":account, "value":entrance__fee})
    tx.wait(1)
    assert fund_me.addressToAmountFunded(account.address)==entrance__fee
    tx2=fund_me.withdraw({"from":account})
    tx2.wait(1)
    assert fund_me.addressToAmountFunded(account.address)==0

def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCAHIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    account=get_account()
    fund_me=deploy_fund_me()
    bad_actor=accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from":bad_actor})