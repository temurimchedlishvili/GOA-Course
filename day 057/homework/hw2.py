# ვაგროვებთ მომხმარებლის 5 საყვარელ ხილს
fruits = []
for i in range(5):
    fruit = input(f"{i+1}) შეიყვანე საყვარელი ხილი: ")
    fruits.append(fruit)

# ვამატებთ 2 დამატებით ხილს
fruits.append("ბანანი")
fruits.append("ანანასი")

# ვშლით ბოლო ელემენტს
fruits.pop()

# ვბეჭდავთ თავდაპირველ სიას
print("საწყისი სია:", fruits)

# ვბეჭდავთ ალფავიტურად დალაგებულს
print("ალფავიტური სორტირება:", sorted(fruits))
