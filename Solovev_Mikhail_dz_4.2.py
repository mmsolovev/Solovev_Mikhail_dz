import requests
from decimal import *


def currency_rates(name):
    name = name.upper()
    value_text = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text

    if name not in value_text:
        return None
    else:
        rubles = value_text[value_text.find('<Value>', value_text.find(name)) + 7:value_text.find('</Value>', value_text.find(name))]
        new_list = rubles.split(',')

    return Decimal('.'.join(new_list))


print(currency_rates('usd'))
print(currency_rates('eur'))
print(currency_rates('EUR'))