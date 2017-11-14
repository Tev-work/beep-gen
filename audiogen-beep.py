#!/usr/bin/env python

# using print as a function (imported from python 3+)
from __future__ import print_function

import sys
import audiogen
import itertools

beep_silence = itertools.chain(audiogen.beep(), audiogen.silence(50), audiogen.beep(), audiogen.silence(50))

audiogen.sampler.write_wav(sys.stdout, beep_silence)