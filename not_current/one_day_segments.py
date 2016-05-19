import subprocess
##PATH=../../../../cygwin64/usr/local/bin/ffmpeg/ffmpeg-20150702-git-03b2b40-win64-shared/bin:$PATH

log = open('full.txt', 'a')

import subprocess

from ATCclock_array import atc_clock
from MEclock_array import me_clock
from WKENDclock_array import we_clock

from days import week
from days import weekend



log = open('full.txt', 'a')
stdout = log
stderr = log

for i in week:
	print i

	command = 'cp ../../../../../../../cygdrive/r/MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_06-00-00.wav MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_06-00-00.wav'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'cp ../../../../../../../cygdrive/r/MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_05-00-00.wav MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_05-00-00.wav'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)


	command = 'cp ../../../../../../../cygdrive/r/MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_08-00-00.wav MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_08-00-00.wav'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'cp ../../../../../../../cygdrive/r/MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_07-00-00.wav MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_07-00-00.wav'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)


	command = 'cp ../../../../../../../cygdrive/r/MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_10-00-00.wav MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_10-00-00.wav'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'cp ../../../../../../../cygdrive/r/MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_09-00-00.wav MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_09-00-00.wav'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)


command = 'chmod 777 *.wav'
c = subprocess.call(command, stdout=log, stderr=log, shell=True)

for i in week:
	print i

	command = 'ffmpeg -nostats -i MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_06-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'ffmpeg -nostats -i MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_08-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'ffmpeg -nostats -i MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_10-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'ffmpeg -nostats -i MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_05-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)

	command = 'ffmpeg -nostats -i MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_07-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)
	
	command = 'ffmpeg -nostats -i MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_09-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
	c = subprocess.call(command, stdout=log, stderr=log, shell=True)
	




for i in week:
	print i

	num_segments = len(me_clock)

	for j in range(0,num_segments):
		command = 'ffmpeg -i MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_05-00-00.wav -acodec copy -to ' + me_clock[j][2] + ' -ss ' + me_clock[j][1] + ' ' +  me_clock[j][0] + '_' + 'MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_05-00-00.wav'
		print command
		c = subprocess.call(command, shell=True)
		command = 'ffmpeg -nostats -i ' + me_clock[j][0] + '_' + 'MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_05-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
		c = subprocess.call(command, stdout=log, stderr=log, shell=True)

		command = 'ffmpeg -i MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_06-00-00.wav -acodec copy -to ' + me_clock[j][2] + ' -ss ' + me_clock[j][1] + ' ' +  me_clock[j][0] + '_' + 'MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_06-00-00.wav'
		print command
		c = subprocess.call(command, shell=True)
		command = 'ffmpeg -nostats -i ' + me_clock[j][0] + '_' + 'MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_06-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
		c = subprocess.call(command, stdout=log, stderr=log, shell=True)


		command = 'ffmpeg -i MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_07-00-00.wav -acodec copy -to ' + me_clock[j][2] + ' -ss ' + me_clock[j][1] + ' ' +  me_clock[j][0] + '_' + 'MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_07-00-00.wav'
		print command
		c = subprocess.call(command, shell=True)
		command = 'ffmpeg -nostats -i ' + me_clock[j][0] + '_' + 'MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_07-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
		c = subprocess.call(command, stdout=log, stderr=log, shell=True)

		command = 'ffmpeg -i MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_08-00-00.wav -acodec copy -to ' + me_clock[j][2] + ' -ss ' + me_clock[j][1] + ' ' +  me_clock[j][0] + '_' + 'MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_08-00-00.wav'
		print command
		c = subprocess.call(command, shell=True)
		command = 'ffmpeg -nostats -i ' + me_clock[j][0] + '_' + 'MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_08-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
		c = subprocess.call(command, stdout=log, stderr=log, shell=True)


		command = 'ffmpeg -i MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_09-00-00.wav -acodec copy -to ' + me_clock[j][2] + ' -ss ' + me_clock[j][1] + ' ' +  me_clock[j][0] + '_' + 'MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_09-00-00.wav'
		print command
		c = subprocess.call(command, shell=True)
		command = 'ffmpeg -nostats -i ' + me_clock[j][0] + '_' + 'MultiCoder_SOAP_4_DCTECH-MC01X_'+i+'-2015_09-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
		c = subprocess.call(command, stdout=log, stderr=log, shell=True)

		command = 'ffmpeg -i MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_10-00-00.wav -acodec copy -to ' + me_clock[j][2] + ' -ss ' + me_clock[j][1] + ' ' +  me_clock[j][0] + '_' + 'MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_10-00-00.wav'
		print command
		c = subprocess.call(command, shell=True)
		command = 'ffmpeg -nostats -i ' + me_clock[j][0] + '_' + 'MultiCoder_SOAP_1_DCTECH-MC01X_'+i+'-2015_10-00-00.wav -filter_complex ebur128=framelog=verbose:peak=true -f null -'
		c = subprocess.call(command, stdout=log, stderr=log, shell=True)





infile = "full.txt"
outfile = "two.txt"
finfile = "three.txt"
cleanfile = "four.txt"

delete_list = ["ffmpeg version N-73361-g03b2b40 Copyright (c) 2000-2015 the FFmpeg developers","Output #0, null, to 'pipe:", "  built with gcc 4.9.2 (GCC)", "  configuration: --disable-static --enable-shared --enable-gpl --enable-version3 --disable-w32threads --enable-avisynth --enable-bzlib --enable-fontconfig --enable-frei0r --enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libbs2b --enable-libcaca --enable-libdcadec --enable-libfreetype --enable-libgme --enable-libgsm --enable-libilbc --enable-libmodplug --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-librtmp --enable-libschroedinger --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvo-aacenc --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxavs --enable-libxvid --enable-lzma --enable-decklink --enable-zlib", "  libavutil      54. 27.100 / 54. 27.100", "  libavcodec     56. 46.100 / 56. 46.100", "  libavformat    56. 40.100 / 56. 40.100", "  libavdevice    56.  4.100 / 56.  4.100", "  libavfilter     5. 19.100 /  5. 19.100", "  libswscale      3.  1.101 /  3.  1.101", "  libswresample   1.  2.100 /  1.  2.100", "  libpostproc    53.  3.100 / 53.  3.100", "Guessed Channel Layout for  Input Stream #0.0 : stereo", "Input #0, wav, from '", "':", "  Metadata:", "    comment         : ", "    date            : ", "    encoder         : Lavf56.40.100", "  Duration: ", "  , bitrate: 1536 kb/s", "    Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 48000 Hz, 2 channels, s16, 1536 kb/s", "Output #0, null, to 'pipe:':", "  Metadata:", "    comment         : ", "    date            : ", "    encoder         : Lavf56.40.100", "    Stream #0:0: Audio: pcm_s16le, 48000 Hz, stereo, s16, 1536 kb/s", "    Metadata:", "      encoder         : Lavc56.46.100 pcm_s16le", "Stream mapping:", "  Stream #0:0 (pcm_s16le) -> ebur128", "  ebur128 -> Stream #0:0 (pcm_s16le)", "Press [q] to stop, [?] for help", "size=N/A time=", " bitrate=N/A    ", "video:0kB audio:", " subtitle:0kB other streams:0kB global headers:0kB muxing overhead: unknown", "[Parsed_ebur128_0 @ 0000000000574900] Summary:", "", "  Integrated loudness:", "  Loudness range:", "  True peak:"]
fin = open(infile)
fout = open(outfile, "w+")

for line in fin:
	for word in delete_list:
		line = line.replace(word, "")
	fout.write(line)

fin.close()

fout.close()

cleanup_list = ["\n","\r"]
fin = open(outfile)
fout = open(finfile, "w+")

for line in fin:
	for word in cleanup_list:
		line = line.replace(word, ",")
	fout.write(line)
fin.close()
fout.close()

last_list = [["Threshold","*"]]
#["dBFS","dBFS\n"]]
#,[",,,,,","*"]]
#,[",,,,","$"],[",,,","%"],[",,","&&"]]
fin = open(finfile)
fout = open(cleanfile, "w+")

for word in last_list:
	for string in finfile:
		print word[0]
		print word[1]
		string = string.replace(',','')
		fout.write(string)
fin.close()
fout.close()