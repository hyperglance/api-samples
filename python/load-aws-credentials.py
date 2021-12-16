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
API_KEY = ('my-api-user', '712399db-9dfd-4d65-a831-f00b42281093')

# Any friendly name for the AWS account
AWS_ACCOUNT_ALIAS = 'My AWS'

# JSON for connecting Hyperglance with commercial AWS accounts
# [Recommended]: Adjust the list of regions for Hyperglance to ingest
JSON = {
		"accountAlias": AWS_ACCOUNT_ALIAS,
		"regions": [
			"us-east-1",
			"us-east-2",
			"us-west-1",
			"us-west-2",
			"eu-west-1",
			"eu-west-2",
			"eu-west-3",
			"eu-central-1",
			"eu-north-1",
			"ap-east-1",
			"ap-south-1",
			"ap-southeast-1",
			"ap-southeast-2",
			"ap-northeast-1",
			"ap-northeast-2",
			"ap-northeast-3",
			"sa-east-1",
			"ca-central-1",
			"me-south-1",
			"af-south-1"
		],
		
		# [Optional]: Provide a cross-account role ARN to connect Hyperglance with accounts external to the one it is running in
		#             Blank here will connect Hyperglance with the account hosting the Instance.
		"roleARN": "",
		
		# [Optional]: If Hyperglance is hosted outside of AWS you can connect using Access/Secret key-pair:
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
	print('.', end='', flush=True)
	time.sleep(3)

print('Hyperglance is now ready!')
