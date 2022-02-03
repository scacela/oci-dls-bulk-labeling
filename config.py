# for help, run:
# python3 help.py

# config file path
config_file_path="~/.oci/config"
# config file profile
config_profile="DEFAULT"
# region identifier of DLS Dataset
region_identifier="us-ashburn-1"
# compartment where DLS Dataset exists
compartment_id = "<Compartment OCID>"
# ocid of the DLS Dataset
dataset_id = "<DLS Dataset OCID>"
# an array where the elements are all of the labels that you will use to annotate records in your DLS Dataset with. Each element is a separate label.
labels = ["<label 1>", "<label 2>", "<label 3>"]
# the algorithm that will be used to assign labels to DLS Dataset records
labeling_algorithm = "first_letter"
# maximum number of DLS Dataset records that can be retrieved from the list_records API operation for labeling
# limit=1000 is the hard limit for list_records
list_records_limit = 1000