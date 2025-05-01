'''
The agent is given a FIXED catalog and it only evaluates it so that it can get a
reward. The agent DOES NOT modify the catalog.
'''

import gymnasium as gym
import catalog
import random

''' Requirements Agent will take classes from the ones that are available in
the observation, but it will have in mind that if it has met all the 'CE' reqs for example it won't take 
another class that also has 'CE' '''

class RequirementsAgent:
    def __init__(self):
        self.reset()
        return 

    def reset(self):
        self.mGradReqs = {'CR': 9, 'CE': 7, 'MCR': 3, 'MCE': 2, 'SCR': 1, 'E': 9} 
        self.mReqsProgress = {'CR': 0, 'CE': 0, 'MCR': 0, 'MCE': 0, 'SCR': 0, 'E': 0}  
        return

    def agent_function(self, fullobservation):
        observation, info = fullobservation
        course_info = info['course_info']
        max_semester_credits = info['max_semester_credits']
        self.mReqsProgress = info['reqs_progress'].copy()

        # Store the indexes of the classes that we can take
        takeable_classes = []
        for i, num in enumerate(observation):
            if num == 1:
                takeable_classes.append(i)
        
        semester = [0] * len(observation)
        semester_credits = 0

        while takeable_classes and semester_credits < max_semester_credits:
            chosen_course = random.choice(takeable_classes)
            
            course = course_info[chosen_course]
            designations = course['Designation']
            course_hours = course['Hours']

            # Skip if adding this course would exceed credit limit
            if semester_credits + course_hours > max_semester_credits:
                takeable_classes.remove(chosen_course)  # Remove to avoid selecting it again
                continue

            # Check if any designation requirement is not yet satisfied
            should_take = False
            for req in designations:
                if self.mReqsProgress[req] < self.mGradReqs[req]:
                    should_take = True
                    break

            if should_take:
                semester[chosen_course] = 1
                semester_credits += course_hours
                
                # Update progress tracking
                if len(designations) == 1:
                    if designations[0] == 'E':
                        self.mReqsProgress[designations[0]] += course_hours
                    else:
                        self.mReqsProgress[designations[0]] += 1
                else:
                    if self.mReqsProgress[designations[0]] == self.mGradReqs[designations[0]]:
                        self.mReqsProgress[designations[1]] += course_hours
                    else:
                        self.mReqsProgress[designations[0]] += 1

            takeable_classes.remove(chosen_course)  # Remove to avoid selecting it again
        
        return semester

