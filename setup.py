from setuptools import setup
from os import path


top_level_directory = path.abspath(path.dirname(__file__))
with open(path.join(top_level_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
   name='kadrovik_g4',
   version='1.1.1',
   description='Take frames from video',
   long_description=long_description,
   long_description_content_type='text/markdown',
   author='Genzo',
   author_email='genzo@bk.ru',
   url='https://github.com/Genzo4/kadrovik',
   project_urls={
           'Bug Tracker': 'https://github.com/Genzo4/kadrovik/issues',
       },
   classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Programming Language :: Python :: 3.9',
      'Programming Language :: Python :: 3.10',
      'Programming Language :: Python :: 3.11',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Intended Audience :: Developers',
      'Intended Audience :: Information Technology',
      'Natural Language :: English',
      'Natural Language :: Russian',
      'Topic :: Scientific/Engineering',
      'Topic :: Software Development',
      'Topic :: Software Development :: Libraries :: Python Modules'
   ],
   keywords=['kadrovik', 'ffmpeg-python', 'ffmpeg', 'g4'],
   license='MIT',
   packages=['kadrovik_g4'],
   install_requires=['ffmpeg-python', 'utilspy-g4>=2.2.0', 'compare_frames_g4'],
   python_requires='>=3.6'
)