""" Synthesizes a blues solo algorithmically """

from Nsound import *
import numpy as np
from numpy.random import choice, rand, random_sample
from random import choice

def add_note(out, instr, key_num, duration, bpm, volume):
    """ Adds a note from the given instrument to the specified stream

        out: the stream to add the note to
        instr: the instrument that should play the note
        key_num: the piano key number (A 440Hzz is 49)
        duration: the duration of the note in beats
        bpm: the tempo of the music
        volume: the volume of the note
	"""
    freq = (2.0**(1/12.0))**(key_num-49)*440.0
    stream = instr.play(duration*(60.0/bpm),freq)
    stream *= volume
    out << stream

# this controls the sample rate for the sound file you will generate
sampling_rate = 44100.0
Wavefile.setDefaults(sampling_rate, 16)

bass = GuitarBass(sampling_rate)	# use a guitar bass as the instrument
solo = AudioStream(sampling_rate, 1)

""" these are the piano key numbers for a 3 octave blues scale in A
	See: http://en.wikipedia.org/wiki/Blues_scale """
blues_scale = [25, 28, 30, 31, 32, 35, 37, 40, 42, 43, 44, 47, 49, 52, 54, 55, 56, 59, 61]
beats_per_minute = 45				# Let's make a slow blues solo


curr_note = 0
add_note(solo, bass, blues_scale[curr_note], 1.0, beats_per_minute, 1.0)
licks = [ [ [1,0.5], [1,0.5], [1, 0.5], [1, 0.5] ,[-1, 0.5], [-1, 0.5], [-1, 0.5], [-1, 0.5], [1, 0.5*1.1], [1, 0.5*0.9], [1, 0.5*1.1], [1, 0.5*0.9] ] ]
for i in range(4):
    lick = choice(licks)
    for note in lick:
        curr_note += note[0]
        add_note(solo, bass, blues_scale[curr_note], note[1], beats_per_minute, 1.0)


backing_track = AudioStream(sampling_rate, 1)
Wavefile.read('backing.wav', backing_track)

m = Mixer()

solo *= 0.4             # adjust relative volumes to taste
backing_track *= 2.0

m.add(2.25, 0, solo)    # delay the solo to match up with backing track   
m.add(0, 0, backing_track)

m.getStream(500.0) >> "slow_blues.wav"