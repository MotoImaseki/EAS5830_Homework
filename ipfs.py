import requests
import json

# Pinata API credentials
PINATA_API_KEY = "your_pinata_api_key795092631b879aad68fb"
PINATA_API_SECRET = "4ba96fa1fe7f413db125a171feaff07deafeabd61261779a12d991f0c0c81790"

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE

  # Convert the dictionary to JSON
  json_data = json.dumps(data)
  
  # Define the Pinata API URL for pinning JSON
  url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    
  # Headers for authentication
  headers = {
    'pinata_api_key': PINATA_API_KEY,
    'pinata_secret_api_key': PINATA_API_SECRET,
    'Content-Type': 'application/json'
  }
    
  # Send the JSON data to Pinata
  try:
    response = requests.post(url, data=json_data, headers=headers)
    response.raise_for_status()
  except requests.RequestException as e:
    raise RuntimeError(f"Failed to pin data to IPFS using Pinata: {e}")
    
  # Extract the CID from the response
  cid = response.json()['IpfsHash']

	return cid

def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	#YOUR CODE HERE	

  # Define the IPFS gateway URL
  url = f"https://gateway.pinata.cloud/ipfs/{cid}"
    
  try:
    response = requests.get(url)
    response.raise_for_status()
  except requests.RequestException as e:
    raise RuntimeError(f"Failed to fetch data from IPFS: {e}")
    
  # Parse the response as JSON
  try:
    data = response.json()
  except json.JSONDecodeError:
    raise RuntimeError("Failed to parse the fetched data as JSON")
  
	assert isinstance(data,dict), f"get_from_ipfs should return a dict"

	return data
