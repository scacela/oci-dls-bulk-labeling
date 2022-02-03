# list records

# import packages
import sys
import json
import oci
from config import *
from oci.data_labeling_service_dataplane.data_labeling_client import DataLabelingClient
from oci.data_labeling_service.data_labeling_management_client import DataLabelingManagementClient

def main():
    # client definition
    def init_dls_dp_client(config, service_endpoint, retry_strategy):
        dls_client = DataLabelingClient(config=config, service_endpoint=service_endpoint, retry_strategy=retry_strategy)
        return dls_client

    config_file = oci.config.from_file(config_file_path, config_profile)
    service_endpoint_dp = f"https://dlsprod-dp.{region_identifier}.oci.oraclecloud.com"
    retry_strategy = oci.retry.DEFAULT_RETRY_STRATEGY

    dls_dp_client = init_dls_dp_client(config_file, service_endpoint_dp, retry_strategy)

    # api call
    try:
        # limit parameter has an implicit value of 10 if not included
        anno_response = dls_dp_client.list_records(compartment_id=compartment_id, dataset_id=dataset_id, is_labeled=False, limit=list_records_limit)
    except Exception as error:
        anno_response = error
        print(anno_response)

    # manage the json
    data = json.loads(str(anno_response.data))
    # record's full display name
    names = [dls_dataset_record["name"] for dls_dataset_record in data["items"]]

    # ocid of each record
    ids = [dls_dataset_record["id"] for dls_dataset_record in data["items"]]

    return(names, ids, len(ids))
