# oci-dls-bulk-labeling
## Annotate a bulk number of records in an OCI Data Labeling Service (DLS) Dataset with labels.

### Data Labeling Service (DLS) Bulk-Labeling tool

Assign your own variables in <b>config.py</b> and then
bulk label your DLS Dataset records with:

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