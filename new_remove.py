import re
import subprocess
import os
import shutil

shutil.copyfile("three.txt", "three.csv")


file_name = "three.csv"

buffered = open(file_name, 'rU').read()
#print type(buffered)

words = re.sub('dBFS,','dBFS\n',buffered)

words = re.sub(',,',',',words)

words = re.sub(',,',',',words)

words = re.sub(',,',',',words)

words = re.sub(',,',',',words)

words = re.sub(',,',',',words)

words = re.sub('\n,','\n',words)
#print words

words = re.sub('originator_reference(.)+I:','I:',words)
#print words

words = re.sub(',2016-(.)+I:',',I:',words)
#print words

words = re.sub('ffmpeg(.)*100','',words)
#print words


words = re.sub('Threshold:(.)*LRA:','LRA:',words)
#print words

words = re.sub('LU,(.)*Peak:','LU,Peak:',words)


words = re.sub('wav,2016(.)*\n2016','wav,2016',words)


words = re.sub(',(\s+)',',',words)

words = re.sub(':(\s+)',':',words)


words = re.sub(',I:',',',words)


words = re.sub(' LUFS,LRA:',',',words)


words = re.sub(' LU,Peak:',',',words)

words = re.sub(' dBFS','',words)

words = re.sub('\n,','\n',words)

words = re.sub(',Multi','Multi',words)


out_file = "four.csv"
output = open(out_file, 'w')
output.write(words)