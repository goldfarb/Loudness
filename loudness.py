
import pexpect

with open("test.txt") as f:
	reader = f.read().splitlines()
	d = list(reader)

def main(i):
	iteration = "//ad.npr.org/News/DC-Production/Media/Recordings/Rollovers/" + str(i)
	fout.write ("\r" + iteration + "\r")
	p = pexpect.spawn("sh")
	p = pexpect.spawn("ffmpeg -nostats -i %s -filter_complex ebur128=framelog=verbose:peak=true -f null -" % iteration) 
	p.logfile = fout
	p.interact(chr(29))
	fout.close()


for a in d:
	script_filename = "script.txt"
	fout = open(script_filename, "a")
	print a
	main(a)


	