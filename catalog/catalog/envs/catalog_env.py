import gymnasium
import numpy as np
from gymnasium import spaces
from catalog.envs.catalog_model import CatalogModel
from catalog.envs.catalog_model import Student
from catalog.envs.catalog_model import getFullCatalog

class CatalogEnv(gymnasium.Env):
    metadata = {
        "render_modes": ["ansi", "none"]
    }

    def __init__(self, render_mode=None, max_semesters=12, max_credits_per_semester=15, catalog=getFullCatalog()):
        """Initialize the Catalog environment.
        
        Args:
            render_mode (str): Only supports 'ansi' for text representation
            max_semesters (int): Maximum number of semesters allowed for graduation
            max_credits_per_semester (int): Maximum credits allowed per semester
            catalog (list): List of course dictionaries representing the course catalog
        """

        self.render_mode = render_mode
        self.max_semesters = max_semesters
        self.max_credits_per_semester = max_credits_per_semester

        # Initialize the model with the provided catalog
        self.model = CatalogModel(catalog)
        
        self.semester_count = 0
        
        # Create a student to track progress, things we can acces:
        # mGradReqs, mReqsProgress, mCatalog, mClassesTaken, mCreditsMax, mCurrent_semester
        # Methods we can use:
        # graduated(student), genSemester(), updateProgress(course), getTakeable(semester), prereqChecker(classesTaken, course)
        # init(classesTaken, catalog, semesterMax = 15, current_semester = "Fall")
        self.student = Student([], self.model.mCatalog, max_credits_per_semester)
        
        # Action space: Which courses the agent takes that semester.
        # 0 is not take, 1 is take
        # The sum of the credits of all the 1s cannot be > than max_credits_per_semester
        self.action_space = spaces.Box(
            low=0,
            high=1,
            shape=(len(self.model.mCatalog),),
            dtype=np.int8
        )
        
        # Observation space is a binary array indicating which courses can be taken
        self.observation_space = spaces.Box(
            low=0,
            high=1,
            shape=(len(self.model.mCatalog),),
            dtype=np.int8
        )

    def reset(self, seed=None, options=None):
        """Reset the environment to initial state."""
        super().reset(seed=seed)
        
        # Reset student and semester tracking
        self.student = Student([], self.model.mCatalog, self.max_credits_per_semester)
        self.semester_count = 0
        
        observation, info = self._get_observation()
        return observation, info

    def _get_observation(self):
        """Convert current state to observation array and return additional info."""
        # Initialize observation array with zeros
        observation = np.zeros(len(self.model.mCatalog), dtype=np.int8)
         
        # Initialize info dictionary with course details
        info = {
            'course_info': []
        }
        
        # For each course in the catalog
        for i, course in enumerate(self.model.mCatalog):
            # Check if course is available this semester
            semester_available = (self.student.mCurrent_semester in course['Semester'])
            
            # Check if prerequisites are met
            prereqs_met = self.student.prereqChecker(self.student.mClassesTaken, course)
            
            # Check if course is already completed
            completed = (course in self.student.mClassesTaken)
            
            # Set observation value
            observation[i] = 1 if (semester_available and prereqs_met and not completed) else 0
            
            # Add course info to info dictionary
            info['course_info'].append({
                'ID': course['ID'],
                'Hours': course['Hours'],
                'Prerequisites': course['Prerequisites'],
                'Designation': course['Designation']
            })
        
        # Add additional state information
        info['max_semester_credits'] = self.student.mCreditsMax
        info['reqs_progress'] = self.student.mReqsProgress
        
        return observation, info

    def step(self, action):
        # Example action: [1, 0, 1, 0] means the student wants to take courses
        # at index 0 and 2. In this example the catalog is 4 long

        # Initialize list to store the selected courses
        selected_courses = []

        # Loop through the action and catalog to collect the classes selected (those with action[i] == 1)
        for i, take_class in enumerate(action):
            if take_class == 1:  # Student wants to take this class
                selected_courses.append(self.model.mCatalog[i])

        # We update the student with these new courses
        # If we don't met the prereqs the class won't be added
        self.student.update_student(selected_courses, self.semester_count)

        # Update semester count
        self.semester_count += 1

        observation, info = self._get_observation()
        reward = self.semester_count
        graduated = self.student.graduated()
        terminated = graduated or self.semester_count >= self.max_semesters
        truncated = False

        # Call render mode
        self.render()
        
        return observation, reward, terminated, truncated, info

    def render(self):
        """Create a text representation of the current state."""
        if self.render_mode is None:
            return 
        if self.render_mode != "ansi":
            raise ValueError("Only ansi render mode is supported")
            
        # Start building the output with semester details
        output = f"\nSemester: {self.student.mCurrent_semester} (Count: {self.semester_count})\n"
        output += "============================ Available Courses ============================\n"
        output += "Index | Course ID | Course Name               | Prereqs Met    | Semester Available\n"
        output += "------------------------------------------------------------------------------\n"

        # Retrieve observation data
        observation, info = self._get_observation()

        # Loop through each course and add its details to the output
        for i, course in enumerate(self.model.mCatalog):
            prereqs_met = self.student.prereqChecker(self.student.mClassesTaken, course)
            available = (observation[i] == 1)
            completed = (course in self.student.mClassesTaken)
            if completed:
                for c in self.student.mClassesTaken:
                    if c['ID'] == course['ID']:
                        sem_completed = str(c['Taken'] + 1)
            
            status = "Completed " +  sem_completed if completed else ("Available" if available else "Not Available (" + course['Semester'][0]  + ")")
            output += f"{i:5} | {course['ID']:9} | {course['Name'][:25]:25} | {prereqs_met!s:15} | {status}\n"

        # Append completed courses
        output += "\n====================================================================\n"
        output += "Completed Courses: " + ", ".join(self.student.getTakenClassIDs())
        output += "\n====================================================================\n"

        # Build the progress report and graduation requirements
        progress_output = ", ".join(f"{key}: {value}" for key, value in self.student.mReqsProgress.items())
        reqs_output = ", ".join(f"{key}: {value}" for key, value in self.student.mGradReqs.items())
        output += f"Progress Report: {progress_output}"
        output += "\n====================================================================\n"
        output += f"Requisites: {reqs_output}"
        output += "\n====================================================================\n"

        # Print the final output
        print(output)
        return 

    def close(self):
        pass
