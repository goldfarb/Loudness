import pexpect

def main(i):
	iteration = "wamu" + str(i)
	fout.write (iteration)
	p = pexpect.spawn("sh")
	p = pexpect.spawn("ffmpeg -nostats -i %s.wav -filter_complex ebur128=framelog=verbose -f null -" % iteration) 
	p.logfile = fout
	p.interact(chr(29))
	fout.close()



 	
for a in range (0,3):
	script_filename = "script.txt"
	fout = open(script_filename, "a")
#	print str(a)
	main(a)