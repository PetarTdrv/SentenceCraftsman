import random

names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "wears"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slow", "hard", "warm", "sad", "fast"]
details = ["near the river", "at home", "in the park"]

print("Hello, this is your first random sentence:")

while True:
    random_names = random.choice(names)
    random_places = random.choice(places)
    random_verbs = random.choice(verbs)
    random_nouns = random.choice(nouns)
    random_adverbs = random.choice(adverbs)
    random_details = random.choice(details)

    print(f"{random_names} from {random_places} {random_adverbs} {random_verbs} {random_nouns}")
    input("Click [Enter] to generate a new one.")