"""
The following script runs a basic experiment software that presents participants with a number choice task.
Users are presented two numbers on each side of the screen and have to decide which number is bigger.
"""

#importing packages
import numpy as np
from psychopy import core, visual, event
import pandas as pd

#defining experimental parameters
initial_numbers = list(range(1,41))
np.random.shuffle(initial_numbers)
initial_numbers = np.array(initial_numbers)

number_sets_or = np.reshape(initial_numbers, (20,2))
number_sets_fl = np.flip(number_sets_or,1)

number_sets = np.concatenate((number_sets_or,number_sets_fl),0)
np.random.shuffle(number_sets)

parameters = []
    
number_sets_str = [str(x) for x in number_sets]
number_sets_str = {x.replace('[','').replace(']','') for x in number_sets_str}

parameters.append(number_sets)


#defining psychopy parameters
win = visual.Window(fullscr = False, color=(-1,-1,-1), units = 'pix')
timer = core.Clock()

#first page
hello_text = visual.TextStim(win, text = 'Hello!\n\nThis experiment is designed to test your numerical cognition.\nYour task is to evaluate which number is larger.\nIf the number on the left is larger, press F and if the number on the right side is larger, press J.\nYou should response in less than a second!\n\n Press ENTER to start.\n\nGood luck!', color =(1,1,1), height = 25)
hello_text.draw()
win.flip()

#starting the experiment
initiate = event.waitKeys(keyList=('return'),clearEvents = True)
if 'return' in initiate:
    pass

#fixation period
fix_cross_h = visual.Line(win, lineColor = (1,1,1), lineWidth = 20, start = (-20, 0), end =(20, 0))
fix_cross_h.draw()
fix_cross_v = visual.Line(win, lineColor = (1,1,1), lineWidth = 20, start = (0, -20), end =(0, 20))
fix_cross_v.draw()
win.flip()
core.wait(2)

#running trials
for x in number_sets_str:
    print(x)
    stimulus = visual.TextStim(win, text = x, height = 30)
    stimulus.draw()
    fix_line = visual.Line(win, lineColor = (1,1,1), lineWidth = 2, start = (0, -20), end =(0, 20))
    fix_line.draw()
    win.flip()
    user_response = event.waitKeys(keyList=('f','j'), clearEvents = True, timeStamped = timer)
    print(user_response)
    
    user_key = user_response[0][0]
    user_rt  = user_response[0][1]
    
    parameters.append(user_response)
    
    #feedback
    if user_rt > 1:
        feedback_text = visual.TextStim(win, text = 'You should respond faster!', color =(1,1,1), height = 25)
        feedback_text.draw()
        win.flip()
        core.wait(1)
    timer.reset()
    
#ending page
ending_text = visual.TextStim(win, text = 'Thank you for your participation!', color =(1,1,1), height = 25)
ending_text.draw()
win.flip()
core.wait(2)

win.close()



#saving the results
df = pd.DataFrame(parameters)
df.to_csv('results.csv')


