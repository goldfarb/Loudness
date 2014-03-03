import os 
	#used to write to the command line

from ffmpeg_out_rep_array import replacements_array

line_count = 0

def num_line_count(doc_name):
	global line_count
		#copies the file we're using so the original isn't messed up
	os.system('cp ' + doc_name + ' temp_0.txt')
	with open (doc_name, 'r') as doc:
		for each_line in doc:
			line_count = line_count + 1
							#print each_line
							#print line_count

def clean_doc(swap_array):
	global line_count
	print 'line count - ' + str(line_count)
	pairs = len(swap_array)
	print 'num of pairs - ' + str(pairs)
			
	for i in range(0, pairs):
		i_file = 'temp_%s.txt' % str(i)
		o_file = 'temp_%s.txt' % str(i + 1)
			
					
					#print swap_array[i]
					#print i_file
					#print o_file
			
		with open(i_file, 'r') as f_in:
			with open(o_file, 'w') as f_out:
							#going through each line in the document
				j = 0
				for line in f_in:
								#print "i = " + str(i) + 'j = ' + str(j)
								#print f_in.name + f_out.name
					f_out.write(line.replace(swap_array[i][0], swap_array[i][1]))
					j = j + 1
				f_out.closed
				f_in.closed
				os.system('rm ' + i_file)
	os.system('cp ' + o_file + ' output.csv')
					
num_line_count('script.txt')
clean_doc(replacements_array)					
