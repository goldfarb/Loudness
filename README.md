Loudness
========

tools we've used:
*  ffmpeg [http://www.ffmpeg.org/]
*  tools internal to MTE
*  r128 based on liebur128 [https://github.com/audionuma/r128x]
  
all were tested against test audio from qualis and some example files were checked in all three ways


--

What we hope to include:
* segment vs. full hour vs. full show
* feed a vs. feed b
* all the shows on one day
* all the days for one show
* snapshot of an individual engineer, producer, in-house


---


for concatenating


for splitting hours into segments to match the clock

ffmpeg -i input.wav -acodec copy -t 00:00:30 -ss 00:02:20 output.wav
