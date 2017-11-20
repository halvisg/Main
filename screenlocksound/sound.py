#!/usr/bin/python

import alsaaudio, time, audioop
import subprocess
inp = alsaaudio.PCM(alsaaudio.PCM_CAPTURE,alsaaudio.PCM_NONBLOCK)

# Sett attributter: Mono, 8000 Hz
inp.setchannels(1)
inp.setrate(8000)
inp.setformat(alsaaudio.PCM_FORMAT_S16_LE)

inp.setperiodsize(160)

while True:
	l,data = inp.read()
	if l:
		if audioop.max(data,2) > 30000:
			subprocess.call("/home/halvis/dev/screenlocksound/echo.sh", shell=True)
	time.sleep(.005)
