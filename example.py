from kadrovik_g4 import Kadrovik


kadrovik = Kadrovik(frame_n=5, out_path='frames/frame_%d.png')
kadrovik.process('input.ts')
