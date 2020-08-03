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
	"values": {
		"Account Alias": AWS_ACCOUNT_ALIAS,
		"Regions": [
			"US East (N. Virginia)",
			#"US East (Ohio)",
			#"US West (N. California)",
			#"US West (Oregon)",
			#"EU (Ireland)",
			#"EU (London)",
			#"EU (Paris)",
			#"EU (Frankfurt)",
			#"EU (Stockholm)",
			#"Asia Pacific (Hong Kong)",
			#"Asia Pacific (Mumbai)",
			#"Asia Pacific (Singapore)",
			#"Asia Pacific (Sydney)",
			#"Asia Pacific (Tokyo)",
			#"Asia Pacific (Seoul)",
			#"Asia Pacific (Osaka-Local)",
			#"South America (Sao Paulo)",
			#"Canada (Central)",
			#"Middle East (Bahrain)",
			#"Africa (Cape Town)"
		],
		
		# [Optional]: Provide a cross-account role ARN to connect Hyperglance with accounts external to the one it is running in:
		#             Blank here will connect Hyperglance with the account hosting the Instance.
		"Role ARN": "",
		
		# [Optional]: If Hyperglance is hosted outside of AWS you can connect using Access/Secret key-pair:
		#"Access Key": "ABCDEFGHIJKLMNOPQRST",
		#"Secret Key": "aBcDeFgHiJkLmNoPqRsTuVwXyZ+aEiOu+123456789"
	}
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
print('Waiting for Hyperglance to ingest cloud data...', end='')
while True:
	status = requests.get(HYPERGLANCE_URL + '/hgapi/integrations/Amazon/{alias}/statistics-and-status'.format(alias=urllib.parse.quote(AWS_ACCOUNT_ALIAS)), auth=API_KEY, verify=False)
	if status.json()['collectionStats']['numOfCompletedCollections'] > 1:
		break;
	print('.', end='')
	time.sleep(3)

print('Hyperglance is now ready!')
