import os
from datetime import datetime

def main():
    # Print a friendly greeting
    print("Hello! This is a simple Python automation script.")
    
    # Display the current local time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {current_time}")
    
    # List files in the current directory
    print("\nFiles in your current folder:")
    for file in os.listdir('.'):
        print(f"- {file}")

if __name__ == "__main__":
    main()
