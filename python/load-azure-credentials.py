import requests
import json
import time
import urllib.parse

requests.packages.urllib3.disable_warnings()


###################
# CONFIGURATION ->
###################

# URL to your Hyperglance Server
HYPERGLANCE_URL = "https://10.0.0.1"

# Unique Hyperglance API name/key pair
# Generate yours here: https://hyperglanceIP/#/admin/hgapi
API_KEY = ('my-api-user', '77415974-1b16-4ee8-af98-6be979611158')

# Any friendly name for the Azure subscription
SUB_ALIAS = 'My Azure Subscription'

# [Required]: Find out what your sib/app/key are here: https://support.hyperglance.com/knowledge/azure-collector-setup
# JSON for connecting Hyperglance with Azure subscriptions
JSON = {
	"accountAlias": SUB_ALIAS,
	"subscriptionId": "enter your azure subscription id here",
	"applicationId": "enter your azure application id here",
	"key": "enter your azure secret key here"
}


#####################
# EXECUTION START ->
#####################

# Post JSON to Hyperglance
print('Adding Azure account to Hyperglance')
r = requests.post(HYPERGLANCE_URL + '/hgapi/integrations/Azure', json=JSON, auth=API_KEY, verify=False)

# Check that everything went okay
if r.status_code != 200:
	print('Error calling API: ' + str(r.status_code))
	print(r.text)
	quit()
if not r.json()['isSuccess']:
	print('Error adding subscription to Hyperglance:')
	print(json.dumps(r.json(), indent=2))
	quit()

# Poll Hyperglance until it has finished ingesting cloud data
print('Waiting for Hyperglance to ingest cloud data...', end='', flush=True)
while True:
	status = requests.get(HYPERGLANCE_URL + '/hgapi/integrations/Azure/{alias}/statistics'.format(alias=urllib.parse.quote(SUB_ALIAS)), auth=API_KEY, verify=False)
	if status.json()['numOfCompletedCycles'] > 1:
		break;
	print('.', end='', flush=True)
	time.sleep(3)

print('Hyperglance is now ready!')
