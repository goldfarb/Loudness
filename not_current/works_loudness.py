import pexpect
import os
import time
from replace_text import num_line_count, clean_doc
from ffmpeg_out_rep_array import replacements_array, tabs_array

with open('files_to_run.txt') as f:
	reader = f.read().splitlines()
	d = list(reader)

def eval(i):
#	iteration = "//ad.npr.org/News/DC-Production/Media/Recordings/Rollovers/" + str(i)
#	iteration = "//ad.npr.org/News/DC-Production/Media/Final/201403/" + str(i)
#	iteration = "//dc-corpfs02/aeshare$/DigitalRadioShare/PROJECTS/Technology\ Strategy/Loudness/Example\ Audio/" + str(i)
	iteration = "//192.168.28.9/xdcache/archive/" + str(i)
#	iteration = str(i)

#	p = pexpect.spawn('sh')
#	p = pexpect.spawn('ffmpeg -nostats -i %s -filter_complex ebur128=framelog=verbose:peak=true -f null -' % iteration) 
	p = os.system('ffmpeg -nostats -i %s -filter_complex ebur128=framelog=verbose:peak=true -f null - > new.txt' % iteration) 
	#fout.write(p)
	#time.sleep(10)
	#p.interact(chr(29))
	#fout.close()


for a in d:
	script_filename = 'script.txt'
	#fout = open(script_filename, 'a')
	print a
	eval(a)

#os.system('touch script.txt')

#num_line_count('script.txt')
#clean_doc(tabs_array)