print(
'''
Data Labeling Service (DLS) Bulk-Labeling tool

1. Install the OCI Python SDK using the instructions
provided here:

https://docs.oracle.com/en-us/iaas/tools/python/2.45.1/installation.html

2. Set up your OCI config file using the instructions
provided here:

https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File

3. Assign your own variables in config.py

4. Bulk label your DLS Dataset records with:

python3 main.py

Valid values for labeling_algorithm are:

"first_letter": the first letter of the DLS
	Dataset record's name must match the first
	letter of the label that it will be
	annotated with.
'''
)