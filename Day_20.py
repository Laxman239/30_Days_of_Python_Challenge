import requests

def fetch_webpage(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        print("✅ Webpage content fetched successfully!\n")
        print(response.text[:1000])  # Displaying only the first 1000 characters
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching the webpage: {e}")

# Example usage
fetch_webpage("https://www.python.org")
