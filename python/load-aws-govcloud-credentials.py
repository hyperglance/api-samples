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

# Any friendly name for the AWS account
AWS_ACCOUNT_ALIAS = 'My Gov AWS'

# JSON for connecting Hyperglance with GovCloud AWS accounts
JSON = {
	"accountAlias": AWS_ACCOUNT_ALIAS,
	"govCloudRegions": [
		 "us-gov-east-1",
		 "us-gov-west-1"
	],
	
	# [Optional]: If Hyperglance is hosted outside of AWS you can connect it to AWS using Access/Secret key-pair:
	#"accessKey": "ABCDEFGHIJKLMNOPQRST",
	#"secretKey": "aBcDeFgHiJkLmNoPqRsTuVwXyZ+aEiOu+123456789",
			
	# [Optional]: Specify if this account should only ingest billing data and not inventory data
	"isBillingOnly": False,
	
	# [Optional]: Organize accounts by grouping related accounts together. E.g. "accountGroups": ["Production", "US", "Team X"]
	"accountGroups": []
}


#####################
# EXECUTION START ->
#####################

# Post JSON to Hyperglance
print('Adding AWS account to Hyperglance')
r = requests.post(HYPERGLANCE_URL + '/hgapi/integrations/Amazon', json=JSON, auth=API_KEY, verify=False)

# Check that everything went okay
if r.status_code != 200:
	print('Error calling API: ' + str(r.status_code))
	print(r.text)
	quit()
if not r.json()['isSuccess']:
	print('Error adding account to Hyperglance:')
	print(json.dumps(r.json(), indent=2))
	quit()

# Poll Hyperglance until it has finished ingesting cloud data
print('Waiting for Hyperglance to ingest cloud data...', end='', flush=True)
while True:
	status = requests.get(HYPERGLANCE_URL + '/hgapi/integrations/Amazon/{alias}/statistics'.format(alias=urllib.parse.quote(AWS_ACCOUNT_ALIAS)), auth=API_KEY, verify=False)
	if status.json()['numOfCompletedCycles'] > 1:
		break;
	print(".", end="", flush=True)
	time.sleep(3)

print('Hyperglance is now ready!')
