import datetime
import sys
sys.path.append("..")
from config import *
import dls_create_annotation
import re

def dirname_to_label(name):
	regex=re.compile(r'^([^/]*)/.*$')
	for l in labels:
		dirname = regex.match(name).groups()[0]
		if l.lower() == dirname.lower():
			return dirname

def main(name, record_id):
	label = dirname_to_label(name=name)
	if label:
		dls_create_annotation.main(label=label, record_id=record_id)
	else:
		print("current time: " + str(datetime.datetime.now()))
		print("No label match for record " + str(name))
		print("with id: " + str(record_id))
		print()