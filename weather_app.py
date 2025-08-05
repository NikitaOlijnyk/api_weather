import random

result = []

def generuj_prognoze(list_city):
    str_ = f"Miasto: {list_city[0]}, Temperatura: {list_city[1]}°C, Warunki: {list_city[2]}"
    result.append(list_city)
    print(str_)

def pokaz_prognozy(command):
    return command.lower() in ['list', 'pogodyyyy', 'l']

def analiza_prognozy(command):
    return command.lower() in ['analiz', 'aaaa', 'a']

def zapisz_raport():
    with open("raport.txt", "w", encoding="utf-8") as f:
        f.write("Raport pogodowy\n")
        f.write("-----------------------------\n")
        for prognoza in result:
            f.write(f"Miasto: {prognoza[0]}, Temperatura: {prognoza[1]}°C, Warunki: {prognoza[2]}\n")

        if result:
            temp_sum = sum([i[1] for i in result])
            temp_avg = temp_sum / len(result)
            highest = max(result, key=lambda x: x[1])
            lowest = min(result, key=lambda x: x[1])

            f.write("\nPodsumowanie analizy:\n")
            f.write(f"Średnia temperatura: {temp_avg:.2f}°C\n")
            f.write(f"Najwyższa temperatura: {highest[1]}°C w mieście {highest[0]}\n")
            f.write(f"Najniższa temperatura: {lowest[1]}°C w mieście {lowest[0]}\n")
        else:
            f.write("\nBrak danych do analizy.\n")

while True:
    temperatura = random.randint(-10, 35)
    weather = random.choice(["Słonecznie", "Deszczowo", "Zachmurzenie"])
    city = input("Wpisz miasto (lub 'list', 'analiz', 'zapisz' aby wywołać opcje): ")

    if pokaz_prognozy(city):
        for prognoza in result:
            print(f"Miasto: {prognoza[0]}, Temp: {prognoza[1]}°C, Warunki: {prognoza[2]}")
    elif analiza_prognozy(city):
        if not result:
            print("Brak danych do analizy.")
            continue
        temp_sum = sum([i[1] for i in result])
        temp_avg = temp_sum / len(result)

        highest = max(result, key=lambda x: x[1])
        lowest = min(result, key=lambda x: x[1])

        print(f"Średnia temperatura: {temp_avg:.2f}°C")
        print(f"Najwyższa temperatura: {highest[1]}°C w mieście {highest[0]}")
        print(f"Najniższa temperatura: {lowest[1]}°C w mieście {lowest[0]}")
    elif city.lower() in ['zapisz', 'z']:
        zapisz_raport()
        print("Raport zapisany do pliku raport.txt")
    else:
        generuj_prognoze([city, temperatura, weather])