#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on Thu May 30 09:41:17 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = '15:5 trial test (2)'  # from the Builder filename that created this script
expInfo = {'Your English Initial (e.g. WWY):': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s' % (expInfo['Your English Initial (e.g. WWY):'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/murmur/Desktop/psychopy-final-5/15:5 trial test (2).py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color='Black', colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "survey1"
survey1Clock = core.Clock()
text_145 = visual.TextStim(win=win, name='text_145',
    text='Before you begin, we would like to collect some personal information.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_146 = visual.TextStim(win=win, name='text_146',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "survey2"
survey2Clock = core.Clock()
text_148 = visual.TextStim(win=win, name='text_148',
    text='Gender:',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_149 = visual.TextStim(win=win, name='text_149',
    text='Press M if you are Male\nPress F if you are Female\nPress N if you do not want to specify',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "survey3"
survey3Clock = core.Clock()
text_147 = visual.TextStim(win=win, name='text_147',
    text='Age:',
    font='Arial',
    pos=(0, 0.2), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_150 = visual.TextStim(win=win, name='text_150',
    text='Press A if you are 18-24 years old\nPress B if you are 25-34 years old\nPress C if you are 35-44 years old \nPress D if you are 45-54 years old\nPress E if you are 55-64 years old\nPress F if you are 65-74 years old\nPress G if you are over 74 years old',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "survey4"
survey4Clock = core.Clock()
text_151 = visual.TextStim(win=win, name='text_151',
    text='Ethnicity:',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_152 = visual.TextStim(win=win, name='text_152',
    text='Press W if you are White\nPress H if you are Hispanic\nPress F if you are African American\nPress N if you are Native American\nPress A if you are Asian\nPress O if you are Other',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "survey5"
survey5Clock = core.Clock()
text_153 = visual.TextStim(win=win, name='text_153',
    text='The highest degree or level of education you have completed:',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_154 = visual.TextStim(win=win, name='text_154',
    text='Press P for lower than high school diploma\nPress H for high school degree or equivalent\nPress B for bachelor degree\nPress M for master degree\nPress D for doctorate',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "introduction"
introductionClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Before we go to the real test, ',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_42 = visual.TextStim(win=win, name='text_42',
    text='let’s start with a practice!',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_43 = visual.TextStim(win=win, name='text_43',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_78 = visual.TextStim(win=win, name='text_78',
    text='Thank you for providing us the above information.',
    font='Arial',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "demo2"
demo2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='we assume you have been assigned to be the 2nd member in your group.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_44 = visual.TextStim(win=win, name='text_44',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_79 = visual.TextStim(win=win, name='text_79',
    text='In this practice,',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demo3"
demo3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='and remember the 2 motion videos shown next.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_45 = visual.TextStim(win=win, name='text_45',
    text='Please fixate at the cross in the centre of the screen',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_46 = visual.TextStim(win=win, name='text_46',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demo4"
demo4Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_47 = visual.TextStim(win=win, name='text_47',
    text='Test begins in',
    font='Arial',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demo5"
demo5Clock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "demomovie1"
demomovie1Clock = core.Clock()
movie_2 = visual.MovieStim3(
    win=win, name='movie_2',
    noAudio = False,
    filename='final motion clip 2/demo/1.mp4',
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=0.0,
    )

# Initialize components for Routine "demo6"
demo6Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "demomovie2"
demomovie2Clock = core.Clock()
movie = visual.MovieStim3(
    win=win, name='movie',
    noAudio = False,
    filename='final motion clip 2/demo/2.mp4',
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=0.0,
    )

# Initialize components for Routine "demo7"
demo7Clock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='After viewing the videos, a memory test will follow.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_50 = visual.TextStim(win=win, name='text_50',
    text='You will be viewing the test video first.',
    font='Arial',
    pos=(0, -0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_51 = visual.TextStim(win=win, name='text_51',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_122 = visual.TextStim(win=win, name='text_122',
    text='You would then be asked whether it has appeared before.',
    font='Arial',
    pos=(0, -0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "demo8"
demo8Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_52 = visual.TextStim(win=win, name='text_52',
    text='Test begins in',
    font='Arial',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demo9"
demo9Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "demotest1"
demotest1Clock = core.Clock()
movie_3 = visual.MovieStim3(
    win=win, name='movie_3',
    noAudio = False,
    filename='final motion clip 2/demo/2.mp4',
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=0.0,
    )

# Initialize components for Routine "demo10"
demo10Clock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='Please indicate your answer with the slider.',
    font='Arial',
    pos=(0, 0.15), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_53 = visual.TextStim(win=win, name='text_53',
    text='Remember that the value refers to your confidence level',
    font='Arial',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_54 = visual.TextStim(win=win, name='text_54',
    text='and it represents the mark you would gain if you are correct',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_56 = visual.TextStim(win=win, name='text_56',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_48 = visual.TextStim(win=win, name='text_48',
    text='or the mark you would lose if you are wrong.',
    font='Arial',
    pos=(0, -0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_49 = visual.TextStim(win=win, name='text_49',
    text='Your performance will be determined by ',
    font='Arial',
    pos=(0, -0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_55 = visual.TextStim(win=win, name='text_55',
    text='the total marks you have at the end of the test.',
    font='Arial',
    pos=(0, -0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "demoanswer1"
demoanswer1Clock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='Has the video appeared before? ',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text='NO                                                                                  YES',
    font='Arial',
    pos=(0, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_4 = visual.RatingScale(win=win, name='rating_4', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='0')
text_17 = visual.TextStim(win=win, name='text_17',
    text='the number indicates your confidence level towards NO/YES:',
    font='Arial',
    pos=(-0.42, -0.315), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text='Please slide the slider and press the display box above to proceed',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "demo11"
demo11Clock = core.Clock()
spacebar = visual.TextStim(win=win, name='spacebar',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
score = visual.TextStim(win=win, name='score',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
correct = visual.TextStim(win=win, name='correct',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "demoanswer2"
demoanswer2Clock = core.Clock()
text_19 = visual.TextStim(win=win, name='text_19',
    text='Has the video appeared before? ',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating_5 = visual.RatingScale(win=win, name='rating_5', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='5')
line = visual.Line(
    win=win, name='line',
    start=(-(0.48, 0.2)[0]/2.0, 0), end=(+(0.48, 0.2)[0]/2.0, 0),
    ori=0, pos=(0, 0.3),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
text_20 = visual.TextStim(win=win, name='text_20',
    text='Since you are assigned to be the 2nd member of your group, \nthe response of 1 of your groupmate will appear for your reference.\n\nIn this case, you will have one additional chance \nto answer to the same question.',
    font='Arial',
    pos=(0, 0.1), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
verticalline = visual.Line(
    win=win, name='verticalline',
    start=(-(0.02, 0.02)[0]/2.0, 0), end=(+(0.02, 0.02)[0]/2.0, 0),
    ori=90, pos=(0,0.3),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
triangle = visual.ShapeStim(
    win=win, name='triangle',
    vertices=[[-(0.03, 0.02)[0]/2.0,-(0.03, 0.02)[1]/2.0], [+(0.03, 0.02)[0]/2.0,-(0.03, 0.02)[1]/2.0], [0,(0.03, 0.02)[1]/2.0]],
    ori=180, pos=(0.101, 0.32),
    lineWidth=1, lineColor=[1.000,0.004,-1.000], lineColorSpace='rgb',
    fillColor=[1.000,0.004,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
memberA = visual.TextStim(win=win, name='memberA',
    text='member A',
    font='Arial',
    pos=(-0.33, 0.3), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_28 = visual.TextStim(win=win, name='text_28',
    text='42',
    font='Arial',
    pos=(0.3, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
text_73 = visual.TextStim(win=win, name='text_73',
    text='NO                                                                                  YES',
    font='Arial',
    pos=(0, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
text_117 = visual.TextStim(win=win, name='text_117',
    text='Please slide the slider and press the display box above to proceed',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);

# Initialize components for Routine "demo12"
demo12Clock = core.Clock()
spacebar2 = visual.TextStim(win=win, name='spacebar2',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.25), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
instruction = visual.TextStim(win=win, name='instruction',
    text='In the real test,\nwe will not tell you whether your answer \nis correct or not after each question.\nLet’s try another question!',
    font='Arial',
    pos=(0, -0.1), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
score2 = visual.TextStim(win=win, name='score2',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
correct2 = visual.TextStim(win=win, name='correct2',
    text='s',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
totalscore = visual.TextStim(win=win, name='totalscore',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "demo13"
demo13Clock = core.Clock()
text_21 = visual.TextStim(win=win, name='text_21',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "demotest2"
demotest2Clock = core.Clock()
movie_4 = visual.MovieStim3(
    win=win, name='movie_4',
    noAudio = False,
    filename='final motion clip 2/demo/1.mp4',
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=0.0,
    )

# Initialize components for Routine "demoanswer3"
demoanswer3Clock = core.Clock()
text_22 = visual.TextStim(win=win, name='text_22',
    text='Has the video appeared before? ',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating_6 = visual.RatingScale(win=win, name='rating_6', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='')
text_74 = visual.TextStim(win=win, name='text_74',
    text='NO                                                                                  YES',
    font='Arial',
    pos=(0, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demoanswer4"
demoanswer4Clock = core.Clock()
text_23 = visual.TextStim(win=win, name='text_23',
    text='Has the video appeared before? ',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating_7 = visual.RatingScale(win=win, name='rating_7', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='5')
polygon = visual.Line(
    win=win, name='polygon',
    start=(-(0.48, 0.2)[0]/2.0, 0), end=(+(0.48, 0.2)[0]/2.0, 0),
    ori=0, pos=(0, 0.3),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon_2 = visual.Line(
    win=win, name='polygon_2',
    start=(-(0.02, 0.02)[0]/2.0, 0), end=(+(0.02, 0.02)[0]/2.0, 0),
    ori=90, pos=(0, 0.3),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
triangle2 = visual.ShapeStim(
    win=win, name='triangle2',
    vertices=[[-(0.03, 0.02)[0]/2.0,-(0.03, 0.02)[1]/2.0], [+(0.03, 0.02)[0]/2.0,-(0.03, 0.02)[1]/2.0], [0,(0.03, 0.02)[1]/2.0]],
    ori=180, pos=(-0.204, 0.32),
    lineWidth=1, lineColor=[1.000,0.004,-1.000], lineColorSpace='rgb',
    fillColor=[1.000,0.004,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
memberA2 = visual.TextStim(win=win, name='memberA2',
    text='member A',
    font='Arial',
    pos=(-0.33, 0.3), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_70 = visual.TextStim(win=win, name='text_70',
    text='-85',
    font='Arial',
    pos=(0.3, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_75 = visual.TextStim(win=win, name='text_75',
    text='NO                                                                                  YES',
    font='Arial',
    pos=(0, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "demo14"
demo14Clock = core.Clock()
text_24 = visual.TextStim(win=win, name='text_24',
    text='Sometimes, the test video shown',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_57 = visual.TextStim(win=win, name='text_57',
    text='may not have appeared before.',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_58 = visual.TextStim(win=win, name='text_58',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demo15"
demo15Clock = core.Clock()
text_25 = visual.TextStim(win=win, name='text_25',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "demotest3"
demotest3Clock = core.Clock()
movie_5 = visual.MovieStim3(
    win=win, name='movie_5',
    noAudio = False,
    filename='final motion clip 2/demo/3.mp4',
    ori=0, pos=(0, 0), opacity=1,
    loop=False,
    depth=0.0,
    )

# Initialize components for Routine "demoanswer5"
demoanswer5Clock = core.Clock()
text_26 = visual.TextStim(win=win, name='text_26',
    text='Has the video appeared before? ',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating_8 = visual.RatingScale(win=win, name='rating_8', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='0')
text_76 = visual.TextStim(win=win, name='text_76',
    text='NO                                                                                  YES',
    font='Arial',
    pos=(0, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "demoanswer6"
demoanswer6Clock = core.Clock()
text_27 = visual.TextStim(win=win, name='text_27',
    text='Has the video appeared before? ',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating_9 = visual.RatingScale(win=win, name='rating_9', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='5')
polygon_3 = visual.Line(
    win=win, name='polygon_3',
    start=(-(0.48, 0.2)[0]/2.0, 0), end=(+(0.48, 0.2)[0]/2.0, 0),
    ori=0, pos=(0, 0.3),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon_4 = visual.Line(
    win=win, name='polygon_4',
    start=(-(0.02, 0.02)[0]/2.0, 0), end=(+(0.02, 0.02)[0]/2.0, 0),
    ori=90, pos=(0, 0.3),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
triangle3 = visual.ShapeStim(
    win=win, name='triangle3',
    vertices=[[-(0.03, 0.02)[0]/2.0,-(0.03, 0.02)[1]/2.0], [+(0.03, 0.02)[0]/2.0,-(0.03, 0.02)[1]/2.0], [0,(0.03, 0.02)[1]/2.0]],
    ori=180, pos=(-0.0504, 0.32),
    lineWidth=1, lineColor=[1.000,0.004,-1.000], lineColorSpace='rgb',
    fillColor=[1.000,0.004,-1.000], fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text_71 = visual.TextStim(win=win, name='text_71',
    text='member A',
    font='Arial',
    pos=(-0.33, 0.3), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_72 = visual.TextStim(win=win, name='text_72',
    text='-21',
    font='Arial',
    pos=(0.3, 0.3), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_77 = visual.TextStim(win=win, name='text_77',
    text='NO                                                                                  YES',
    font='Arial',
    pos=(0, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);

# Initialize components for Routine "demo16"
demo16Clock = core.Clock()
nicejob = visual.TextStim(win=win, name='nicejob',
    text='Nice Job!',
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
spacebar3 = visual.TextStim(win=win, name='spacebar3',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
intruction2 = visual.TextStim(win=win, name='intruction2',
    text='You have finished the demo test.',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
totalscore2 = visual.TextStim(win=win, name='totalscore2',
    text='x',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "test1"
test1Clock = core.Clock()
text_29 = visual.TextStim(win=win, name='text_29',
    text='Let’s begin the real experiment!',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_59 = visual.TextStim(win=win, name='text_59',
    text='Now you will be randomly assigned into a group of 4 people',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_60 = visual.TextStim(win=win, name='text_60',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "test2"
test2Clock = core.Clock()
text_61 = visual.TextStim(win=win, name='text_61',
    text='Loading...',
    font='Arial',
    pos=(-0.02, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_30 = visual.TextStim(win=win, name='text_30',
    text='...',
    font='Arial',
    pos=(0.06, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_32 = visual.TextStim(win=win, name='text_32',
    text='...',
    font='Arial',
    pos=(0.06, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "test3"
test3Clock = core.Clock()
text_34 = visual.TextStim(win=win, name='text_34',
    text='You are assigned to group',
    font='Arial',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_31 = visual.TextStim(win=win, name='text_31',
    text='You are the           member of the group',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_33 = visual.TextStim(win=win, name='text_33',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
group13 = visual.TextStim(win=win, name='group13',
    text='#13',
    font='Arial',
    pos=(0.02, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
no4 = visual.TextStim(win=win, name='no4',
    text='4th',
    font='Arial',
    pos=(-0.06,0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "test4"
test4Clock = core.Clock()
text_35 = visual.TextStim(win=win, name='text_35',
    text='Please remember the 45 motion videos shown next ',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_62 = visual.TextStim(win=win, name='text_62',
    text='Please fixate at the cross in the center of the screen',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_63 = visual.TextStim(win=win, name='text_63',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "test5"
test5Clock = core.Clock()
text_36 = visual.TextStim(win=win, name='text_36',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_37 = visual.TextStim(win=win, name='text_37',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_38 = visual.TextStim(win=win, name='text_38',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_64 = visual.TextStim(win=win, name='text_64',
    text='Test begins in',
    font='Arial',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "testfixation"
testfixationClock = core.Clock()
text_39 = visual.TextStim(win=win, name='text_39',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testvideo"
testvideoClock = core.Clock()

# Initialize components for Routine "mathtest"
mathtestClock = core.Clock()
text_40 = visual.TextStim(win=win, name='text_40',
    text='All the videos have been played.',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_118 = visual.TextStim(win=win, name='text_118',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_119 = visual.TextStim(win=win, name='text_119',
    text='Please calculate the answers for the maths questions',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_123 = visual.TextStim(win=win, name='text_123',
    text='before the memory test.',
    font='Arial',
    pos=(0, -0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "mathquestion1"
mathquestion1Clock = core.Clock()
text_41 = visual.TextStim(win=win, name='text_41',
    text='17-8 = ?\n',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
rating = visual.RatingScale(win=win, name='rating', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', ' 100'], scale='', markerStart='0')
text_65 = visual.TextStim(win=win, name='text_65',
    text='Please slide the slider and press the display box above to proceed',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "mathquestion2"
mathquestion2Clock = core.Clock()
text_66 = visual.TextStim(win=win, name='text_66',
    text='22-11+7 = ?',
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_67 = visual.TextStim(win=win, name='text_67',
    text='Please slide the slider and press the display box above to proceed',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_2 = visual.RatingScale(win=win, name='rating_2', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='0')

# Initialize components for Routine "mathquestion3"
mathquestion3Clock = core.Clock()
text_68 = visual.TextStim(win=win, name='text_68',
    text='24-31+5 = ? ',
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_69 = visual.TextStim(win=win, name='text_69',
    text='Please slide the slider and press the display box above to proceed',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_3 = visual.RatingScale(win=win, name='rating_3', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='0')

# Initialize components for Routine "mathquestion4"
mathquestion4Clock = core.Clock()
text_131 = visual.TextStim(win=win, name='text_131',
    text='12-9+5 = ? ',
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_132 = visual.TextStim(win=win, name='text_132',
    text='Please slide the slider and press the display box above to proceed',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_14 = visual.RatingScale(win=win, name='rating_14', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='0')

# Initialize components for Routine "mathquestion5"
mathquestion5Clock = core.Clock()
text_133 = visual.TextStim(win=win, name='text_133',
    text='21-12+5 = ?',
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_134 = visual.TextStim(win=win, name='text_134',
    text='Please slide the slider and press the display box above to proceed',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_15 = visual.RatingScale(win=win, name='rating_15', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='0')

# Initialize components for Routine "mathquestion6"
mathquestion6Clock = core.Clock()
text_135 = visual.TextStim(win=win, name='text_135',
    text='4+9-3 = ?',
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_136 = visual.TextStim(win=win, name='text_136',
    text='Please slide the slider and press the display box above to proceed',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_16 = visual.RatingScale(win=win, name='rating_16', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='0')

# Initialize components for Routine "mathquestion7"
mathquestion7Clock = core.Clock()
text_137 = visual.TextStim(win=win, name='text_137',
    text='5-21+7 = ?',
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_138 = visual.TextStim(win=win, name='text_138',
    text='Please slide the slider and press the display box above to proceed',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_17 = visual.RatingScale(win=win, name='rating_17', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='0')

# Initialize components for Routine "mathquestion8"
mathquestion8Clock = core.Clock()
text_139 = visual.TextStim(win=win, name='text_139',
    text='2-5+9 = ?',
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_140 = visual.TextStim(win=win, name='text_140',
    text='Please slide the slider and press the display box above to proceed',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_18 = visual.RatingScale(win=win, name='rating_18', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='0')

# Initialize components for Routine "mathquestion9"
mathquestion9Clock = core.Clock()
text_141 = visual.TextStim(win=win, name='text_141',
    text='7+9+8 = ?',
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_142 = visual.TextStim(win=win, name='text_142',
    text='Please slide the slider and press the display box above to proceed',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_19 = visual.RatingScale(win=win, name='rating_19', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='0')

# Initialize components for Routine "mathquestion10"
mathquestion10Clock = core.Clock()
text_143 = visual.TextStim(win=win, name='text_143',
    text='9-15+3 = ?',
    font='Arial',
    pos=(0, 0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_144 = visual.TextStim(win=win, name='text_144',
    text='Please slide the slider and press the display box above to proceed',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
rating_20 = visual.RatingScale(win=win, name='rating_20', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', '100'], scale='', markerStart='0')

# Initialize components for Routine "pretest"
pretestClock = core.Clock()
text_102 = visual.TextStim(win=win, name='text_102',
    text='Here comes the memory test.',
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_103 = visual.TextStim(win=win, name='text_103',
    text='Please press spacebar when you are ready',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_104 = visual.TextStim(win=win, name='text_104',
    text='4th',
    font='Arial',
    pos=(-0.05, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_105 = visual.TextStim(win=win, name='text_105',
    text='3',
    font='Arial',
    pos=(-0.21, -0.05), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
text_120 = visual.TextStim(win=win, name='text_120',
    text='As you are the          member of the group,',
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_121 = visual.TextStim(win=win, name='text_121',
    text='you will have          more chances to answer the same question.',
    font='Arial',
    pos=(0, -0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);

# Initialize components for Routine "demo8"
demo8Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_11 = visual.TextStim(win=win, name='text_11',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text='1',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_52 = visual.TextStim(win=win, name='text_52',
    text='Test begins in',
    font='Arial',
    pos=(0, 0.1), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "testfixation_2"
testfixation_2Clock = core.Clock()
text_106 = visual.TextStim(win=win, name='text_106',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testmovie"
testmovieClock = core.Clock()

# Initialize components for Routine "loop1"
loop1Clock = core.Clock()
rating_10 = visual.RatingScale(win=win, name='rating_10', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['100', '100'], scale='', markerStart='0')
text_107 = visual.TextStim(win=win, name='text_107',
    text='NO                                                                                  YES',
    font='Arial',
    pos=(0, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_127 = visual.TextStim(win=win, name='text_127',
    text='Has the video appeared before? ',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "loop2"
loop2Clock = core.Clock()
rating_11 = visual.RatingScale(win=win, name='rating_11', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['100', '100'], scale='', markerStart='0')
polygon_5 = visual.Line(
    win=win, name='polygon_5',
    start=(-(0.48, 0.2)[0]/2.0, 0), end=(+(0.48, 0.2)[0]/2.0, 0),
    ori=0, pos=(0, 0.3),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
trianglecon1 = visual.ShapeStim(
    win=win, name='trianglecon1',
    vertices=[[-(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [+(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [0,(0.5, 0.5)[1]/2.0]],
    ori=0, pos=(0.084, 0.32),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
polygon_6 = visual.Line(
    win=win, name='polygon_6',
    start=(-(0.02, 0.02)[0]/2.0, 0), end=(+(0.02, 0.02)[0]/2.0, 0),
    ori=90, pos=(0, 0.3),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
conScore = visual.TextStim(win=win, name='conScore',
    text='2',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_108 = visual.TextStim(win=win, name='text_108',
    text='member A',
    font='Arial',
    pos=(-0.33, 0.3), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
from random import uniform, random
from random import uniform, random, choice, sample
text_124 = visual.TextStim(win=win, name='text_124',
    text='NO                                                                                  YES',
    font='Arial',
    pos=(0, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
text_128 = visual.TextStim(win=win, name='text_128',
    text='Has the video appeared before? ',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);

# Initialize components for Routine "loop3"
loop3Clock = core.Clock()
rating_12 = visual.RatingScale(win=win, name='rating_12', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['100', '100'], scale='')
polygon_7 = visual.Line(
    win=win, name='polygon_7',
    start=(-(0.48, 0.2)[0]/2.0, 0), end=(+(0.48, 0.2)[0]/2.0, 0),
    ori=0, pos=(0, 0.2),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon_8 = visual.Line(
    win=win, name='polygon_8',
    start=(-(0.02, 0.02)[0]/2.0, 0), end=(+(0.02, 0.02)[0]/2.0, 0),
    ori=90, pos=(0, 0.2),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
trianglecon2 = visual.ShapeStim(
    win=win, name='trianglecon2',
    vertices=[[-(0.084, 0.32)[0]/2.0,-(0.084, 0.32)[1]/2.0], [+(0.084, 0.32)[0]/2.0,-(0.084, 0.32)[1]/2.0], [0,(0.084, 0.32)[1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
conScore2 = visual.TextStim(win=win, name='conScore2',
    text='3',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_109 = visual.TextStim(win=win, name='text_109',
    text='member B',
    font='Arial',
    pos=(-0.33, 0.2), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
polygon_9 = visual.Line(
    win=win, name='polygon_9',
    start=(-(0.48, 0.2)[0]/2.0, 0), end=(+(0.48, 0.2)[0]/2.0, 0),
    ori=0, pos=(0, 0.3),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
polygon_10 = visual.Line(
    win=win, name='polygon_10',
    start=(-(0.02, 0.02)[0]/2.0, 0), end=(+(0.02, 0.02)[0]/2.0, 0),
    ori=90, pos=(0, 0.3),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
triangle3_1 = visual.ShapeStim(
    win=win, name='triangle3_1',
    vertices=[[-(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [+(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [0,(0.5, 0.5)[1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
conScore1_1 = visual.TextStim(win=win, name='conScore1_1',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_110 = visual.TextStim(win=win, name='text_110',
    text='member A',
    font='Arial',
    pos=(-0.33, 0.3), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
text_125 = visual.TextStim(win=win, name='text_125',
    text='NO                                                                                  YES',
    font='Arial',
    pos=(0, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-14.0);
text_129 = visual.TextStim(win=win, name='text_129',
    text='Has the video appeared before? ',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-15.0);

# Initialize components for Routine "loop4"
loop4Clock = core.Clock()
rating_13 = visual.RatingScale(win=win, name='rating_13', marker='triangle', size=1.0, pos=[0.0, -0.4], low=1, high=7, labels=[''], scale='')
polygon_11 = visual.Line(
    win=win, name='polygon_11',
    start=(-(0.48, 0.2)[0]/2.0, 0), end=(+(0.48, 0.2)[0]/2.0, 0),
    ori=0, pos=(0, 0.1),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
polygon_12 = visual.Line(
    win=win, name='polygon_12',
    start=(-(0.02, 0.02)[0]/2.0, 0), end=(+(0.02, 0.02)[0]/2.0, 0),
    ori=90, pos=(0, 0.1),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
triangle4 = visual.ShapeStim(
    win=win, name='triangle4',
    vertices=[[-(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [+(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [0,(0.5, 0.5)[1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
conScore3 = visual.TextStim(win=win, name='conScore3',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-5.0);
text_111 = visual.TextStim(win=win, name='text_111',
    text='member C',
    font='Arial',
    pos=(-0.33, 0.1), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
triangle1_2 = visual.ShapeStim(
    win=win, name='triangle1_2',
    vertices=[[-(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [+(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [0,(0.5, 0.5)[1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
polygon_13 = visual.Line(
    win=win, name='polygon_13',
    start=(-(0.48, 0.2)[0]/2.0, 0), end=(+(0.48, 0.2)[0]/2.0, 0),
    ori=0, pos=(0, 0.3),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
polygon_14 = visual.Line(
    win=win, name='polygon_14',
    start=(-(0.02, 0.02)[0]/2.0, 0), end=(+(0.02, 0.02)[0]/2.0, 0),
    ori=90, pos=(0, 0.3),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
conScore1_2 = visual.TextStim(win=win, name='conScore1_2',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
text_112 = visual.TextStim(win=win, name='text_112',
    text='member A',
    font='Arial',
    pos=(-0.33, 0.3), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);
triangle2_1 = visual.ShapeStim(
    win=win, name='triangle2_1',
    vertices=[[-(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [+(0.5, 0.5)[0]/2.0,-(0.5, 0.5)[1]/2.0], [0,(0.5, 0.5)[1]/2.0]],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-14.0, interpolate=True)
polygon_15 = visual.Line(
    win=win, name='polygon_15',
    start=(-(0.02, 0.02)[0]/2.0, 0), end=(+(0.02, 0.02)[0]/2.0, 0),
    ori=90, pos=(0, 0.2),
    lineWidth=5, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-15.0, interpolate=True)
polygon_16 = visual.Line(
    win=win, name='polygon_16',
    start=(-(0.48, 0.2)[0]/2.0, 0), end=(+(0.48, 0.2)[0]/2.0, 0),
    ori=0, pos=(0, 0.2),
    lineWidth=7, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-16.0, interpolate=True)
conScore2_1 = visual.TextStim(win=win, name='conScore2_1',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);
text_113 = visual.TextStim(win=win, name='text_113',
    text='member B',
    font='Arial',
    pos=(-0.33, 0.2), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-18.0);
text_126 = visual.TextStim(win=win, name='text_126',
    text='NO                                                                                  YES',
    font='Arial',
    pos=(0, -0.15), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-20.0);
text_130 = visual.TextStim(win=win, name='text_130',
    text='Has the video appeared before? ',
    font='Arial',
    pos=(0, 0.4), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-21.0);

# Initialize components for Routine "Bye"
ByeClock = core.Clock()
text_114 = visual.TextStim(win=win, name='text_114',
    text='GOOD JOB!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
text_115 = visual.TextStim(win=win, name='text_115',
    text='You’ve completed the test!',
    font='Arial',
    pos=(0, -0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
text_116 = visual.TextStim(win=win, name='text_116',
    text='Please press spacebar to continue',
    font='Arial',
    pos=(0, -0.2), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "survey1"-------
t = 0
survey1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_16 = keyboard.Keyboard()
# keep track of which components have finished
survey1Components = [text_145, text_146, key_resp_16]
for thisComponent in survey1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "survey1"-------
while continueRoutine:
    # get current time
    t = survey1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_145* updates
    if t >= 0.0 and text_145.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_145.tStart = t  # not accounting for scr refresh
        text_145.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_145, 'tStartRefresh')  # time at next scr refresh
        text_145.setAutoDraw(True)
    
    # *text_146* updates
    if t >= 0.0 and text_146.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_146.tStart = t  # not accounting for scr refresh
        text_146.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_146, 'tStartRefresh')  # time at next scr refresh
        text_146.setAutoDraw(True)
    
    # *key_resp_16* updates
    if t >= 0.0 and key_resp_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_16.tStart = t  # not accounting for scr refresh
        key_resp_16.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
        key_resp_16.status = STARTED
        # keyboard checking is just starting
        key_resp_16.clearEvents(eventType='keyboard')
    if key_resp_16.status == STARTED:
        theseKeys = key_resp_16.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in survey1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey1"-------
for thisComponent in survey1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_145.started', text_145.tStartRefresh)
thisExp.addData('text_145.stopped', text_145.tStopRefresh)
thisExp.addData('text_146.started', text_146.tStartRefresh)
thisExp.addData('text_146.stopped', text_146.tStopRefresh)
# the Routine "survey1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "survey2"-------
t = 0
survey2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_17 = keyboard.Keyboard()
# keep track of which components have finished
survey2Components = [text_148, text_149, key_resp_17]
for thisComponent in survey2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "survey2"-------
while continueRoutine:
    # get current time
    t = survey2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_148* updates
    if t >= 0.0 and text_148.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_148.tStart = t  # not accounting for scr refresh
        text_148.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_148, 'tStartRefresh')  # time at next scr refresh
        text_148.setAutoDraw(True)
    
    # *text_149* updates
    if t >= 0.0 and text_149.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_149.tStart = t  # not accounting for scr refresh
        text_149.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_149, 'tStartRefresh')  # time at next scr refresh
        text_149.setAutoDraw(True)
    
    # *key_resp_17* updates
    if t >= 0.0 and key_resp_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_17.tStart = t  # not accounting for scr refresh
        key_resp_17.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
        key_resp_17.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
        key_resp_17.clearEvents(eventType='keyboard')
    if key_resp_17.status == STARTED:
        theseKeys = key_resp_17.getKeys(keyList=['m', 'n', 'f'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_17.keys = theseKeys.name  # just the last key pressed
            key_resp_17.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in survey2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey2"-------
for thisComponent in survey2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_148.started', text_148.tStartRefresh)
thisExp.addData('text_148.stopped', text_148.tStopRefresh)
thisExp.addData('text_149.started', text_149.tStartRefresh)
thisExp.addData('text_149.stopped', text_149.tStopRefresh)
# check responses
if key_resp_17.keys in ['', [], None]:  # No response was made
    key_resp_17.keys = None
thisExp.addData('key_resp_17.keys',key_resp_17.keys)
if key_resp_17.keys != None:  # we had a response
    thisExp.addData('key_resp_17.rt', key_resp_17.rt)
thisExp.addData('key_resp_17.started', key_resp_17.tStartRefresh)
thisExp.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
thisExp.nextEntry()
# the Routine "survey2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "survey3"-------
t = 0
survey3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_18 = keyboard.Keyboard()
# keep track of which components have finished
survey3Components = [text_147, text_150, key_resp_18]
for thisComponent in survey3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "survey3"-------
while continueRoutine:
    # get current time
    t = survey3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_147* updates
    if t >= 0.0 and text_147.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_147.tStart = t  # not accounting for scr refresh
        text_147.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_147, 'tStartRefresh')  # time at next scr refresh
        text_147.setAutoDraw(True)
    
    # *text_150* updates
    if t >= 0.0 and text_150.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_150.tStart = t  # not accounting for scr refresh
        text_150.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_150, 'tStartRefresh')  # time at next scr refresh
        text_150.setAutoDraw(True)
    
    # *key_resp_18* updates
    if t >= 0.0 and key_resp_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_18.tStart = t  # not accounting for scr refresh
        key_resp_18.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
        key_resp_18.clearEvents(eventType='keyboard')
    if key_resp_18.status == STARTED:
        theseKeys = key_resp_18.getKeys(keyList=['a', 'b', 'c', 'd', 'e', 'f', 'g'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_18.keys = theseKeys.name  # just the last key pressed
            key_resp_18.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in survey3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey3"-------
for thisComponent in survey3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_147.started', text_147.tStartRefresh)
thisExp.addData('text_147.stopped', text_147.tStopRefresh)
thisExp.addData('text_150.started', text_150.tStartRefresh)
thisExp.addData('text_150.stopped', text_150.tStopRefresh)
# check responses
if key_resp_18.keys in ['', [], None]:  # No response was made
    key_resp_18.keys = None
thisExp.addData('key_resp_18.keys',key_resp_18.keys)
if key_resp_18.keys != None:  # we had a response
    thisExp.addData('key_resp_18.rt', key_resp_18.rt)
thisExp.addData('key_resp_18.started', key_resp_18.tStartRefresh)
thisExp.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
thisExp.nextEntry()
# the Routine "survey3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "survey4"-------
t = 0
survey4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_19 = keyboard.Keyboard()
# keep track of which components have finished
survey4Components = [text_151, text_152, key_resp_19]
for thisComponent in survey4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "survey4"-------
while continueRoutine:
    # get current time
    t = survey4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_151* updates
    if t >= 0.0 and text_151.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_151.tStart = t  # not accounting for scr refresh
        text_151.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_151, 'tStartRefresh')  # time at next scr refresh
        text_151.setAutoDraw(True)
    
    # *text_152* updates
    if t >= 0.0 and text_152.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_152.tStart = t  # not accounting for scr refresh
        text_152.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_152, 'tStartRefresh')  # time at next scr refresh
        text_152.setAutoDraw(True)
    
    # *key_resp_19* updates
    if t >= 0.0 and key_resp_19.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_19.tStart = t  # not accounting for scr refresh
        key_resp_19.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
        key_resp_19.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
        key_resp_19.clearEvents(eventType='keyboard')
    if key_resp_19.status == STARTED:
        theseKeys = key_resp_19.getKeys(keyList=['w', 'h', 'f', 'n', 'a', 'o'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_19.keys = theseKeys.name  # just the last key pressed
            key_resp_19.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in survey4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey4"-------
for thisComponent in survey4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_151.started', text_151.tStartRefresh)
thisExp.addData('text_151.stopped', text_151.tStopRefresh)
thisExp.addData('text_152.started', text_152.tStartRefresh)
thisExp.addData('text_152.stopped', text_152.tStopRefresh)
# check responses
if key_resp_19.keys in ['', [], None]:  # No response was made
    key_resp_19.keys = None
thisExp.addData('key_resp_19.keys',key_resp_19.keys)
if key_resp_19.keys != None:  # we had a response
    thisExp.addData('key_resp_19.rt', key_resp_19.rt)
thisExp.addData('key_resp_19.started', key_resp_19.tStartRefresh)
thisExp.addData('key_resp_19.stopped', key_resp_19.tStopRefresh)
thisExp.nextEntry()
# the Routine "survey4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "survey5"-------
t = 0
survey5Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_20 = keyboard.Keyboard()
# keep track of which components have finished
survey5Components = [text_153, text_154, key_resp_20]
for thisComponent in survey5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "survey5"-------
while continueRoutine:
    # get current time
    t = survey5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_153* updates
    if t >= 0.0 and text_153.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_153.tStart = t  # not accounting for scr refresh
        text_153.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_153, 'tStartRefresh')  # time at next scr refresh
        text_153.setAutoDraw(True)
    
    # *text_154* updates
    if t >= 0.0 and text_154.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_154.tStart = t  # not accounting for scr refresh
        text_154.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_154, 'tStartRefresh')  # time at next scr refresh
        text_154.setAutoDraw(True)
    
    # *key_resp_20* updates
    if t >= 0.0 and key_resp_20.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_20.tStart = t  # not accounting for scr refresh
        key_resp_20.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        key_resp_20.clearEvents(eventType='keyboard')
    if key_resp_20.status == STARTED:
        theseKeys = key_resp_20.getKeys(keyList=['p', 'h', 'b', 'm', 'd'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_20.keys = theseKeys.name  # just the last key pressed
            key_resp_20.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in survey5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey5"-------
for thisComponent in survey5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_153.started', text_153.tStartRefresh)
thisExp.addData('text_153.stopped', text_153.tStopRefresh)
thisExp.addData('text_154.started', text_154.tStartRefresh)
thisExp.addData('text_154.stopped', text_154.tStopRefresh)
# check responses
if key_resp_20.keys in ['', [], None]:  # No response was made
    key_resp_20.keys = None
thisExp.addData('key_resp_20.keys',key_resp_20.keys)
if key_resp_20.keys != None:  # we had a response
    thisExp.addData('key_resp_20.rt', key_resp_20.rt)
thisExp.addData('key_resp_20.started', key_resp_20.tStartRefresh)
thisExp.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
thisExp.nextEntry()
# the Routine "survey5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "introduction"-------
t = 0
introductionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp = keyboard.Keyboard()
# keep track of which components have finished
introductionComponents = [text, key_resp, text_42, text_43, text_78]
for thisComponent in introductionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "introduction"-------
while continueRoutine:
    # get current time
    t = introductionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # not accounting for scr refresh
        text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    if t >= 0.5 and key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp.tStart = t  # not accounting for scr refresh
        key_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        key_resp.clearEvents(eventType='keyboard')
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_42* updates
    if t >= 0.0 and text_42.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_42.tStart = t  # not accounting for scr refresh
        text_42.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_42, 'tStartRefresh')  # time at next scr refresh
        text_42.setAutoDraw(True)
    
    # *text_43* updates
    if t >= 0.0 and text_43.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_43.tStart = t  # not accounting for scr refresh
        text_43.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_43, 'tStartRefresh')  # time at next scr refresh
        text_43.setAutoDraw(True)
    
    # *text_78* updates
    if t >= 0.0 and text_78.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_78.tStart = t  # not accounting for scr refresh
        text_78.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_78, 'tStartRefresh')  # time at next scr refresh
        text_78.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introductionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "introduction"-------
for thisComponent in introductionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('text_42.started', text_42.tStartRefresh)
thisExp.addData('text_42.stopped', text_42.tStopRefresh)
thisExp.addData('text_43.started', text_43.tStartRefresh)
thisExp.addData('text_43.stopped', text_43.tStopRefresh)
thisExp.addData('text_78.started', text_78.tStartRefresh)
thisExp.addData('text_78.stopped', text_78.tStopRefresh)
# the Routine "introduction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo2"-------
t = 0
demo2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = keyboard.Keyboard()
# keep track of which components have finished
demo2Components = [text_2, key_resp_2, text_44, text_79]
for thisComponent in demo2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo2"-------
while continueRoutine:
    # get current time
    t = demo2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # not accounting for scr refresh
        text_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # not accounting for scr refresh
        key_resp_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        key_resp_2.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_44* updates
    if t >= 0.0 and text_44.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_44.tStart = t  # not accounting for scr refresh
        text_44.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_44, 'tStartRefresh')  # time at next scr refresh
        text_44.setAutoDraw(True)
    
    # *text_79* updates
    if t >= 0.0 and text_79.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_79.tStart = t  # not accounting for scr refresh
        text_79.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_79, 'tStartRefresh')  # time at next scr refresh
        text_79.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo2"-------
for thisComponent in demo2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('text_44.started', text_44.tStartRefresh)
thisExp.addData('text_44.stopped', text_44.tStopRefresh)
thisExp.addData('text_79.started', text_79.tStartRefresh)
thisExp.addData('text_79.stopped', text_79.tStopRefresh)
# the Routine "demo2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo3"-------
t = 0
demo3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = keyboard.Keyboard()
# keep track of which components have finished
demo3Components = [text_3, key_resp_3, text_45, text_46]
for thisComponent in demo3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo3"-------
while continueRoutine:
    # get current time
    t = demo3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # not accounting for scr refresh
        text_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # not accounting for scr refresh
        key_resp_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        key_resp_3.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_45* updates
    if t >= 0.0 and text_45.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_45.tStart = t  # not accounting for scr refresh
        text_45.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_45, 'tStartRefresh')  # time at next scr refresh
        text_45.setAutoDraw(True)
    
    # *text_46* updates
    if t >= 0.0 and text_46.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_46.tStart = t  # not accounting for scr refresh
        text_46.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_46, 'tStartRefresh')  # time at next scr refresh
        text_46.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo3"-------
for thisComponent in demo3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('text_45.started', text_45.tStartRefresh)
thisExp.addData('text_45.stopped', text_45.tStopRefresh)
thisExp.addData('text_46.started', text_46.tStartRefresh)
thisExp.addData('text_46.stopped', text_46.tStopRefresh)
# the Routine "demo3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo4"-------
t = 0
demo4Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
demo4Components = [text_4, text_5, text_6, text_47]
for thisComponent in demo4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demo4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if t >= 0 and text_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_4.tStart = t  # not accounting for scr refresh
        text_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    frameRemains = 0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_4.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_4.tStop = t  # not accounting for scr refresh
        text_4.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
        text_4.setAutoDraw(False)
    
    # *text_5* updates
    if t >= 1 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # not accounting for scr refresh
        text_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    frameRemains = 1 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_5.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_5.tStop = t  # not accounting for scr refresh
        text_5.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
        text_5.setAutoDraw(False)
    
    # *text_6* updates
    if t >= 2 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # not accounting for scr refresh
        text_6.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    frameRemains = 2 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_6.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_6.tStop = t  # not accounting for scr refresh
        text_6.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
        text_6.setAutoDraw(False)
    
    # *text_47* updates
    if t >= 0.0 and text_47.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_47.tStart = t  # not accounting for scr refresh
        text_47.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_47, 'tStartRefresh')  # time at next scr refresh
        text_47.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_47.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_47.tStop = t  # not accounting for scr refresh
        text_47.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_47, 'tStopRefresh')  # time at next scr refresh
        text_47.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo4"-------
for thisComponent in demo4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
thisExp.addData('text_47.started', text_47.tStartRefresh)
thisExp.addData('text_47.stopped', text_47.tStopRefresh)

# ------Prepare to start Routine "demo5"-------
t = 0
demo5Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
demo5Components = [text_7]
for thisComponent in demo5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo5"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demo5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t  # not accounting for scr refresh
        text_7.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_7.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_7.tStop = t  # not accounting for scr refresh
        text_7.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
        text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo5"-------
for thisComponent in demo5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# ------Prepare to start Routine "demomovie1"-------
t = 0
demomovie1Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
demomovie1Components = [movie_2]
for thisComponent in demomovie1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demomovie1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demomovie1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie_2* updates
    if t >= 0.0 and movie_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        movie_2.tStart = t  # not accounting for scr refresh
        movie_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(movie_2, 'tStartRefresh')  # time at next scr refresh
        movie_2.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if movie_2.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        movie_2.tStop = t  # not accounting for scr refresh
        movie_2.frameNStop = frameN  # exact frame index
        win.timeOnFlip(movie_2, 'tStopRefresh')  # time at next scr refresh
        movie_2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demomovie1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demomovie1"-------
for thisComponent in demomovie1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('movie_2.started', movie_2.tStartRefresh)
thisExp.addData('movie_2.stopped', movie_2.tStopRefresh)

# ------Prepare to start Routine "demo6"-------
t = 0
demo6Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
demo6Components = [text_8]
for thisComponent in demo6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo6"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demo6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t  # not accounting for scr refresh
        text_8.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_8.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_8.tStop = t  # not accounting for scr refresh
        text_8.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
        text_8.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo6"-------
for thisComponent in demo6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)

# ------Prepare to start Routine "demomovie2"-------
t = 0
demomovie2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
demomovie2Components = [movie]
for thisComponent in demomovie2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demomovie2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demomovie2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie* updates
    if t >= 0.0 and movie.status == NOT_STARTED:
        # keep track of start time/frame for later
        movie.tStart = t  # not accounting for scr refresh
        movie.frameNStart = frameN  # exact frame index
        win.timeOnFlip(movie, 'tStartRefresh')  # time at next scr refresh
        movie.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if movie.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        movie.tStop = t  # not accounting for scr refresh
        movie.frameNStop = frameN  # exact frame index
        win.timeOnFlip(movie, 'tStopRefresh')  # time at next scr refresh
        movie.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demomovie2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demomovie2"-------
for thisComponent in demomovie2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('movie.started', movie.tStartRefresh)
thisExp.addData('movie.stopped', movie.tStopRefresh)

# ------Prepare to start Routine "demo7"-------
t = 0
demo7Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = keyboard.Keyboard()
# keep track of which components have finished
demo7Components = [text_9, key_resp_4, text_50, text_51, text_122]
for thisComponent in demo7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo7"-------
while continueRoutine:
    # get current time
    t = demo7Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t  # not accounting for scr refresh
        text_9.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # not accounting for scr refresh
        key_resp_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        key_resp_4.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_50* updates
    if t >= 0.0 and text_50.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_50.tStart = t  # not accounting for scr refresh
        text_50.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_50, 'tStartRefresh')  # time at next scr refresh
        text_50.setAutoDraw(True)
    
    # *text_51* updates
    if t >= 0.0 and text_51.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_51.tStart = t  # not accounting for scr refresh
        text_51.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_51, 'tStartRefresh')  # time at next scr refresh
        text_51.setAutoDraw(True)
    
    # *text_122* updates
    if t >= 0.0 and text_122.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_122.tStart = t  # not accounting for scr refresh
        text_122.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_122, 'tStartRefresh')  # time at next scr refresh
        text_122.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo7"-------
for thisComponent in demo7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
thisExp.addData('text_50.started', text_50.tStartRefresh)
thisExp.addData('text_50.stopped', text_50.tStopRefresh)
thisExp.addData('text_51.started', text_51.tStartRefresh)
thisExp.addData('text_51.stopped', text_51.tStopRefresh)
thisExp.addData('text_122.started', text_122.tStartRefresh)
thisExp.addData('text_122.stopped', text_122.tStopRefresh)
# the Routine "demo7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo8"-------
t = 0
demo8Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
demo8Components = [text_10, text_11, text_12, text_52]
for thisComponent in demo8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo8"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demo8Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t  # not accounting for scr refresh
        text_10.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_10.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_10.tStop = t  # not accounting for scr refresh
        text_10.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
        text_10.setAutoDraw(False)
    
    # *text_11* updates
    if t >= 1 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t  # not accounting for scr refresh
        text_11.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_11.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_11.tStop = t  # not accounting for scr refresh
        text_11.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
        text_11.setAutoDraw(False)
    
    # *text_12* updates
    if t >= 2 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t  # not accounting for scr refresh
        text_12.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    frameRemains = 2 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_12.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_12.tStop = t  # not accounting for scr refresh
        text_12.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
        text_12.setAutoDraw(False)
    
    # *text_52* updates
    if t >= 0.0 and text_52.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_52.tStart = t  # not accounting for scr refresh
        text_52.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
        text_52.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_52.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_52.tStop = t  # not accounting for scr refresh
        text_52.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_52, 'tStopRefresh')  # time at next scr refresh
        text_52.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo8"-------
for thisComponent in demo8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
thisExp.addData('text_52.started', text_52.tStartRefresh)
thisExp.addData('text_52.stopped', text_52.tStopRefresh)

# ------Prepare to start Routine "demo9"-------
t = 0
demo9Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
demo9Components = [text_13]
for thisComponent in demo9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo9"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demo9Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if t >= 0.0 and text_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_13.tStart = t  # not accounting for scr refresh
        text_13.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_13.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_13.tStop = t  # not accounting for scr refresh
        text_13.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_13, 'tStopRefresh')  # time at next scr refresh
        text_13.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo9"-------
for thisComponent in demo9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)

# ------Prepare to start Routine "demotest1"-------
t = 0
demotest1Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
demotest1Components = [movie_3]
for thisComponent in demotest1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demotest1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demotest1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie_3* updates
    if t >= 0.0 and movie_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        movie_3.tStart = t  # not accounting for scr refresh
        movie_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(movie_3, 'tStartRefresh')  # time at next scr refresh
        movie_3.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if movie_3.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        movie_3.tStop = t  # not accounting for scr refresh
        movie_3.frameNStop = frameN  # exact frame index
        win.timeOnFlip(movie_3, 'tStopRefresh')  # time at next scr refresh
        movie_3.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demotest1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demotest1"-------
for thisComponent in demotest1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('movie_3.started', movie_3.tStartRefresh)
thisExp.addData('movie_3.stopped', movie_3.tStopRefresh)

# ------Prepare to start Routine "demo10"-------
t = 0
demo10Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = keyboard.Keyboard()
# keep track of which components have finished
demo10Components = [text_14, key_resp_5, text_53, text_54, text_56, text_48, text_49, text_55]
for thisComponent in demo10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo10"-------
while continueRoutine:
    # get current time
    t = demo10Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_14* updates
    if t >= 0.0 and text_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_14.tStart = t  # not accounting for scr refresh
        text_14.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # not accounting for scr refresh
        key_resp_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        key_resp_5.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_53* updates
    if t >= 0.0 and text_53.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_53.tStart = t  # not accounting for scr refresh
        text_53.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_53, 'tStartRefresh')  # time at next scr refresh
        text_53.setAutoDraw(True)
    
    # *text_54* updates
    if t >= 0.0 and text_54.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_54.tStart = t  # not accounting for scr refresh
        text_54.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_54, 'tStartRefresh')  # time at next scr refresh
        text_54.setAutoDraw(True)
    
    # *text_56* updates
    if t >= 0.0 and text_56.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_56.tStart = t  # not accounting for scr refresh
        text_56.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_56, 'tStartRefresh')  # time at next scr refresh
        text_56.setAutoDraw(True)
    
    # *text_48* updates
    if t >= 0.0 and text_48.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_48.tStart = t  # not accounting for scr refresh
        text_48.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_48, 'tStartRefresh')  # time at next scr refresh
        text_48.setAutoDraw(True)
    
    # *text_49* updates
    if t >= 0.0 and text_49.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_49.tStart = t  # not accounting for scr refresh
        text_49.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_49, 'tStartRefresh')  # time at next scr refresh
        text_49.setAutoDraw(True)
    
    # *text_55* updates
    if t >= 0.0 and text_55.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_55.tStart = t  # not accounting for scr refresh
        text_55.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_55, 'tStartRefresh')  # time at next scr refresh
        text_55.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo10"-------
for thisComponent in demo10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
thisExp.addData('text_53.started', text_53.tStartRefresh)
thisExp.addData('text_53.stopped', text_53.tStopRefresh)
thisExp.addData('text_54.started', text_54.tStartRefresh)
thisExp.addData('text_54.stopped', text_54.tStopRefresh)
thisExp.addData('text_56.started', text_56.tStartRefresh)
thisExp.addData('text_56.stopped', text_56.tStopRefresh)
thisExp.addData('text_48.started', text_48.tStartRefresh)
thisExp.addData('text_48.stopped', text_48.tStopRefresh)
thisExp.addData('text_49.started', text_49.tStartRefresh)
thisExp.addData('text_49.stopped', text_49.tStopRefresh)
thisExp.addData('text_55.started', text_55.tStartRefresh)
thisExp.addData('text_55.stopped', text_55.tStopRefresh)
# the Routine "demo10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoanswer1"-------
t = 0
demoanswer1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_4.reset()
# keep track of which components have finished
demoanswer1Components = [text_15, text_16, rating_4, text_17, text_18]
for thisComponent in demoanswer1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demoanswer1"-------
while continueRoutine:
    # get current time
    t = demoanswer1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if t >= 0.0 and text_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_15.tStart = t  # not accounting for scr refresh
        text_15.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    
    # *text_16* updates
    if t >= 0.0 and text_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_16.tStart = t  # not accounting for scr refresh
        text_16.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
        text_16.setAutoDraw(True)
    # *rating_4* updates
    if t >= 0.0 and rating_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_4.tStart = t  # not accounting for scr refresh
        rating_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_4, 'tStartRefresh')  # time at next scr refresh
        rating_4.setAutoDraw(True)
    continueRoutine &= rating_4.noResponse  # a response ends the trial
    
    # *text_17* updates
    if t >= 0.0 and text_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_17.tStart = t  # not accounting for scr refresh
        text_17.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    
    # *text_18* updates
    if t >= 0.0 and text_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_18.tStart = t  # not accounting for scr refresh
        text_18.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
        text_18.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoanswer1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoanswer1"-------
for thisComponent in demoanswer1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
thisExp.addData('text_16.started', text_16.tStartRefresh)
thisExp.addData('text_16.stopped', text_16.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_4.response', rating_4.getRating())
thisExp.addData('rating_4.rt', rating_4.getRT())
thisExp.nextEntry()
thisExp.addData('rating_4.started', rating_4.tStart)
thisExp.addData('rating_4.stopped', rating_4.tStop)
marker_1 = rating_4.getRating()
markerposition1 = rating_4.getRating()

noresponse = rating_4.noResponse
if (rating_4 == noresponse):
    marker_1 = 0
thisExp.addData('text_17.started', text_17.tStartRefresh)
thisExp.addData('text_17.stopped', text_17.tStopRefresh)
thisExp.addData('text_18.started', text_18.tStartRefresh)
thisExp.addData('text_18.stopped', text_18.tStopRefresh)
# the Routine "demoanswer1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo11"-------
t = 0
demo11Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = keyboard.Keyboard()
if (marker_1 == 0):
    answer = 'incorrect'
if (marker_1 > 0):
    answer = 'correct'
if (marker_1 < 0): 
    answer = 'incorrect'

correct = visual.TextStim(win=win, name='correct',
    text='Your answer is ' '%s' %(answer),
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
score = visual.TextStim(win=win, name='score',
    text='Your score is ' '%3i' %(marker_1),
    font='Arial',
    pos=(0, -0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
# keep track of which components have finished
demo11Components = [key_resp_6, spacebar, score, correct]
for thisComponent in demo11Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo11"-------
while continueRoutine:
    # get current time
    t = demo11Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # not accounting for scr refresh
        key_resp_6.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        key_resp_6.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_6.keys = theseKeys.name  # just the last key pressed
            key_resp_6.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # *spacebar* updates
    if t >= 0.0 and spacebar.status == NOT_STARTED:
        # keep track of start time/frame for later
        spacebar.tStart = t  # not accounting for scr refresh
        spacebar.frameNStart = frameN  # exact frame index
        win.timeOnFlip(spacebar, 'tStartRefresh')  # time at next scr refresh
        spacebar.setAutoDraw(True)
    
    # *score* updates
    if t >= 0.0 and score.status == NOT_STARTED:
        # keep track of start time/frame for later
        score.tStart = t  # not accounting for scr refresh
        score.frameNStart = frameN  # exact frame index
        win.timeOnFlip(score, 'tStartRefresh')  # time at next scr refresh
        score.setAutoDraw(True)
    
    # *correct* updates
    if t >= 0.0 and correct.status == NOT_STARTED:
        # keep track of start time/frame for later
        correct.tStart = t  # not accounting for scr refresh
        correct.frameNStart = frameN  # exact frame index
        win.timeOnFlip(correct, 'tStartRefresh')  # time at next scr refresh
        correct.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo11Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo11"-------
for thisComponent in demo11Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('spacebar.started', spacebar.tStartRefresh)
thisExp.addData('spacebar.stopped', spacebar.tStopRefresh)
thisExp.addData('score.started', score.tStartRefresh)
thisExp.addData('score.stopped', score.tStopRefresh)
thisExp.addData('correct.started', correct.tStartRefresh)
thisExp.addData('correct.stopped', correct.tStopRefresh)
# the Routine "demo11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoanswer2"-------
t = 0
demoanswer2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_5.reset()
rating_5Clock = core.Clock()
rating_5 = visual.RatingScale(win=win, name='rating_5', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', ' 100'], scale='', markerStart = markerposition1)
# keep track of which components have finished
demoanswer2Components = [text_19, rating_5, line, text_20, verticalline, triangle, memberA, text_28, text_73, text_117]
for thisComponent in demoanswer2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demoanswer2"-------
while continueRoutine:
    # get current time
    t = demoanswer2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_19* updates
    if t >= 0.0 and text_19.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_19.tStart = t  # not accounting for scr refresh
        text_19.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
        text_19.setAutoDraw(True)
    # *rating_5* updates
    if t >= 0.0 and rating_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_5.tStart = t  # not accounting for scr refresh
        rating_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_5, 'tStartRefresh')  # time at next scr refresh
        rating_5.setAutoDraw(True)
    continueRoutine &= rating_5.noResponse  # a response ends the trial
    
    # *line* updates
    if t >= 0.0 and line.status == NOT_STARTED:
        # keep track of start time/frame for later
        line.tStart = t  # not accounting for scr refresh
        line.frameNStart = frameN  # exact frame index
        win.timeOnFlip(line, 'tStartRefresh')  # time at next scr refresh
        line.setAutoDraw(True)
    
    # *text_20* updates
    if t >= 0.0 and text_20.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_20.tStart = t  # not accounting for scr refresh
        text_20.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
        text_20.setAutoDraw(True)
    
    # *verticalline* updates
    if t >= 0.0 and verticalline.status == NOT_STARTED:
        # keep track of start time/frame for later
        verticalline.tStart = t  # not accounting for scr refresh
        verticalline.frameNStart = frameN  # exact frame index
        win.timeOnFlip(verticalline, 'tStartRefresh')  # time at next scr refresh
        verticalline.setAutoDraw(True)
    
    # *triangle* updates
    if t >= 0.0 and triangle.status == NOT_STARTED:
        # keep track of start time/frame for later
        triangle.tStart = t  # not accounting for scr refresh
        triangle.frameNStart = frameN  # exact frame index
        win.timeOnFlip(triangle, 'tStartRefresh')  # time at next scr refresh
        triangle.setAutoDraw(True)
    
    # *memberA* updates
    if t >= 0.0 and memberA.status == NOT_STARTED:
        # keep track of start time/frame for later
        memberA.tStart = t  # not accounting for scr refresh
        memberA.frameNStart = frameN  # exact frame index
        win.timeOnFlip(memberA, 'tStartRefresh')  # time at next scr refresh
        memberA.setAutoDraw(True)
    
    # *text_28* updates
    if t >= 0.0 and text_28.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_28.tStart = t  # not accounting for scr refresh
        text_28.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
        text_28.setAutoDraw(True)
    
    # *text_73* updates
    if t >= 0.0 and text_73.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_73.tStart = t  # not accounting for scr refresh
        text_73.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_73, 'tStartRefresh')  # time at next scr refresh
        text_73.setAutoDraw(True)
    
    # *text_117* updates
    if t >= 0.0 and text_117.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_117.tStart = t  # not accounting for scr refresh
        text_117.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_117, 'tStartRefresh')  # time at next scr refresh
        text_117.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoanswer2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoanswer2"-------
for thisComponent in demoanswer2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_19.started', text_19.tStartRefresh)
thisExp.addData('text_19.stopped', text_19.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_5.response', rating_5.getRating())
thisExp.addData('rating_5.rt', rating_5.getRT())
thisExp.nextEntry()
thisExp.addData('rating_5.started', rating_5.tStart)
thisExp.addData('rating_5.stopped', rating_5.tStop)
marker_2 = rating_5.getRating()
thisExp.addData('line.started', line.tStartRefresh)
thisExp.addData('line.stopped', line.tStopRefresh)
thisExp.addData('text_20.started', text_20.tStartRefresh)
thisExp.addData('text_20.stopped', text_20.tStopRefresh)
thisExp.addData('verticalline.started', verticalline.tStartRefresh)
thisExp.addData('verticalline.stopped', verticalline.tStopRefresh)
thisExp.addData('triangle.started', triangle.tStartRefresh)
thisExp.addData('triangle.stopped', triangle.tStopRefresh)
thisExp.addData('memberA.started', memberA.tStartRefresh)
thisExp.addData('memberA.stopped', memberA.tStopRefresh)
thisExp.addData('text_28.started', text_28.tStartRefresh)
thisExp.addData('text_28.stopped', text_28.tStopRefresh)
thisExp.addData('text_73.started', text_73.tStartRefresh)
thisExp.addData('text_73.stopped', text_73.tStopRefresh)
thisExp.addData('text_117.started', text_117.tStartRefresh)
thisExp.addData('text_117.stopped', text_117.tStopRefresh)
noresponse = rating_5.noResponse
if (rating_5 == noresponse):
    marker_2 = marker_1
# the Routine "demoanswer2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo12"-------
t = 0
demo12Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_7 = keyboard.Keyboard()
if(marker_2 == 0):
    answer2 = 'incorrect'
if (marker_2 > 0):
    answer2 = 'correct'
if (marker_2 < 0): 
    answer2 = 'incorrect'

correct2 = visual.TextStim(win=win, name='correct2',
    text='Your answer is ' '%s' %(answer2),
    font='Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
    
score2 = visual.TextStim(win=win, name='score2',
    text='Your score is ' '%3i' %(marker_2),
    font='Arial',
    pos=(0, 0.05), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

x = marker_1 + marker_2

totalscore = visual.TextStim(win=win, name='totalscore',
    text='Your total score is ' '%3i' %(x),
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
# keep track of which components have finished
demo12Components = [spacebar2, key_resp_7, instruction, score2, correct2, totalscore]
for thisComponent in demo12Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo12"-------
while continueRoutine:
    # get current time
    t = demo12Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *spacebar2* updates
    if t >= 0.0 and spacebar2.status == NOT_STARTED:
        # keep track of start time/frame for later
        spacebar2.tStart = t  # not accounting for scr refresh
        spacebar2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(spacebar2, 'tStartRefresh')  # time at next scr refresh
        spacebar2.setAutoDraw(True)
    
    # *key_resp_7* updates
    if t >= 0.0 and key_resp_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_7.tStart = t  # not accounting for scr refresh
        key_resp_7.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        key_resp_7.clearEvents(eventType='keyboard')
    if key_resp_7.status == STARTED:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *instruction* updates
    if t >= 0.0 and instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruction.tStart = t  # not accounting for scr refresh
        instruction.frameNStart = frameN  # exact frame index
        win.timeOnFlip(instruction, 'tStartRefresh')  # time at next scr refresh
        instruction.setAutoDraw(True)
    
    # *score2* updates
    if t >= 0.0 and score2.status == NOT_STARTED:
        # keep track of start time/frame for later
        score2.tStart = t  # not accounting for scr refresh
        score2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(score2, 'tStartRefresh')  # time at next scr refresh
        score2.setAutoDraw(True)
    
    # *correct2* updates
    if t >= 0.0 and correct2.status == NOT_STARTED:
        # keep track of start time/frame for later
        correct2.tStart = t  # not accounting for scr refresh
        correct2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(correct2, 'tStartRefresh')  # time at next scr refresh
        correct2.setAutoDraw(True)
    
    # *totalscore* updates
    if t >= 0.0 and totalscore.status == NOT_STARTED:
        # keep track of start time/frame for later
        totalscore.tStart = t  # not accounting for scr refresh
        totalscore.frameNStart = frameN  # exact frame index
        win.timeOnFlip(totalscore, 'tStartRefresh')  # time at next scr refresh
        totalscore.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo12Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo12"-------
for thisComponent in demo12Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('spacebar2.started', spacebar2.tStartRefresh)
thisExp.addData('spacebar2.stopped', spacebar2.tStopRefresh)
thisExp.addData('instruction.started', instruction.tStartRefresh)
thisExp.addData('instruction.stopped', instruction.tStopRefresh)
thisExp.addData('score2.started', score2.tStartRefresh)
thisExp.addData('score2.stopped', score2.tStopRefresh)
thisExp.addData('correct2.started', correct2.tStartRefresh)
thisExp.addData('correct2.stopped', correct2.tStopRefresh)
thisExp.addData('totalscore.started', totalscore.tStartRefresh)
thisExp.addData('totalscore.stopped', totalscore.tStopRefresh)
# the Routine "demo12" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo13"-------
t = 0
demo13Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
demo13Components = [text_21]
for thisComponent in demo13Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo13"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demo13Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_21* updates
    if t >= 0.0 and text_21.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_21.tStart = t  # not accounting for scr refresh
        text_21.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
        text_21.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_21.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_21.tStop = t  # not accounting for scr refresh
        text_21.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_21, 'tStopRefresh')  # time at next scr refresh
        text_21.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo13Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo13"-------
for thisComponent in demo13Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_21.started', text_21.tStartRefresh)
thisExp.addData('text_21.stopped', text_21.tStopRefresh)

# ------Prepare to start Routine "demotest2"-------
t = 0
demotest2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
demotest2Components = [movie_4]
for thisComponent in demotest2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demotest2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demotest2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie_4* updates
    if t >= 0.0 and movie_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        movie_4.tStart = t  # not accounting for scr refresh
        movie_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(movie_4, 'tStartRefresh')  # time at next scr refresh
        movie_4.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if movie_4.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        movie_4.tStop = t  # not accounting for scr refresh
        movie_4.frameNStop = frameN  # exact frame index
        win.timeOnFlip(movie_4, 'tStopRefresh')  # time at next scr refresh
        movie_4.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demotest2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demotest2"-------
for thisComponent in demotest2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('movie_4.started', movie_4.tStartRefresh)
thisExp.addData('movie_4.stopped', movie_4.tStopRefresh)

# ------Prepare to start Routine "demoanswer3"-------
t = 0
demoanswer3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_6.reset()
rating_6Clock = core.Clock()
rating_6 = visual.RatingScale(win=win, name='rating_5', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', ' 100'], scale='', markerStart = 0)

# keep track of which components have finished
demoanswer3Components = [text_22, rating_6, text_74]
for thisComponent in demoanswer3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demoanswer3"-------
while continueRoutine:
    # get current time
    t = demoanswer3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_22* updates
    if t >= 0.0 and text_22.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_22.tStart = t  # not accounting for scr refresh
        text_22.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
        text_22.setAutoDraw(True)
    # *rating_6* updates
    if t >= 0.0 and rating_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_6.tStart = t  # not accounting for scr refresh
        rating_6.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_6, 'tStartRefresh')  # time at next scr refresh
        rating_6.setAutoDraw(True)
    continueRoutine &= rating_6.noResponse  # a response ends the trial
    
    # *text_74* updates
    if t >= 0.0 and text_74.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_74.tStart = t  # not accounting for scr refresh
        text_74.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_74, 'tStartRefresh')  # time at next scr refresh
        text_74.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoanswer3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoanswer3"-------
for thisComponent in demoanswer3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_22.started', text_22.tStartRefresh)
thisExp.addData('text_22.stopped', text_22.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_6.response', rating_6.getRating())
thisExp.addData('rating_6.rt', rating_6.getRT())
thisExp.nextEntry()
thisExp.addData('rating_6.started', rating_6.tStart)
thisExp.addData('rating_6.stopped', rating_6.tStop)
marker_3 = rating_6.getRating()
markerposition2 = rating_6.getRating()
thisExp.addData('text_74.started', text_74.tStartRefresh)
thisExp.addData('text_74.stopped', text_74.tStopRefresh)
noresponse = rating_6.noResponse
if (rating_6 == noresponse):
    marker_3 = 0
# the Routine "demoanswer3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoanswer4"-------
t = 0
demoanswer4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_7.reset()
rating_7Clock = core.Clock()
rating_7 = visual.RatingScale(win=win, name='rating_5', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', ' 100'], scale='', markerStart = markerposition2)
# keep track of which components have finished
demoanswer4Components = [text_23, rating_7, polygon, polygon_2, triangle2, memberA2, text_70, text_75]
for thisComponent in demoanswer4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demoanswer4"-------
while continueRoutine:
    # get current time
    t = demoanswer4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_23* updates
    if t >= 0.0 and text_23.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_23.tStart = t  # not accounting for scr refresh
        text_23.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
        text_23.setAutoDraw(True)
    # *rating_7* updates
    if t >= 0.0 and rating_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_7.tStart = t  # not accounting for scr refresh
        rating_7.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_7, 'tStartRefresh')  # time at next scr refresh
        rating_7.setAutoDraw(True)
    continueRoutine &= rating_7.noResponse  # a response ends the trial
    
    # *polygon* updates
    if t >= 0.0 and polygon.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon.tStart = t  # not accounting for scr refresh
        polygon.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    
    # *polygon_2* updates
    if t >= 0.0 and polygon_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_2.tStart = t  # not accounting for scr refresh
        polygon_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    
    # *triangle2* updates
    if t >= 0.0 and triangle2.status == NOT_STARTED:
        # keep track of start time/frame for later
        triangle2.tStart = t  # not accounting for scr refresh
        triangle2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(triangle2, 'tStartRefresh')  # time at next scr refresh
        triangle2.setAutoDraw(True)
    
    # *memberA2* updates
    if t >= 0.0 and memberA2.status == NOT_STARTED:
        # keep track of start time/frame for later
        memberA2.tStart = t  # not accounting for scr refresh
        memberA2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(memberA2, 'tStartRefresh')  # time at next scr refresh
        memberA2.setAutoDraw(True)
    
    # *text_70* updates
    if t >= 0.0 and text_70.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_70.tStart = t  # not accounting for scr refresh
        text_70.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_70, 'tStartRefresh')  # time at next scr refresh
        text_70.setAutoDraw(True)
    
    # *text_75* updates
    if t >= 0.0 and text_75.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_75.tStart = t  # not accounting for scr refresh
        text_75.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_75, 'tStartRefresh')  # time at next scr refresh
        text_75.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoanswer4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoanswer4"-------
for thisComponent in demoanswer4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_23.started', text_23.tStartRefresh)
thisExp.addData('text_23.stopped', text_23.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_7.response', rating_7.getRating())
thisExp.addData('rating_7.rt', rating_7.getRT())
thisExp.nextEntry()
thisExp.addData('rating_7.started', rating_7.tStart)
thisExp.addData('rating_7.stopped', rating_7.tStop)
marker_4 = rating_7.getRating()

thisExp.addData('polygon.started', polygon.tStartRefresh)
thisExp.addData('polygon.stopped', polygon.tStopRefresh)
thisExp.addData('polygon_2.started', polygon_2.tStartRefresh)
thisExp.addData('polygon_2.stopped', polygon_2.tStopRefresh)
thisExp.addData('triangle2.started', triangle2.tStartRefresh)
thisExp.addData('triangle2.stopped', triangle2.tStopRefresh)
thisExp.addData('memberA2.started', memberA2.tStartRefresh)
thisExp.addData('memberA2.stopped', memberA2.tStopRefresh)
thisExp.addData('text_70.started', text_70.tStartRefresh)
thisExp.addData('text_70.stopped', text_70.tStopRefresh)
thisExp.addData('text_75.started', text_75.tStartRefresh)
thisExp.addData('text_75.stopped', text_75.tStopRefresh)
noresponse = rating_7.noResponse
if (rating_7 == noresponse):
    marker_4 = marker3
# the Routine "demoanswer4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo14"-------
t = 0
demo14Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = keyboard.Keyboard()
# keep track of which components have finished
demo14Components = [text_24, key_resp_8, text_57, text_58]
for thisComponent in demo14Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo14"-------
while continueRoutine:
    # get current time
    t = demo14Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_24* updates
    if t >= 0.0 and text_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_24.tStart = t  # not accounting for scr refresh
        text_24.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
        text_24.setAutoDraw(True)
    
    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t  # not accounting for scr refresh
        key_resp_8.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        key_resp_8.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_57* updates
    if t >= 0.0 and text_57.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_57.tStart = t  # not accounting for scr refresh
        text_57.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_57, 'tStartRefresh')  # time at next scr refresh
        text_57.setAutoDraw(True)
    
    # *text_58* updates
    if t >= 0.0 and text_58.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_58.tStart = t  # not accounting for scr refresh
        text_58.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_58, 'tStartRefresh')  # time at next scr refresh
        text_58.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo14Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo14"-------
for thisComponent in demo14Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_24.started', text_24.tStartRefresh)
thisExp.addData('text_24.stopped', text_24.tStopRefresh)
thisExp.addData('text_57.started', text_57.tStartRefresh)
thisExp.addData('text_57.stopped', text_57.tStopRefresh)
thisExp.addData('text_58.started', text_58.tStartRefresh)
thisExp.addData('text_58.stopped', text_58.tStopRefresh)
# the Routine "demo14" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo15"-------
t = 0
demo15Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
demo15Components = [text_25]
for thisComponent in demo15Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo15"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demo15Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_25* updates
    if t >= 0.0 and text_25.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_25.tStart = t  # not accounting for scr refresh
        text_25.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
        text_25.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_25.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_25.tStop = t  # not accounting for scr refresh
        text_25.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_25, 'tStopRefresh')  # time at next scr refresh
        text_25.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo15Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo15"-------
for thisComponent in demo15Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_25.started', text_25.tStartRefresh)
thisExp.addData('text_25.stopped', text_25.tStopRefresh)

# ------Prepare to start Routine "demotest3"-------
t = 0
demotest3Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
demotest3Components = [movie_5]
for thisComponent in demotest3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demotest3"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demotest3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *movie_5* updates
    if t >= 0.0 and movie_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        movie_5.tStart = t  # not accounting for scr refresh
        movie_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(movie_5, 'tStartRefresh')  # time at next scr refresh
        movie_5.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if movie_5.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        movie_5.tStop = t  # not accounting for scr refresh
        movie_5.frameNStop = frameN  # exact frame index
        win.timeOnFlip(movie_5, 'tStopRefresh')  # time at next scr refresh
        movie_5.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demotest3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demotest3"-------
for thisComponent in demotest3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('movie_5.started', movie_5.tStartRefresh)
thisExp.addData('movie_5.stopped', movie_5.tStopRefresh)

# ------Prepare to start Routine "demoanswer5"-------
t = 0
demoanswer5Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_8.reset()
rating_8Clock = core.Clock()
rating_8 = visual.RatingScale(win=win, name='rating_8', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', ' 100'], scale='', markerStart = 0)

# keep track of which components have finished
demoanswer5Components = [text_26, rating_8, text_76]
for thisComponent in demoanswer5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demoanswer5"-------
while continueRoutine:
    # get current time
    t = demoanswer5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_26* updates
    if t >= 0.0 and text_26.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_26.tStart = t  # not accounting for scr refresh
        text_26.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
        text_26.setAutoDraw(True)
    # *rating_8* updates
    if t >= 0.0 and rating_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_8.tStart = t  # not accounting for scr refresh
        rating_8.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_8, 'tStartRefresh')  # time at next scr refresh
        rating_8.setAutoDraw(True)
    continueRoutine &= rating_8.noResponse  # a response ends the trial
    
    # *text_76* updates
    if t >= 0.0 and text_76.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_76.tStart = t  # not accounting for scr refresh
        text_76.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_76, 'tStartRefresh')  # time at next scr refresh
        text_76.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoanswer5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoanswer5"-------
for thisComponent in demoanswer5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_26.started', text_26.tStartRefresh)
thisExp.addData('text_26.stopped', text_26.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_8.response', rating_8.getRating())
thisExp.addData('rating_8.rt', rating_8.getRT())
thisExp.nextEntry()
thisExp.addData('rating_8.started', rating_8.tStart)
thisExp.addData('rating_8.stopped', rating_8.tStop)
marker_5 = rating_8.getRating()
markerposition2 = rating_8.getRating()
thisExp.addData('text_76.started', text_76.tStartRefresh)
thisExp.addData('text_76.stopped', text_76.tStopRefresh)
noresponse = rating_8.noResponse
if (rating_8 == noresponse):
    marker_5 = 0
# the Routine "demoanswer5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demoanswer6"-------
t = 0
demoanswer6Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_9.reset()
rating_9Clock = core.Clock()
rating_9 = visual.RatingScale(win=win, name='rating_9', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', ' 100'], scale='', markerStart = markerposition2)
# keep track of which components have finished
demoanswer6Components = [text_27, rating_9, polygon_3, polygon_4, triangle3, text_71, text_72, text_77]
for thisComponent in demoanswer6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demoanswer6"-------
while continueRoutine:
    # get current time
    t = demoanswer6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_27* updates
    if t >= 0.0 and text_27.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_27.tStart = t  # not accounting for scr refresh
        text_27.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
        text_27.setAutoDraw(True)
    # *rating_9* updates
    if t >= 0.0 and rating_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_9.tStart = t  # not accounting for scr refresh
        rating_9.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_9, 'tStartRefresh')  # time at next scr refresh
        rating_9.setAutoDraw(True)
    continueRoutine &= rating_9.noResponse  # a response ends the trial
    
    # *polygon_3* updates
    if t >= 0.0 and polygon_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_3.tStart = t  # not accounting for scr refresh
        polygon_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
        polygon_3.setAutoDraw(True)
    
    # *polygon_4* updates
    if t >= 0.0 and polygon_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon_4.tStart = t  # not accounting for scr refresh
        polygon_4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
        polygon_4.setAutoDraw(True)
    
    # *triangle3* updates
    if t >= 0.0 and triangle3.status == NOT_STARTED:
        # keep track of start time/frame for later
        triangle3.tStart = t  # not accounting for scr refresh
        triangle3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(triangle3, 'tStartRefresh')  # time at next scr refresh
        triangle3.setAutoDraw(True)
    
    # *text_71* updates
    if t >= 0.0 and text_71.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_71.tStart = t  # not accounting for scr refresh
        text_71.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_71, 'tStartRefresh')  # time at next scr refresh
        text_71.setAutoDraw(True)
    
    # *text_72* updates
    if t >= 0.0 and text_72.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_72.tStart = t  # not accounting for scr refresh
        text_72.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_72, 'tStartRefresh')  # time at next scr refresh
        text_72.setAutoDraw(True)
    
    # *text_77* updates
    if t >= 0.0 and text_77.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_77.tStart = t  # not accounting for scr refresh
        text_77.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_77, 'tStartRefresh')  # time at next scr refresh
        text_77.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demoanswer6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demoanswer6"-------
for thisComponent in demoanswer6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_27.started', text_27.tStartRefresh)
thisExp.addData('text_27.stopped', text_27.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_9.response', rating_9.getRating())
thisExp.addData('rating_9.rt', rating_9.getRT())
thisExp.nextEntry()
thisExp.addData('rating_9.started', rating_9.tStart)
thisExp.addData('rating_9.stopped', rating_9.tStop)
marker_6 = rating_9.getRating()
thisExp.addData('polygon_3.started', polygon_3.tStartRefresh)
thisExp.addData('polygon_3.stopped', polygon_3.tStopRefresh)
thisExp.addData('polygon_4.started', polygon_4.tStartRefresh)
thisExp.addData('polygon_4.stopped', polygon_4.tStopRefresh)
thisExp.addData('triangle3.started', triangle3.tStartRefresh)
thisExp.addData('triangle3.stopped', triangle3.tStopRefresh)
thisExp.addData('text_71.started', text_71.tStartRefresh)
thisExp.addData('text_71.stopped', text_71.tStopRefresh)
thisExp.addData('text_72.started', text_72.tStartRefresh)
thisExp.addData('text_72.stopped', text_72.tStopRefresh)
thisExp.addData('text_77.started', text_77.tStartRefresh)
thisExp.addData('text_77.stopped', text_77.tStopRefresh)
noresponse = rating_9.noResponse
if (rating_9 == noresponse):
    marker_6 = marker_5
# the Routine "demoanswer6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo16"-------
t = 0
demo16Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = keyboard.Keyboard()
y = int(marker_1) + int(marker_2) + int(marker_3) + int(marker_4) - int(marker_5) - int(marker_6)

totalscore2 = visual.TextStim(win=win, name='totalscore2',
    text='Your total score is ' '%3i' %(y),
    font='Arial',
    pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
# keep track of which components have finished
demo16Components = [nicejob, key_resp_9, spacebar3, intruction2, totalscore2]
for thisComponent in demo16Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo16"-------
while continueRoutine:
    # get current time
    t = demo16Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *nicejob* updates
    if t >= 0.0 and nicejob.status == NOT_STARTED:
        # keep track of start time/frame for later
        nicejob.tStart = t  # not accounting for scr refresh
        nicejob.frameNStart = frameN  # exact frame index
        win.timeOnFlip(nicejob, 'tStartRefresh')  # time at next scr refresh
        nicejob.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t  # not accounting for scr refresh
        key_resp_9.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        key_resp_9.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *spacebar3* updates
    if t >= 0.0 and spacebar3.status == NOT_STARTED:
        # keep track of start time/frame for later
        spacebar3.tStart = t  # not accounting for scr refresh
        spacebar3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(spacebar3, 'tStartRefresh')  # time at next scr refresh
        spacebar3.setAutoDraw(True)
    
    # *intruction2* updates
    if t >= 0.0 and intruction2.status == NOT_STARTED:
        # keep track of start time/frame for later
        intruction2.tStart = t  # not accounting for scr refresh
        intruction2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(intruction2, 'tStartRefresh')  # time at next scr refresh
        intruction2.setAutoDraw(True)
    
    # *totalscore2* updates
    if t >= 0.0 and totalscore2.status == NOT_STARTED:
        # keep track of start time/frame for later
        totalscore2.tStart = t  # not accounting for scr refresh
        totalscore2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(totalscore2, 'tStartRefresh')  # time at next scr refresh
        totalscore2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo16Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo16"-------
for thisComponent in demo16Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('nicejob.started', nicejob.tStartRefresh)
thisExp.addData('nicejob.stopped', nicejob.tStopRefresh)
thisExp.addData('spacebar3.started', spacebar3.tStartRefresh)
thisExp.addData('spacebar3.stopped', spacebar3.tStopRefresh)
thisExp.addData('intruction2.started', intruction2.tStartRefresh)
thisExp.addData('intruction2.stopped', intruction2.tStopRefresh)
thisExp.addData('totalscore2.started', totalscore2.tStartRefresh)
thisExp.addData('totalscore2.stopped', totalscore2.tStopRefresh)
# the Routine "demo16" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test1"-------
t = 0
test1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_10 = keyboard.Keyboard()
# keep track of which components have finished
test1Components = [text_29, key_resp_10, text_59, text_60]
for thisComponent in test1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "test1"-------
while continueRoutine:
    # get current time
    t = test1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_29* updates
    if t >= 0.0 and text_29.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_29.tStart = t  # not accounting for scr refresh
        text_29.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
        text_29.setAutoDraw(True)
    
    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t  # not accounting for scr refresh
        key_resp_10.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        key_resp_10.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_59* updates
    if t >= 0.0 and text_59.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_59.tStart = t  # not accounting for scr refresh
        text_59.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_59, 'tStartRefresh')  # time at next scr refresh
        text_59.setAutoDraw(True)
    
    # *text_60* updates
    if t >= 0.0 and text_60.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_60.tStart = t  # not accounting for scr refresh
        text_60.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_60, 'tStartRefresh')  # time at next scr refresh
        text_60.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test1"-------
for thisComponent in test1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_29.started', text_29.tStartRefresh)
thisExp.addData('text_29.stopped', text_29.tStopRefresh)
thisExp.addData('text_59.started', text_59.tStartRefresh)
thisExp.addData('text_59.stopped', text_59.tStopRefresh)
thisExp.addData('text_60.started', text_60.tStartRefresh)
thisExp.addData('text_60.stopped', text_60.tStopRefresh)
# the Routine "test1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test2"-------
t = 0
test2Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(4.000000)
# update component parameters for each repeat
# keep track of which components have finished
test2Components = [text_61, text_30, text_32]
for thisComponent in test2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "test2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = test2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_61* updates
    if t >= 0.0 and text_61.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_61.tStart = t  # not accounting for scr refresh
        text_61.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_61, 'tStartRefresh')  # time at next scr refresh
        text_61.setAutoDraw(True)
    frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_61.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_61.tStop = t  # not accounting for scr refresh
        text_61.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_61, 'tStopRefresh')  # time at next scr refresh
        text_61.setAutoDraw(False)
    
    # *text_30* updates
    if t >= 3 and text_30.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_30.tStart = t  # not accounting for scr refresh
        text_30.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    frameRemains = 3 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_30.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_30.tStop = t  # not accounting for scr refresh
        text_30.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
        text_30.setAutoDraw(False)
    
    # *text_32* updates
    if t >= 1 and text_32.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_32.tStart = t  # not accounting for scr refresh
        text_32.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_32, 'tStartRefresh')  # time at next scr refresh
        text_32.setAutoDraw(True)
    frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_32.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_32.tStop = t  # not accounting for scr refresh
        text_32.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_32, 'tStopRefresh')  # time at next scr refresh
        text_32.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test2"-------
for thisComponent in test2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_61.started', text_61.tStartRefresh)
thisExp.addData('text_61.stopped', text_61.tStopRefresh)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
thisExp.addData('text_32.started', text_32.tStartRefresh)
thisExp.addData('text_32.stopped', text_32.tStopRefresh)

# ------Prepare to start Routine "test3"-------
t = 0
test3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_11 = keyboard.Keyboard()
# keep track of which components have finished
test3Components = [text_34, key_resp_11, text_31, text_33, group13, no4]
for thisComponent in test3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "test3"-------
while continueRoutine:
    # get current time
    t = test3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_34* updates
    if t >= 0.0 and text_34.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_34.tStart = t  # not accounting for scr refresh
        text_34.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_34, 'tStartRefresh')  # time at next scr refresh
        text_34.setAutoDraw(True)
    
    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t  # not accounting for scr refresh
        key_resp_11.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        key_resp_11.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_31* updates
    if t >= 0.0 and text_31.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_31.tStart = t  # not accounting for scr refresh
        text_31.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_31, 'tStartRefresh')  # time at next scr refresh
        text_31.setAutoDraw(True)
    
    # *text_33* updates
    if t >= 0.0 and text_33.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_33.tStart = t  # not accounting for scr refresh
        text_33.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_33, 'tStartRefresh')  # time at next scr refresh
        text_33.setAutoDraw(True)
    
    # *group13* updates
    if t >= 0.0 and group13.status == NOT_STARTED:
        # keep track of start time/frame for later
        group13.tStart = t  # not accounting for scr refresh
        group13.frameNStart = frameN  # exact frame index
        win.timeOnFlip(group13, 'tStartRefresh')  # time at next scr refresh
        group13.setAutoDraw(True)
    
    # *no4* updates
    if t >= 0.0 and no4.status == NOT_STARTED:
        # keep track of start time/frame for later
        no4.tStart = t  # not accounting for scr refresh
        no4.frameNStart = frameN  # exact frame index
        win.timeOnFlip(no4, 'tStartRefresh')  # time at next scr refresh
        no4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test3"-------
for thisComponent in test3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_34.started', text_34.tStartRefresh)
thisExp.addData('text_34.stopped', text_34.tStopRefresh)
thisExp.addData('text_31.started', text_31.tStartRefresh)
thisExp.addData('text_31.stopped', text_31.tStopRefresh)
thisExp.addData('text_33.started', text_33.tStartRefresh)
thisExp.addData('text_33.stopped', text_33.tStopRefresh)
thisExp.addData('group13.started', group13.tStartRefresh)
thisExp.addData('group13.stopped', group13.tStopRefresh)
thisExp.addData('no4.started', no4.tStartRefresh)
thisExp.addData('no4.stopped', no4.tStopRefresh)
# the Routine "test3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test4"-------
t = 0
test4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_12 = keyboard.Keyboard()
# keep track of which components have finished
test4Components = [text_35, key_resp_12, text_62, text_63]
for thisComponent in test4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "test4"-------
while continueRoutine:
    # get current time
    t = test4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_35* updates
    if t >= 0.0 and text_35.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_35.tStart = t  # not accounting for scr refresh
        text_35.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_35, 'tStartRefresh')  # time at next scr refresh
        text_35.setAutoDraw(True)
    
    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t  # not accounting for scr refresh
        key_resp_12.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        key_resp_12.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_62* updates
    if t >= 0.0 and text_62.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_62.tStart = t  # not accounting for scr refresh
        text_62.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_62, 'tStartRefresh')  # time at next scr refresh
        text_62.setAutoDraw(True)
    
    # *text_63* updates
    if t >= 0.0 and text_63.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_63.tStart = t  # not accounting for scr refresh
        text_63.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_63, 'tStartRefresh')  # time at next scr refresh
        text_63.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test4"-------
for thisComponent in test4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_35.started', text_35.tStartRefresh)
thisExp.addData('text_35.stopped', text_35.tStopRefresh)
thisExp.addData('text_62.started', text_62.tStartRefresh)
thisExp.addData('text_62.stopped', text_62.tStopRefresh)
thisExp.addData('text_63.started', text_63.tStartRefresh)
thisExp.addData('text_63.stopped', text_63.tStopRefresh)
# the Routine "test4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "test5"-------
t = 0
test5Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
test5Components = [text_36, text_37, text_38, text_64]
for thisComponent in test5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "test5"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = test5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_36* updates
    if t >= 0.0 and text_36.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_36.tStart = t  # not accounting for scr refresh
        text_36.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_36, 'tStartRefresh')  # time at next scr refresh
        text_36.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_36.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_36.tStop = t  # not accounting for scr refresh
        text_36.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_36, 'tStopRefresh')  # time at next scr refresh
        text_36.setAutoDraw(False)
    
    # *text_37* updates
    if t >= 1 and text_37.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_37.tStart = t  # not accounting for scr refresh
        text_37.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_37, 'tStartRefresh')  # time at next scr refresh
        text_37.setAutoDraw(True)
    frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_37.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_37.tStop = t  # not accounting for scr refresh
        text_37.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_37, 'tStopRefresh')  # time at next scr refresh
        text_37.setAutoDraw(False)
    
    # *text_38* updates
    if t >= 2 and text_38.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_38.tStart = t  # not accounting for scr refresh
        text_38.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_38, 'tStartRefresh')  # time at next scr refresh
        text_38.setAutoDraw(True)
    frameRemains = 2 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_38.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_38.tStop = t  # not accounting for scr refresh
        text_38.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_38, 'tStopRefresh')  # time at next scr refresh
        text_38.setAutoDraw(False)
    
    # *text_64* updates
    if t >= 0.0 and text_64.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_64.tStart = t  # not accounting for scr refresh
        text_64.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_64, 'tStartRefresh')  # time at next scr refresh
        text_64.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_64.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_64.tStop = t  # not accounting for scr refresh
        text_64.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_64, 'tStopRefresh')  # time at next scr refresh
        text_64.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in test5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "test5"-------
for thisComponent in test5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_36.started', text_36.tStartRefresh)
thisExp.addData('text_36.stopped', text_36.tStopRefresh)
thisExp.addData('text_37.started', text_37.tStartRefresh)
thisExp.addData('text_37.stopped', text_37.tStopRefresh)
thisExp.addData('text_38.started', text_38.tStartRefresh)
thisExp.addData('text_38.stopped', text_38.tStopRefresh)
thisExp.addData('text_64.started', text_64.tStartRefresh)
thisExp.addData('text_64.stopped', text_64.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('vid.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testfixation"-------
    t = 0
    testfixationClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    testfixationComponents = [text_39]
    for thisComponent in testfixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "testfixation"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testfixationClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_39* updates
        if t >= 0.0 and text_39.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_39.tStart = t  # not accounting for scr refresh
            text_39.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_39, 'tStartRefresh')  # time at next scr refresh
            text_39.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_39.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_39.tStop = t  # not accounting for scr refresh
            text_39.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_39, 'tStopRefresh')  # time at next scr refresh
            text_39.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testfixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testfixation"-------
    for thisComponent in testfixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_39.started', text_39.tStartRefresh)
    trials.addData('text_39.stopped', text_39.tStopRefresh)
    
    # ------Prepare to start Routine "testvideo"-------
    t = 0
    testvideoClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    movie_6 = visual.MovieStim3(
        win=win, name='movie_6',
        noAudio = False,
        filename=vid,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        size=(1280,780),
        depth=0.0,
        )
    # keep track of which components have finished
    testvideoComponents = [movie_6]
    for thisComponent in testvideoComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "testvideo"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testvideoClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movie_6* updates
        if t >= 0.0 and movie_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            movie_6.tStart = t  # not accounting for scr refresh
            movie_6.frameNStart = frameN  # exact frame index
            win.timeOnFlip(movie_6, 'tStartRefresh')  # time at next scr refresh
            movie_6.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if movie_6.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            movie_6.tStop = t  # not accounting for scr refresh
            movie_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(movie_6, 'tStopRefresh')  # time at next scr refresh
            movie_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testvideoComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testvideo"-------
    for thisComponent in testvideoComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('movie_6.started', movie_6.tStartRefresh)
    trials.addData('movie_6.stopped', movie_6.tStopRefresh)
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "mathtest"-------
t = 0
mathtestClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_13 = keyboard.Keyboard()
# keep track of which components have finished
mathtestComponents = [text_40, key_resp_13, text_118, text_119, text_123]
for thisComponent in mathtestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mathtest"-------
while continueRoutine:
    # get current time
    t = mathtestClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_40* updates
    if t >= 0.0 and text_40.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_40.tStart = t  # not accounting for scr refresh
        text_40.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_40, 'tStartRefresh')  # time at next scr refresh
        text_40.setAutoDraw(True)
    
    # *key_resp_13* updates
    if t >= 0.0 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t  # not accounting for scr refresh
        key_resp_13.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        key_resp_13.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = key_resp_13.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_118* updates
    if t >= 0.0 and text_118.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_118.tStart = t  # not accounting for scr refresh
        text_118.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_118, 'tStartRefresh')  # time at next scr refresh
        text_118.setAutoDraw(True)
    
    # *text_119* updates
    if t >= 0.0 and text_119.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_119.tStart = t  # not accounting for scr refresh
        text_119.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_119, 'tStartRefresh')  # time at next scr refresh
        text_119.setAutoDraw(True)
    
    # *text_123* updates
    if t >= 0.0 and text_123.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_123.tStart = t  # not accounting for scr refresh
        text_123.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_123, 'tStartRefresh')  # time at next scr refresh
        text_123.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mathtestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mathtest"-------
for thisComponent in mathtestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_40.started', text_40.tStartRefresh)
thisExp.addData('text_40.stopped', text_40.tStopRefresh)
thisExp.addData('text_118.started', text_118.tStartRefresh)
thisExp.addData('text_118.stopped', text_118.tStopRefresh)
thisExp.addData('text_119.started', text_119.tStartRefresh)
thisExp.addData('text_119.stopped', text_119.tStopRefresh)
thisExp.addData('text_123.started', text_123.tStartRefresh)
thisExp.addData('text_123.stopped', text_123.tStopRefresh)
# the Routine "mathtest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mathquestion1"-------
t = 0
mathquestion1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating.reset()
# keep track of which components have finished
mathquestion1Components = [text_41, rating, text_65]
for thisComponent in mathquestion1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mathquestion1"-------
while continueRoutine:
    # get current time
    t = mathquestion1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_41* updates
    if t >= 0.0 and text_41.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_41.tStart = t  # not accounting for scr refresh
        text_41.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_41, 'tStartRefresh')  # time at next scr refresh
        text_41.setAutoDraw(True)
    # *rating* updates
    if t >= 0.0 and rating.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating.tStart = t  # not accounting for scr refresh
        rating.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating, 'tStartRefresh')  # time at next scr refresh
        rating.setAutoDraw(True)
    continueRoutine &= rating.noResponse  # a response ends the trial
    
    # *text_65* updates
    if t >= 0.0 and text_65.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_65.tStart = t  # not accounting for scr refresh
        text_65.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_65, 'tStartRefresh')  # time at next scr refresh
        text_65.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mathquestion1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mathquestion1"-------
for thisComponent in mathquestion1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_41.started', text_41.tStartRefresh)
thisExp.addData('text_41.stopped', text_41.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating.response', rating.getRating())
thisExp.addData('rating.rt', rating.getRT())
thisExp.nextEntry()
thisExp.addData('rating.started', rating.tStart)
thisExp.addData('rating.stopped', rating.tStop)
thisExp.addData('text_65.started', text_65.tStartRefresh)
thisExp.addData('text_65.stopped', text_65.tStopRefresh)
# the Routine "mathquestion1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mathquestion2"-------
t = 0
mathquestion2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_2.reset()
# keep track of which components have finished
mathquestion2Components = [text_66, text_67, rating_2]
for thisComponent in mathquestion2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mathquestion2"-------
while continueRoutine:
    # get current time
    t = mathquestion2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_66* updates
    if t >= 0.0 and text_66.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_66.tStart = t  # not accounting for scr refresh
        text_66.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_66, 'tStartRefresh')  # time at next scr refresh
        text_66.setAutoDraw(True)
    
    # *text_67* updates
    if t >= 0.0 and text_67.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_67.tStart = t  # not accounting for scr refresh
        text_67.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_67, 'tStartRefresh')  # time at next scr refresh
        text_67.setAutoDraw(True)
    # *rating_2* updates
    if t >= 0.0 and rating_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_2.tStart = t  # not accounting for scr refresh
        rating_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_2, 'tStartRefresh')  # time at next scr refresh
        rating_2.setAutoDraw(True)
    continueRoutine &= rating_2.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mathquestion2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mathquestion2"-------
for thisComponent in mathquestion2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_66.started', text_66.tStartRefresh)
thisExp.addData('text_66.stopped', text_66.tStopRefresh)
thisExp.addData('text_67.started', text_67.tStartRefresh)
thisExp.addData('text_67.stopped', text_67.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_2.response', rating_2.getRating())
thisExp.addData('rating_2.rt', rating_2.getRT())
thisExp.nextEntry()
thisExp.addData('rating_2.started', rating_2.tStart)
thisExp.addData('rating_2.stopped', rating_2.tStop)
# the Routine "mathquestion2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mathquestion3"-------
t = 0
mathquestion3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_3.reset()
# keep track of which components have finished
mathquestion3Components = [text_68, text_69, rating_3]
for thisComponent in mathquestion3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mathquestion3"-------
while continueRoutine:
    # get current time
    t = mathquestion3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_68* updates
    if t >= 0.0 and text_68.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_68.tStart = t  # not accounting for scr refresh
        text_68.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_68, 'tStartRefresh')  # time at next scr refresh
        text_68.setAutoDraw(True)
    
    # *text_69* updates
    if t >= 0.0 and text_69.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_69.tStart = t  # not accounting for scr refresh
        text_69.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_69, 'tStartRefresh')  # time at next scr refresh
        text_69.setAutoDraw(True)
    # *rating_3* updates
    if t >= 0.0 and rating_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_3.tStart = t  # not accounting for scr refresh
        rating_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_3, 'tStartRefresh')  # time at next scr refresh
        rating_3.setAutoDraw(True)
    continueRoutine &= rating_3.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mathquestion3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mathquestion3"-------
for thisComponent in mathquestion3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_68.started', text_68.tStartRefresh)
thisExp.addData('text_68.stopped', text_68.tStopRefresh)
thisExp.addData('text_69.started', text_69.tStartRefresh)
thisExp.addData('text_69.stopped', text_69.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_3.response', rating_3.getRating())
thisExp.addData('rating_3.rt', rating_3.getRT())
thisExp.nextEntry()
thisExp.addData('rating_3.started', rating_3.tStart)
thisExp.addData('rating_3.stopped', rating_3.tStop)
# the Routine "mathquestion3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mathquestion4"-------
t = 0
mathquestion4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_14.reset()
# keep track of which components have finished
mathquestion4Components = [text_131, text_132, rating_14]
for thisComponent in mathquestion4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mathquestion4"-------
while continueRoutine:
    # get current time
    t = mathquestion4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_131* updates
    if t >= 0.0 and text_131.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_131.tStart = t  # not accounting for scr refresh
        text_131.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_131, 'tStartRefresh')  # time at next scr refresh
        text_131.setAutoDraw(True)
    
    # *text_132* updates
    if t >= 0.0 and text_132.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_132.tStart = t  # not accounting for scr refresh
        text_132.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_132, 'tStartRefresh')  # time at next scr refresh
        text_132.setAutoDraw(True)
    # *rating_14* updates
    if t >= 0.0 and rating_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_14.tStart = t  # not accounting for scr refresh
        rating_14.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_14, 'tStartRefresh')  # time at next scr refresh
        rating_14.setAutoDraw(True)
    continueRoutine &= rating_14.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mathquestion4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mathquestion4"-------
for thisComponent in mathquestion4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_131.started', text_131.tStartRefresh)
thisExp.addData('text_131.stopped', text_131.tStopRefresh)
thisExp.addData('text_132.started', text_132.tStartRefresh)
thisExp.addData('text_132.stopped', text_132.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_14.response', rating_14.getRating())
thisExp.addData('rating_14.rt', rating_14.getRT())
thisExp.nextEntry()
thisExp.addData('rating_14.started', rating_14.tStart)
thisExp.addData('rating_14.stopped', rating_14.tStop)
# the Routine "mathquestion4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mathquestion5"-------
t = 0
mathquestion5Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_15.reset()
# keep track of which components have finished
mathquestion5Components = [text_133, text_134, rating_15]
for thisComponent in mathquestion5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mathquestion5"-------
while continueRoutine:
    # get current time
    t = mathquestion5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_133* updates
    if t >= 0.0 and text_133.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_133.tStart = t  # not accounting for scr refresh
        text_133.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_133, 'tStartRefresh')  # time at next scr refresh
        text_133.setAutoDraw(True)
    
    # *text_134* updates
    if t >= 0.0 and text_134.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_134.tStart = t  # not accounting for scr refresh
        text_134.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_134, 'tStartRefresh')  # time at next scr refresh
        text_134.setAutoDraw(True)
    # *rating_15* updates
    if t >= 0.0 and rating_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_15.tStart = t  # not accounting for scr refresh
        rating_15.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_15, 'tStartRefresh')  # time at next scr refresh
        rating_15.setAutoDraw(True)
    continueRoutine &= rating_15.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mathquestion5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mathquestion5"-------
for thisComponent in mathquestion5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_133.started', text_133.tStartRefresh)
thisExp.addData('text_133.stopped', text_133.tStopRefresh)
thisExp.addData('text_134.started', text_134.tStartRefresh)
thisExp.addData('text_134.stopped', text_134.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_15.response', rating_15.getRating())
thisExp.addData('rating_15.rt', rating_15.getRT())
thisExp.nextEntry()
thisExp.addData('rating_15.started', rating_15.tStart)
thisExp.addData('rating_15.stopped', rating_15.tStop)
# the Routine "mathquestion5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mathquestion6"-------
t = 0
mathquestion6Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_16.reset()
# keep track of which components have finished
mathquestion6Components = [text_135, text_136, rating_16]
for thisComponent in mathquestion6Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mathquestion6"-------
while continueRoutine:
    # get current time
    t = mathquestion6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_135* updates
    if t >= 0.0 and text_135.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_135.tStart = t  # not accounting for scr refresh
        text_135.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_135, 'tStartRefresh')  # time at next scr refresh
        text_135.setAutoDraw(True)
    
    # *text_136* updates
    if t >= 0.0 and text_136.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_136.tStart = t  # not accounting for scr refresh
        text_136.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_136, 'tStartRefresh')  # time at next scr refresh
        text_136.setAutoDraw(True)
    # *rating_16* updates
    if t >= 0.0 and rating_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_16.tStart = t  # not accounting for scr refresh
        rating_16.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_16, 'tStartRefresh')  # time at next scr refresh
        rating_16.setAutoDraw(True)
    continueRoutine &= rating_16.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mathquestion6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mathquestion6"-------
for thisComponent in mathquestion6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_135.started', text_135.tStartRefresh)
thisExp.addData('text_135.stopped', text_135.tStopRefresh)
thisExp.addData('text_136.started', text_136.tStartRefresh)
thisExp.addData('text_136.stopped', text_136.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_16.response', rating_16.getRating())
thisExp.addData('rating_16.rt', rating_16.getRT())
thisExp.nextEntry()
thisExp.addData('rating_16.started', rating_16.tStart)
thisExp.addData('rating_16.stopped', rating_16.tStop)
# the Routine "mathquestion6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mathquestion7"-------
t = 0
mathquestion7Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_17.reset()
# keep track of which components have finished
mathquestion7Components = [text_137, text_138, rating_17]
for thisComponent in mathquestion7Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mathquestion7"-------
while continueRoutine:
    # get current time
    t = mathquestion7Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_137* updates
    if t >= 0.0 and text_137.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_137.tStart = t  # not accounting for scr refresh
        text_137.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_137, 'tStartRefresh')  # time at next scr refresh
        text_137.setAutoDraw(True)
    
    # *text_138* updates
    if t >= 0.0 and text_138.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_138.tStart = t  # not accounting for scr refresh
        text_138.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_138, 'tStartRefresh')  # time at next scr refresh
        text_138.setAutoDraw(True)
    # *rating_17* updates
    if t >= 0.0 and rating_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_17.tStart = t  # not accounting for scr refresh
        rating_17.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_17, 'tStartRefresh')  # time at next scr refresh
        rating_17.setAutoDraw(True)
    continueRoutine &= rating_17.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mathquestion7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mathquestion7"-------
for thisComponent in mathquestion7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_137.started', text_137.tStartRefresh)
thisExp.addData('text_137.stopped', text_137.tStopRefresh)
thisExp.addData('text_138.started', text_138.tStartRefresh)
thisExp.addData('text_138.stopped', text_138.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_17.response', rating_17.getRating())
thisExp.addData('rating_17.rt', rating_17.getRT())
thisExp.nextEntry()
thisExp.addData('rating_17.started', rating_17.tStart)
thisExp.addData('rating_17.stopped', rating_17.tStop)
# the Routine "mathquestion7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mathquestion8"-------
t = 0
mathquestion8Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_18.reset()
# keep track of which components have finished
mathquestion8Components = [text_139, text_140, rating_18]
for thisComponent in mathquestion8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mathquestion8"-------
while continueRoutine:
    # get current time
    t = mathquestion8Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_139* updates
    if t >= 0.0 and text_139.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_139.tStart = t  # not accounting for scr refresh
        text_139.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_139, 'tStartRefresh')  # time at next scr refresh
        text_139.setAutoDraw(True)
    
    # *text_140* updates
    if t >= 0.0 and text_140.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_140.tStart = t  # not accounting for scr refresh
        text_140.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_140, 'tStartRefresh')  # time at next scr refresh
        text_140.setAutoDraw(True)
    # *rating_18* updates
    if t >= 0.0 and rating_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_18.tStart = t  # not accounting for scr refresh
        rating_18.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_18, 'tStartRefresh')  # time at next scr refresh
        rating_18.setAutoDraw(True)
    continueRoutine &= rating_18.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mathquestion8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mathquestion8"-------
for thisComponent in mathquestion8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_139.started', text_139.tStartRefresh)
thisExp.addData('text_139.stopped', text_139.tStopRefresh)
thisExp.addData('text_140.started', text_140.tStartRefresh)
thisExp.addData('text_140.stopped', text_140.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_18.response', rating_18.getRating())
thisExp.addData('rating_18.rt', rating_18.getRT())
thisExp.nextEntry()
thisExp.addData('rating_18.started', rating_18.tStart)
thisExp.addData('rating_18.stopped', rating_18.tStop)
# the Routine "mathquestion8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mathquestion9"-------
t = 0
mathquestion9Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_19.reset()
# keep track of which components have finished
mathquestion9Components = [text_141, text_142, rating_19]
for thisComponent in mathquestion9Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mathquestion9"-------
while continueRoutine:
    # get current time
    t = mathquestion9Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_141* updates
    if t >= 0.0 and text_141.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_141.tStart = t  # not accounting for scr refresh
        text_141.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_141, 'tStartRefresh')  # time at next scr refresh
        text_141.setAutoDraw(True)
    
    # *text_142* updates
    if t >= 0.0 and text_142.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_142.tStart = t  # not accounting for scr refresh
        text_142.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_142, 'tStartRefresh')  # time at next scr refresh
        text_142.setAutoDraw(True)
    # *rating_19* updates
    if t >= 0.0 and rating_19.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_19.tStart = t  # not accounting for scr refresh
        rating_19.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_19, 'tStartRefresh')  # time at next scr refresh
        rating_19.setAutoDraw(True)
    continueRoutine &= rating_19.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mathquestion9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mathquestion9"-------
for thisComponent in mathquestion9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_141.started', text_141.tStartRefresh)
thisExp.addData('text_141.stopped', text_141.tStopRefresh)
thisExp.addData('text_142.started', text_142.tStartRefresh)
thisExp.addData('text_142.stopped', text_142.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_19.response', rating_19.getRating())
thisExp.addData('rating_19.rt', rating_19.getRT())
thisExp.nextEntry()
thisExp.addData('rating_19.started', rating_19.tStart)
thisExp.addData('rating_19.stopped', rating_19.tStop)
# the Routine "mathquestion9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "mathquestion10"-------
t = 0
mathquestion10Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_20.reset()
# keep track of which components have finished
mathquestion10Components = [text_143, text_144, rating_20]
for thisComponent in mathquestion10Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "mathquestion10"-------
while continueRoutine:
    # get current time
    t = mathquestion10Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_143* updates
    if t >= 0.0 and text_143.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_143.tStart = t  # not accounting for scr refresh
        text_143.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_143, 'tStartRefresh')  # time at next scr refresh
        text_143.setAutoDraw(True)
    
    # *text_144* updates
    if t >= 0.0 and text_144.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_144.tStart = t  # not accounting for scr refresh
        text_144.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_144, 'tStartRefresh')  # time at next scr refresh
        text_144.setAutoDraw(True)
    # *rating_20* updates
    if t >= 0.0 and rating_20.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_20.tStart = t  # not accounting for scr refresh
        rating_20.frameNStart = frameN  # exact frame index
        win.timeOnFlip(rating_20, 'tStartRefresh')  # time at next scr refresh
        rating_20.setAutoDraw(True)
    continueRoutine &= rating_20.noResponse  # a response ends the trial
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in mathquestion10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "mathquestion10"-------
for thisComponent in mathquestion10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_143.started', text_143.tStartRefresh)
thisExp.addData('text_143.stopped', text_143.tStopRefresh)
thisExp.addData('text_144.started', text_144.tStartRefresh)
thisExp.addData('text_144.stopped', text_144.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_20.response', rating_20.getRating())
thisExp.addData('rating_20.rt', rating_20.getRT())
thisExp.nextEntry()
thisExp.addData('rating_20.started', rating_20.tStart)
thisExp.addData('rating_20.stopped', rating_20.tStop)
# the Routine "mathquestion10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pretest"-------
t = 0
pretestClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_14 = keyboard.Keyboard()
# keep track of which components have finished
pretestComponents = [text_102, text_103, key_resp_14, text_104, text_105, text_120, text_121]
for thisComponent in pretestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "pretest"-------
while continueRoutine:
    # get current time
    t = pretestClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_102* updates
    if t >= 0.0 and text_102.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_102.tStart = t  # not accounting for scr refresh
        text_102.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_102, 'tStartRefresh')  # time at next scr refresh
        text_102.setAutoDraw(True)
    
    # *text_103* updates
    if t >= 0.0 and text_103.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_103.tStart = t  # not accounting for scr refresh
        text_103.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_103, 'tStartRefresh')  # time at next scr refresh
        text_103.setAutoDraw(True)
    
    # *key_resp_14* updates
    if t >= 0.0 and key_resp_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_14.tStart = t  # not accounting for scr refresh
        key_resp_14.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        key_resp_14.clearEvents(eventType='keyboard')
    if key_resp_14.status == STARTED:
        theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # *text_104* updates
    if t >= 0.0 and text_104.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_104.tStart = t  # not accounting for scr refresh
        text_104.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_104, 'tStartRefresh')  # time at next scr refresh
        text_104.setAutoDraw(True)
    
    # *text_105* updates
    if t >= 0.0 and text_105.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_105.tStart = t  # not accounting for scr refresh
        text_105.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_105, 'tStartRefresh')  # time at next scr refresh
        text_105.setAutoDraw(True)
    
    # *text_120* updates
    if t >= 0.0 and text_120.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_120.tStart = t  # not accounting for scr refresh
        text_120.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_120, 'tStartRefresh')  # time at next scr refresh
        text_120.setAutoDraw(True)
    
    # *text_121* updates
    if t >= 0.0 and text_121.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_121.tStart = t  # not accounting for scr refresh
        text_121.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_121, 'tStartRefresh')  # time at next scr refresh
        text_121.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in pretestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pretest"-------
for thisComponent in pretestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_102.started', text_102.tStartRefresh)
thisExp.addData('text_102.stopped', text_102.tStopRefresh)
thisExp.addData('text_103.started', text_103.tStartRefresh)
thisExp.addData('text_103.stopped', text_103.tStopRefresh)
thisExp.addData('text_104.started', text_104.tStartRefresh)
thisExp.addData('text_104.stopped', text_104.tStopRefresh)
thisExp.addData('text_105.started', text_105.tStartRefresh)
thisExp.addData('text_105.stopped', text_105.tStopRefresh)
thisExp.addData('text_120.started', text_120.tStartRefresh)
thisExp.addData('text_120.stopped', text_120.tStopRefresh)
thisExp.addData('text_121.started', text_121.tStartRefresh)
thisExp.addData('text_121.stopped', text_121.tStopRefresh)
# the Routine "pretest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "demo8"-------
t = 0
demo8Clock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
demo8Components = [text_10, text_11, text_12, text_52]
for thisComponent in demo8Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "demo8"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = demo8Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t  # not accounting for scr refresh
        text_10.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_10.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_10.tStop = t  # not accounting for scr refresh
        text_10.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
        text_10.setAutoDraw(False)
    
    # *text_11* updates
    if t >= 1 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t  # not accounting for scr refresh
        text_11.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    frameRemains = 1 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_11.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_11.tStop = t  # not accounting for scr refresh
        text_11.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
        text_11.setAutoDraw(False)
    
    # *text_12* updates
    if t >= 2 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t  # not accounting for scr refresh
        text_12.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    frameRemains = 2 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_12.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_12.tStop = t  # not accounting for scr refresh
        text_12.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
        text_12.setAutoDraw(False)
    
    # *text_52* updates
    if t >= 0.0 and text_52.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_52.tStart = t  # not accounting for scr refresh
        text_52.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_52, 'tStartRefresh')  # time at next scr refresh
        text_52.setAutoDraw(True)
    frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_52.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_52.tStop = t  # not accounting for scr refresh
        text_52.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_52, 'tStopRefresh')  # time at next scr refresh
        text_52.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in demo8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "demo8"-------
for thisComponent in demo8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
thisExp.addData('text_52.started', text_52.tStartRefresh)
thisExp.addData('text_52.stopped', text_52.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('vid 2.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testfixation_2"-------
    t = 0
    testfixation_2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    testfixation_2Components = [text_106]
    for thisComponent in testfixation_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "testfixation_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testfixation_2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_106* updates
        if t >= 0.0 and text_106.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_106.tStart = t  # not accounting for scr refresh
            text_106.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_106, 'tStartRefresh')  # time at next scr refresh
            text_106.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_106.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_106.tStop = t  # not accounting for scr refresh
            text_106.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_106, 'tStopRefresh')  # time at next scr refresh
            text_106.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testfixation_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testfixation_2"-------
    for thisComponent in testfixation_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_106.started', text_106.tStartRefresh)
    trials_2.addData('text_106.stopped', text_106.tStopRefresh)
    
    # ------Prepare to start Routine "testmovie"-------
    t = 0
    testmovieClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    movie_7 = visual.MovieStim3(
        win=win, name='movie_7',
        noAudio = False,
        filename=vid2,
        ori=0, pos=(0, 0), opacity=1,
        loop=False,
        size=(1280,780),
        depth=0.0,
        )
    # keep track of which components have finished
    testmovieComponents = [movie_7]
    for thisComponent in testmovieComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "testmovie"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = testmovieClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *movie_7* updates
        if t >= 0.0 and movie_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            movie_7.tStart = t  # not accounting for scr refresh
            movie_7.frameNStart = frameN  # exact frame index
            win.timeOnFlip(movie_7, 'tStartRefresh')  # time at next scr refresh
            movie_7.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if movie_7.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            movie_7.tStop = t  # not accounting for scr refresh
            movie_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(movie_7, 'tStopRefresh')  # time at next scr refresh
            movie_7.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testmovieComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testmovie"-------
    for thisComponent in testmovieComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('movie_7.started', movie_7.tStartRefresh)
    trials_2.addData('movie_7.stopped', movie_7.tStopRefresh)
    
    # ------Prepare to start Routine "loop1"-------
    t = 0
    loop1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rating_10.reset()
    rating_10 = visual.RatingScale(win=win, name='rating_10', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', ' 100'], scale='', markerStart = 0)
    
    # keep track of which components have finished
    loop1Components = [rating_10, text_107, text_127]
    for thisComponent in loop1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "loop1"-------
    while continueRoutine:
        # get current time
        t = loop1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating_10* updates
        if t >= 0.0 and rating_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_10.tStart = t  # not accounting for scr refresh
            rating_10.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_10, 'tStartRefresh')  # time at next scr refresh
            rating_10.setAutoDraw(True)
        continueRoutine &= rating_10.noResponse  # a response ends the trial
        
        # *text_107* updates
        if t >= 0.0 and text_107.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_107.tStart = t  # not accounting for scr refresh
            text_107.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_107, 'tStartRefresh')  # time at next scr refresh
            text_107.setAutoDraw(True)
        
        # *text_127* updates
        if t >= 0.0 and text_127.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_127.tStart = t  # not accounting for scr refresh
            text_127.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_127, 'tStartRefresh')  # time at next scr refresh
            text_127.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loop1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loop1"-------
    for thisComponent in loop1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('rating_10.response', rating_10.getRating())
    trials_2.addData('rating_10.rt', rating_10.getRT())
    trials_2.addData('rating_10.started', rating_10.tStart)
    trials_2.addData('rating_10.stopped', rating_10.tStop)
    marker_1 = rating_10.getRating()
    
    noresponse = rating_10.noResponse
    if (rating_10 == noresponse):
        marker_1 = 0
    trials_2.addData('text_107.started', text_107.tStartRefresh)
    trials_2.addData('text_107.stopped', text_107.tStopRefresh)
    trials_2.addData('text_127.started', text_127.tStartRefresh)
    trials_2.addData('text_127.stopped', text_127.tStopRefresh)
    # the Routine "loop1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "loop2"-------
    t = 0
    loop2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rating_11.reset()
    rating_11 = visual.RatingScale(win=win, name='rating_11', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', ' 100'], scale='', markerStart= marker_1)
    a = randint(-10,11)
    b = randint(0,11)
    
    c = randint(-10,11)
    d = randint(0,11)
    
    e = randint(-10,11)
    f = randint(0,11)
    
    cr1 = (marker_1+a-10)
    cr2 = (marker_1+a+c-20)
    cr3 = (marker_1+a+c+e-30)
    
    cr4 = (marker_1+a-20)
    cr5 = (marker_1+a+c-40)
    cr6 = (marker_1+a+c+e-60)
    
    cr7 = (marker_1+a-40)
    cr8 = (marker_1+a+c-80)
    cr9 = (marker_1+a+c+e-120)
    
    cr10 = randint(-100,101)
    cr11 = randint(-100,101)
    cr12 = randint(-100,101)
    
    cr13 = (marker_1-b)
    cr14 = (marker_1-d)
    cr15 = (marker_1-f)
    
    cr16 = (marker_1+10+a)
    cr17 = (marker_1+10+a+10-d)
    cr18 = (marker_1+10+a+10-d+10-f)
    
    cr19 = (marker_1+a)
    cr20 = (marker_1+c)
    cr21 = (marker_1+e)
    
    cr22 = (marker_1+20+a)
    cr23 = (marker_1+20+a+20-d)
    cr24 = (marker_1+20+a+20-d+20-f)
    
    cr25 = (marker_1+40+a)
    cr26 = (marker_1+40+a+40+c)
    cr27 = (marker_1+40+a+40+c+40+e)
    
    cr28 = (marker_1+b)
    cr29 = (marker_1+d)
    cr30 = (marker_1+f)
    
    cr31 = (marker_1-10+a)
    cr32 = (marker_1-10+a-10+d)
    cr33 = (marker_1-10+a-10+d-10+f)
    
    cr34 = (marker_1+20+a)
    cr35 = (marker_1+20+a+20+c)
    cr36 = (marker_1+20+a+20+c+20+e)
    
    confeda1 = [cr1, cr2, cr3]
    confeda2 = [cr4, cr5, cr6]
    confeda3 = [cr7, cr8, cr9]
    confeda4 = [cr10, cr11, cr12]
    confeda5 = [cr13, cr14, cr15]
    
    confeda6 = [cr16, cr17, cr18]
    confeda7 = [cr4, cr5, cr6]
    confeda8 = [cr1, cr2, cr3]
    confeda9 = [cr10, cr11, cr12]
    confeda10 = [cr19, cr20, cr21]
    
    confeda11 = [cr16, cr17, cr18]
    confeda12 = [cr22, cr23, cr24]
    confeda13 = [cr4, cr5, cr6]
    confeda14 = [cr10, cr11, cr12]
    confeda15 = [cr19, cr20, cr21]
    
    confeda16 = [cr16, cr17, cr18]
    confeda17 = [cr22, cr23, cr24]
    confeda18 = [cr25, cr26, cr27]
    confeda19 = [cr10, cr11, cr12]
    confeda20 = [cr28, cr29, cr30]
    
    confeda21 = [cr16, cr17, cr18]
    confeda22 = [cr22, cr23, cr24]
    confeda23 = [cr31, cr32, cr33]
    confeda24 = [cr10, cr11, cr12]
    confeda25 = [cr19, cr20, cr21]
    
    confeda26 = [cr1, cr2, cr3]
    confeda27 = [cr34, cr35, cr36]
    confeda28 = [cr22, cr23, cr24]
    confeda29 = [cr10, cr11, cr12]
    confeda30 = [cr19, cr20, cr21]
    
    ListConfedA = [confeda1, confeda1, confeda2, confeda2, confeda3, confeda3, confeda4, confeda5]
    confedA = choice(ListConfedA)
    
    ListConfedB = [confeda6, confeda6, confeda7, confeda7, confeda8, confeda8, confeda9, confeda10]
    confedB = choice(ListConfedB)
    
    ListConfedC = [confeda11, confeda11, confeda12, confeda12, confeda13, confeda13, confeda14, confeda15]
    confedC = choice(ListConfedC)
    
    ListConfedD = [confeda16, confeda16, confeda17, confeda17, confeda18, confeda18, confeda19, confeda20]
    confedD = choice(ListConfedD)
    
    ListConfedE = [confeda21, confeda21, confeda22, confeda22, confeda23, confeda23, confeda24, confeda25]
    confedE = choice(ListConfedE)
    
    ListConfedF = [confeda26, confeda26, confeda27, confeda27, confeda28, confeda28, confeda29, confeda30]
    confedF = choice(ListConfedF)
    
    
    confed = []
    if marker_1 in range(60,101):
        confed = confedA[0]
    elif marker_1 in range(30,60):
        confed = confedB[0]
    elif marker_1 in range(0,30):
        confed = confedC[0]
    elif marker_1 in range(-100,-59):
        confed = confedD[0]
    elif marker_1 in range(-59,-29):
        confed = confedE[0]
    elif marker_1 in range(-29,0):
        confed = confedF[0]
    
    
    conScore = visual.TextStim(win=win, name='conScore',
        text='%3i' %(confed),
        font='Arial',
        pos=(0.3, 0.3), height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    TriPos = (confed*2.4)/1000
    
    trianglecon1 = visual.ShapeStim(
        win=win, name='trianglecpn1',
        vertices=[[-(0.030, 0.020)[0]/2.0,-(0.030, 0.020)[1]/2.0], [+(0.030, 0.020)[0]/2.0,-(0.030, 0.020)[1]/2.0], [0,(0.030, 0.020)[1]/2.0]],
        ori=180, pos=(TriPos, 0.32),
        lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
        fillColor=[1,1,1], fillColorSpace='rgb',
        opacity=1, depth=-3.0, interpolate=True)
    
    
    confedtwo = []
    if marker_1 in range(60,101):
        confedtwo = confedA[1]
    elif marker_1 in range(30,60):
        confedtwo = confedB[1]
    elif marker_1 in range(0,30):
        confedtwo = confedC[1]
    elif marker_1 in range(-100,-59):
        confedtwo = confedD[1]
    elif marker_1 in range(-60,-29):
        confedtwo = confedE[1]
    elif marker_1 in range(-30,0):
        confedtwo = confedF[1]
    
    confedthree = []
    if marker_1 in range(60,101):
        confedthree = confedA[2]
    elif marker_1 in range(30,60):
        confedthree = confedB[2]
    elif marker_1 in range(0,30):
        confedthree = confedC[2]
    elif marker_1 in range(-100,-59):
        confedthree = confedD[2]
    elif confedthree in range(-59,-29):
        confedthree = confedE[2]
    elif marker_1 in range(-29,0):
        confedthree = confedF[2]
    # keep track of which components have finished
    loop2Components = [rating_11, polygon_5, trianglecon1, polygon_6, conScore, text_108, text_124, text_128]
    for thisComponent in loop2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "loop2"-------
    while continueRoutine:
        # get current time
        t = loop2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating_11* updates
        if t >= 0.0 and rating_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_11.tStart = t  # not accounting for scr refresh
            rating_11.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_11, 'tStartRefresh')  # time at next scr refresh
            rating_11.setAutoDraw(True)
        continueRoutine &= rating_11.noResponse  # a response ends the trial
        
        # *polygon_5* updates
        if t >= 0.0 and polygon_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_5.tStart = t  # not accounting for scr refresh
            polygon_5.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(True)
        
        # *trianglecon1* updates
        if t >= 0.0 and trianglecon1.status == NOT_STARTED:
            # keep track of start time/frame for later
            trianglecon1.tStart = t  # not accounting for scr refresh
            trianglecon1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(trianglecon1, 'tStartRefresh')  # time at next scr refresh
            trianglecon1.setAutoDraw(True)
        
        # *polygon_6* updates
        if t >= 0.0 and polygon_6.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_6.tStart = t  # not accounting for scr refresh
            polygon_6.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
            polygon_6.setAutoDraw(True)
        
        # *conScore* updates
        if t >= 0.0 and conScore.status == NOT_STARTED:
            # keep track of start time/frame for later
            conScore.tStart = t  # not accounting for scr refresh
            conScore.frameNStart = frameN  # exact frame index
            win.timeOnFlip(conScore, 'tStartRefresh')  # time at next scr refresh
            conScore.setAutoDraw(True)
        
        # *text_108* updates
        if t >= 0.0 and text_108.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_108.tStart = t  # not accounting for scr refresh
            text_108.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_108, 'tStartRefresh')  # time at next scr refresh
            text_108.setAutoDraw(True)
        
        # *text_124* updates
        if t >= 0.0 and text_124.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_124.tStart = t  # not accounting for scr refresh
            text_124.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_124, 'tStartRefresh')  # time at next scr refresh
            text_124.setAutoDraw(True)
        
        # *text_128* updates
        if t >= 0.0 and text_128.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_128.tStart = t  # not accounting for scr refresh
            text_128.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_128, 'tStartRefresh')  # time at next scr refresh
            text_128.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loop2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loop2"-------
    for thisComponent in loop2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('rating_11.response', rating_11.getRating())
    trials_2.addData('rating_11.rt', rating_11.getRT())
    trials_2.addData('rating_11.started', rating_11.tStart)
    trials_2.addData('rating_11.stopped', rating_11.tStop)
    marker_2 = rating_11.getRating()
    
    noresponse = rating_11.noResponse
    if (rating_11 == noresponse):
        marker_2 = marker_1
    trials_2.addData('polygon_5.started', polygon_5.tStartRefresh)
    trials_2.addData('polygon_5.stopped', polygon_5.tStopRefresh)
    trials_2.addData('trianglecon1.started', trianglecon1.tStartRefresh)
    trials_2.addData('trianglecon1.stopped', trianglecon1.tStopRefresh)
    trials_2.addData('polygon_6.started', polygon_6.tStartRefresh)
    trials_2.addData('polygon_6.stopped', polygon_6.tStopRefresh)
    trials_2.addData('conScore.started', conScore.tStartRefresh)
    trials_2.addData('conScore.stopped', conScore.tStopRefresh)
    trials_2.addData('text_108.started', text_108.tStartRefresh)
    trials_2.addData('text_108.stopped', text_108.tStopRefresh)
    thisExp.addData('Confed1', confed)
    trials_2.addData('text_124.started', text_124.tStartRefresh)
    trials_2.addData('text_124.stopped', text_124.tStopRefresh)
    trials_2.addData('text_128.started', text_128.tStartRefresh)
    trials_2.addData('text_128.stopped', text_128.tStopRefresh)
    # the Routine "loop2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "loop3"-------
    t = 0
    loop3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rating_12.reset()
    rating_12 = visual.RatingScale(win=win, name='rating_12', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', ' 100'], scale='', markerStart= marker_2)
    confedtwo = []
    if marker_1 in range(60,101):
        confedtwo = confedA[1]
    elif marker_1 in range(30,60):
        confedtwo = confedB[1]
    elif marker_1 in range(0,30):
        confedtwo = confedC[1]
    elif marker_1 in range(-100,-59):
        confedtwo = confedD[1]
    elif marker_1 in range(-59,-29):
        confedtwo = confedE[1]
    elif marker_1 in range(-29,0):
        confedtwo = confedF[1]
    
    conScore2 = visual.TextStim(win=win, name='conScore2',
        text='%3i' %(confedtwo),
        font='Arial',
        pos=(0.3, 0.2), height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    TriPos2 = (confedtwo*2.4)/1000
    
    trianglecon2 = visual.ShapeStim(
        win=win, name='trianglecon2',
        vertices=[[-(0.030, 0.020)[0]/2.0,-(0.030, 0.020)[1]/2.0], [+(0.030, 0.020)[0]/2.0,-(0.030, 0.020)[1]/2.0], [0,(0.030, 0.020)[1]/2.0]],
        ori=180, pos=(TriPos2, 0.22),
        lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
        fillColor=[1,1,1], fillColorSpace='rgb',
        opacity=1, depth=-3.0, interpolate=True)
    conScore1_1 = visual.TextStim(win=win, name='conScore1_1',
        text='%3i' %(confed),
        font='Arial',
        pos=(0.3, 0.3), height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    TriPos = (confed*2.4)/1000
    
    triangle3_1 = visual.ShapeStim(
        win=win, name='triangle3_1',
        vertices=[[-(0.030, 0.020)[0]/2.0,-(0.030, 0.020)[1]/2.0], [+(0.030, 0.020)[0]/2.0,-(0.030, 0.020)[1]/2.0], [0,(0.030, 0.020)[1]/2.0]],
        ori=180, pos=(TriPos, 0.32),
        lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
        fillColor=[1,1,1], fillColorSpace='rgb',
        opacity=1, depth=-3.0, interpolate=True)
    # keep track of which components have finished
    loop3Components = [rating_12, polygon_7, polygon_8, trianglecon2, conScore2, text_109, polygon_9, polygon_10, triangle3_1, conScore1_1, text_110, text_125, text_129]
    for thisComponent in loop3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "loop3"-------
    while continueRoutine:
        # get current time
        t = loop3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating_12* updates
        if t >= 0.0 and rating_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_12.tStart = t  # not accounting for scr refresh
            rating_12.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_12, 'tStartRefresh')  # time at next scr refresh
            rating_12.setAutoDraw(True)
        continueRoutine &= rating_12.noResponse  # a response ends the trial
        
        # *polygon_7* updates
        if t >= 0.0 and polygon_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_7.tStart = t  # not accounting for scr refresh
            polygon_7.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
            polygon_7.setAutoDraw(True)
        
        # *polygon_8* updates
        if t >= 0.0 and polygon_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_8.tStart = t  # not accounting for scr refresh
            polygon_8.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_8, 'tStartRefresh')  # time at next scr refresh
            polygon_8.setAutoDraw(True)
        
        # *trianglecon2* updates
        if t >= 0.0 and trianglecon2.status == NOT_STARTED:
            # keep track of start time/frame for later
            trianglecon2.tStart = t  # not accounting for scr refresh
            trianglecon2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(trianglecon2, 'tStartRefresh')  # time at next scr refresh
            trianglecon2.setAutoDraw(True)
        
        # *conScore2* updates
        if t >= 0.0 and conScore2.status == NOT_STARTED:
            # keep track of start time/frame for later
            conScore2.tStart = t  # not accounting for scr refresh
            conScore2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(conScore2, 'tStartRefresh')  # time at next scr refresh
            conScore2.setAutoDraw(True)
        
        # *text_109* updates
        if t >= 0.0 and text_109.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_109.tStart = t  # not accounting for scr refresh
            text_109.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_109, 'tStartRefresh')  # time at next scr refresh
            text_109.setAutoDraw(True)
        
        # *polygon_9* updates
        if t >= 0.0 and polygon_9.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_9.tStart = t  # not accounting for scr refresh
            polygon_9.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_9, 'tStartRefresh')  # time at next scr refresh
            polygon_9.setAutoDraw(True)
        
        # *polygon_10* updates
        if t >= 0.0 and polygon_10.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_10.tStart = t  # not accounting for scr refresh
            polygon_10.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_10, 'tStartRefresh')  # time at next scr refresh
            polygon_10.setAutoDraw(True)
        
        # *triangle3_1* updates
        if t >= 0.0 and triangle3_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            triangle3_1.tStart = t  # not accounting for scr refresh
            triangle3_1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(triangle3_1, 'tStartRefresh')  # time at next scr refresh
            triangle3_1.setAutoDraw(True)
        
        # *conScore1_1* updates
        if t >= 0.0 and conScore1_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            conScore1_1.tStart = t  # not accounting for scr refresh
            conScore1_1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(conScore1_1, 'tStartRefresh')  # time at next scr refresh
            conScore1_1.setAutoDraw(True)
        
        # *text_110* updates
        if t >= 0.0 and text_110.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_110.tStart = t  # not accounting for scr refresh
            text_110.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_110, 'tStartRefresh')  # time at next scr refresh
            text_110.setAutoDraw(True)
        
        # *text_125* updates
        if t >= 0.0 and text_125.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_125.tStart = t  # not accounting for scr refresh
            text_125.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_125, 'tStartRefresh')  # time at next scr refresh
            text_125.setAutoDraw(True)
        
        # *text_129* updates
        if t >= 0.0 and text_129.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_129.tStart = t  # not accounting for scr refresh
            text_129.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_129, 'tStartRefresh')  # time at next scr refresh
            text_129.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loop3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loop3"-------
    for thisComponent in loop3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('rating_12.response', rating_12.getRating())
    trials_2.addData('rating_12.rt', rating_12.getRT())
    trials_2.addData('rating_12.started', rating_12.tStart)
    trials_2.addData('rating_12.stopped', rating_12.tStop)
    marker_3 = rating_12.getRating()
    
    noresponse = rating_12.noResponse
    if (rating_12 == noresponse):
        marker_3 = marker_2
    trials_2.addData('polygon_7.started', polygon_7.tStartRefresh)
    trials_2.addData('polygon_7.stopped', polygon_7.tStopRefresh)
    trials_2.addData('polygon_8.started', polygon_8.tStartRefresh)
    trials_2.addData('polygon_8.stopped', polygon_8.tStopRefresh)
    trials_2.addData('trianglecon2.started', trianglecon2.tStartRefresh)
    trials_2.addData('trianglecon2.stopped', trianglecon2.tStopRefresh)
    trials_2.addData('conScore2.started', conScore2.tStartRefresh)
    trials_2.addData('conScore2.stopped', conScore2.tStopRefresh)
    trials_2.addData('text_109.started', text_109.tStartRefresh)
    trials_2.addData('text_109.stopped', text_109.tStopRefresh)
    trials_2.addData('polygon_9.started', polygon_9.tStartRefresh)
    trials_2.addData('polygon_9.stopped', polygon_9.tStopRefresh)
    trials_2.addData('polygon_10.started', polygon_10.tStartRefresh)
    trials_2.addData('polygon_10.stopped', polygon_10.tStopRefresh)
    trials_2.addData('triangle3_1.started', triangle3_1.tStartRefresh)
    trials_2.addData('triangle3_1.stopped', triangle3_1.tStopRefresh)
    trials_2.addData('conScore1_1.started', conScore1_1.tStartRefresh)
    trials_2.addData('conScore1_1.stopped', conScore1_1.tStopRefresh)
    trials_2.addData('text_110.started', text_110.tStartRefresh)
    trials_2.addData('text_110.stopped', text_110.tStopRefresh)
    thisExp.addData('Confed2', confedtwo)
    trials_2.addData('text_125.started', text_125.tStartRefresh)
    trials_2.addData('text_125.stopped', text_125.tStopRefresh)
    trials_2.addData('text_129.started', text_129.tStartRefresh)
    trials_2.addData('text_129.stopped', text_129.tStopRefresh)
    # the Routine "loop3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "loop4"-------
    t = 0
    loop4Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    rating_13.reset()
    rating_13 = visual.RatingScale(win=win, name='rating_13', marker='triangle', size=1.0, pos=[0.0, -0.4], low=-100, high=100, labels=['-100', ' 100'], scale='', markerStart= marker_3)
    confedthree = []
    if marker_1 in range(60,101):
        confedthree = confedA[2]
    elif marker_1 in range(30,60):
        confedthree = confedB[2]
    elif marker_1 in range(0,30):
        confedthree = confedC[2]
    elif marker_1 in range(-100,-59):
        confedthree = confedD[2]
    elif marker_1 in range(-59,-29):
        confedthree = confedE[2]
    elif marker_1 in range(-29,0):
        confedthree = confedF[2]
    
    
    conScore3 = visual.TextStim(win=win, name='conScore3',
        text='%3i' %(confedthree),
        font='Arial',
        pos=(0.3, 0.1), height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    TriPos3 = (confedthree*2.4)/1000
    
    triangle4 = visual.ShapeStim(
        win=win, name='triangle4',
        vertices=[[-(0.030, 0.020)[0]/2.0,-(0.030, 0.020)[1]/2.0], [+(0.030, 0.020)[0]/2.0,-(0.030, 0.020)[1]/2.0], [0,(0.030, 0.020)[1]/2.0]],
        ori=180, pos=(TriPos3, 0.12),
        lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
        fillColor=[1,1,1], fillColorSpace='rgb',
        opacity=1, depth=-3.0, interpolate=True)
    conScore1_2 = visual.TextStim(win=win, name='conScore1_2',
        text='%3i' %(confed),
        font='Arial',
        pos=(0.3, 0.3), height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    TriPos = (confed*2.4)/1000
    
    triangle1_2 = visual.ShapeStim(
        win=win, name='triangle1_2',
        vertices=[[-(0.030, 0.020)[0]/2.0,-(0.030, 0.020)[1]/2.0], [+(0.030, 0.020)[0]/2.0,-(0.030, 0.020)[1]/2.0], [0,(0.030, 0.020)[1]/2.0]],
        ori=180, pos=(TriPos, 0.32),
        lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
        fillColor=[1,1,1], fillColorSpace='rgb',
        opacity=1, depth=-3.0, interpolate=True)
    conScore2_1 = visual.TextStim(win=win, name='conScore2_1',
        text='%3i' %(confedtwo),
        font='Arial',
        pos=(0.3, 0.2), height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    
    TriPos2 = (confedtwo*2.4)/1000
    
    triangle2_1 = visual.ShapeStim(
        win=win, name='triangle2_1',
        vertices=[[-(0.030, 0.020)[0]/2.0,-(0.030, 0.020)[1]/2.0], [+(0.030, 0.020)[0]/2.0,-(0.030, 0.020)[1]/2.0], [0,(0.030, 0.020)[1]/2.0]],
        ori=180, pos=(TriPos2, 0.22),
        lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
        fillColor=[1,1,1], fillColorSpace='rgb',
        opacity=1, depth=-3.0, interpolate=True)
    # keep track of which components have finished
    loop4Components = [rating_13, polygon_11, polygon_12, triangle4, conScore3, text_111, triangle1_2, polygon_13, polygon_14, conScore1_2, text_112, triangle2_1, polygon_15, polygon_16, conScore2_1, text_113, text_126, text_130]
    for thisComponent in loop4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "loop4"-------
    while continueRoutine:
        # get current time
        t = loop4Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *rating_13* updates
        if t >= 0.0 and rating_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            rating_13.tStart = t  # not accounting for scr refresh
            rating_13.frameNStart = frameN  # exact frame index
            win.timeOnFlip(rating_13, 'tStartRefresh')  # time at next scr refresh
            rating_13.setAutoDraw(True)
        continueRoutine &= rating_13.noResponse  # a response ends the trial
        
        # *polygon_11* updates
        if t >= 0.0 and polygon_11.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_11.tStart = t  # not accounting for scr refresh
            polygon_11.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_11, 'tStartRefresh')  # time at next scr refresh
            polygon_11.setAutoDraw(True)
        
        # *polygon_12* updates
        if t >= 0.0 and polygon_12.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_12.tStart = t  # not accounting for scr refresh
            polygon_12.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_12, 'tStartRefresh')  # time at next scr refresh
            polygon_12.setAutoDraw(True)
        
        # *triangle4* updates
        if t >= 0.0 and triangle4.status == NOT_STARTED:
            # keep track of start time/frame for later
            triangle4.tStart = t  # not accounting for scr refresh
            triangle4.frameNStart = frameN  # exact frame index
            win.timeOnFlip(triangle4, 'tStartRefresh')  # time at next scr refresh
            triangle4.setAutoDraw(True)
        
        # *conScore3* updates
        if t >= 0.0 and conScore3.status == NOT_STARTED:
            # keep track of start time/frame for later
            conScore3.tStart = t  # not accounting for scr refresh
            conScore3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(conScore3, 'tStartRefresh')  # time at next scr refresh
            conScore3.setAutoDraw(True)
        
        # *text_111* updates
        if t >= 0.0 and text_111.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_111.tStart = t  # not accounting for scr refresh
            text_111.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_111, 'tStartRefresh')  # time at next scr refresh
            text_111.setAutoDraw(True)
        
        # *triangle1_2* updates
        if t >= 0.0 and triangle1_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            triangle1_2.tStart = t  # not accounting for scr refresh
            triangle1_2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(triangle1_2, 'tStartRefresh')  # time at next scr refresh
            triangle1_2.setAutoDraw(True)
        
        # *polygon_13* updates
        if t >= 0.0 and polygon_13.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_13.tStart = t  # not accounting for scr refresh
            polygon_13.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_13, 'tStartRefresh')  # time at next scr refresh
            polygon_13.setAutoDraw(True)
        
        # *polygon_14* updates
        if t >= 0.0 and polygon_14.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_14.tStart = t  # not accounting for scr refresh
            polygon_14.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_14, 'tStartRefresh')  # time at next scr refresh
            polygon_14.setAutoDraw(True)
        
        # *conScore1_2* updates
        if t >= 0.0 and conScore1_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            conScore1_2.tStart = t  # not accounting for scr refresh
            conScore1_2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(conScore1_2, 'tStartRefresh')  # time at next scr refresh
            conScore1_2.setAutoDraw(True)
        
        # *text_112* updates
        if t >= 0.0 and text_112.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_112.tStart = t  # not accounting for scr refresh
            text_112.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_112, 'tStartRefresh')  # time at next scr refresh
            text_112.setAutoDraw(True)
        
        # *triangle2_1* updates
        if t >= 0.0 and triangle2_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            triangle2_1.tStart = t  # not accounting for scr refresh
            triangle2_1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(triangle2_1, 'tStartRefresh')  # time at next scr refresh
            triangle2_1.setAutoDraw(True)
        
        # *polygon_15* updates
        if t >= 0.0 and polygon_15.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_15.tStart = t  # not accounting for scr refresh
            polygon_15.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_15, 'tStartRefresh')  # time at next scr refresh
            polygon_15.setAutoDraw(True)
        
        # *polygon_16* updates
        if t >= 0.0 and polygon_16.status == NOT_STARTED:
            # keep track of start time/frame for later
            polygon_16.tStart = t  # not accounting for scr refresh
            polygon_16.frameNStart = frameN  # exact frame index
            win.timeOnFlip(polygon_16, 'tStartRefresh')  # time at next scr refresh
            polygon_16.setAutoDraw(True)
        
        # *conScore2_1* updates
        if t >= 0.0 and conScore2_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            conScore2_1.tStart = t  # not accounting for scr refresh
            conScore2_1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(conScore2_1, 'tStartRefresh')  # time at next scr refresh
            conScore2_1.setAutoDraw(True)
        
        # *text_113* updates
        if t >= 0.0 and text_113.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_113.tStart = t  # not accounting for scr refresh
            text_113.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_113, 'tStartRefresh')  # time at next scr refresh
            text_113.setAutoDraw(True)
        
        # *text_126* updates
        if t >= 0.0 and text_126.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_126.tStart = t  # not accounting for scr refresh
            text_126.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_126, 'tStartRefresh')  # time at next scr refresh
            text_126.setAutoDraw(True)
        
        # *text_130* updates
        if t >= 0.0 and text_130.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_130.tStart = t  # not accounting for scr refresh
            text_130.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_130, 'tStartRefresh')  # time at next scr refresh
            text_130.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in loop4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "loop4"-------
    for thisComponent in loop4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('rating_13.response', rating_13.getRating())
    trials_2.addData('rating_13.rt', rating_13.getRT())
    trials_2.addData('rating_13.started', rating_13.tStart)
    trials_2.addData('rating_13.stopped', rating_13.tStop)
    marker_4 = rating_13.getRating()
    
    noresponse = rating_13.noResponse
    if (rating_13 == noresponse):
        marker_4 = marker_3
    trials_2.addData('polygon_11.started', polygon_11.tStartRefresh)
    trials_2.addData('polygon_11.stopped', polygon_11.tStopRefresh)
    trials_2.addData('polygon_12.started', polygon_12.tStartRefresh)
    trials_2.addData('polygon_12.stopped', polygon_12.tStopRefresh)
    trials_2.addData('triangle4.started', triangle4.tStartRefresh)
    trials_2.addData('triangle4.stopped', triangle4.tStopRefresh)
    trials_2.addData('conScore3.started', conScore3.tStartRefresh)
    trials_2.addData('conScore3.stopped', conScore3.tStopRefresh)
    trials_2.addData('text_111.started', text_111.tStartRefresh)
    trials_2.addData('text_111.stopped', text_111.tStopRefresh)
    trials_2.addData('triangle1_2.started', triangle1_2.tStartRefresh)
    trials_2.addData('triangle1_2.stopped', triangle1_2.tStopRefresh)
    trials_2.addData('polygon_13.started', polygon_13.tStartRefresh)
    trials_2.addData('polygon_13.stopped', polygon_13.tStopRefresh)
    trials_2.addData('polygon_14.started', polygon_14.tStartRefresh)
    trials_2.addData('polygon_14.stopped', polygon_14.tStopRefresh)
    trials_2.addData('conScore1_2.started', conScore1_2.tStartRefresh)
    trials_2.addData('conScore1_2.stopped', conScore1_2.tStopRefresh)
    trials_2.addData('text_112.started', text_112.tStartRefresh)
    trials_2.addData('text_112.stopped', text_112.tStopRefresh)
    trials_2.addData('triangle2_1.started', triangle2_1.tStartRefresh)
    trials_2.addData('triangle2_1.stopped', triangle2_1.tStopRefresh)
    trials_2.addData('polygon_15.started', polygon_15.tStartRefresh)
    trials_2.addData('polygon_15.stopped', polygon_15.tStopRefresh)
    trials_2.addData('polygon_16.started', polygon_16.tStartRefresh)
    trials_2.addData('polygon_16.stopped', polygon_16.tStopRefresh)
    trials_2.addData('conScore2_1.started', conScore2_1.tStartRefresh)
    trials_2.addData('conScore2_1.stopped', conScore2_1.tStopRefresh)
    trials_2.addData('text_113.started', text_113.tStartRefresh)
    trials_2.addData('text_113.stopped', text_113.tStopRefresh)
    thisExp.addData('Confed3', confedthree)
    trials_2.addData('text_126.started', text_126.tStartRefresh)
    trials_2.addData('text_126.stopped', text_126.tStopRefresh)
    trials_2.addData('text_130.started', text_130.tStartRefresh)
    trials_2.addData('text_130.stopped', text_130.tStopRefresh)
    # the Routine "loop4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'

# get names of stimulus parameters
if trials_2.trialList in ([], [None], None):
    params = []
else:
    params = trials_2.trialList[0].keys()
# save data for this loop
trials_2.saveAsExcel(filename + '.xlsx', sheetName='trials_2',
    stimOut=params,
    dataOut=['n','all_mean','all_std', 'all_raw'])

# ------Prepare to start Routine "Bye"-------
t = 0
ByeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_15 = keyboard.Keyboard()
# keep track of which components have finished
ByeComponents = [text_114, text_115, text_116, key_resp_15]
for thisComponent in ByeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Bye"-------
while continueRoutine:
    # get current time
    t = ByeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_114* updates
    if t >= 0.0 and text_114.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_114.tStart = t  # not accounting for scr refresh
        text_114.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_114, 'tStartRefresh')  # time at next scr refresh
        text_114.setAutoDraw(True)
    
    # *text_115* updates
    if t >= 0.0 and text_115.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_115.tStart = t  # not accounting for scr refresh
        text_115.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_115, 'tStartRefresh')  # time at next scr refresh
        text_115.setAutoDraw(True)
    
    # *text_116* updates
    if t >= 0.0 and text_116.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_116.tStart = t  # not accounting for scr refresh
        text_116.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_116, 'tStartRefresh')  # time at next scr refresh
        text_116.setAutoDraw(True)
    
    # *key_resp_15* updates
    if t >= 0.0 and key_resp_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_15.tStart = t  # not accounting for scr refresh
        key_resp_15.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        key_resp_15.clearEvents(eventType='keyboard')
    if key_resp_15.status == STARTED:
        theseKeys = key_resp_15.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ByeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Bye"-------
for thisComponent in ByeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_114.started', text_114.tStartRefresh)
thisExp.addData('text_114.stopped', text_114.tStopRefresh)
thisExp.addData('text_115.started', text_115.tStartRefresh)
thisExp.addData('text_115.stopped', text_115.tStopRefresh)
thisExp.addData('text_116.started', text_116.tStartRefresh)
thisExp.addData('text_116.stopped', text_116.tStopRefresh)
# the Routine "Bye" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
