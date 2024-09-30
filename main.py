import json
from datetime import datetime

# File where reflections are stored
DATA_FILE = 'reflections.json'

# Load reflections from the JSON file
def load_data():
    try:
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save reflections to the JSON file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Add a new reflection
def add_reflection():
    date = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    reflection = input("Enter your reflection: ")
    mood = input("Enter your current mood: ")
    tags = input("Add tags (comma separated): ").split(',')

    entry = {
        'date': date,
        'reflection': reflection,
        'mood': mood,
        'tags': [tag.strip() for tag in tags]
    }

    data = load_data()
    data.append(entry)
    save_data(data)
    print("Reflection added successfully!\n")

# View all past reflections
def view_reflections():
    data = load_data()
    if data:
        for entry in data:
            print(f"Date: {entry['date']}")
            print(f"Reflection: {entry['reflection']}")
            print(f"Mood: {entry['mood']}")
            print(f"Tags: {', '.join(entry['tags'])}\n")
    else:
        print("No reflections found.\n")

# Main menu to interact with the tracker
def main_menu():
    while True:
        print("Personal Reflection Tracker")
        print("1. Add Reflection")
        print("2. View Reflections")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_reflection()
        elif choice == '2':
            view_reflections()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the tracker
if __name__ == "__main__":
    main_menu()
