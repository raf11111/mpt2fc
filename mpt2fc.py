# Proof of concept ModplugTracker to Future Composer pattern converter
#
# Rafal Szyja (Raf/Vulture Design), June 2015

import os
import remotevice

notes = ['C-', 'C#', 'D-', 'D#', 'E-', 'F-', 'F#', 'G-', 'G#', 'A-', 'A#', 'B-']
hexval = []
# PARAMTERS
basicduration = 4
transpose = -12
destpattern = 2

def storehex(value):
    hexval.append(value)
    #print hex(value)
    pass

with open("michu3.txt") as f:
    data = f.readlines()

    dur = 0
    snd = -1

    for row in data:
        note = row.replace('|', '')

        if note[0] == '.':
            dur = dur + 1
            continue

        newsnd = int(note[3:5])
        if newsnd != snd:
            notetohex = 0xc0 + newsnd
            storehex(notetohex)
            snd = newsnd

        if dur > 0:
            notetohex = 0x80 + dur * basicduration
            storehex(notetohex)
            dur = 0

        halftone = notes.index(note[:2])
        octave = int(note[2:3])
        notetohex = octave * 12 + halftone + transpose

        storehex(notetohex)

monitorstring = ""

for v in hexval:
    monitorstring = monitorstring + " %02.X" % (v)

print "> 7" + str(destpattern) +"00" + monitorstring + " ff"
remotevice.sendCommand("> 7" + str(destpattern) +"00" + monitorstring + " ff \n")




