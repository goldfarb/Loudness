with open('writetext.txt', 'w') as file_out:
	with open('output.txt', 'r') as file_in:
		file_out.write(line.replace("a", "XXX")

	with open(out_file, 'w') as fout:
		with open(in_file, 'r') as fin:
			for line in fin:
				fout.write(line.replace('\n', '\t'))
		fin.close()
	fout.close()