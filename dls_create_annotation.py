# input vars: dataset id and compartment id

# import packages

import sys
import json
import oci
from config import *
from oci.data_labeling_service_dataplane.data_labeling_client import DataLabelingClient
from oci.data_labeling_service.data_labeling_management_client import DataLabelingManagementClient
from oci.data_labeling_service_dataplane.models import GenericEntity
from oci.data_labeling_service_dataplane.models import Label
from oci.data_labeling_service_dataplane.models import CreateAnnotationDetails

def main(label, record_id):
    # client definition
    def init_dls_dp_client(config, service_endpoint, retry_strategy):
        dls_client = DataLabelingClient(config=config, service_endpoint=service_endpoint, retry_strategy=retry_strategy)
        return dls_client

    config_file = oci.config.from_file(config_file_path, config_profile)
    service_endpoint_dp = f"https://dlsprod-dp.{region_identifier}.oci.oraclecloud.com"
    retry_strategy = oci.retry.DEFAULT_RETRY_STRATEGY
    
    dls_dp_client = init_dls_dp_client(config_file, service_endpoint_dp, retry_strategy)

    # payload
    labels_obj = [Label(label=label)]
    entity_type = "GENERIC"
    entity_obj = [GenericEntity(entity_type=entity_type, labels=labels_obj)]
    
    create_annotation_details_obj = CreateAnnotationDetails(record_id=record_id, compartment_id=compartment_id, entities=entity_obj)

    # api call
    print(create_annotation_details_obj)
    try:
        anno_response = dls_dp_client.create_annotation(create_annotation_details=create_annotation_details_obj)
    except Exception as error:
        anno_response = error
        print(anno_response)
    return anno_response.data