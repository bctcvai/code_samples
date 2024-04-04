def calculate_statistics_v1(species_sightings):
    """
    Calculate mean and median counts
    """
    # Calculate mean
    total_count = sum(species_sightings["Sightings"])
    num_species = len(species_sightings)
    mean_count_poor = total_count / num_species

    # Calculate median 
    sorted_counts = sorted(species_sightings["Sightings"])
    if num_species % 2 == 0:
        median_count_poor = (
            sorted_counts[num_species // 2 - 1] + sorted_counts[num_species // 2]
        ) / 2
    else:
        median_count_poor = sorted_counts[num_species // 2]

    return mean_count_poor, median_count_poor


import pandas as pd


def calculate_statistics(species_sightings):
    """
    Calculate basic statistics on species counts.
    """
    # Calculate mean, median, minimum, and maximum
    mean_count = species_sightings["Sightings"].mean()
    median_count = species_sightings["Sightings"].median()
    min_count = species_sightings["Sightings"].min()
    max_count = species_sightings["Sightings"].max()

    # Additional statistics calculations can be added here

    return mean_count, median_count, min_count, max_count
