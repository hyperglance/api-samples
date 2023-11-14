import requests
from urllib.parse import urlencode

requests.packages.urllib3.disable_warnings()

###################
# CONFIGURATION ->
###################

# URL to your Hyperglance Server
HYPERGLANCE_URL = "https://10.0.0.1"

# Unique Hyperglance API name/key pair
# Generate yours here: https://hyperglanceIP/#/admin/hgapi
API_KEY = ('my-api-user', '77415974-1b16-4ee8-af98-6be979611158')

# filtering options - individual components are optional
FILTERS = {
    "datasource": 'Amazon',
    "account": None,
    "tag_key":'zest',
    "tag_value":'test',
    "type": None
}

FILTERS = {key: value for key, value in FILTERS.items() if value is not None}

url_params = urlencode(FILTERS)

#####################
# EXECUTION START ->
#####################

# Post JSON to Hyperglance
print('Searching Hyperglance inventory')
r = requests.get(f"{HYPERGLANCE_URL}/hgapi/inventory?{url_params}", auth=API_KEY, verify=False)

# Check that everything went okay
if r.status_code != 200:
	print('Error calling API: ' + str(r.status_code))
	print(r.text)
	quit()
	
print(r.content)
