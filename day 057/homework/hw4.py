students = {
    "Ana": 95,
    "Giorgi": 88,
    "Luka": 76
}

# ვბეჭდავთ სტუდენტებს, ვისაც >=90 ქულა აქვს
print("სტუდენტები >=90 ქულით:")
for name, score in students.items():
    if score >= 90:
        print(f"{name}: {score}")

# ვამატებთ ახალ სტუდენტს update()-ით
students.update({"Nino": 100})

# საბოლოო dictionary
print("საბოლოო students:", students)
