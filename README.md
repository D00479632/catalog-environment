# Course Catalog Optimizer

This project implements a gymnasium environment for optimizing a university course catalog schedule to minimize the average time to graduation for students. It demonstrates the classical search hill climbing algorithm to find optimal semester arrangements for courses.

## Overview

The environment simulates students taking courses according to prerequisite requirements and semester availability constraints. The goal is to find the best arrangement of when courses are offered (Fall vs Spring) to minimize the number of semesters students need to graduate.

The project consists of two main components:
1. A gymnasium environment (`catalog/`) that simulates student progression through courses
2. Demo agents (`catalog-agents/`) that showcase different approaches to optimizing the catalog

## Environment Details

The environment is defined in `catalog/catalog/envs/` and includes:
- `catalog_model.py`: Core logic for course prerequisites, graduation requirements, and student simulation
- State representation of available courses and taken courses
- Actions to select courses for a semester within credit limits
- Reward based on number of semesters to graduate

### Key Features
- Realistic course prerequisites and co-requisites
- Multiple degree requirement categories (Core required, Electives, Math, Science)
- Semester-specific course availability
- Credit hour limitations per semester

## Agents

The project includes several demo agents in `catalog-agents/`:

### Random Agent (`random_agent.py`)
- Randomly selects available courses each semester
- Respects credit hour limits and prerequisites
- Baseline for comparison

### Requirements Agent (`reqs_agent.py`)
- Prioritizes courses based on graduation requirements
- Tracks progress toward different requirement categories
- More strategic selection than random agent

### Catalog Search (`catalog_search.py`)
- Implements hill climbing with random restarts
- Optimizes semester assignments for courses
- Aims to minimize average graduation time across many simulated students

## Usage

To install the environment use the `Makefile` in that directory to install the module in your local pip.

To run the catalog optimization:
Inside the catalog-agents directory
`python3 catalog_runner.py catalog-search -f output_catalog.json` you can also `python3 catalog_runner.py -h` to see more options.

To measure performance with different agents:
Inside the catalog-agents directory
`python3 catalog_runner.py catalog-measure -f catalog.json -a requirements` you can also `python3 catalog_runner.py -h` to see more options.

## Requirements
- Python 3.8+
- gymnasium

## Project Structure
catalog/
├── catalog/
│   └── envs/
│       ├── catalog_env.py
│       └── catalog_model.py
└── setup.py
catalog-agents/
├── catalog_runner.py
├── catalog_search.py
├── random_agent.py
└── reqs_agent.py