# Python Examples [Hyperglance API]

Use these Python samples to get started with the Hyperglance API:

* Use the `load-*-credentials.py` scripts to load cloud credentials into Hyperglance to connect it with your cloud platform.
* Use the `diagram-to-*.py` scripts to export the Hyperglance diagram into PNG, VSDX or JSON.

See our [below examples](#Examples-Using-These-Scripts) of combining these two kinds of scripts together to programmatically generate a diagram of an AWS or Azure environment.


## Pre-Setup

To run these samples you will need [Python 3](https://www.python.org/).

1. Clone or [download](https://github.com/hyperglance/api-samples/archive/master.zip) this repository.


2. Install the libs:

    ```
    pip install -r requirements.txt
    ```

3. [Generate your Hyperglance API key.](https://support.hyperglance.com/knowledge/getting-started-with-the-hyperglance-api)


## Configuring a Sample Script

Each `.py` file is an individal sample and has a `CONFIGURATION` section at the top of each file. To run one you will first need to open it and adjust the variables in that section.

All scripts have these configuration properties in common:

* `HYPERGLANCE_URL`: Set the URL to your Hyperglance Instance/VM.
* `API_KEY`: Set the name and generated secret for your [Hyperglance API Key](https://support.hyperglance.com/knowledge/getting-started-with-the-hyperglance-api).


### Configuring the load credentials scripts

* The `load-aws*-credentials.py` scripts require you to adjust the `JSON` variable to set the regions, any cross-account Role ARN or acccess/secret keys.

    > __Note:__ The details required here are the same as the ones needed when adding an AWS account via the Hyperglance UI. [[Read More]](https://support.hyperglance.com/knowledge/adding-new-aws-accounts-to-hyperglance)

* The `load-azure-credentials.py` script requires you to adjust the `JSON` variable to set your Subscription ID as well as an AzureAD Application ID & associated secret key.

    > __Note:__ The details required here are the same as those needed when adding an Azure subscription via the Hyperglance UI. [[Read More]](https://support.hyperglance.com/knowledge/azure-collector-setup)


### Configuring the diagram export scripts

`diagram-to-json.py` does not require any further configuration and will print the entire inventory as JSON.

By default the `diagram-to-png.py` and `diagram-to-vsdx.py` scripts will export an entire AWS or Azure diagram - you __must__ set the `TO_EXPORT` variable to export either an AWS or Azure diagram.

Both scripts come with a variety of alternative `JSON` payload examples that demonstrate other use-cases:

* Export entire AWS or Azure diagram according to `TO_EXPORT`. (default)
* Export an AWS Account.
* Export an AWS VPC.
* Export an Azure Subscription.
* Export an Azure Resource Group.
* Export a Hyperglance [tag-view](https://support.hyperglance.com/knowledge/tag-view).

These other JSON examples are commented-out in the scripts so you can uncomment and adjust them as desired.

## Examples Using These Scripts

### __Example:__ Programmatically add new AWS account credentials and export the resulting diagram

```
# Add AWS credentials
python load-aws-credentials.py

# Or use this for AWS GovCloud
# python load-aws-govcloud-credentials.py 

# In the configuration section of the below scripts set TO_EXPORT='Amazon'

# Export to PNG
python diagram-to-png.py

# Export to VSDX
python diagram-to-vsdx.py
```

### __Example:__ Programmatically add new Azure subscription credentials and export the resulting diagram

```
# Add Azure subscription credentials
python load-azure-credentials.py

# In the configuration section of the below scripts set TO_EXPORT='Azure'

# Export to PNG
python diagram-to-png.py

# Export to VSDX
python diagram-to-vsdx.py
```

### __Example:__ Export a pre-existing diagram

If Hyperglance is already setup and diagramming your cloud environment use this to export that diagram. This works whether you connected Hyperglance to your cloud using the API or using the UI.

```
# In the configuration section of the below scripts set TO_EXPORT to either 'Amazon' or 'Azure' as appropriate.

# Export to PNG
python diagram-to-png.py

# Export to VSDX
python diagram-to-vsdx.py
```