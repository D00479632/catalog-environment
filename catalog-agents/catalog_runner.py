#!/usr/bin/env python3

import gymnasium as gym
import json
import argparse
import logging
import sys
import os

import catalog
from catalog import getFullCatalog
from random_agent import RandomAgent
from reqs_agent import RequirementsAgent
import catalog_search

# init env: (self, render_mode=None, max_semesters=12, max_credits_per_semester=15, catalog=CatalogModel.getFullCatalog())
def create_environment(render_mode, max_semesters, max_credits_per_semester, catalog):
    env = gym.make('catalog/Catalog-v0', render_mode=render_mode, max_semesters=max_semesters, max_credits_per_semester=max_credits_per_semester, catalog=catalog)
    if max_semesters:
        env = gym.wrappers.TimeLimit(env, max_episode_steps=max_semesters)

    return env

def destroy_environment(env):
    env.close()
    return

def run_one_episode(env, agent):
    observation, info = env.reset()
    agent.reset()
    terminated = False
    truncated = False
    total_reward = 0
    while not (terminated or truncated):
        action = agent.agent_function((observation, info))
        observation, reward, terminated, truncated, info = env.step(action)
        total_reward = reward
    return total_reward

def run_many_episodes(env, episode_count, agent):
    reward_sum = 0
    for i in range(episode_count):
        reward_sum += run_one_episode(env, agent)
    destroy_environment(env)
    reward = reward_sum / episode_count
    return reward

def run_many_episodes_statistical(env, episode_count, agent):
    rewards = []
    for i in range(episode_count):
        reward = run_one_episode(env, agent)
        rewards.append(reward)
    destroy_environment(env)
    
    # Calculate statistics
    avg_reward = sum(rewards) // len(rewards)
    min_reward = min(rewards)
    max_reward = max(rewards)
    
    return {
        'average_semesters': avg_reward,
        'min_semesters': min_reward,
        'max_semesters': max_reward,
        'total_runs': episode_count
    }

def parse_args(argv):
    parser = argparse.ArgumentParser(prog=argv[0], description='Catalog Search and Execution for AI project')
    parser.add_argument(
            'action', 
            default='catalog-search',
            choices=[ 'catalog-search', 'catalog-measure' ],
            nargs='?', 
            help="desired action"
    )
    parser.add_argument(
        "--episode-count",
        "-c",
        type=int, 
        help="number of episodes to run when measuring",
        default=1
    )
    parser.add_argument(
        "--max-semesters",
        "-s",
        type=int, 
        help="maximum number of semesters taken by student (default: 50)",
        default=50
    )
    parser.add_argument(
        "--logging-level",
        "-l",
        type=str,
        help="logging level: warn, info, debug",
        choices=("warn", "info", "debug"),
        default="warn",
    )
    parser.add_argument(
        "--max-credits-per-semester",
        type=int, 
        help="Maximum number of credits a student can take per semester (default: 15)",
        default=15
    )
    parser.add_argument(
        "--render-mode",
        "-r",
        type=str,
        help="display style (render mode): ansi, none",
        choices=("ansi", "none"),
        default="ansi",
    )
    parser.add_argument(
        "--catalog-file",
        "-f",
        type=str,
        help="file to store/load catalog",
        default="",
    )
    parser.add_argument(
        "--agent",
        "-a",
        type=str,
        choices=["random", "requirements"],
        default="random",
        help="Select which agent to use for measurements"
    )

    my_args = parser.parse_args(argv[1:])
    if my_args.logging_level == "warn":
        my_args.logging_level = logging.WARN
    elif my_args.logging_level == "info":
        my_args.logging_level = logging.INFO
    elif my_args.logging_level == "debug":
        my_args.logging_level = logging.DEBUG

    if my_args.render_mode == "none":
        my_args.render_mode = None

    if my_args.action in ("catalog-search", "catalog-measure"):
        if my_args.catalog_file == "":
            raise Exception("Must specify a catalog file name.")

    return my_args

def load_catalog(my_args):
    if os.path.exists(my_args.catalog_file):
        with open(my_args.catalog_file, "r") as read_file:
            catalog = json.load(read_file)
    else:
        catalog = getFullCatalog()

    return catalog

def save_catalog(my_args, catalog):
    with open(my_args.catalog_file, "w") as write_file:
        json.dump(catalog, write_file, indent=2)
    return

def do_catalog_search(my_args):
    catalog = catalog_search.catalog_search()
    save_catalog(my_args, catalog)
    #print(catalog)
    return

def get_agent(agent_type):
    """Returns the appropriate agent based on the agent type string."""
    agents = {
        "random": RandomAgent,
        "requirements": RequirementsAgent
    }
    if agent_type not in agents:
        raise ValueError(f"Unknown agent type: {agent_type}")
    return agents[agent_type]()

def do_catalog_measure(my_args):
    catalog = load_catalog(my_args)
    agent = get_agent(my_args.agent)
    env = create_environment(my_args.render_mode, my_args.max_semesters, my_args.max_credits_per_semester, catalog)
    reward = run_many_episodes(env, my_args.episode_count, agent)
    print(f"Reward: {reward}")
    return

def do_catalog_statistical_measure(my_args):
    catalog = load_catalog(my_args)
    agent = get_agent(my_args.agent)
    
    # Run with different max credits per semester
    credit_limits = [12, 15, 18, 20]
    results = {}
    
    for credits in credit_limits:
        env = create_environment(
            my_args.render_mode, 
            my_args.max_semesters, 
            credits, 
            catalog
        )
        stats = run_many_episodes_statistical(env, my_args.episode_count, agent)
        results[f'max_credits_{credits}'] = stats
    
    # Print formatted results
    print("\nStatistical Results:")
    print("===================")
    for credits, stats in results.items():
        print(f"\nMax Credits Per Semester: {credits.split('_')[-1]}")
        print(f"Average Semesters to Graduate: {stats['average_semesters']:.2f}")
        print(f"Min Semesters: {stats['min_semesters']}")
        print(f"Max Semesters: {stats['max_semesters']}")
        print(f"Total Runs: {stats['total_runs']}")
    
    return results

def main(argv):
    my_args = parse_args(argv)
    logging.basicConfig(level=my_args.logging_level)

    actions = {
        "catalog-search": do_catalog_search,
        "catalog-measure": do_catalog_measure,
    }
    if my_args.action in actions:
        actions[my_args.action](my_args)
    else:
        raise Exception("{} not in known actions.".format(my_args.action))

    return

if __name__ == "__main__":
    main(sys.argv)
