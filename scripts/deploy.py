from brownie import FundMe, MockV3Aggregator, network, config
from scripts.helpful_script import deploy_mocks, get_account, LOCAL_BLOCKCAHIN_ENVIRONMENTS
from web3 import Web3

def deploy_fund_me():
    account=get_account() 
    print("We are here")
    #fundme.deploy deploys from rinkedby wallet address 
    #The address is that of the V3 Aggregator and passes it directly to the constructor
    #If we are on a persistent network like rinkeby, use the associated address
    #otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCAHIN_ENVIRONMENTS:
        price_feed_address=config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address= MockV3Aggregator[-1].address
        print(price_feed_address)
        print("Mocks Deployed")
    fund_me=FundMe.deploy(price_feed_address,{"from":account}, publish_source=config["networks"][network.show_active()].get("verify"))
    #fund_me.address is the adress you are sending to 
    print(f"Contract deployed to {fund_me.address}")
    return fund_me
def main():
    deploy_fund_me()
    