import requests

clean = []

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


url = "http://www.islamicfinder.us/index.php/api/prayer_times"
params = {
    "country":"PK",
    "zipcode": "54700"
    
}
response = requests.get(url, params=params)
data = response.json()
payares=data["results"]
city=data["settings"]["location"]["city"]
country=data["settings"]["location"]["country"]

url = "https://api.aladhan.com/v1/timingsByCity"
params = {
    "city":city ,
    "country": country,
    "method": 1  # Adjust the method based on calculation preferences
}
response = requests.get(url, params=params)
data = response.json()
prayers = data["data"]['timings']
hijri = data['data']['date']['hijri']['date']

for prayer in prayers:
    clean.append(prayers[prayer])


clean.append(hijri)
clean.append(hadith_number)
clean.append( hadith_book)
clean.append(hadith_english)
clean.append(hadith_arabic)

whole = f"Prayers Timing: \n\nFajr: {clean[0]}\nZuhr: {clean[2]}\nAsr: {clean[3]}\nMaghrib: {clean[5]}\nIsha: {clean[6]}\n\nToday's Date: {clean[11]}\n\nHadith Details: \n\nHadith Number: {clean[12]}\nHadith Book: {clean[13]}\n\nEnglish: {clean[14]}\n\nArabic: {clean[15]}"
print(whole)