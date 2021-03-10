from requests import get
from decimal import Decimal
from datetime import datetime


def currency_rates(currency=None):
    if currency:
        currency = currency.upper()
        url = r"http://www.cbr.ru/scripts/XML_daily.asp"
        response = get(url)
        server_answer = response.headers.get("Date").split(" ", maxsplit=4)
        server_date = datetime.strptime(f"{server_answer[2]} {server_answer[1]} {server_answer[3]}", "%b %d %Y")
        content = response.content.decode(encoding=response.encoding)
        curse_dict = {}

        for el in content.split("<CharCode>")[1:]:
            char_code = el.strip()[:3]
            nominal = el.split("<Nominal>")[1][0:5].replace("<", "").replace("/", "").replace("N", "").replace("o", "")
            value = el.split("<Value>")[1][:7]
            curse_dict[char_code] = {"nominal": nominal, "value": value}

        if currency in curse_dict:
            result = Decimal(str(curse_dict.get(currency)["value"]).replace(",", "."))
            price_rub = result / Decimal(curse_dict.get(currency)["nominal"])
            return f"{float(price_rub.quantize(Decimal('1.00')))}, {server_date.date()}"


print(currency_rates("uSd"))
print(currency_rates("EUR"))
