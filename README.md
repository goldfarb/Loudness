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

compile all of the meter information [rollovers, from content depot, LWoSF, from APM, others?]
  
  keep track of the source (rollover, content depot)
  
  remove rows for expunged files
  
  add row for monophonic 256
  
  write cleanup for the cart chunks

---


for concatenating

-

for splitting hours into segments to match the clock

ffmpeg -i input.wav -acodec copy -t 00:00:30 -ss 00:02:20 output.wav


--------

for in house - shows, with loudness
  same shows, with LRA error bars
  
over the course of a day

programs; promos; newscast;

put CD metadata with the shows

list of what we're missing still
