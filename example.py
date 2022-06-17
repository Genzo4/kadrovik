import ffmpeg

stream = ffmpeg.input(
    'output.ts'
).filter(
    'select',
    'not(mod(n,5))',
).output(
    'frames\\out%d.png',
    vsync = 'vfr'
).overwrite_output(
).run(quiet=False)
#print(stream.compile())
#).run(quiet=False)
