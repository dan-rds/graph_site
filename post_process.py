#!/usr/bin/env python3
'''-------------------------------------
post_process.py

    by Daniel Richards (ddrichar@ucsc.edu)
       on 6-19-2018
-------------------------------------- 
'''
import yaml, json, sys, os
dirs = os.listdir('./glance/tree_data/')

print(dirs)
head = {}
heads_children = []
for parent_dir in dirs:
	dir_dict = {'name': parent_dir, 'children':[]}

#	dir_dict = {'name': parent_dir, 'children':[]}
	reports = os.listdir('./glance/tree_data/' + parent_dir)
	for f in reports:
		if 'h' in f:
			json_file = open('./glance/tree_data/' + parent_dir + "/" + f).read()
			head = json.loads(json_file)
			head["children_hardware"] = head["children"]
		else:
			json_file = open('./glance/tree_data/' + parent_dir + "/" + f).read()
			heads_children.append(json.loads(json_file))
	print (reports)
head["children"] = heads_children
with open("temp.json", 'w') as f:
	json.dump(head, f,indent = 4)
# blh0_Digilab_2018-06-19.yml
'''with open('device.yaml', 'r') as y_file:
	data_json = (json.dumps(yaml.load(y_file), sort_keys=True, indent=2))
	with open('/Users/daniel/graph/tree_temp.json', 'w') as tr:
		tr.write(data_json)'''