import subprocess
##PATH=../../../../cygwin64/usr/local/bin/ffmpeg/ffmpeg-20150702-git-03b2b40-win64-shared/bin:$PATH

log = open('full.txt', 'a')

import subprocess

week = ['08-03', '08-04', '08-05', '08-06', '08-07']
weekend = ['08-08', '08-09']



log = open('full.txt', 'a')
stdout = log
stderr = log

for i in week:
	print i

	command = 'ffmpeg -nostats -i MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_06-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'ffmpeg -nostats -i MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_17-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'ffmpeg -nostats -i MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_05-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'ffmpeg -nostats -i MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_16-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)
	


for i in weekend:
	print i

	command = 'ffmpeg -nostats -i MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_09-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'ffmpeg -nostats -i MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_17-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'ffmpeg -nostats -i MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_08-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)
