import requests

def fetch_random_hadith():
    api_url = "https://www.thaqalayn-api.net/api/random"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            hadith_data = response.json()
            hadith_text_english = hadith_data["englishText"]
            hadith_text_arabic = hadith_data["arabicText"]
            hadith_book = hadith_data["book"]
            hadith_number = hadith_data["id"]
            return hadith_text_english, hadith_text_arabic, hadith_book, hadith_number
        else:
            print("Failed to fetch Hadith. Response status code:", response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

# Usage example
hadith_english, hadith_arabic, hadith_book, hadith_number = fetch_random_hadith()
if hadith_english and hadith_arabic:
    print("Hadith Number:", hadith_number)
    print("Book:", hadith_book)
    print("English Text:", hadith_english)
    print("Arabic Text:", hadith_arabic)
else:
    print("Failed to fetch Hadith.")