import os

# Get the current directory
current_directory = os.getcwd()

# Specify the folder name containing the text files
folder_name = "dataset"

# Combine current directory and folder name
folder_path = os.path.join(current_directory, folder_name)

database = []

# Function to parse each line in a file and extract the data
def parse_line(line):
    parts = line.strip().split(',')
    if len(parts) == 4:
        try:
            entry = {
                'id': int(parts[0]),
                'date_time': parts[1],
                'longitude': float(parts[2]),
                'latitude': float(parts[3])
            }
            return entry
        except ValueError:
            print("Error parsing line:", line)
    else:
        print("Invalid line format:", line)

# Function to read entries from a file and append them to the database
def read_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            entry = parse_line(line)
            if entry:
                database.append(entry)

# Function to recursively traverse the folder and read files
def traverse_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                read_file(file_path)

# Start traversing the folder
traverse_folder(folder_path)

# Now 'database' contains all entries from all files

# Write the contents of the database to a new text file
n=0
output_file_path = os.path.join(current_directory, "output_database.txt")
with open(output_file_path, 'w') as output_file:
    for entry in database:
       
        output_file.write(f"{entry['id']},{entry['date_time']},{entry['longitude']},{entry['latitude']}\n")
output_file_path = os.path.join(current_directory, "released_database.txt")
with open(output_file_path, 'w') as output_file:
    for entry in database:
       if(entry['id']<150):
         output_file.write(f"{entry['id']},{entry['date_time']},{entry['longitude']},{entry['latitude']}\n")
         n+=1

print("Output written to:", output_file_path)
# Function to append ", 1" at the end of each line in a file
def append_to_each_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            line = line.strip() + ",1\n"
            file.write(line)

# Call the function to append ", 1" to each line in the file
append_to_each_line("released_database.txt")
