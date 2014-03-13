tabs_array = [['\r\n', ''], \
['\n', ''], \
[', from \'//', '\n//'], \
['comment         : ', '\t'], \
['originator_reference', '\t'], \
['I:         ', '\t'], \
[' LUFS\n    Threshold', '\t'], \
['LRA:         ', '\t'], \
[' LU\n', '\t'], \
['Peak:       ', '\t'], \
[' dBFS', '\t'], \
[',', ' ']
]

#creates array with [input, replacement]
replacements_array = [['built on', ''], \
['configuration: --enable-gpl --enable-version3 --disable-w32threads --enable-avisynth --enable-bzlib --enable-fontconfig --enable-frei0r --enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libcaca --enable-libfreetype --enable-libgsm --enable-libilbc --enable-libmodplug --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-librtmp --enable-libschroedinger --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvo-aacenc --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libx264 --enable-libx265 --enable-libxavs --enable-libxvid --enable-zlib', ''], \
# older version of ffmpeg
['libavutil      52. 65.100 / 52. 65.100', ''], \
['libavcdc \ \   55. 52.102 / 55. 52.102', ''], \
['libavformat    55. 33.100 / 55. 33.100', ''], \
['libavdevice    55. 10.100 / 55. 10.100', ''], \
['libavfilter     4.  1.103 /  4.  1.103', ''], \
['libavcodec     55. 52.102 / 55. 52.102', ''], \
['libswscale      2.  5.101 /  2.  5.101', ''], \
['libswresample   0. 17.104 /  0. 17.104', ''], \
['libpostproc    52.  3.100 / 52.  3.100', ''], \
# newer version of ffmpeg
['libavutil      52. 66.101 / 52. 66.101', ''], \
['libavcdc \ \   55. 52.102 / 55. 52.102', ''], \
['libavformat    55. 33.101 / 55. 33.101', ''], \
['libavdevice    55. 11.100 / 55. 11.100', ''], \
['libavfilter     4.  3.100 /  4.  3.100', ''], \
['libavcodec     55. 52.102 / 55. 52.102', ''], \
['libswscale      2.  5.101 /  2.  5.101', ''], \
['libswresample   0. 18.100 /  0. 18.100', ''], \
['libpostproc    52.  3.100 / 52.  3.100', ''], \
#
['Guessed Channel Layout for  Input Stream #0.0 : stereo', ''], \
['Input #0, wav, from', ''], \
['Metadata:',''], \
['wav\'','wav'], \
['coding_history  : ', ''], \
#
['A=PCM,F=48000,W=16,M=stereo', ''], \
['A=MPEG1L2,F=48000,B=192,W=16,M=stereo', ''], \
['A=MPEG1L2,F=48000,B=192,W=16,M=stereo,T=D.A.V.I.D. GmbH Audio Conversion Software V8.00', ''], \
#
['A=MPEG1L2,F=44100,B=256,M=STEREO,T=CV_PcxTl2NP', '--256/STEREO--'], \
['A=MPEG1L2,F=44100,B=128,M=STEREO,T=CV_PcxTl2NP', '--128/STEREO--'], \
['A=MPEG1L2,F=44100,B=128,M=MONO,T=CV_PcxTl2NP', '--128/MONO--'], \
#
['A=PCM,F=48000,W=16,M=stereo,T=D.A.V.I.D. GmbH Audio Conversion Software V7.00', ''], \
['A=PCM,F=48000,W=16,M=stereo,T=D.A.V.I.D. GmbH Audio Conversion Software V8.00', ''], \
#
['Stream #0:0: Audio: pcm_s16le, 48000 Hz, stereo, s16, 1536 kb/s', ''], \
['Stream #0:0: Audio: pcm_s16le, 48000 Hz, mono, s16, 768 kb/s', ''], \
#
['Stream #0:0: Audio: pcm_s16le ([1][0][0][0] / 0x0001), 48000 Hz, stereo, s16, 1536 kb/s', ''], \
['Stream #0:0: Audio: mp2 (P[0][0][0] / 0x0050), 44100 Hz, stereo, s16p, 256 kb/s',''], \
['Stream #0:0: Audio: mp2 (P[0][0][0] / 0x0050), 44100 Hz, stereo, s16p, 256 kb/s',''], \
['Stream #0:0: Audio: mp2 (P[0][0][0] / 0x0050), 44100 Hz, mono, s16p, 128 kb/s',''], \
#
["Output #0, null, to 'pipe:':", ''], \
#
['encoder         : Lavf55.33.100', ''], \
['encoder         : Lavf55.33.101', ''], \
#
['Stream mapping:', ''], \
['Stream #0:0 (pcm_s16le) -> ebur128', ''], \
['Stream #0:0 (mp2) -> ebur128', ''], \
['ebur128 -> Stream #0:0 (pcm_s16le)', ''], \
['Press [q] to stop, [?] for help', ''], \
['size=N/A ', ''], \
['bitrate=N/A', ''], \
['time_reference  : 0', ''], \
['with gcc 4.8.2 (GCC)', ''], \
# older version
['ffmpeg version N-60797-g76dd01e Copyright (c) 2000-2014 the FFmpeg developers', ''], \
# newer version
['ffmpeg version N-61143-g64e4bd7 Copyright (c) 2000-2014 the FFmpeg developers', ''], \
#
['kB subtitle:0 data:0 global headers:0kB muxing overhead -100.000000%', ''], \
['video:0kB audio:', ''], \
#
['[Parsed_ebur128_0 @ 02c55760]', ''], \
['[Parsed_ebur128_0 @ 0368af60]', ''], \
['[Parsed_ebur128_0 @ 035fce20]', ''], \
['[Parsed_ebur128_0 @ 0350ce20]', ''], \
#change the following with a new ffmpeg build
['Feb 20 2014 22:01:52', ''], \
['Mar  7 2014 00:01:08', ''], \
#
['subtitle:0 data:0 global headers:0kB muxing overhead -100', ''], \
#['comment         : ',''], \
['date            : ',''], \
['  :  ',' '], \
['      ',' '], \
['  ',' '], \
['  ',' '], \
['\r\n', ''], \
['\n', ''], \
#[', from \'//', '\n//'], \
['comment         : ', '\t'], \
#['originator_reference', '\t'], \
['I: ', '\t'], \
[' LUFS Threshold', '\t'], \
[': LRA: ', '\t'], \
[' LU', '\t'], \
['Peak: ', '\t'], \
[',', ' '], \
['\n','\t'], \
['\n','\t'], \
['   --', '\t'], \
['--   :  ', '\t'], \
['\t ','\t'], \
[' \t','\t'], \
['\t ','\t'], \
['\t\t\t\t','\t'], \
['\t\t\t','\t'], \
['\t\t','\t'], \
['\t\t','\t'], \
['\t:\t','\t'], \
['\t:','\t'], \
[':\t','\t'], \
['\n','\t'], \
[' dBFS', '\n'], \
#['//','\n//']
[".wav           '//",'.wav\t//'], \
["           '//","//"], \
["           //","//"], \
['No such file or directory//', 'Nope\n//'], \
['No such file or directory          //', 'Nope\n//']]