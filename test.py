# [out, in]
test_arrary = [['\t', '\n'], ['\t', '\r'], ['\r//ad.npr.org/', '//ad.npr.org/'], ['\t', '\t\t\t'], ['\r', '\t\r'], ['\t', '\t \t\t'], ['\r\n', '\r'], ['\t', 'configuration: --enable-gpl --enable-version3 --disable-w32threads --enable-avisynth --enable-bzlib --enable-fontconfig --enable-frei0r --enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libcaca --enable-libfreetype --enable-libgsm --enable-libilbc --enable-libmodplug --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-librtmp --enable-libschroedinger --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvo-aacenc --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libx264 --enable-libx265 --enable-libxavs --enable-libxvid --enable-zlib'], ['\t', 'Guessed Channel Layout for  Input Stream #0.0 : stereo	Input #0, wav, from '], ['\t', 'Metadata:	    comment         : '], ['\t', 'mapping:	  Stream #0:0 (pcm_s16le) -> ebur128	  ebur128 -> Stream #0:0 (pcm_s16le)	Press [q] to stop, [?] for help	size=N/A '], ['\t', 'bitrate=N/A    		video:0kB '], ['\t', 'subtitle:0 data:0 global headers:0kB muxing overhead -100.000000%	[Parsed_ebur128_0 @ 02fe74a0] Summary:'], ['\t', 'Stream #0:0: Audio: pcm_s16le, 48000 Hz, stereo, s16, 1536 kb/s	Stream']]

repl_num = len(test_arrary)

for i in range (0,repl_num):
	print i
	print test_arrary[i][1]
	print test_arrary[i][0]
	print "\r"
