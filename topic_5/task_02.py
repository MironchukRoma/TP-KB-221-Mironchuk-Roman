import http.client
import json

def отримати_курс_валюти(код_валюти):
    try:
        conn = http.client.HTTPSConnection("bank.gov.ua")
        conn.request("GET", f"/NBUStatService/v1/statdirectory/exchange?valcode={код_валюти}&json")
        response = conn.getresponse()
        дані = json.loads(response.read().decode("utf-8"))
        return дані[0]["rate"] if isinstance(дані, list) and дані else None
    except Exception as е:
        print(f"Помилка при отриманні курсу валюти: {е}")
        return None

while True:
    try:
        сума = float(input("Введіть суму в гривнях: "))
        if сума <= 0:
            print("Помилка: Сума повинна бути більше нуля.")
            continue

        код_валюти = input("Введіть валюту для конвертації (EUR, USD, AED): ").upper()

        if код_валюти not in ["EUR", "USD", "AED"]:
            print("Помилка: Код валюти введений невірно або дана валюта не підтримується. Спробуйте ще раз.")
            continue

        курс = отримати_курс_валюти(код_валюти)

        if курс is not None:
            конвертована_сума = сума / курс
            print(f"{сума} UAH = {конвертована_сума:.2f} {код_валюти}")
        else:
            print("Спробуйте ще раз.")
    except ValueError:
        print("Помилка: Введіть коректне число.")
