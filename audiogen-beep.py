#!/usr/bin/env python

# using print as a function (imported from python 3+)
from __future__ import print_function

import sys
import audiogen
import itertools

beep_silence = itertools.chain(
    audiogen.beep(),
    audiogen.silence(0.5),
    audiogen.beep(),
    audiogen.silence(8),
)

# audiogen.sampler.write_wav(sys.stdout, beep_silence)

with open("output.wav", "wb") as f:
    audiogen.sampler.write_wav(f, beep_silence)