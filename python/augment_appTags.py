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

# The ID of a Hyperglance resource (get this from the URL on the Diagram page or from ./diagram-to-json.py)
node_UID = "AcmeApp|example topology|NODE|network|node3"

# JSON for attaching apptags (Tag Views) to a Hyperglance resource
JSON = {
    "appTags": [
        {
            "UID": node_UID,
            "appTags": ["AugmentedAppTag1", "AugmentedAppTag2"]
        }
    ]
}


#####################
# EXECUTION START ->
#####################

# Post JSON to Hyperglance
print('Augmenting App Tags')
r = requests.put(HYPERGLANCE_URL + '/hgapi/augment', json=JSON, auth=API_KEY, verify=False)

# Check that everything went okay
if r.status_code != 200:
    print('Error calling API: ' + str(r.status_code))
    print(r.text)
    quit()

if not (r.text == 'Augmentation Successful!'):
    print('Error adding account to Hyperglance:')
    print(json.dumps(r.json(), indent=2))
    quit()

print(r.text)

