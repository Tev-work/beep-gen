#!/usr/bin/env python

# using print as a function (imported from python 3+)
from __future__ import print_function

import audiogen
import itertools

# mix 440 Hz and 445 Hz tones to get 5 Hz beating
beats = audiogen.util.mixer(
        (audiogen.tone(440), audiogen.tone(445)),
        [(audiogen.util.constant(1), audiogen.util.constant(1))]
)

with open("output.wav", "wb") as f:
    audiogen.sampler.write_wav(f, beats)