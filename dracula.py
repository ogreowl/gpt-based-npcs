import openai
import time

openai.api_key = "Insert Openai API Key"
wait = 2
talking_to_dracula_control = False;
talking_to_dracula_v1 = False;
talking_to_dracula_v2 = False;
talking_to_dracula_v3 = False;
talking_to_dracula_v4 = False;
talking_to_dracula_v5 = False;
talking_to_dracula_v6 = False;

dracula_prompts = {
    "background" : """
    You are acting as an NPC for Dracula, the vampire. 
    In this game, you are disguised as merchant in the city of Riverdale; Riverdale is a small town located between some beautiful mountains that is home to both orcs and humans; there are some wizards who study there; the political system is corrupted from the influence of gangs; the city occasionally sees dragons fly nearby. 
    You do not want people to know that you are a vampire, though occasionally, you may accidentally give away information that implies
    that you are. 
    Be subtle and clever in your responses. Do your best to create an immersive experience for the player. 
    """,
    "where_from" : "A traveler asks ‘where are you from?’ Generate 1-3 sentences of dialogue in response:",
    "selling_anything": "A traveler asks ‘are you selling anything?’ In this game, you are selling potions & scrolls. Generate 1-3 sentences of dialogue in response:",
    "tell_me_more": "A traveler asks 'where you are from.' You say: {statement} He then asks 'tell me more about your homeland.' Generate 1-3 sentences of dialogue in response:",
    "seen_dragons": "A traveler asks 'where you are from.' You say: {statement} He then asks 'Have you seen any dragons there?' Generate 1-3 sentences of dialogue in response:",
    "buy_scrolls": "A traveler asks 'are selling anything.' You say: {statement} He then asks 'Can I buy some scrolls?' Generate 1-3 sentences of dialogue in response:",
    "buy_potions": "A traveler asks 'are selling anything.' You say: {statement} He then asks 'Can I buy some potions?' Generate 1-3 sentences of dialogue in response:",
    "nevermind": "A traveler asks 'are selling anything.' You say: {statement} He then says 'Nevermind?' Generate 1-3 sentences of dialogue in response:",
}

def dracula_v1(prompt):

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=dracula_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message
def dracula_v2(prompt):

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=dracula_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.1,
    )

    message = response.choices[0].text.strip()
    return message
def dracula_v3(prompt):

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=dracula_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=.9,
    )

    message = response.choices[0].text.strip()
    return message
def dracula_v4(prompt):

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=dracula_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message
def dracula_v5(prompt):

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=dracula_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.1,
    )

    message = response.choices[0].text.strip()
    return message
def dracula_v6(prompt):
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=dracula_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=.9,
    )

    message = response.choices[0].text.strip()
    return message

print("""

--

Hello user! In this program, you can interact with 1 of 7 different 
versions of Dracula, the quintessential vampire that exists across many different lores. 
The purpose of this program is to illustrate how prompt-engineering gpt prompts within 
dialogue trees can be used to create immersive experiences with NPCs. 

Here are the 7 different versions of Dracula you can have the chance to talk to:

--

Dracula Control: 
This is a verison of dracula made to respond using a standard, non-AI-enhanced dialogue tree. 
All of this responses are pre-written, and they do not change every time you talk to him.

--

Dracula Version 1:
Model: text-davinci-002
Temperature: 0.5
Prompts: Complex

Dracula Version 2:
Model: text-davinci-002
Temperature: 0.1
Prompts: Complex

Dracula Version 3:
Model: text-davinci-002
Temperature: 0.9
Prompts: Complex

--

Dracula Version 4:
Model: text-davinci-003
Temperature: 0.5
Prompts: Complex

Dracula Version 5:
Model: text-davinci-003
Temperature: 0.1
Prompts: Complex

Dracula Version 6:
Model: text-davinci-003
Temperature: 0.9
Prompts: Complex

""")

choice = input("Which version of Dracula would you like to talk to? control, 1, 2, 3, 4, 5 or 6?")

if choice == "control":
    talking_to_dracula_control = True;
elif choice == "1":
    talking_to_dracula_v1 = True;
elif choice == "2":
    talking_to_dracula_v2 = True;
elif choice == "3":
    talking_to_dracula_v3 = True;
elif choice == "4":
    talking_to_dracula_v4 = True;
elif choice == "5":
    talking_to_dracula_v5 = True;
elif choice == "6":
    talking_to_dracula_v5 = True;

while talking_to_dracula_control:
    time.sleep(wait)
    print("You approach the vampire Dracula. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        time.sleep(wait)
        print("Dracula: I hail from the ancient land of Transylvania. I am a creature of the night, a vampire, bound by darkness.")
        time.sleep(wait)
        print("1: Tell me more about Transylvania.")
        print("2: Have you encountered any other supernatural creatures during your time?")
        choice = input("Choose your input:")
        time.sleep(wait)
        if choice == "1":
            print("Dracula: Transylvania is a region in present-day Romania, known for its dark and mysterious forests, as well as its ancient castles. It is a land steeped in folklore and legends.")
        elif choice == "2":
            print("Dracula: Over the centuries, I have encountered many supernatural beings, such as werewolves, witches, and other vampires.")

    elif choice == "2":
        print("Dracula: I have no material possessions to sell, but I can offer you knowledge of the dark arts and the secrets of immortality.")
        time.sleep(wait)
        print("1: Tell me about the dark arts.")
        print("2: How can I become immortal like you?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        time.sleep(wait)
        if choice == "1":
            print("Dracula: The dark arts are a collection of forbidden knowledge and practices, often involving the manipulation of life and death, as well as the summoning of otherworldly powers.")
        elif choice == "2":
            print("Dracula: Immortality comes at a great cost. One must be willing to embrace the darkness and forsake their humanity, becoming a vampire like myself.")
        elif choice == "3":
            print("Dracula: Very well, let me know if you need anything else.")

    time.sleep(1)

    print("Dracula: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_dracula_control = False

while talking_to_dracula_v1:

    print("You approach a mysterious merchant. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = dracula_v1(dracula_prompts["where_from"])
        print("Mysterious Merchant: " + statement)
        time.sleep(wait)
        print("1: Tell me more about your homeland.")
        print("2: Have you seen any dragons?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement = dracula_v1(dracula_prompts["tell_me_more"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)
        elif choice == "2":
            newStatement = dracula_v1(dracula_prompts["seen_dragons"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)

    elif choice == "2":
        statement = dracula_v1(dracula_prompts["selling_anything"])
        print("Mysterious Merchant: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement = dracula_v1(dracula_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement = dracula_v1( dracula_prompts["buy_potions"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)
        elif choice == "3":
            newStatement = dracula_v1(dracula_prompts["nevermind"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)

    time.sleep(1)

    print("Mysterious Merchant: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_dracula_v1 = False
        
while talking_to_dracula_v2:
    print("You approach a mysterious merchant. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = dracula_v2(dracula_prompts["where_from"])
        print("Mysterious Merchant: " + statement)
        time.sleep(wait)
        print("1: Tell me more about your homeland.")
        print("2: Have you seen any dragons?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  dracula_v2(dracula_prompts["tell_me_more"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)
        elif choice == "2":
            newStatement =  dracula_v2(dracula_prompts["seen_dragons"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)

    elif choice == "2":
        statement =  dracula_v2(dracula_prompts["selling_anything"])
        print("Mysterious Merchant: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  dracula_v2(dracula_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  dracula_v2(dracula_prompts["buy_potions"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)
        elif choice == "3":
            newStatement =  dracula_v2(dracula_prompts["nevermind"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)

    time.sleep(1)

    print("Mysterious Merchant: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_dracula_v2 = False

while talking_to_dracula_v3:
    print("You approach a mysterious merchant. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = dracula_v3(dracula_prompts["where_from"])
        print("Mysterious Merchant: " + statement)
        time.sleep(wait)
        print("1: Tell me more about your homeland.")
        print("2: Have you seen any dragons?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  dracula_v3(dracula_prompts["tell_me_more"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)
        elif choice == "2":
            newStatement =  dracula_v3(dracula_prompts["seen_dragons"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)

    elif choice == "2":
        statement =  dracula_v3(dracula_prompts["selling_anything"])
        print("Mysterious Merchant: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  dracula_v3(dracula_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  dracula_v3(dracula_prompts["buy_potions"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)
        elif choice == "3":
            newStatement =  dracula_v3(dracula_prompts["nevermind"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)

    time.sleep(1)

    print("Mysterious Merchant: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_dracula_v3 = False

while talking_to_dracula_v4:
    print("You approach a mysterious merchant. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = dracula_v4(dracula_prompts["where_from"])
        print("Mysterious Merchant: " + statement)
        time.sleep(wait)
        print("1: Tell me more about your homeland.")
        print("2: Have you seen any dragons?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  dracula_v4(dracula_prompts["tell_me_more"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)
        elif choice == "2":
            newStatement =  dracula_v4(dracula_prompts["seen_dragons"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)

    elif choice == "2":
        statement =  dracula_v4(dracula_prompts["selling_anything"])
        print("Mysterious Merchant: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  dracula_v4(dracula_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  dracula_v4(dracula_prompts["buy_potions"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)
        elif choice == "3":
            newStatement =  dracula_v4(dracula_prompts["nevermind"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)

    time.sleep(1)

    print("Mysterious Merchant: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_dracula_v4 = False

while talking_to_dracula_v5:
    print("You approach a mysterious merchant. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = dracula_v5(dracula_prompts["where_from"])
        print("Mysterious Merchant: " + statement)
        time.sleep(wait)
        print("1: Tell me more about your homeland.")
        print("2: Have you seen any dragons?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  dracula_v5(dracula_prompts["tell_me_more"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)
        elif choice == "2":
            newStatement =  dracula_v5(dracula_prompts["seen_dragons"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)

    elif choice == "2":
        statement =  dracula_v5(dracula_prompts["selling_anything"])
        print("Mysterious Merchant: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  dracula_v5(dracula_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  dracula_v5(dracula_prompts["buy_potions"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)
        elif choice == "3":
            newStatement =  dracula_v5(dracula_prompts["nevermind"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)

    time.sleep(1)

    print("Mysterious Merchant: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_dracula_v5 = False

while talking_to_dracula_v6:
    print("You approach a mysterious merchant. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = dracula_v6(dracula_prompts["where_from"])
        print("Mysterious Merchant: " + statement)
        time.sleep(wait)
        print("1: Tell me more about your homeland.")
        print("2: Have you seen any dragons?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  dracula_v6(dracula_prompts["tell_me_more"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)
        elif choice == "2":
            newStatement =  dracula_v6(dracula_prompts["seen_dragons"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)

    elif choice == "2":
        statement =  dracula_v6(dracula_prompts["selling_anything"])
        print("Mysterious Merchant: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  dracula_v6(dracula_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  dracula_v6(dracula_prompts["buy_potions"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)
        elif choice == "3":
            newStatement =  dracula_v6(dracula_prompts["nevermind"].format(statement=statement))
            print("Mysterious Merchant: " + newStatement)

    time.sleep(1)

    print("Mysterious Merchant: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_dracula_v6 = False
