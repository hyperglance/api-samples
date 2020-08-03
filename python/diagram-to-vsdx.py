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

# Name of the file to generate
FILENAME = "hyperglance-{}.vsdx".format(datetime.datetime.now().strftime('%Y%m%d%H%M%S'))

# Do you want to export AWS (Amazon) or Azure?
TO_EXPORT = 'Amazon' # or 'Azure'

# Example: Export the entire Amazon/Azure diagram
JSON = {
	"datasource": "Datasource_Group",
	"account": TO_EXPORT,
	"id": TO_EXPORT
}

# Example: Export one AWS Account
#JSON = {
#	"datasource": "Amazon",
#	"account": "My AWS",
#	"id": "account:My AWS"
#}

# Example: Export an AWS VPC
#JSON = {
#	"datasource": "Amazon",
#	"account": "My AWS",
#	"id": "vpc-123456789"
#}

# Example: Export one Azure Subscription
#JSON = {
#	"datasource": "Azure",
#	"account": "My Azure Subscription",
#	"id": "sub:My Azure Subscription"
#}

# Example: Export one Azure Resource Group
# Note: Resource Groups are considered tag-views in Hyperglance (see next example)
#JSON = {
#	"datasource": "Azure",
#	"tagViewIds": ["Resource Group: name-of-my-resource-grp"]
#}

# Example: Export a tag-view
# See also: https://support.hyperglance.com/knowledge/tag-view
#JSON = {
#	"datasource": "Amazon", # or "Azure"
#	"tagViewIds": ["Name of a Tag View"]
#}


#####################
# EXECUTION START ->
#####################

# Call export API
print('Exporting diagram to VSDX...')
r = requests.post(HYPERGLANCE_URL + '/hgapi/export-vsdx', json=JSON, auth=API_KEY, verify=False)

# Check that everything went okay
if r.status_code != 200:
	print('Error calling API: ' + str(r.status_code))
	print(r.text)
	quit()

# Write to file
with open(FILENAME, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)

print('Export complete: ' + FILENAME)
