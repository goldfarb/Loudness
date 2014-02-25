import os
os.system('ffmpeg -nostats -i MultiCoder_SOAP_4_DCTECH-MC02_02-21-2014_15-29-59.wav -filter_complex ebur128=framelog=verbose:peak=true -f null - > out.txt')

"""from subprocess import call
call (['ffmpeg', '-nostats', '-i', 'MultiCoder_SOAP_4_DCTECH-MC02_02-21-2014_15-29-59.wav', '-filter_complex', 'ebur128=framelog=verbose:peak=true', '-f', 'null', '-'])
"""