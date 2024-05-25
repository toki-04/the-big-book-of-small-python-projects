import random

#Set up the constants:
OBJECT_PRONOUNS: list[str] = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS: list[str] = ['Her', 'His', 'Their']
ONAL_PRONOUNS: list[str] = ['She', 'He', 'They']

STATES: list[str] = [
    'California', 'Texas', 'Florida', 'New York',
    'Pennsylvania', 'Illinois', 'Ohio', 'Georgia',
    'North Carolina', 'Michigan'
]

NOUNS: list[str] = [
    'Athlete', 'Clown', 'Shovel',
    'Paleo Diet', 'Doctor', 'Parent',
    'Cat', 'Dog', 'Chicken', 'Robot',
    'Video Game', 'Avocado', 'Plastic Straw',
    'Serial Killer', 'Telephone Psychic'
]

PLACES: list [str] = [
    'House', 'Attic', 'Bank Deposit Box',
    'School', 'Basement', 'Workplace',
    'Donut Shop', 'Apocalypse Bunker'
]

WHEN: list[str] = [
    'Soon', 'This Year', 'Later Today',
    'RIGHT NOW', 'Next Week'
]

def main() -> None:
    print("Clickbait Headline Generator")
    print('By Al Sweigart al@inventwithpython.com')
    print()

    print("Our website needs to trick people into looking at ads!")
    while True:
        print("Enter the number of clickbait headilnes to generate:")
        response: str = input("> ")

        if not response.isdecimal():
            print("Please enter a number.")
        else:
            number_of_headlines = int(response)
            break

    for i in range(number_of_headlines):
        click_bait_type = random.randint(1, 8)

        if click_bait_type == 1:
            headline = generate_are_millenials_killing_headline()
        elif click_bait_type == 2:
            headline = generate_what_you_dont_know_headline()
        elif click_bait_type == 3:
            headline = generate_big_companies_hate_her_headline()
        elif click_bait_type == 4:
            headline = generate_you_wont_believe_headline()
        elif click_bait_type == 5:
            headline = generate_dont_want_you_to_know_headline()
        elif click_bait_type == 6:
            headline = generate_gift_idea_headline()
        elif click_bait_type == 7:
            headline = generate_reason_why_headline()
        elif click_bait_type == 8:
            headline = generate_job_automated_headline()

        print(headline)
    print()

    website: str = random.choice([
        "wobsite", "blag", "Facebuuk", "Googles",
        "Facesbook", "Tweedie", "Pastagram",
    ])

    when: str = random.choice(WHEN).lower()
    print(f"Post these to our {website} {when} or you're fired!")

# Each of these functions returns a different type of headline
def generate_are_millenials_killing_headline() -> str:
    noun: str = random.choice(NOUNS)
    return f"Are Millenials Killing the {noun} Industry?"

def generate_what_you_dont_know_headline() -> str:
    noun: str = random.choice(NOUNS)
    plural_noun: str = random.choice(NOUNS) + "s"
    when: str = random.choice(WHEN)
    return f"Without This {noun}, {plural_noun} Could Kill You {when}"

def generate_big_companies_hate_her_headline() -> str:
    pronoun: str = random.choice(OBJECT_PRONOUNS)
    state: str = random.choice(STATES)
    noun_1: str = random.choice(NOUNS)
    noun_2: str = random.choice(NOUNS)
    return f"Big Companies Hate {pronoun}! See How This {state} {noun_1} Invented a Cheaper {noun_2}."

def generate_you_wont_believe_headline() -> str:
    state: str = random.choice(STATES)
    noun: str = random.choice(NOUNS)
    pronoun: str = random.choice(POSSESIVE_PRONOUNS)
    place: str = random.choice(PLACES)
    return f"You won't Believe What This {state} {noun} Found in {pronoun} {place}."

def generate_dont_want_you_to_know_headline() -> str:
    plural_noun_1 = random.choice(NOUNS) + "s"
    plural_noun_2 = random.choice(NOUNS) + "s"
    return f"What {plural_noun_1} Don't Want You To Know About {plural_noun_2}."


def generate_gift_idea_headline() -> str:
    number: int = random.randint(7, 15)
    noun: str = random.choice(NOUNS)
    state: str = random.choice(STATES)
    return f"{number} Git Ideas to Give Your {noun} From {state}"

def generate_reason_why_headline() -> str:
    number_1: int = random.randint(3, 19)
    plural_noun: str = random.choice(NOUNS) + "s"
    # number 2 should not be larger than number_1:
    number_2: int = random.randint(1, number_1)
    return f"{number_1} Reasons Why {plural_noun} Are More Interesting Than You Think (Number {number_2} Will Surprise You!)"

def generate_job_automated_headline() -> str:
    state: str = random.choice(STATES)
    noun: str = random.choice(NOUNS)

    i: int = random.randint(0, 2)
    pronoun_1: str = POSSESIVE_PRONOUNS[i]
    pronoun_2: str = POSSESIVE_PRONOUNS[i]

    if pronoun_1 == "Their":
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun_1} Job. {pronoun_2} Were Wrong."
    else:
        return f"This {state} {noun} Didn't Think Robots Would Take {pronoun_1} Job. {pronoun_2} Was Wrong."


if __name__ == "__main__":
    main()

























