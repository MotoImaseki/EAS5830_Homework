import json
from web3 import Web3
from web3.middleware import geth_poa_middleware
from web3.providers.rpc import HTTPProvider

'''If you use one of the suggested infrastructure providers, the url will be of the form
now_url  = f"https://eth.nownodes.io/{now_token}"
alchemy_url = f"https://eth-mainnet.alchemyapi.io/v2/{alchemy_token}"
infura_url = f"https://mainnet.infura.io/v3/{infura_token}"
'''


def connect_to_eth():
	url = "https://mainnet.infura.io/v3/bb2d1d58ca844bef821efb503cc72c8c"  # FILL THIS IN
	w3 = Web3(HTTPProvider(url))
	assert w3.is_connected(), f"Failed to connect to provider at {url}"

	return w3


def connect_with_middleware(contract_json):
	with open(contract_json, "r") as f:
		d = json.load(f)
		d = d['bsc']
		address = d['address']
		abi = d['abi']

	# TODO complete this method
	# The first section will be the same as "connect_to_eth()" but with other selected url
	url = "https://bsc-testnet.infura.io/v3/bb2d1d58ca844bef821efb503cc72c8c"
	w3 = Web3(HTTPProvider(url))

	# The second section requires you to inject middleware into your w3 object and
	# create a contract object. Read more on the docs pages at https://web3py.readthedocs.io/en/stable/middleware.html
	# and https://web3py.readthedocs.io/en/stable/web3.contract.html

	# Inject middleware into w3 object
	w3.middleware_onion.inject(geth_poa_middleware, layer=0)
  # Check the connection
	assert w3.is_connected(), f"Failed to connect to provider at {url}"

	# Create the contract object
	contract = w3.eth.contract(address=Web3.to_checksum_address(address), abi=abi)

	return w3, contract


if __name__ == "__main__":
	connect_to_eth()
