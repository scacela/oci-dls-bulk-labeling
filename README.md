# oci-dls-bulk-labeling
## Annotate a bulk number of records in an OCI Data Labeling Service (DLS) Dataset with labels.

### Data Labeling Service (DLS) Bulk-Labeling tool

1. Set up your [OCI config file](https://docs.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File).
2. Assign your own variables in <b>config.py</b>.
3. bulk label your DLS Dataset records with:

	```
	python3 main.py
	```
	\
	Valid values for labeling_algorithm are:\
	\
	<b>"first_letter"</b>: the first letter of the DLS
		Dataset record's name must match the first
		letter of the label that it will be
		annotated with.