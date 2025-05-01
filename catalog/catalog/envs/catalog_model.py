def getFullCatalog():
    # This is what the state looks like
    '''
    List of dictionaries, each representing a course
    Each course has:
    ID: str, Name: str, Hours: int, Prerequisites: list of lists of IDs,
    Designation: list of str, and Semester: str
    '''
    fullCatalog = [
            # Computer Science Core Requirements
            {'ID': 'CS 1400', 'Name': 'Fundamentals of Programming', 'Hours': 3, 'Prerequisites': [[]], 'Designation': ['CR'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            {'ID': 'CS 1410', 'Name': 'Object Oriented Programming', 'Hours': 3, 'Prerequisites': [['CS 1400']], 'Designation': ['CR'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            {'ID': 'CS 2420', 'Name': 'Introduction to Algorithms and Data Structures', 'Hours': 3, 'Prerequisites': [['CS 1410']], 'Designation': ['CR'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            {'ID': 'CS 2450', 'Name': 'Software Engineering', 'Hours': 3, 'Prerequisites': [['CS 1410']], 'Designation': ['CR'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            {'ID': 'CS 2810', 'Name': 'Computer Organization and Architecture', 'Hours': 3, 'Prerequisites': [['CS 1410']], 'Designation': ['CR'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            {'ID': 'CS 3005', 'Name': 'Programming in C++', 'Hours': 3, 'Prerequisites': [['CS 1410']], 'Designation': ['CR'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            {'ID': 'CS 3510', 'Name': 'Algorithms', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 2810', 'CS 2100']], 'Designation': ['CR'], 'Semester': ['Spring'], 'Taken': []},
            {'ID': 'CS 3530', 'Name': 'Computational Theory', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 2810', 'CS 2100'], ['CS 2100']], 'Designation': ['CR'], 'Semester': ['Fall'], 'Taken': []},
            {'ID': 'CS 4600', 'Name': 'Senior Project', 'Hours': 3, 'Prerequisites': [['CS 3005']], 'Designation': ['CR'], 'Semester': ['Spring'], 'Taken': []},

            # Computer Science Core Electives
            # Complete at least seven (7) courses from the following
            {'ID': 'CS 3150', 'Name': 'Computer Networks', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 2810']], 'Designation': ['CE', 'E'], 'Semester': ['Spring'], 'Taken': []},
            {'ID': 'CS 3400', 'Name': 'Operating Systems', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 2810', 'CS 3005']], 'Designation': ['CE', 'E'], 'Semester': ['Fall'], 'Taken': []},
            {'ID': 'CS 3410', 'Name': 'Distributed Systems', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 2810']], 'Designation': ['CE', 'E'], 'Semester': ['Spring'], 'Taken': []},
            {'ID': 'CS 3520', 'Name': 'Programming Languages', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 2810']], 'Designation': ['CE', 'E'], 'Semester': ['Fall'], 'Taken': []},
            {'ID': 'CS 3600', 'Name': 'Graphics Programming', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 3005']], 'Designation': ['CE', 'E'], 'Semester': ['Spring'], 'Taken': []},
            {'ID': 'CS 4300', 'Name': 'Artificial Intelligence', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 2810', 'CS 3005']], 'Designation': ['CE', 'E'], 'Semester': ['Fall'], 'Taken': []},
            {'ID': 'CS 4307', 'Name': 'Database Systems', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 2810']], 'Designation': ['CE', 'E'], 'Semester': ['Spring'], 'Taken': []},
            {'ID': 'CS 4320', 'Name': 'Machine Learning', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 2810', 'CS 3005']], 'Designation': ['CE', 'E'], 'Semester': ['Spring'], 'Taken': []},
            {'ID': 'CS 4550', 'Name': 'Compilers', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 2810', 'CS 3005']], 'Designation': ['CE', 'E'], 'Semester': ['Spring'], 'Taken': []},
            {'ID': 'SE 3200', 'Name': 'Web Application Development I', 'Hours': 3, 'Prerequisites': [['CS 1410', 'CS 2810']], 'Designation': ['CE', 'E'], 'Semester': ['Fall', 'Spring'], 'Taken': []},

            # Math Core Requirements
            {'ID': 'MATH 1210', 'Name': 'Calculus I', 'Hours':4, 'Prerequisites':[[]], 'Designation':['MCR'], 'Semester':['Fall', 'Spring'], 'Taken': []},
            {'ID': 'CS 2100', 'Name': 'Discrete Structures', 'Hours':3, 'Prerequisites':[['MATH 1210','CS 1410']], 'Designation':['MCR'], 'Semester':['Fall', 'Spring'], 'Taken': []},
            {'ID': 'MATH 3400', 'Name': 'Probability & Statistics', 'Hours':3, 'Prerequisites':[['MATH 1220']], 'Designation':['MCR'], 'Semester':['Fall'], 'Taken': []},

            # Math Core Electives
            # Complete at least two (2) courses from the following:
            {'ID': 'MATH 1220', 'Name': 'Calculus II', 'Hours':4, 'Prerequisites':[['MATH 1210']], 'Designation':['MCE'], 'Semester':['Fall', 'Spring'], 'Taken': []},
            {'ID': 'MATH 2210', 'Name': 'Multivariable Calculus', 'Hours':4, 'Prerequisites':[['MATH 1220']], 'Designation':['MCE'], 'Semester':['Fall', 'Spring'], 'Taken': []},
            {'ID': 'MATH 2250', 'Name': 'Differential Equations and Linear Algebra', 'Hours':4, 'Prerequisites':[['MATH 1220']], 'Designation':['MCE'], 'Semester':['Spring'], 'Taken': []},
            {'ID': 'MATH 2270', 'Name': 'Linear Algebra', 'Hours':3, 'Prerequisites':[['MATH 1210']], 'Designation':['MCE'], 'Semester':['Fall', 'Spring'], 'Taken': []},
            {'ID': 'MATH 2280', 'Name': 'Ordinary Differential Equations', 'Hours':3, 'Prerequisites':[['MATH 1220']], 'Designation':['MCE'], 'Semester':['Spring'], 'Taken': []},
            #{'ID': 'MATH 3050', 'Name': 'Stochastic Modeling and Applications', 'Hours':3, 'Prerequisites':[['MATH 2050'],['STAT 2040'],['MATH 3060'],['Math 3400']], 'Designation':['MCE'], 'Semester':['Spring'], 'Taken': []},
            {'ID': 'MATH 3450', 'Name': 'Statistical Inference', 'Hours':3, 'Prerequisites':[['MATH 3400']], 'Designation':['MCE'], 'Semester':['Spring'], 'Taken': []},
            {'ID': 'MATH 3605', 'Name': 'Introduction to Modeling and Simulation', 'Hours':3, 'Prerequisites':[['MATH 3400']], 'Designation':['MCE'], 'Semester':['Spring'], 'Taken': []},
            # for math 3905 what does FA (even) mean?
            #{'ID': 'MATH 3905', 'Name': 'Cryptography and Codes', 'Hours':3, 'Prerequisites':[['CS 1400 ', 'MATH 2200'],['CS 2100']], 'Designation':['MCE'], 'Semester':['Fall'], 'Taken': []},
            # for math 3905 what does SP (odd) mean?
            #{'ID': 'MATH 4005', 'Name': 'Quantum Computing and Cryptography', 'Hours':3, 'Prerequisites':[['CS 1400 ', 'MATH 2200'],['CS 1400', 'MATH 2270']], 'Designation':['MCE'], 'Semester':['Spring'], 'Taken': []},

            # Science Core Requirement
            # Complete one (1) course with lab from the following:
            # I just put it together but there is the class and a lab that in total are 5 credits
            {'ID': 'BIO 1610', 'Name': ' Principles of Biology I', 'Hours':5, 'Prerequisites':[[]], 'Designation':['SCR'], 'Semester':['Fall', 'Spring'], 'Taken': []},
            {'ID': 'CHEM 1210 ', 'Name': 'Principles of Chemistry I', 'Hours':5, 'Prerequisites':[[]], 'Designation':['SCR'], 'Semester':['Fall', 'Spring'], 'Taken': []},
            {'ID': 'PHYS 2210 ', 'Name': 'Physics/Scientists Engineers I', 'Hours':5, 'Prerequisites':[['MATH 1210']], 'Designation':['SCR'], 'Semester':['Fall'], 'Taken': []},

            # Computer Science Elective Requirements
            # Complete at least nine (9) credits from the following:
            {'ID': 'CS 3500', 'Name': 'Game Development', 'Hours': 3, 'Prerequisites': [['CS 3005']], 'Designation': ['E'], 'Semester': ['Fall'], 'Taken': []},
            # Research (up to 6 credits)
            {'ID': 'CS 4800R', 'Name': 'Undergraduate Research', 'Hours': 1, 'Prerequisites': [['CS 2420', 'CS 2810']], 'Designation': ['E'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            {'ID': 'CS 4920R', 'Name': 'Internship', 'Hours': 1, 'Prerequisites': [['CS 2420', 'CS 2810', 'CS 3005']], 'Designation': ['E'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            # Seminar (up to 4 credits)
            {'ID': 'CS 4992R', 'Name': 'Computer Science Seminar', 'Hours': 1, 'Prerequisites': [['CS 2420', 'CS 2810']], 'Designation': ['E'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            {'ID': 'CS 4991R', 'Name': 'Competitive Programming', 'Hours': 0.5, 'Prerequisites': [['CS 1400']], 'Designation': ['E'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            {'ID': 'IT 1100', 'Name': 'Introduction to Unix/Linux', 'Hours': 3, 'Prerequisites': [[]], 'Designation': ['E'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            #{'ID': 'IT 2700', 'Name': 'Information Security', 'Hours': 3, 'Prerequisites': [['CS 1400', 'IT 2400']], 'Designation': ['E'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            #{'ID': 'IT 3100', 'Name': 'Systems Design and Administration', 'Hours': 3, 'Prerequisites': [['CS 1400', 'IT 1100' ,'IT 1500', 'IT 2400'],['IT 1100', 'IT 1500', 'CS 3150']], 'Designation': ['E'], 'Semester': ['Fall'], 'Taken': []},
            #{'ID': 'IT 3110', 'Name': 'System Automation', 'Hours': 3, 'Prerequisites': [['CS 1410', 'IT 3100']], 'Designation': ['E'], 'Semester': ['Spring'], 'Taken': []},
            {'ID': 'IT 4200', 'Name': 'DevOps Lifecycle Management', 'Hours': 3, 'Prerequisites': [['CS 1400', 'IT 2400'],['CS 2810']], 'Designation': ['E'], 'Semester': ['Fall'], 'Taken': []},
            {'ID': 'SE 1400', 'Name': 'Web Design', 'Hours': 3, 'Prerequisites': [[]], 'Designation': ['E'], 'Semester': ['Fall', 'Spring'], 'Taken': []},
            {'ID': 'SE 3010', 'Name': 'Mobile Application Development for Android', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 3005']], 'Designation': ['E'], 'Semester': ['Spring'], 'Taken': []},
            {'ID': 'SE 3020', 'Name': 'Mobile Application Development: iOS', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 3005']], 'Designation': ['E'], 'Semester': ['Fall'], 'Taken': []},
            {'ID': 'SE 3100', 'Name': 'Software Practices', 'Hours': 3, 'Prerequisites': [['SE 2450'],['CS 2450'],['WEB 3450']], 'Designation': ['E'], 'Semester': ['Spring'], 'Taken': []},
            {'ID': 'SE 4200', 'Name': 'Web Application Development II', 'Hours': 3, 'Prerequisites': [['SE 3200']], 'Designation': ['E'], 'Semester': ['Spring'], 'Taken': []},
            {'ID': 'SE 3150', 'Name': 'Software Quality', 'Hours': 3, 'Prerequisites': [['SE 2450'],['CS 2450'],['WEB 3450']], 'Designation': ['E'], 'Semester': ['Fall'], 'Taken': []},
            {'ID': 'SE 3400', 'Name': 'Human-Computer Interaction', 'Hours': 3, 'Prerequisites': [['SE 1400'],['WEB 1400']], 'Designation': ['E'], 'Semester': ['Fall'], 'Taken': []},
            {'ID': 'SE 3450', 'Name': 'User Experience Design', 'Hours': 3, 'Prerequisites': [['SE 1400']], 'Designation': ['E'], 'Semester': ['Spring'], 'Taken': []},
        ]

    return fullCatalog

import random 
from copy import deepcopy
import itertools

class Student:
    def __init__(self, classesTaken, catalog, creditsMax=15, current_semester="Fall"):
        # GE: general education, CR: core required, CE: core elective, 
        # MCR: math core required, MCE: math core elective, SCR: science, E: elective
        # CR, CE, MCR, MCE, SCR: course count
        # E: credit count
        self.mGradReqs = {'CR': 9, 'CE': 7, 'MCR': 3, 'MCE': 2, 'SCR': 1, 'E': 9} 
        # When taking classes update this variable to see if you took everything you need 
        self.mReqsProgress = {'CR': 0, 'CE': 0, 'MCR': 0, 'MCE': 0, 'SCR': 0, 'E': 0}  
        self.mCatalog = catalog
        self.mClassesTaken = classesTaken
        self.mCreditsMax = creditsMax
        self.mCurrent_semester = current_semester
        return

    def getTakenClassIDs(self):
        ids_list = []
        for course in self.mClassesTaken:
            ids_list.append(course["ID"])
        return ids_list

    def graduated(self):
        ''' If the student has met all the requirements to graduate then True. '''
        for req in self.mGradReqs:
            if self.mGradReqs[req] > self.mReqsProgress[req]:
                return False
        return True

    def update_student(self, courses, semester_count):
        ''' Takes a list of courses that the student wants to take that semester
        and updates it '''
        # I am going to assume that the choices are good and all the requirements are met

        # Update the semester
        if self.mCurrent_semester == "Fall":
            self.mCurrent_semester = "Spring"
        else:
            self.mCurrent_semester = "Fall"

        for course in courses:
            
            if self.prereqChecker(self.mClassesTaken, course):
                course['Taken'] = semester_count
                self.mClassesTaken.append(course)

                # Update mReqsProgress
                self.updateProgress(course)
            else:
                print(f"Prerequisites not met for course: {course}")

        return
        
    def genSemester(self):
        ''' Generate a semester (for now ONLY BASED ON PREREQS) '''
        semester = []
        credit_num = 0
        takeable_classes = self.getTakeable(self.mCurrent_semester)
        #print(f'takeable_classes: {takeable_classes}')
        # While we can still take credits
        while credit_num < self.mCreditsMax and len(takeable_classes) > 0:
            # Choose a random class that we can take (we meet reqs)
            chosen_course = random.choice(takeable_classes)
            #print(f'chosen_course: {chosen_course}')

            if (credit_num + chosen_course['Hours']) <= self.mCreditsMax:
                # Update everything according to the course selected
                semester.append(chosen_course)
                credit_num += chosen_course['Hours']
                self.mClassesTaken.append(chosen_course)
                self.updateProgress(chosen_course)

            # Remove the class from the choices
            takeable_classes.remove(chosen_course)

        if self.mCurrent_semester == "Fall":
            self.mCurrent_semester = "Spring"
        else:
            self.mCurrent_semester = "Fall"

        #print(f'semester: {semester}')
        return semester

    def updateProgress(self, course):
        ''' This function updates self.mReqsProgress so that its easier to check
        if grad requirements are met '''
        designation = course['Designation']
        # If there is only one item in the designation
        if len(designation) == 1:
            if designation[0] == "CR":
                self.mReqsProgress["CR"] += 1
            if designation[0] == "CE":
                self.mReqsProgress["CE"] += 1
            if designation[0] == "MCR":
                self.mReqsProgress["MCR"] += 1
            if designation[0] == "MCE":
                self.mReqsProgress["MCE"] += 1
            if designation[0] == "SCR":
                self.mReqsProgress["SCR"] += 1
            if designation[0] == "E":
                self.mReqsProgress["E"] += course['Hours']

        # The only case for this is when it has both "CE" and "E"
        else:
            if self.mReqsProgress['CE'] == 9:
                self.mReqsProgress['E'] += course['Hours']
            else:
                self.mReqsProgress['CE'] += 1

        return 

    def getTakeable(self, semester):
        takeable = []
        # Loop though the list of dictionaries
        for course in self.mCatalog:
            # If the class is offered the semeseter we are in
            if semester in course['Semester']:
                # If we haven't already taken the class
                if course not in self.mClassesTaken:
                    # If True (we meet all the prereqs)
                    if self.prereqChecker(self.mClassesTaken, course):
                        # Then we can take the class
                        takeable.append(course)
        return takeable

    def prereqChecker(self, classesTaken, selectedCourse):
        taken = set()
        # Create a set of IDs of every class we have taken
        for course in classesTaken:
            taken.add(course['ID'])

        prereq_list = []
        # For every list of prereqs in the class (its a list in case is an 'or' prerequisite 
        for req_list in selectedCourse['Prerequisites']:
            prereq = set()
            # For every prereq in the list
            for req in req_list:
                # We add it as a prereq
                prereq.add(req)
            prereq_list.append(set(prereq))

        # Iterate through the prerequisites and check if we have taken the classes required
        for prer in prereq_list:
            if prer.issubset(taken):
                return True
        return False

class CatalogModel:
    def __init__(self, catalog=getFullCatalog()):
        # Computer Science catalog as a list of dictionaries
        self.mCatalog = catalog
        return

    def reset(self):
        # We don't need this
        return 

    def GOAL_TEST(self):
        # Inside the student class we have a goal test called graduated
        pass

    def ACTIONS(self, catalog):
        ''' Given a catalog return the list of classes that where I can make a
        change '''
        actions = []
        for i in range(len(catalog)):
            course = catalog[i]
            # If the course is only taught in one semester
            if len(course['Semester']) == 1:
                actions.append(course)

        # The actions list could be empty, that just means there is no action to
        # take in that course because it being taught in both spring and fall
        return actions

    def RESULT(self, catalog, course_id):
        ''' Takes a catalog and a course_id to change when that class is being
        offered (fall or spring). Returns the catalog with the change. '''
        # We look for the course id
        for course in catalog:
            if course['ID'] == course_id:
                # Change the semester to the opposite of what they have
                if course['Semester'] == "Fall":
                    course['Semester'] = "Spring"
                    break
                else:
                    course['Semester'] = "Fall"
                    break

        return catalog


    def simulateStudent(self, catalog):
        # For now classes taken will always be empty
        # Default student max credits per semester to 15
        student = Student([], catalog)
        semesters = 0
        maxSemesters = 50
        while not student.graduated() and semesters <= maxSemesters:
            student.genSemester()
            semesters += 1

        return semesters

    def UTILITY(self, catalog, n_students):
        ''' My utility is simulating n_students with the given catalog and
        returning the average semesters that they took to graduate '''
        total = 0
        for i in range(n_students):
            total += self.simulateStudent(catalog)

        average = total/n_students
        return average

    def RANDOM(self):
        ''' Generates a random catalog. The random paramters are the when the 'CE' classes are offered. '''
        # Create a deep copy of the original catalog
        random_catalog = deepcopy(self.mCatalog)
        
        # For each course in the catalog
        for course in random_catalog:
            # Only modify CE courses that are currently offered in one semester
            if 'CE' in course['Designation'] and len(course['Semester']) == 1:
                # Randomly assign either Fall or Spring
                course['Semester'] = [random.choice(['Fall', 'Spring'])]
        
        return random_catalog
    
    def NEIGHBORS(self, catalog):
        '''
        The neighbors are len(ce_courses)
        '''
        neighbors = []
        # For each course in the catalog
        for course in catalog:
            # Only look at CE courses taught in one semester
            if 'CE' in course['Designation'] and len(course['Semester']) == 1:
                # Make a complete copy of the original catalog
                new_catalog = deepcopy(catalog)
                # Find this specific course in the new catalog copy
                for new_course in new_catalog:
                    if new_course['ID'] == course['ID']:
                        # Flip just this one course's semester
                        if new_course['Semester'][0] == 'Fall':
                            new_course['Semester'] = ['Spring']
                        else:
                            new_course['Semester'] = ['Fall']
                        break
                # Add this catalog (with just one course changed) to neighbors
                neighbors.append(new_catalog)
        
        return neighbors

    '''
    # Trying to make the runtime smaller by making smaller neighbors.
    def NEIGHBORS(self, catalog):
        # Only modify a subset of CE courses each time
        # For example, randomly select 4-5 courses instead of all 9
        neighbors = []
        ce_courses = []
        for course in catalog:
            if 'CE' in course['Designation'] and len(course['Semester']) == 1:
                ce_courses.append(course)
        
        # Randomly select a subset
        if len(ce_courses) > 5:
            ce_courses = random.sample(ce_courses, 5)
        
        # Rest of function remains the same
        # This is a permutation with repetition that will retrurn all the
        # permutations of 0, 1 for the courses 0 being fall and 1 being spring
        # to generate the new catalogs. Eg. (0, 0, 0) that would be all the
        # classes are fall
        # This is 2^n where n is len(ce_courses)
        # Now generates 2^5 = 32 neighbors instead of 512
        for perm in itertools.product(range(2), repeat=len(ce_courses)):
            for i, semester in enumerate(perm):
                if semester == 0:
                    # Change to fall
                    ce_courses[i]['Semester'] = ['Fall']
                if semester == 1:
                    # Change to spring
                    ce_courses[i]['Semester'] = ['Spring']
            # Now we have the new ce_e_courses so lets make a new catalog
            new_catalog = deepcopy(self.mCatalog)
            for course in new_catalog:
                for change in ce_courses:
                    if course['ID'] == change['ID']:
                        course['Designation'] = change['Designation']
            neighbors.append(new_catalog)

        return neighbors
    '''

    '''
    def NEIGHBORS(self, catalog):
        # The permutation with repetition of the designated 'CE' 'E' classes
        # of being fall or spring 
        neighbors = []
        ce_courses = []
        for course in catalog:
            designations = course['Designation']
            #if 'CE' in designations or 'E' in designations:
            # If i do it this way it might be too much
            if 'CE' in designations :
                if len(course['Semester']) == 1:
                    ce_courses.append(course)
        # This is a permutation with repetition that will retrurn all the
        # permutations of 0, 1 for the courses 0 being fall and 1 being spring
        # to generate the new catalogs. Eg. (0, 0, 0) that would be all the
        # classes are fall
        # This is 2^n where n is len(ce_courses)
        # ce_courses is 9 so there are 512 permutations
        for perm in itertools.product(range(2), repeat=len(ce_courses)):
            for i, semester in enumerate(perm):
                if semester == 0:
                    # Change to fall
                    ce_courses[i]['Semester'] = ['Fall']
                if semester == 1:
                    # Change to spring
                    ce_courses[i]['Semester'] = ['Spring']
            # Now we have the new ce_e_courses so lets make a new catalog
            new_catalog = deepcopy(self.mCatalog)
            for course in new_catalog:
                for change in ce_courses:
                    if course['ID'] == change['ID']:
                        course['Designation'] = change['Designation']
            neighbors.append(new_catalog)

        return neighbors
    '''

'''
#TESTING NEIGHBORS
catalog = [
        {'ID': 'PHYS 2210 ', 'Name': 'Physics/Scientists Engineers I', 'Hours':5, 'Prerequisites':[['MATH 1210']], 'Designation':['SCR'], 'Semester':['Fall']},
        {'ID': 'CS 3150', 'Name': 'Computer Networks', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 2810']], 'Designation': ['CE', 'E'], 'Semester': ['Spring']},
        {'ID': 'SE 3400', 'Name': 'Human-Computer Interaction', 'Hours': 3, 'Prerequisites': [['SE 1400'],['WEB 1400']], 'Designation': ['CE', 'E'], 'Semester': ['Fall']},
        {'ID': 'CS 4800R', 'Name': 'Undergraduate Research', 'Hours': 1, 'Prerequisites': [['CS 2420', 'CS 2810']], 'Designation': ['E'], 'Semester': ['Fall', 'Spring']},
        ]
model = CatalogModel()
model.mCatalog = catalog
neighbors = model.NEIGHBORS(catalog)
for i in neighbors:
    print(i)
    print('\n')

# TESTING NEIGHBORS
catalog = [
        {'ID': 'PHYS 2210 ', 'Name': 'Physics/Scientists Engineers I', 'Hours':5, 'Prerequisites':[['MATH 1210']], 'Designation':['SCR'], 'Semester':['Fall']},
        {'ID': 'CS 3150', 'Name': 'Computer Networks', 'Hours': 3, 'Prerequisites': [['CS 2420', 'CS 2810']], 'Designation': ['CE', 'E'], 'Semester': ['Spring']},
        {'ID': 'SE 3400', 'Name': 'Human-Computer Interaction', 'Hours': 3, 'Prerequisites': [['SE 1400'],['WEB 1400']], 'Designation': ['CE', 'E'], 'Semester': ['Fall']},
        {'ID': 'CS 4800R', 'Name': 'Undergraduate Research', 'Hours': 1, 'Prerequisites': [['CS 2420', 'CS 2810']], 'Designation': ['E'], 'Semester': ['Fall', 'Spring']},
        ]
model = CatalogModel()
model.mCatalog = catalog
random_catalog = model.RANDOM()
print(random_catalog)
'''