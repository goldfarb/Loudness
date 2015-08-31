with open("out.txt", "w") as fout:

	with open("script.txt", "r") as fin:
		for line in fin:
			fout.write(line.replace('\n', '\t'))
fin.close()

fout.close()

with open("sort.txt", "w") as fout:

	with open("out.txt", "r") as fin:
		for line in fin:
			fout.write(line.replace('\r', '\t'))
fin.close()

fout.close()

with open("out.txt", "w") as fout:

	with open("sort.txt", "r") as fin:
		for line in fin:
			fout.write(line.replace('//ad.npr.org/', '\r//ad.npr.org/'))
fin.close()

fout.close()

with open("sort.txt", "w") as fout:

	with open("out.txt", "r") as fin:
		for line in fin:
			fout.write(line.replace('configuration: --enable-gpl --enable-version3 --disable-w32threads --enable-avisynth --enable-bzlib --enable-fontconfig --enable-frei0r --enable-gnutls --enable-iconv --enable-libass --enable-libbluray --enable-libcaca --enable-libfreetype --enable-libgsm --enable-libilbc --enable-libmodplug --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenjpeg --enable-libopus --enable-librtmp --enable-libschroedinger --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvo-aacenc --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwavpack --enable-libx264 --enable-libx265 --enable-libxavs --enable-libxvid --enable-zlib', '\t'))
fin.close()

fout.close()

with open("out.txt", "w") as fout:

	with open("sort.txt", "r") as fin:
		for line in fin:
			fout.write(line.replace('\t\t\t', '\t'))
fin.close()

fout.close()


with open("sort.txt", "w") as fout:

	with open("out.txt", "r") as fin:
		for line in fin:
			fout.write(line.replace('\t\r', '\r'))
fin.close()

fout.close()


with open("out.txt", "w") as fout:

	with open("sort.txt", "r") as fin:
		for line in fin:
			fout.write(line.replace('\t  \t\t', '\t'))
fin.close()

fout.close()

with open("sort.txt", "w") as fout:

	with open("out.txt", "r") as fin:
		for line in fin:
			fout.write(line.replace('\r', '\r\n'))
fin.close()

fout.close()
