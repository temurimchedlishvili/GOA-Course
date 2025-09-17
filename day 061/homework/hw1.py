import random

def words():
    word_list = ["hello", "world", "how", "coffee", "tea"]
    word = random.choice(word_list)

    guessed_word = ["_" for _ in word]  # საიდუმლო სიტყვა დაფარული
    right_word = set()
    hearts = 6

    print("გამოცნობილი სიტყვა:", " ".join(guessed_word))

    while hearts > 0:
        game = input("შემოიტანეთ ასო: ").lower()

        # უკვე შეყვანილი ასო
        if game in right_word:
            print("ეს ასო უკვე სცადე.")
            continue

        right_word.add(game)

        if game in word:
            print("სწორია ✅")
            # განვაახლებთ guessed_word
            for i, ch in enumerate(word):
                if ch == game:
                    guessed_word[i] = game
        else:
            hearts -= 1
            print("არასწორია ❌ | დაგრჩა", hearts, "გული")

        print(" ".join(guessed_word))

        # თუ ყველა ასო გამოიცნო
        if "_" not in guessed_word:
            print("გილოცავ 🎉! სიტყვა იყო:", word)
            break
    else:
        print("თამაში დამთავრდა. სიტყვა იყო:", word)

# თამაშის გაშვება
words()
