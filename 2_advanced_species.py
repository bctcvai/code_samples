import argparse
import pandas as pd
import plotly.express as px


def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.
    """
    data = pd.read_csv(file_path)
    return data


def analyze_data(data):
    """
    Perform basic analysis on the loaded data.
    Calculate the total number of sightings for each species.
    """
    species_sightings = data["Species"].value_counts().reset_index()
    species_sightings.columns = ["Species", "Sightings"]
    return species_sightings


def display_results(species_sightings):
    """
    Display the analysis results.
    """
    print("Species Sightings:")
    print(species_sightings)


def plot_results(species_sightings):
    """
    Generate a bar plot of the species sightings.
    """
    fig = px.bar(
        species_sightings, x="Species", y="Sightings", title="Species Sightings"
    )
    fig.show()


def main():
    parser = argparse.ArgumentParser(description="Analyze marine species sightings.")
    parser.add_argument(
        "file_path", type=str, help="Path to the CSV file containing the data"
    )
    parser.add_argument(
        "--plot", action="store_true", help="Generate a plot of the species sightings"
    )
    args = parser.parse_args()

    # Load data from the CSV file
    data = load_data(args.file_path)

    # Analyze the loaded data
    species_sightings = analyze_data(data)

    # Display the analysis results
    display_results(species_sightings)

    # Generate a plot if requested
    if args.plot:
        plot_results(species_sightings)


if __name__ == "__main__":
    main()
