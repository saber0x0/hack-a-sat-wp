#!/usr/bin/python3
# coding:utf-8

#!/usr/bin/python3
# coding:utf-8

#!/usr/bin/python3
# coding:utf-8

import sys
import numpy
from gnuradio import gr, digital
from gnuradio import blocks
from gnuradio import analog
from gnuradio.filter import firdes

class phasor(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Phasor")

        self.samp_rate = 32000

        self.wav_file_source_0 = blocks.wavfile_source(
            'provide/challenge.wav', False)
        self.clock_recovery_mm_0 = digital.clock_recovery_mm_ff(
            4, 7.65625e-06, 500e-06, 175e-06, 5e-06)
        self.skip_head_0 = blocks.skiphead(itemsize=4, nitems_to_skip=5)
        self.binary_slicer_0 = digital.binary_slicer_fb()
        self.pack_k_bits_0 = blocks.pack_k_bits_bb(8)
        self.file_sink_0 = blocks.file_sink(
            1,
            'provide/out2.bin',
            False)
        self.file_sink_0.set_unbuffered(False)

        self.connect((self.wav_file_source_0, 0), (self.clock_recovery_mm_0, 0))
        self.connect((self.clock_recovery_mm_0, 0), (self.skip_head_0, 0))
        self.connect((self.skip_head_0, 0), (self.binary_slicer_0, 0))
        self.connect((self.binary_slicer_0, 0), (self.pack_k_bits_0, 0))
        self.connect((self.pack_k_bits_0, 0), (self.file_sink_0, 0))

if __name__ == '__main__':
    tb = phasor()
    tb.start()
    tb.wait()
"""
file_path = sys.argv[1]
d = numpy.fromfile(file_path, dtype=numpy.uint8)
for i in range(8):
    p = numpy.packbits(d[i:])
    file_out_path = 'packed_o{:01d}.bin'.format(i)
    p.tofile(file_out_path)
"""
