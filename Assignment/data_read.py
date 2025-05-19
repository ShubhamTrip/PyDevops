import json

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        
            name = data.get("name", "N/A")
            age = data.get("age", "N/A")
            skills = data.get("skills", [])

            print("Extracted Information:")
            print(f"Name   : {name}")
            print(f"Age    : {age}")
            print("Skills :")
            for skill in skills:
                print(f"  - {skill}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"Error: File '{filename}' is not a valid JSON file.")

if __name__ == "__main__":
    read_json_file("data.json")
