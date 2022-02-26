import datetime
import sys
sys.path.append("..")
from config import *
import dls_create_annotation
import re

def match_to_label(name):
	regex=re.compile(first_match_regex_pattern)
	for l in labels:
		match = regex.match(name).groups()[0]
		if l == match:
			return l

def main(name, record_id):
	label = match_to_label(name=name)
	if label:
		dls_create_annotation.main(label=label, record_id=record_id)
	else:
		print("current time: " + str(datetime.datetime.now()))
		print("No label match for record " + str(name))
		print("with id: " + str(record_id))
		print()