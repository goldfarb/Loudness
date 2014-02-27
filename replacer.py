import linecache, os
from subprocess import call
#input, replacement
replacements_arrary = [['configuration: --enable-gpl --enable-version3 --disable-w32threads --enable-avisynth --enable-bzlib --enable-fontconfig --enable-frei0r --enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libcaca --enable-libfreetype --enable-libgsm --enable-libilbc --enable-libmodplug --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-librtmp --enable-libschroedinger --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvo-aacenc --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libx264 --enable-libx265 --enable-libxavs --enable-libxvid --enable-zlib', 'BOO'], ['  libavutil      52. 65.100 / 52. 65.100', 'HISS'], \
['  libavcodec     55. 52.102 / 55. 52.102\n  libavformat    55. 33.100 / 55. 33.100', 'OTHER']]

os.system('cp sort.txt inter_0.txt')
with open ('sort.txt', 'r') as f:
	num_lines = 0
	for each_line in f:
		num_lines = num_lines + 1
print num_lines

for i in range (0,num_lines):
		print i
		in_file = 'inter_%s.txt' % str(i)
		out_file = 'inter_%s.txt' % str(i + 1)
	
		with open(out_file, 'w') as fout:
			with open(in_file, 'r') as fin:
				for line in fin:
					fout.write(line.replace(replacements_arrary[i][1], replacements_arrary[i][0]))
			fin.close()
		fout.close()
		call(['rm', in_file])



# [out, in]
"""replacements_arrary = [['\t', '\n'], ['\t', '\r'], ['\r//ad.npr.org/', '//ad.npr.org/'], ['\t', '\t\t'], ['\t', '\t\t\t'], \
['\t', '\t '], ['\r', '\t\r'], ['\t', '\t \t\t'], ['\r\n', '\r'], \
['\t', 'configuration: --enable-gpl --enable-version3 --disable-w32threads --enable-avisynth --enable-bzlib --enable-fontconfig --enable-frei0r \
--enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libcaca --enable-libfreetype --enable-libgsm --enable-libilbc --enable-libmodplug \
--enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-librtmp --enable-libschroedinger \
--enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvo-aacenc --enable-libvo-amrwbenc \
--enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libx264 --enable-libx265 --enable-libxavs --enable-libxvid --enable-zlib'], ['\t', '\t  \tmapping:\tStream #0:0 '], \
['\t', 'Guessed Channel Layout for  Input Stream #0.0 : stereo	Input #0, wav, from '], ['\t', 'Metadata:\t  comment         : '], \
['\t', 'mapping:\tStream #0:0 \(pcm_s16le\) -> ebur128\tebur128 -> Stream #0:0 \(pcm_s16le\)\tPress \[q\] to stop, \[\?\] for help\tsize=N/A'], \
['\t', ' bitrate=N/A    \tvideo:0kB '], ['\t', 'subtitle:0 data:0 global headers:0kB muxing overhead -100.000000%	[Parsed_ebur128_0 @ 02fe74a0] Summary:'],\
 ['\t', 'Stream #0:0: Audio: pcm_s16le, 48000 Hz, stereo, s16, 1536 kb/s	Stream'], \
 ['\t', 'Copyright \(c\) 2000-2014 the FFmpeg developers\tbuilt on '], ['\t', '\t  date            : '], ['\t', '\t ']]
"""
#repl_num = len(replacements_arrary)

#call(['cp', 'sort.txt', 'inter_0.txt'])

#print repl_num

#replace_list = []

"""with open('replacement.txt', 'r') as f:
    rep_lines = f.readlines()
    num_lines_i = len([l for l in rep_lines if l.strip(' \n') != ''])

with open('input.txt', 'r') as f:
    new_lines = f.readlines()
    num_lines_o = len([l for l in new_lines if l.strip(' \n') != ''])


print num_lines_o
print num_lines_i"""

# this creates the file which is the array
"""list_file = 'list_file.txt'
	fout = open(list_file, 'a')
	
	for i in range(num_lines_o):
		i_line = linecache.getline('replacement.txt', i)
		s_i_line = i_line.rstrip('\n')
	
		o_line = linecache.getline('input.txt', i)
		s_o_line = o_line.rstrip('\n')
	
		replace_list.append([s_i_line, s_o_line])
		new_line = s_o_line + "," + s_i_line + "\r\n"
		fout.write(new_line)"""	

# print replace_list

#use this

"""for i in range (0,repl_num):
		print i
		in_file = 'inter_%s.txt' % str(i)
		out_file = 'inter_%s.txt' % str(i + 1)
	
		with open(out_file, 'w') as fout:
			with open(in_file, 'r') as fin:
				for line in fin:
					fout.write(line.replace(replacements_arrary[i][1], replacements_arrary[i][0]))
			fin.close()
		fout.close()
		call(['rm', in_file])
	"""	

"""for i in range(num_lines_o):
	print i
	print replace_list[i]


	print '\r\r\r'
	

	in_file = 'inter_%s.txt' % str(i)
	out_file = 'inter_%s.txt' % str(i + 1)

	print in_file
	print out_file

	with open(out_file, 'w') as fout:
		with open(in_file, 'r') as fin:
			for line in fin:
				fout.write(line.replace('\n', '\t'))
		fin.close()
	fout.close()
	call(['rm', in_file])

"""