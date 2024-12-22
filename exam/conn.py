from web3 import Web3
from contract_info import address_contract, abi
from web3.middleware import ExtraDataToPOAMiddleware

class Func():
    def __init__(self, rpc_url = 'http://127.0.0.1:8545'):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
        self.w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer= 0)
        self.contract = self.w3.eth.contract(address= address_contract, abi = abi)

    def func_get_num(self):
        return self.contract.functions.get_prop_number().call()
    
    def func_get_prop(self, p_id):
        return self.contract.functions.get_properties(p_id).call()
    
    def func_create_prop(self, p_owner, p_type, year, gos_num):
        try:
            tx = self.contract.functions.create_property(p_owner, p_type, year, gos_num).transact({'from':'0xf0BEF8734Cb8446d8BEdB4Fa6E74a07d7879cdFa'})
            self.w3.eth.wait_for_transaction_receipt(tx)
        except Exception as e:
            print(f'error creating property: {e}')


# con = Func()
# num = con.func_get_num()
# print(num)

# p_owner = '0xf0BEF8734Cb8446d8BEdB4Fa6E74a07d7879cdFa'
# p_type = 'airplane'
# year = 1999
# gos_num = 'f321fh'
# con.func_create_prop(p_owner, p_type, year, gos_num)
# print('имущество добавлено')

# num = con.func_get_num()
# print(num)

# data = con.func_get_prop(3)
# print(data)
