import subprocess

with open ('files_to_run_bbc.txt') as f:
	reader = f.read().splitlines()
	d = list(reader)

def loudness_reading(i):
#	iteration = "//192.168.28.9/xdcache/archive/" + str(i)
#	iteration = "//dc-corpfs02/aeshare$/DigitalRadioShare/PROJECTS/Technology\ Strategy/Loudness/Example\ Audio/More\ Shows/" + str(i)
	iteration = "//ad.npr.org/News/DC-Production/Media/Recordings/Ops/" + str(i)
	command = 'ffmpeg -nostats -i ' + iteration + ' -filter_complex ebur128=peak=true -f null -'
	log = open('log_file_bbc.txt', 'a')
	c = subprocess.call([command], stdout=log, stderr=log, shell=True)
	log.close()

for a in d:
	loudness_reading(a)
