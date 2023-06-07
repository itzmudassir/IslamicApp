import requests

def fetch_random_hadith():
    api_url = "https://www.thaqalayn-api.net/api/random"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            hadith_data = response.json()
            hadith_text = hadith_data["englishText"]
            return hadith_text
        else:
            print("Failed to fetch Hadith. Response status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

# Usage example
hadith = fetch_random_hadith()
if hadith:
    print(hadith)
else:
    print("Failed to fetch Hadith.")
