
import json
from places import Place

def main():
    places_file = 'places.json'
    place_objects = []

    try:
        with open(places_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

    except FileNotFoundError:
        print(f"Error: The file '{places_file}' was not found. Make sure it's in the same directory.")
        return
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{places_file}'. Check the file format.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return

    for place_data in data:
        try:
            name = place_data['name']
            description = place_data['description']
            place = Place(name, description)
            place_objects.append(place)
        except KeyError as e:
            print(f"Warning: Missing key {e} in one of the JSON place entries.")
            continue

    print("List of Places:")
    for place in place_objects:
        print(place)

if __name__ == '__main__':
    main()