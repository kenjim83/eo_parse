import string, os

# in_folder = "C:\\Users\\miwa\\Documents\\Python\\EO_extraction\\Tri_reports\\"

# flist = os.listdir(in_folder)

# eo_parse = open(in_folder + "\\Final_EO.csv", 'w')

# header = "ID, X, Y, Z, O, P, K\n"

# eo_parse.write(header)

# The line below is called a 'debugger'
# It will stop the code execution in the terminal window
# wherever you put it. You can then type the variable names to 
# see what you have access to. Type to 'quit()' to exit debugger.

import csv



def to_list(str):
    return filter(lambda x: x!='', str.rstrip().split(' '))

def parse_file(file):
	data = []
	for line in file:
		line = line.replace('image ID','image_ID')
		row_data = to_list(line)

		if 'KAPPA' in row_data:
			empty_lines = 0
		
		try:
		  empty_lines
		except NameError:
			continue
		else:
			if not row_data:
				empty_lines += 1 
			
			if empty_lines > 1:
				break
			else:
				data.append(row_data)
				continue
	return data

def write_to_csv(filename, data):
	with open(filename, 'w') as fp:
	    a = csv.writer(fp, delimiter=',')
	    a.writerows(data)

# Parse file, write to csv
f = open('swath11.txt','r')
data = parse_file(f)
write_to_csv('output.csv', data)
