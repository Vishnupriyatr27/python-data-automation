import csv
from validator import validate_record
from database import insert_record

def process_file(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            name = row['name']
            age = int(row['age'])
            email = row['email']
            
            if validate_record(name, age, email):
                insert_record(name, age, email)
            else:
                print(f"Invalid record skipped: {row}")
