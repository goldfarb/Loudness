import csv
	    
with open('files_list.txt', 'rb') as f:
	with open ('files_to_run.txt', 'w') as g:

		reader = csv.reader(f, delimiter='\t')

		for row in reader:
			g.write(row[0] + '\r')