import openai
import time

openai.api_key = "Insert your OpenAI API Key";
wait = 2
talking_to_gandalf_control = False;
talking_to_gandalf_v1 = False;
talking_to_gandalf_v2 = False;
talking_to_gandalf_v3 = False;
talking_to_gandalf_v4 = False;
talking_to_gandalf_v5 = False;
talking_to_gandalf_v6 = False;

gandalf_prompts = {
    "background" : """
    You are acting as an NPC for Gandalf, a wizard from J.R.R. Tolkien's Middle-earth legendarium.
    """,
    "where_from" : "A traveler asks ‘where are you from?’ Generate 1-3 sentences of dialogue in response:",
    "selling_anything": "A traveler asks ‘are you selling anything?’ In this game, you are selling potions & scrolls. Generate 1-3 sentences of dialogue in response:",
    "tell_me_more": "A traveler asks 'where you are from.' You say: {statement} He then asks 'tell me more about your homeland.' Generate 1-3 sentences of dialogue in response:",
    "seen_dragons": "A traveler asks 'where you are from.' You say: {statement} He then asks 'Have you seen any dragons there?' Generate 1-3 sentences of dialogue in response:",
    "buy_scrolls": "A traveler asks 'are selling anything.' You say: {statement} He then asks 'Can I buy some scrolls?' Generate 1-3 sentences of dialogue in response:",
    "buy_potions": "A traveler asks 'are selling anything.' You say: {statement} He then asks 'Can I buy some potions?' Generate 1-3 sentences of dialogue in response:",
    "nevermind": "A traveler asks 'are selling anything.' You say: {statement} He then says 'Nevermind?' Generate 1-3 sentences of dialogue in response:",
}

def gandalf_v1(prompt):

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gandalf_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message
def gandalf_v2(prompt):

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gandalf_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.1,
    )

    message = response.choices[0].text.strip()
    return message
def gandalf_v3(prompt):

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gandalf_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=.9,
    )

    message = response.choices[0].text.strip()
    return message
def gandalf_v4(prompt):

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gandalf_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message
def gandalf_v5(prompt):

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gandalf_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.1,
    )

    message = response.choices[0].text.strip()
    return message
def gandalf_v6(prompt):
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=gandalf_prompts["background"] + prompt,
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
versions of Gandalf, a wizard from J.R.R. Tolkien's Middle-earth legendarium.The 
purpose of this program is to illustrate how prompt-engineering gpt prompts within 
dialogue trees can be used to create immersive experiences with NPCs. 

Here are the 7 different versions of gandalf you can have the chance to talk to:

--

Gandalf Control: 
This is a verison of gandalf made to respond using a standard, non-AI-enhanced dialogue tree. 
All of this responses are pre-written, and they do not change every time you talk to him.

--

Gandalf Version 1:
Model: text-davinci-002
Temperature: 0.5
Prompts: Complex

Gandalf Version 2:
Model: text-davinci-002
Temperature: 0.1
Prompts: Complex

Gandalf Version 3:
Model: text-davinci-002
Temperature: 0.9
Prompts: Complex

--

Gandalf Version 4:
Model: text-davinci-003
Temperature: 0.5
Prompts: Complex

Gandalf Version 5:
Model: text-davinci-003
Temperature: 0.1
Prompts: Complex

Gandalf Version 6:
Model: text-davinci-003
Temperature: 0.9
Prompts: Complex

""")

choice = input("Which version of Gandalf would you like to talk to? control, 1, 2, 3, 4, 5 or 6?")

if choice == "control":
    talking_to_gandalf_control = True;
elif choice == "1":
    talking_to_gandalf_v1 = True;
elif choice == "2":
    talking_to_gandalf_v2 = True;
elif choice == "3":
    talking_to_gandalf_v3 = True;
elif choice == "4":
    talking_to_gandalf_v4 = True;
elif choice == "5":
    talking_to_gandalf_v5 = True;
elif choice == "6":
    talking_to_gandalf_v5 = True;

while talking_to_gandalf_control:
    time.sleep(wait)
    print("You approach the wizard Gandalf. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        time.sleep(wait)
        print("Gandalf: I am a Maia, originally from the Undying Lands. I was sent to Middle-earth to aid in the fight against the darkness.")
        time.sleep(wait)
        print("1: Tell me more about the Undying Lands.")
        print("2: Have you encountered any dragons during your time in Middle-earth?")
        choice = input("Choose your input:")
        time.sleep(wait)
        if choice == "1":
            print("Gandalf: The Undying Lands, also known as Aman, are home to the immortal beings called the Ainur, as well as the elves who chose to live there. It is a land of beauty and peace, far removed from the troubles of Middle-earth.")
        elif choice == "2":
            print("Gandalf: Indeed, I have encountered dragons in my time. One such dragon was Smaug, who was defeated by the combined efforts of dwarves, men, and elves.")

    elif choice == "2":
        print("Gandalf: I am not a merchant, but I can offer you wisdom and guidance. What do you seek?")
        time.sleep(wait)
        print("1: Tell me about the One Ring.")
        print("2: How can I become a powerful wizard?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        time.sleep(wait)
        if choice == "1":
            print("Gandalf: The One Ring was forged by the Dark Lord Sauron to control the other Rings of Power. It is a dangerous artifact that must be kept out of his reach, for it would bring about the doom of Middle-earth.")
        elif choice == "2":
            print("Gandalf: True power comes from wisdom, humility, and selflessness. Study the arcane arts, seek understanding, and always use your abilities for the greater good.")
        elif choice == "3":
            print("Gandalf: Very well, let me know if you need anything else.")

    time.sleep(1)

    print("Gandalf: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_gandalf_control = False

while talking_to_gandalf_v1:
    print("You approach the wizard Gandalf. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = gandalf_v1(gandalf_prompts["where_from"])
        print("Gandalf: " + statement)
        time.sleep(wait)
        print("1: Tell me more about your homeland.")
        print("2: Have you seen any dragons?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement = gandalf_v1(gandalf_prompts["tell_me_more"].format(statement=statement))
            print("Gandalf: " + newStatement)
        elif choice == "2":
            newStatement = gandalf_v1(gandalf_prompts["seen_dragons"].format(statement=statement))
            print("Gandalf: " + newStatement)

    elif choice == "2":
        statement = gandalf_v1(gandalf_prompts["selling_anything"])
        print("Gandalf: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement = gandalf_v1(gandalf_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement = gandalf_v1( gandalf_prompts["buy_potions"].format(statement=statement))
            print("Gandalf: " + newStatement)
        elif choice == "3":
            newStatement = gandalf_v1(gandalf_prompts["nevermind"].format(statement=statement))
            print("Gandalf: " + newStatement)

    time.sleep(1)

    print("Gandalf: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_gandalf_v1 = False

while talking_to_gandalf_v2:
    print("You approach the wizard Gandalf. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = gandalf_v2(gandalf_prompts["where_from"])
        print("Gandalf: " + statement)
        time.sleep(wait)
        print("1: Tell me more about your homeland.")
        print("2: Have you seen any dragons?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  gandalf_v2(gandalf_prompts["tell_me_more"].format(statement=statement))
            print("Gandalf: " + newStatement)
        elif choice == "2":
            newStatement =  gandalf_v2(gandalf_prompts["seen_dragons"].format(statement=statement))
            print("Gandalf: " + newStatement)

    elif choice == "2":
        statement =  gandalf_v2(gandalf_prompts["selling_anything"])
        print("Gandalf: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  gandalf_v2(gandalf_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  gandalf_v2(gandalf_prompts["buy_potions"].format(statement=statement))
            print("Gandalf: " + newStatement)
        elif choice == "3":
            newStatement =  gandalf_v2(gandalf_prompts["nevermind"].format(statement=statement))
            print("Gandalf: " + newStatement)

    time.sleep(1)

    print("gandalf: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_gandalf_v2 = False

while talking_to_gandalf_v3:
    print("You approach the wizard Gandalf. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = gandalf_v3(gandalf_prompts["where_from"])
        print("Gandalf: " + statement)
        time.sleep(wait)
        print("1: Tell me more about your homeland.")
        print("2: Have you seen any dragons?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  gandalf_v3(gandalf_prompts["tell_me_more"].format(statement=statement))
            print("Gandalf: " + newStatement)
        elif choice == "2":
            newStatement =  gandalf_v3(gandalf_prompts["seen_dragons"].format(statement=statement))
            print("Gandalf: " + newStatement)

    elif choice == "2":
        statement =  gandalf_v3(gandalf_prompts["selling_anything"])
        print("Gandalf: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  gandalf_v3(gandalf_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  gandalf_v3(gandalf_prompts["buy_potions"].format(statement=statement))
            print("Gandalf: " + newStatement)
        elif choice == "3":
            newStatement =  gandalf_v3(gandalf_prompts["nevermind"].format(statement=statement))
            print("Gandalf: " + newStatement)

    time.sleep(1)

    print("Gandalf: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_gandalf_v3 = False

while talking_to_gandalf_v4:
    print("You approach the wizard Gandalf. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = gandalf_v4(gandalf_prompts["where_from"])
        print("Gandalf: " + statement)
        time.sleep(wait)
        print("1: Tell me more about your homeland.")
        print("2: Have you seen any dragons?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  gandalf_v4(gandalf_prompts["tell_me_more"].format(statement=statement))
            print("Gandalf: " + newStatement)
        elif choice == "2":
            newStatement =  gandalf_v4(gandalf_prompts["seen_dragons"].format(statement=statement))
            print("Gandalf: " + newStatement)

    elif choice == "2":
        statement =  gandalf_v4(gandalf_prompts["selling_anything"])
        print("Gandalf: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  gandalf_v4(gandalf_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  gandalf_v4(gandalf_prompts["buy_potions"].format(statement=statement))
            print("Gandalf: " + newStatement)
        elif choice == "3":
            newStatement =  gandalf_v4(gandalf_prompts["nevermind"].format(statement=statement))
            print("Gandalf: " + newStatement)

    time.sleep(1)

    print("Gandalf: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_gandalf_v4 = False

while talking_to_gandalf_v5:
    print("You approach the wizard Gandalf. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = gandalf_v5(gandalf_prompts["where_from"])
        print("Gandalf: " + statement)
        time.sleep(wait)
        print("1: Tell me more about your homeland.")
        print("2: Have you seen any dragons?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  gandalf_v5(gandalf_prompts["tell_me_more"].format(statement=statement))
            print("Gandalf: " + newStatement)
        elif choice == "2":
            newStatement =  gandalf_v5(gandalf_prompts["seen_dragons"].format(statement=statement))
            print("Gandalf: " + newStatement)

    elif choice == "2":
        statement =  gandalf_v5(gandalf_prompts["selling_anything"])
        print("Gandalf: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  gandalf_v5(gandalf_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  gandalf_v5(gandalf_prompts["buy_potions"].format(statement=statement))
            print("Gandalf: " + newStatement)
        elif choice == "3":
            newStatement =  gandalf_v5(gandalf_prompts["nevermind"].format(statement=statement))
            print("Gandalf: " + newStatement)

    time.sleep(1)

    print("Gandalf: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_gandalf_v5 = False

while talking_to_gandalf_v6:
    print("You approach the wizard Gandalf. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = gandalf_v6(gandalf_prompts["where_from"])
        print("Gandalf: " + statement)
        time.sleep(wait)
        print("1: Tell me more about your homeland.")
        print("2: Have you seen any dragons?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  gandalf_v6(gandalf_prompts["tell_me_more"].format(statement=statement))
            print("Gandalf: " + newStatement)
        elif choice == "2":
            newStatement =  gandalf_v6(gandalf_prompts["seen_dragons"].format(statement=statement))
            print("Gandalf: " + newStatement)

    elif choice == "2":
        statement =  gandalf_v6(gandalf_prompts["selling_anything"])
        print("Gandalf: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  gandalf_v6(gandalf_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  gandalf_v6(gandalf_prompts["buy_potions"].format(statement=statement))
            print("Gandalf: " + newStatement)
        elif choice == "3":
            newStatement =  gandalf_v6(gandalf_prompts["nevermind"].format(statement=statement))
            print("Gandalf: " + newStatement)

    time.sleep(1)

    print("Gandalf: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_gandalf_v6 = False
