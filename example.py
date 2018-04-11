from am_smart_contracts_interface.am import AMContractInterface

am = AMContractInterface()
test_balance = am.get_amc_balance("0x4D8Cf569C2fd7C436F44dEa3763C6BF967358e8D")
print("Balance of ico: " +str(test_balance))
test_data = am.get_transaction_data("0x2797A13C01F62b8b53d24c763363785128835aFf")
assert(test_data == '0x33b5fa750000000000000000000000002797a13c01f62b8b53d24c763363785128835aff')
print("Message data for transaction: " + test_data)
test_total_invest = am.get_total_invested_ether()
print("Total invested ether: " + str(test_total_invest))
pass