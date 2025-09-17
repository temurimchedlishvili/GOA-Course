# მომხმარებელი შეიყვანს 3 ქვეყანას
countries = []
for i in range(3):
    country = input(f"შეიყვანე ქვეყანა {i+1}: ")
    countries.append(country)

# ვქმნით dictionary-ს (ქვეყანა: დედაქალაქი)
capitals = {
    countries[0]: "თბილისი",
    countries[1]: "ბერლინი",
    countries[2]: "პარიზი"
}

# ვბეჭდავთ ყველა ქვეყანას და დედაქალაქს
print("\nქვეყნები და დედაქალაქები:")
for country, capital in capitals.items():
    print(f"{country} → {capital}")

# მომხმარებელს ეკითხება ქვეყანა
search = input("\nშეიყვანე ქვეყნის სახელი: ")

if search in capitals:
    print(f"{search}-ის დედაქალაქია {capitals[search]}")
else:
    print("Country not found")
