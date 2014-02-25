import linecache
from subprocess import call

call(["cp", "sort.txt", "inter_0.txt"])
replace_list = []

with open('replacement.txt', 'r') as f:
    rep_lines = f.readlines()
    num_lines_i = len([l for l in rep_lines if l.strip(' \n') != ''])

with open('input.txt', 'r') as f:
    new_lines = f.readlines()
    num_lines_o = len([l for l in new_lines if l.strip(' \n') != ''])


print num_lines_o
print num_lines_i

for i in range(num_lines_o):
	i_line = linecache.getline('replacement.txt', i)
	s_i_line = i_line.rstrip('\n')

	o_line = linecache.getline('input.txt', i)
	s_o_line = o_line.rstrip('\n')

	replace_list.append([s_i_line, s_o_line])

print replace_list

for i in range(num_lines_o):
	print i
	print replace_list[i]


	print "\r\r\r"
	

	in_file = "inter_%s.txt" % str(i)
	out_file = "inter_%s.txt" % str(i + 1)


	with open(out_file, "w") as fout:
		with open(in_file, "r") as fin:
			for line in fin:
				fout.write(line.replace('\n', '\t'))
		fin.close()
	fout.close()
	call(["rm", in_file])

