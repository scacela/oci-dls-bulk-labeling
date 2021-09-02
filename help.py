print(
'''
Data Labeling Service (DLS) Bulk-Labeling tool

Assign your own variables in config.py and then
bulk label your DLS Dataset records with:

python3 main.py

Valid values for labeling_algorithm are:

"first_letter": the first letter of the DLS
	Dataset record's name must match the first
	letter of the label that it will be
	annotated with.
'''
)