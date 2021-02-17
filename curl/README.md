# CURL Examples [Hyperglance API]

CURL commandline examples for exporting a Hyperglance diagram to a PNG or VSDX.

## Getting Started

For these examples to work you must already have a diagram in Hyperglance that you want to export:

* [See instructions for connecting Hyperglance to AWS](https://support.hyperglance.com/knowledge/adding-new-aws-accounts-to-hyperglance)
    * __Note:__ In these examples we assume the Account Alias was set to "__My AWS__".
* [See instructions for connecting Hyperglance to Azure](https://support.hyperglance.com/knowledge/azure-collector-setup)
    * __Note:__ In these examples we assume the Subscription Alias was set to "__My Azure Subscription__".
* Or use our [Python samples](../python) to connect an account or subscription programmatically.

You also need to [generate your Hyperglance API key](https://support.hyperglance.com/knowledge/getting-started-with-the-hyperglance-api) and set the key's name followed by a colon followed by the generated secret as the value for CURL's `--user` parameter. For example: `--user my-api-user:77415974-1b16-4ee8-af98-6be979611158`.


Choose a use-case to get started:

1. [Export entire AWS diagram](#Export-entire-AWS-diagram)
1. [Export a single AWS account](#Export-a-single-AWS-account)
1. [Export an AWS VPC](#Export-an-AWS-VPC)
1. [Export entire Azure diagram](#Export-entire-Azure-diagram)
1. [Export a single Azure subscription](#Export-a-single-Azure-subscription)
1. [Export an Azure Resource Group](#Export-an-Azure-Resource-Group)
1. [Export a Hyperglance Tag View](#Export-Resources-with-Certain-Tags)

## Use-Case Examples

### Export entire AWS diagram

To PNG:
```bash
curl -fk https://10.0.0.1/hgapi/export-png \
  --output hyperglance.png \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "datasource":"Datasource_Group", "account":"Amazon", "id":"Amazon" }' \
  --request POST --header "Content-Type: application/json"
```

To VSDX:
```bash
curl -fk https://10.0.0.1/hgapi/export-vsdx \
  --output hyperglance.vsdx \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "datasource":"Datasource_Group", "account":"Amazon", "id":"Amazon" }' \
  --request POST --header "Content-Type: application/json"
```

### Export a single AWS account

To PNG:
```bash
curl -fk https://10.0.0.1/hgapi/export-png \
  --output hyperglance.png \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "datasource":"Amazon", "account":"My AWS", "id":"account:My AWS" }' \
  --request POST --header "Content-Type: application/json"
```

To VSDX:
```bash
curl -fk https://10.0.0.1/hgapi/export-vsdx \
  --output hyperglance.vsdx \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "datasource":"Amazon", "account":"My AWS", "id":"account:My AWS" }' \
  --request POST --header "Content-Type: application/json"
```

### Export an AWS VPC

To PNG:
```bash
curl -fk https://10.0.0.1/hgapi/export-png \
  --output hyperglance.png \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "datasource":"Amazon", "account":"My AWS", "id":"vpc-123456789" }' \
  --request POST --header "Content-Type: application/json"
```

To VSDX:
```bash
curl -fk https://10.0.0.1/hgapi/export-vsdx \
  --output hyperglance.vsdx \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "datasource":"Amazon", "account":"My AWS", "id":"vpc-123456789" }' \
  --request POST --header "Content-Type: application/json"
```

### Export entire Azure diagram

To PNG:
```bash
curl -fk https://10.0.0.1/hgapi/export-png \
  --output hyperglance.png \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "datasource":"Datasource_Group", "account":"Azure", "id":"Azure" }' \
  --request POST --header "Content-Type: application/json"
```

To VSDX:
```bash
curl -fk https://10.0.0.1/hgapi/export-vsdx \
  --output hyperglance.vsdx \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "datasource":"Datasource_Group", "account":"Azure", "id":"Azure" }' \
  --request POST --header "Content-Type: application/json"
```

### Export a single Azure subscription

To PNG:
```bash
curl -fk https://10.0.0.1/hgapi/export-png \
  --output hyperglance.png \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "datasource":"Azure", "account":"My Azure Subscription", "id":"sub:My Azure Subscription" }' \
  --request POST --header "Content-Type: application/json"
```

To VSDX:
```bash
curl -fk https://10.0.0.1/hgapi/export-vsdx \
  --output hyperglance.vsdx \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "datasource":"Azure", "account":"My Azure Subscription", "id":"sub:My Azure Subscription" }' \
  --request POST --header "Content-Type: application/json"
```

### Export an Azure Resource Group

In this example the name of the resource group is "name-of-my-resource-grp". Azure Resource Groups are considered tag-views in Hyperglance (see [Export a tag-view](#export-a-tag-view))

To PNG:
```bash
curl -fk https://10.0.0.1/hgapi/export-png \
  --output hyperglance.png \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "datasource":"Azure", "tagViewIds": ["Resource Group: name-of-my-resource-grp"] }' \
  --request POST --header "Content-Type: application/json"
```

To VSDX:
```bash
curl -fk https://10.0.0.1/hgapi/export-vsdx \
  --output hyperglance.vsdx \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "datasource":"Azure", "tagViewIds": ["Resource Group: name-of-my-resource-grp"] }' \
  --request POST --header "Content-Type: application/json"
```

### Export Resources with Certain Tags

To PNG:
```bash
curl -fk https://10.0.0.1/hgapi/export-png \
  --output hyperglance.png \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "tags":[{"key":"MyTag", "value":"TheValue"}], "includeDependencies":true }' \
  --request POST --header "Content-Type: application/json"
```

To VSDX:
```bash
curl -fk https://10.0.0.1/hgapi/export-vsdx \
  --output hyperglance.vsdx \
  --user my-api-user:77415974-1b16-4ee8-af98-6be979611158 \
  --data '{ "tags":[{"key":"MyTag", "value":"TheValue"}], "includeDependencies":true }' \
  --request POST --header "Content-Type: application/json"
```
