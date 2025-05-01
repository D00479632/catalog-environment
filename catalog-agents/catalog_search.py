#!/usr/bin/env python3

import gymnasium as gym
import catalog
from catalog import CatalogModel
from catalog import Student
import random
import time

def HillClimbing(model, n_students):
    """
    Find catalog with largest obtainable utility function value.
    Starting from current catalog, evaluate neighbors and move to better ones.
    """
    current_catalog = model.mCatalog
    current_utility = model.UTILITY(current_catalog, n_students)
    
    while True:
        current_neighbor = None

        # Get all neighboring catalogs (different semester arrangements)
        for neighbor in model.NEIGHBORS(current_catalog):
            neighbor_utility = model.UTILITY(neighbor, n_students)
            #print(f'neighbor utility {neighbor_utility}')
            if neighbor_utility < current_utility:  # Using < because utility is number of semesters (lower is better)
                #print('new best utility')
                current_utility = neighbor_utility
                current_neighbor = neighbor

        # If no better neighbor found, we've reached a local maximum
        if current_neighbor is None:
            break
            
        current_catalog = current_neighbor

    return current_catalog

def RandomRestartHillClimbing(model, num_restarts=5, n_students=10):
    """
    Repeatedly execute HillClimbing() with different random catalog arrangements.
    
    Args:
        model: CatalogModel instance
        num_restarts: Number of random restarts to perform
    """
    best_catalog = model.mCatalog
    best_utility = model.UTILITY(best_catalog, n_students)

    for _ in range(num_restarts):
        # Get a random catalog as starting point
        model.mCatalog = model.RANDOM()
        
        # Run hill climbing from this random start
        peak_catalog = HillClimbing(model, n_students)
        peak_utility = model.UTILITY(peak_catalog, n_students)
        
        # Update best if this peak is better
        if peak_utility < best_utility:  # Lower is better (fewer semesters)
            best_catalog = peak_catalog
            best_utility = peak_utility

    return best_catalog

def catalog_search():
    """Main function to find optimal catalog arrangement."""
    start_time = time.time()
    
    n_students = 100
    # Since we are not passing any catalog it will use the function getFullCatalog()
    model = CatalogModel()
    
    # Run random-restart hill climbing to find best catalog
    best_catalog = RandomRestartHillClimbing(model, 50, n_students)
    
    # Print final utility (average semesters to graduate)
    final_utility = model.UTILITY(best_catalog, n_students)
    
    # Calculate and print elapsed time
    elapsed_time = time.time() - start_time
    print(f'Execution time: {elapsed_time:.2f} seconds with {n_students} students.')
    print(f'Average semesters to graduate: {final_utility:.2f}')
    print(f'Best catalog arrangement found.')
    
    return best_catalog
