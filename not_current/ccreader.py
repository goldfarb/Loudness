import readcondep
import subprocess

with open('cd_file_names_02.txt') as f:
	reader = f.read().splitlines()
	d = list(reader)

def meta_reader(i):
	iteration = str(i)
#	command = 'cdputils/readcondep.py //ad.npr.org/News/DC-Production/Media/Recordings/Rollovers/' + iteration +' -a'
	command = 'cdputils/readcondep.py 	//192.168.28.9/xdcache/archive/' + iteration +' -a'
	log = open('meta_cd_log_02.txt', 'a')
	log.write(iteration)
	c = subprocess.call([command], stdout=log, stderr=log, shell=True)
	log.close()

for a in d:
	meta_reader(a)