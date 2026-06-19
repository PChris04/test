import os
from datetime import datetime
import requests
from bs4 import BeautifulSoup


def fetch_page_title(url: str) -> str:
    """Fetch a webpage and return its title."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.title.string.strip() if soup.title else "No title found"


def main():
    # Print a friendly greeting
    print("Hello! This is a simple Python automation script.")

    # Display the current local time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {current_time}")

    # List files in the current directory
    print("\nFiles in your current folder:")
    for file in os.listdir("."):
        print(f"- {file}")

    # Fetch and display the title of a webpage
    url = "https://example.com"
    print(f"\nFetching page title from: {url}")
    title = fetch_page_title(url)
    print(f"Page Title: {title}")


if __name__ == "__main__":
    main()
