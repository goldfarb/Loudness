
import pexpect
from replace_text import num_line_count, clean_doc
from ffmpeg_out_rep_array import replacements_array

num_line_count('sort.txt')
print 'all the lines  -- ' + str(line_count)

clean_doc(replacements_array)



with open('files_to_run.txt') as f:
	reader = f.read().splitlines()
	d = list(reader)

def eval(i):
	iteration = '//ad.npr.org/News/DC-Production/Media/Recordings/Rollovers/' + str(i)
	fout.write ('\r' + iteration + '\r')
	p = pexpect.spawn('sh')
	p = pexpect.spawn('ffmpeg -nostats -i %s -filter_complex ebur128=framelog=verbose:peak=true -f null -' % iteration) 
	p.logfile = fout
	p.interact(chr(29))
	fout.close()


for a in d:
	script_filename = 'script.txt'
	fout = open(script_filename, 'a')
	print a
	eval(a)

num_line_count('script.txt')
clean_doc(replacements_array)