from database import create_table
from processor import process_file

def main():
    print("Starting Data Processing...")
    
    create_table()
    process_file("sample_data.csv")
    
    print("Data processing completed!")

if __name__ == "__main__":
    main()
