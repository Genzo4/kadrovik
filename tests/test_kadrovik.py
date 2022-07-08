import pytest
import os
import glob
from kadrovik_g4 import Kadrovik
from utilspy_g4 import compareFrames, templatedRemoveFiles


def _removeTempFiles() -> None:
    """
    Remove temp files
    :rtype: None
    :return: None
    """

    templatedRemoveFiles('tests/frames/*.png')


def test_1():
    kadrovik = Kadrovik()

    assert kadrovik.video == ''
    assert kadrovik.frameN == 5
    assert kadrovik.outPath == 'frame_%d.png'


def test_2():
    kadrovik = Kadrovik(video='test.mp4', frameN=10, outPath='test%d.png')

    assert kadrovik.video == 'test.mp4'
    assert kadrovik.frameN == 10
    assert kadrovik.outPath == 'test%d.png'

    kadrovik.video = 'test2.mkv'
    kadrovik.frameN = 15
    kadrovik.outPath = 'out_path/out_path.png'

    assert kadrovik.video == 'test2.mkv'
    assert kadrovik.frameN == 15
    assert kadrovik.outPath == 'out_path/out_path.png'


def test_3():
    _removeTempFiles()

    kadrovik = Kadrovik(frameN=5, outPath='tests/frames/frame_%d.png')
    kadrovik.process('tests/test.mp4')

    for i in [1, 2, 3, 4]:
        assert compareFrames('tests/frames/frame_%i.png' % i, 'tests/good_frames/frame_%i.png' % i)

    _removeTempFiles()


def test_print(capsys):
    kadrovik = Kadrovik(video='test.mp4', frameN=10, outPath='test%d.png')
    print(kadrovik)
    captured = capsys.readouterr()
    assert captured.out == 'test.mp4 => test%d.png (10)\n'
