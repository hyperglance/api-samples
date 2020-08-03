import requests
import datetime

requests.packages.urllib3.disable_warnings()


###################
# CONFIGURATION ->
###################

# URL to your Hyperglance Server
HYPERGLANCE_URL = "https://10.0.0.1"

# Unique Hyperglance API name/key pair
# Generate yours here: https://hyperglanceIP/#/admin/hgapi
API_KEY = ('my-api-user', '77415974-1b16-4ee8-af98-6be979611158')


#####################
# EXECUTION START ->
#####################

# Call export API
r = requests.get(HYPERGLANCE_URL + '/hgapi/network', auth=API_KEY, verify=False)

# Check that everything went okay
if r.status_code != 200:
	print('Error calling API: ' + str(r.status_code))
	print(r.text)
	quit()

# Print JSON
print(r.json())
