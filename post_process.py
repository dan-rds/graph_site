#!/usr/bin/env python3
'''-------------------------------------
post_process.py

    by Daniel Richards (ddrichar@ucsc.edu)
       on 6-19-2018
-------------------------------------- 
'''
# import yaml, json, sys, os
# dirs = os.listdir('./glance/tree_data/')

# print(dirs)
# root = {"name": " ", "stroke":1, "children":[]}


# for parent_dir in dirs:
# 	dir_dict = {'name': parent_dir, 'stroke': "1", 'children':[]}
# 	heads_children = []
# 	head = {}
# 	print (dir_dict)
# 	reports = os.listdir('./glance/tree_data/' + parent_dir)
# 	print (reports)
# 	for f in reports:

# 		if 'h' in f:
# 			print('./glance/tree_data/' + parent_dir + "/" + f)
# 			json_file = open('./glance/tree_data/' + parent_dir + "/" + f).read()
# 			head = json.loads(json_file)
# 			head["children_hardware"] = head["children"]
# 			head["children"] = ''
# 		else:
# 			json_file = open('./glance/tree_data/' + parent_dir + "/" + f).read()
# 			heads_children.append(json.loads(json_file))
# 			print( parent_dir + "/" + f)
		
# 	head["children"] = heads_children
# 	print("append", len(heads_children), len(head["children"]),"\n\n\n\n\n\n")
# 	dir_dict["children"].append(head)

# 	root["children"].append(dir_dict)
	

# #print (root)
# #print(root["children"][0]["children"])
# with open("tree_data.json", 'w') as f:
# 	json.dump(root, f,indent = 4)


# import csv
# dirs = os.listdir('./glance/csv_data/')

# # print(dirs)

# # end_values = []

# # for f in dirs:
# # 	with open('./glance/csv_data/' + f, 'r') as csvfile:
# # 		spamreader = csv.reader(csvfile)
# # 		head = spamreader.get
# # 		for row in spamreader:
# # 			print (', '.join(row))



# import pandas as pd
# types = ["NICs", "GPUs", "CPUs", "Disks", "Memory", "SYS"]
# for t in types:
# 	combined_csv = pd.concat( [ pd.read_csv('./glance/csv_data/' + f ) for f in list(filter(lambda x: t in x, dirs)) ] )
# 	combined_csv.to_csv( t + ".csv", index=False )







i = "100"





print("i  [" ,type(i).__name__, "]   :", i)










#print (root)
#print(root["children"][0]["children"])

'''with open('device.yaml', 'r') as y_file:
	data_json = (json.dumps(yaml.load(y_file), sort_keys=True, indent=2))
	with open('/Users/daniel/graph/tree_temp.json', 'w') as tr:
		tr.write(data_json)'''








