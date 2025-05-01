
'''
The agent is given a FIXED catalog and it only evaluates it so that it can get a
reward. The agent DOES NOT modify the catalog.
'''

import gymnasium as gym
import catalog
import random

''' Random Agent will take random classes from the ones that are available in
the observation, there will be no further logic in the process '''
class RandomAgent:
    def __init__(self):
        self.reset()
        return 

    def reset(self):
        self.mReqsProgress = {'CR': 0, 'CE': 0, 'MCR': 0, 'MCE': 0, 'SCR': 0, 'E': 0}  
        return

    def agent_function(self, fullobservation):
        # Return the action based on the current policy and state
        observation, info = fullobservation
        course_info = info['course_info']
        max_semester_credits = info['max_semester_credits']
        self.mReqsProgress = info['reqs_progress']

        # Store the indexes of the classes that we can take
        takeable_classes = []
        for i, num in enumerate(observation):
            if num == 1:
                takeable_classes.append(i)

        semester = []
        for i in observation:
            semester.append(0)

        semester_credits = 0
        # Now we change the indexes of the classes that we want to take
        true = True
        while true:
            if takeable_classes == []:
                #print("Cannot take more classes.")
                #print(f'Reqs Progress: {self.mReqsProgress}')
                break
            chosen_course = random.choice(takeable_classes)
            # Update credits
            if (semester_credits + course_info[chosen_course]['Hours']) <= max_semester_credits:
                semester_credits += course_info[chosen_course]['Hours']
                semester[chosen_course] = 1
            else:
                true = False
                
        '''
        debug = []
        for i in observation:
            debug.append(0)
        '''

        return semester

