# Course Catalog Scheduling Environment

This project implements a Gymnasium environment that simulates a university course catalog optimization problem where the goal is to improve student graduation times by adjusting the catalog by changing when courses are offered.

## Environment Description

The environment simulates course scheduling with the following key features:

### State Space
- Binary array indicating which courses can be taken in the current semester
- Each position represents a course, where 1 means the course is available to take and 0 means it's not
- Availability is determined by:
  - Course being offered in current semester
  - Prerequisites being met
  - Course not already taken

### Action Space
- Binary array matching the length of the course catalog
- 1 indicates taking a course, 0 indicates not taking it
- Total credits of selected courses must not exceed the semester credit limit

### Reward System
- Reward is equal to the number of semesters taken to graduate
- Lower rewards (fewer semesters) are better
- Episode terminates when either:
  - Student graduates (meets all requirements)
  - Maximum semester limit is reached

### Graduation Requirements
Students must complete:
- Core Requirements (CR): 9 courses
- Core Electives (CE): 7 courses
- Math Core Requirements (MCR): 3 courses
- Math Core Electives (MCE): 2 courses
- Science Core Requirement (SCR): 1 course
- Electives (E): 9 credits

## Implemented Agents

### Random Agent
- Takes random courses from available options each semester
- Only considers credit limit constraints
- Used as a baseline for performance comparison

### Requirements Agent
- Makes informed decisions based on graduation requirements
- Prioritizes courses that fulfill unfulfilled requirements
- Considers both credit limits and course designations
- Tracks progress toward each graduation requirement category

## Usage

The environment can be run with different configurations:

```python
import gymnasium as gym

# Create environment with custom parameters
env = gym.make('catalog/Catalog-v0',
    render_mode="ansi",  # or "none"
    max_semesters=12,
    max_credits_per_semester=15,
    catalog=custom_catalog  # optional
)

# Run statistical analysis
# --episodes is the times the env will run
# --output is the file it will be saved in (statistical_results.pdf is deafault)
python3 generate_report.py --episodes 100 --output statistical_results.pdf

# Measure performance of current catalog
# Run python3 catalog_runner.py --help to see more options
python3 catalog_runner.py catalog-measure -f <filename w/ json catalog>

# Search for optimal catalog configuration
# Run python3 catalog_runner.py --help to see more options
python3 catalog_runner.py do_catalog_search -f <filename to save catalog>
```

### Measurement and Optimization Tools

The project includes two main tools for analyzing and improving catalog configurations:

#### Catalog Measurement
The `do_catalog_measure` command evaluates the performance of a given catalog configuration:
- Runs multiple episodes with specified agent
- Reports average graduation time and success rates
- Useful for baseline measurements and comparing configurations

#### Catalog Search
The `do_catalog_search` command uses optimization to find improved catalog schedules:
- Iteratively tests different course offering patterns
- Aims to minimize average graduation time
- Saves the best-performing configuration to a JSON file
- Supports different agent types for evaluation

## Statistical Analysis

The project includes tools for generating statistical reports comparing agent performance across different credit load limits. Reports include:
- Average semesters to graduate
- Minimum semesters taken
- Maximum semesters taken
- Total number of simulation runs
The output of this is a pdf file.
