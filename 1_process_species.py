import csv


def load_data(file_path):
    """
    Load data from a CSV file into a list of dictionaries.
    Each dictionary represents a row in the CSV file.
    """
    data = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def analyze_data(data):
    """
    Perform basic analysis on the loaded data.
    Calculate the total number of sightings for each species.
    """
    species_sightings = {}
    for row in data:
        species = row["Species"]
        if species in species_sightings:
            species_sightings[species] += 1
        else:
            species_sightings[species] = 1
    return species_sightings


def display_results(species_sightings):
    """
    Display the analysis results.
    """
    print("Species Sightings:")
    for species, sightings in species_sightings.items():
        print(f"{species}: {sightings}")


def main():
    # Path to the CSV file containing the data
    file_path = "marine_species_sightings.csv"

    # Load data from the CSV file
    data = load_data(file_path)

    # Analyze the loaded data
    species_sightings = analyze_data(data)

    # Display the analysis results
    display_results(species_sightings)


if __name__ == "__main__":
    main()
