import requests
import random

# Function to fetch a random hadith from any book
def fetch_random_hadith():
    # Dictionary of available collections with their corresponding book names
    collections = {
        "eng-abudawud": "Sunan Abi Dawood",
        "eng-bukhari": "Sahih al-Bukhari",
        "eng-ibnmajah": "Sunan Ibn Majah",
        "eng-malik": "Muwatta Malik",
        "eng-muslim": "Sahih Muslim",
        "eng-nasai": "Sunan an-Nasa'i",
        "eng-tirmidhi": "Jami` at-Tirmidhi",
        # Add more collection names and book names as desired
    }

    # Select a random collection from the dictionary
    collection_name = random.choice(list(collections.keys()))
    book_name = collections[collection_name]

    # API base URL
    base_url = "https://cdn.jsdelivr.net/gh/fawazahmed0/hadith-api@1/editions/"

    # Construct the URL for the specific collection
    collection_url = f"{base_url}{collection_name}.json"

    try:
        # Send a GET request to fetch the collection data
        response = requests.get(collection_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the response JSON
            collection_data = response.json()

            # Get the total number of hadiths in the collection
            total_hadiths = len(collection_data["hadiths"])

            # Generate a random hadith number
            hadith_number = random.randint(1, total_hadiths)

            # Fetch the random hadith
            hadith = collection_data["hadiths"][hadith_number]

            # Return the book name and hadith text
            return book_name, hadith["text"]
        else:
            print(f"Failed to fetch hadith. Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
book_name, random_hadith = fetch_random_hadith()

# Print the fetched random hadith and book name
print(f"Book: {book_name}")
print(f"Random Hadith: {random_hadith}")
