

income_per_state = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total_income = sum(income_per_state.values())

# Calcular e exibir o percentual de cada estado
for state, valor in income_per_state.items():
    percentual = (valor / total_income) * 100
    print(f"{state}: {percentual:.2f}% do total")
