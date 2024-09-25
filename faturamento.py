

import json

with open('dados.json', 'r') as arquivo_json:
    income_data = json.load(arquivo_json)

income_valid = [day["faturamento"] for day in income_data["dias"] if day["faturamento"] > 0]

minor_income = min(income_valid)
most_income = max(income_valid)
media_income = sum(income_valid) / len(income_valid)
above_media = len([day for day in income_valid if day > media_income])

print(f"Menor faturamento: R$ {minor_income:.2f}")
print(f"Maior faturamento: R$ {most_income:.2f}")
print(f"Dias com faturamento acima da média: {above_media}")
