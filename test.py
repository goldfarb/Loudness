with open("test.txt") as f:
	reader = f.read().splitlines()
	d = list(reader)


for a in d:
	script_filename = "script.txt"
	fout = open(script_filename, "a")
	print a