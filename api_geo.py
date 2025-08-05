import requests
from datetime import date
import csv

def get_coordinates(city):
    try:
        resp = requests.get(
            f"https://geocoding-api.open-meteo.com/v1/search?name={city}",
            timeout=5
        )
        resp.raise_for_status()
        data = resp.json()
        results = data.get("results")
        if results:
            return results[0]["latitude"], results[0]["longitude"]
        else:
            print(f"[WARN] Nie znaleziono miasta: {city}")
    except (requests.ConnectionError, requests.Timeout):
        print(f"[WARN] Błąd sieci dla miasta: {city}")
    except requests.HTTPError as e:
        print(f"[WARN] Błąd HTTP dla miasta {city}: {e}")
    return None, None

def get_weather(lat, lon, city):
    try:
        resp = requests.get(
            f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true",
            timeout=5
        )
        resp.raise_for_status()
        data = resp.json()
        weather = data.get("current_weather")
        if weather:
            return weather["temperature"], weather["windspeed"]
        else:
            print(f"[WARN] Brak danych pogodowych: {city}")
    except (requests.ConnectionError, requests.Timeout):
        print(f"[WARN] Błąd sieci (pogoda) dla miasta: {city}")
    except requests.HTTPError as e:
        print(f"[WARN] Błąd HTTP (pogoda) dla miasta {city}: {e}")
    return None, None

def main():
    input_text = input("Wpisz miasta po przecinku: ")
    miasta = [m.strip() for m in input_text.split(",") if m.strip()]
    if not miasta:
        print("Błąd: Nie podano żadnych poprawnych miast.")
        return

    results = []

    for miasto in miasta:
        lat, lon = get_coordinates(miasto)
        if lat is None or lon is None:
            continue
        temp, wind = get_weather(lat, lon, miasto)
        if temp is None or wind is None:
            continue
        results.append((miasto, temp, wind))

    print(f"{'City':10} | {'Temp [°C]':>9} | {'Wind [km/h]':>11}")
    for city, temp, wind in results:
        print(f"{city:10} | {temp:9.1f} | {wind:11.1f}")

    today = date.today().isoformat()
    filename = f"pogoda_{today}.csv"
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["city", "temperature_c", "wind_kmh"])
        for city, temp, wind in results:
            writer.writerow([city, temp, wind])
    print(f"\nDane zapisane do pliku: {filename}")

if __name__ == "__main__":
    main()
