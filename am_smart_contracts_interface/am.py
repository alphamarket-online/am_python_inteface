import web3
import am_smart_contracts_interface.am_abi as am_abi


class AMContractInterface:
    def __init__(self):
        # w3 = web3.Web3(web3.HTTPProvider("https://rinkeby.infura.io/xxxxxxxxx")) # Test network
        w3 = web3.Web3(web3.HTTPProvider("https://api.myetherapi.com/eth")) # Real network
        self._amc_contract = w3.eth.contract(
            abi=am_abi.amc_abi,
            # address="0xc4aB0302F2BeA6DE476614f7c20DaE8F35D03A08") # Test network
            address="0xc26aA9AD649C5Def6d7f94fc46667F70210fE565") # Real network
        self._am_ico_contract = w3.eth.contract(
            # abi=am_abi.test_am_ico_abi, # Test network
            abi=am_abi.am_ico_abi, # Real network
            # address="0x9A0f9bdBAf42e98172F6CDC07caAFa9a7c75762c") # Test network
            address="0x4D8Cf569C2fd7C436F44dEa3763C6BF967358e8D") # Real network

    def get_amc_balance(self, address):
        return self._amc_contract.functions.balanceOf(address).call()

    def get_total_invested_ether(self):
        return self._am_ico_contract.functions.totalInvestment().call()

    def get_transaction_data(self, referer_address="0x0000000000000000000000000000000000000000"):
        return self._am_ico_contract.encodeABI(fn_name='buyTokensWithRef', args=[referer_address])
