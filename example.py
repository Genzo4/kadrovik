from kadrovik_g4 import Kadrovik


kadrovik = Kadrovik(frameN = 5, outPath = 'frames/frame_%d.png')
kadrovik.process('input.ts')
