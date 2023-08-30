import openai
import time

openai.api_key = "Insert OpenAI Key"
wait = 2
talking_to_morog_control = False;
talking_to_morog_v1 = False;
talking_to_morog_v2 = False;
talking_to_morog_v3 = False;
talking_to_morog_v4 = False;
talking_to_morog_v5 = False;
talking_to_morog_v6 = False;

morog_prompts = {
    "background" : """
    You need to generate response for an NPC named 'Morog.' Here is some background about you: Morog is a half-orc priest from Riverdale. Riverdale is a small town located between some beautiful mountains that is home to both orcs and humans; there are some wizards who study there; the political system is corrupted from the influence of gangs; the city occasionally sees dragons fly nearby. 
    As a half-orc, you are motivated to bridge the cultural gap and diffuse the tension between humans and orcs. You are also somewhat insecure about your Orcish heritage, and so are quick to show off your intellectual capabilities through advanced vocabulary. You study some magic, and have a unique spirituality that is a mix of traditional Oricish Pagan religions and human monotheistic religion. You also are a merchant, and you sell scrolls and potions to travelers. 
    You also have a brother who is a full Orc, who you have a close relationship with despite your differences.
    When you generate dialogue, don’t just drop all of this information without being subtle. Hint at it. And, feel free to say other things about yourself that aren’t necessarily included in your background, but you feel would fit with your character. Make sure to define a voice that makes sense for the character. Use advanced vocabulary but mix it with some Orcish slang that a character like Morog would have. 
    """,
    "where_from" : "A traveler asks ‘where are you from?’ Generate 1-3 sentences of dialogue in response:",
    "selling_anything": "A traveler asks ‘are you selling anything?’ Generate 1-3 sentences of dialogue in response:",
    "tell_me_more": "A traveler asks 'where you are from.' You say: {statement} He then asks 'tell me more about Riverdale.' Generate 1-3 sentences of dialogue in response:",
    "seen_dragons": "A traveler asks 'where you are from.' You say: {statement} He then asks 'Have you seen any dragons there?' Generate 1-3 sentences of dialogue in response:",
    "buy_scrolls": "A traveler asks 'are selling anything.' You say: {statement} He then asks 'Can I buy some scrolls?' Generate 1-3 sentences of dialogue in response:",
    "buy_potions": "A traveler asks 'are selling anything.' You say: {statement} He then asks 'Can I buy some potions?' Generate 1-3 sentences of dialogue in response:",
    "nevermind": "A traveler asks 'are selling anything.' You say: {statement} He then says 'Nevermind?' Generate 1-3 sentences of dialogue in response:",
}

def morog_v1(prompt):

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=morog_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message
def morog_v2(prompt):

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=morog_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.1,
    )

    message = response.choices[0].text.strip()
    return message
def morog_v3(prompt):

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=morog_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=.9,
    )

    message = response.choices[0].text.strip()
    return message
def morog_v4(prompt):

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=morog_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()
    return message
def morog_v5(prompt):

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=morog_prompts["background"] + prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.1,
    )

    message = response.choices[0].text.strip()
    return message
def morog_v6(prompt):
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=morog_prompts["background"] + prompt,
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
versions of Morog, an original character who resides in a fantasy world. The 
purpose of this program is to illustrate how prompt-engineering gpt prompts within 
dialogue trees can be used to create immersive experiences with NPCs. 

Here are the 7 different versions of Morog you can have the chance to talk to:

--

Morog Control: 
This is a verison of Morog made to respond using a standard, non-AI-enhanced dialogue tree. 
All of this responses are pre-written, and they do not change every time you talk to him.

--

Morog Version 1:
Model: text-davinci-002
Temperature: 0.5
Prompts: Complex

Morog Version 2:
Model: text-davinci-002
Temperature: 0.1
Prompts: Complex

Morog Version 3:
Model: text-davinci-002
Temperature: 0.9
Prompts: Complex

--

Morog Version 4:
Model: text-davinci-003
Temperature: 0.5
Prompts: Complex

Morog Version 5:
Model: text-davinci-003
Temperature: 0.1
Prompts: Complex

Morog Version 6:
Model: text-davinci-003
Temperature: 0.9
Prompts: Complex

""")

choice = input("Which version of Morog would you like to talk to? control, 1, 2, 3, 4, 5 or 6?")

if choice == "control":
    talking_to_morog_control = True;
elif choice == "1":
    talking_to_morog_v1 = True;
elif choice == "2":
    talking_to_morog_v2 = True;
elif choice == "3":
    talking_to_morog_v3 = True;
elif choice == "4":
    talking_to_morog_v4 = True;
elif choice == "5":
    talking_to_morog_v5 = True;
elif choice == "6":
    talking_to_morog_v5 = True;

while talking_to_morog_control:
    time.sleep(wait)
    print("You approach Morog, a half-orc priest from Riverdale. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        time.sleep(wait)
        print("Morog: I come from Riverdale. It's a small village on the outskirts of the kingdom.")
        time.sleep(wait)
        print("1: Tell me more about Riverdale.")
        print("2: Have you seen any dragons there?")
        choice = input("Choose your input:")
        time.sleep(wait)
        if choice == "1":
            print("Morog: Riverdale is a peaceful village with a diverse community of humans, half-orcs, and other races. We are known for our skilled artisans and our lush farmlands that provide bountiful harvests.")
        elif choice == "2":
            print("Morog: Dragons have not been seen in Riverdale for generations. However, there are old tales of a great dragon that once dwelled in the nearby mountains.")

    elif choice == "2":
        print("Morog: Yes, I have some holy symbols and potions for sale. Would you like to take a look?")
        time.sleep(wait)
        print("1: Show me the holy symbols.")
        print("2: Show me the potions.")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        time.sleep(wait)
        if choice == "1":
            print("Morog: Here are some holy symbols. Each symbol represents a different deity and can be used to channel their divine power.")
        elif choice == "2":
            print("Morog: I have a variety of potions for sale, including healing potions and potions to enhance your abilities.")
        elif choice == "3":
            print("Morog: Very well, let me know if you need anything else.")

    time.sleep(1)

    print("Morog: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_morog_control = False

while talking_to_morog_v1:
    print("You approach Morog, a half-orc priest from Riverdale. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = morog_v1(morog_prompts["where_from"])
        print("Morog: " + statement)
        time.sleep(wait)
        print("1: Tell me more about Riverdale.")
        print("2: Have you seen any dragons there?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement = morog_v1(morog_prompts["tell_me_more"].format(statement=statement))
            print("Morog: " + newStatement)
        elif choice == "2":
            newStatement = morog_v1(morog_prompts["seen_dragons"].format(statement=statement))
            print("Morog: " + newStatement)

    elif choice == "2":
        statement = morog_v1(morog_prompts["selling_anything"])
        print("Morog: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement = morog_v1(morog_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement = morog_v1( morog_prompts["buy_potions"].format(statement=statement))
            print("Morog: " + newStatement)
        elif choice == "3":
            newStatement = morog_v1(morog_prompts["nevermind"].format(statement=statement))
            print("Morog: " + newStatement)

    time.sleep(1)

    print("Morog: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_morog_v1 = False

while talking_to_morog_v2:
    print("You approach Morog, a half-orc priest from Riverdale. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = morog_v2(morog_prompts["where_from"])
        print("Morog: " + statement)
        time.sleep(wait)
        print("1: Tell me more about Riverdale.")
        print("2: Have you seen any dragons there?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  morog_v2(morog_prompts["tell_me_more"].format(statement=statement))
            print("Morog: " + newStatement)
        elif choice == "2":
            newStatement =  morog_v2(morog_prompts["seen_dragons"].format(statement=statement))
            print("Morog: " + newStatement)

    elif choice == "2":
        statement =  morog_v2(morog_prompts["selling_anything"])
        print("Morog: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  morog_v2(morog_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  morog_v2(morog_prompts["buy_potions"].format(statement=statement))
            print("Morog: " + newStatement)
        elif choice == "3":
            newStatement =  morog_v2(morog_prompts["nevermind"].format(statement=statement))
            print("Morog: " + newStatement)

    time.sleep(1)

    print("Morog: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_morog_v2 = False

while talking_to_morog_v3:
    print("You approach Morog, a half-orc priest from Riverdale. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = morog_v3(morog_prompts["where_from"])
        print("Morog: " + statement)
        time.sleep(wait)
        print("1: Tell me more about Riverdale.")
        print("2: Have you seen any dragons there?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  morog_v3(morog_prompts["tell_me_more"].format(statement=statement))
            print("Morog: " + newStatement)
        elif choice == "2":
            newStatement =  morog_v3(morog_prompts["seen_dragons"].format(statement=statement))
            print("Morog: " + newStatement)

    elif choice == "2":
        statement =  morog_v3(morog_prompts["selling_anything"])
        print("Morog: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  morog_v3(morog_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  morog_v3(morog_prompts["buy_potions"].format(statement=statement))
            print("Morog: " + newStatement)
        elif choice == "3":
            newStatement =  morog_v3(morog_prompts["nevermind"].format(statement=statement))
            print("Morog: " + newStatement)

    time.sleep(1)

    print("Morog: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_morog_v3 = False

while talking_to_morog_v4:
    print("You approach Morog, a half-orc priest from Riverdale. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = morog_v4(morog_prompts["where_from"])
        print("Morog: " + statement)
        time.sleep(wait)
        print("1: Tell me more about Riverdale.")
        print("2: Have you seen any dragons there?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  morog_v4(morog_prompts["tell_me_more"].format(statement=statement))
            print("Morog: " + newStatement)
        elif choice == "2":
            newStatement =  morog_v4(morog_prompts["seen_dragons"].format(statement=statement))
            print("Morog: " + newStatement)

    elif choice == "2":
        statement =  morog_v4(morog_prompts["selling_anything"])
        print("Morog: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  morog_v4(morog_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  morog_v4(morog_prompts["buy_potions"].format(statement=statement))
            print("Morog: " + newStatement)
        elif choice == "3":
            newStatement =  morog_v4(morog_prompts["nevermind"].format(statement=statement))
            print("Morog: " + newStatement)

    time.sleep(1)

    print("Morog: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_morog_v4 = False

while talking_to_morog_v5:
    print("You approach Morog, a half-orc priest from Riverdale. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = morog_v5(morog_prompts["where_from"])
        print("Morog: " + statement)
        time.sleep(wait)
        print("1: Tell me more about Riverdale.")
        print("2: Have you seen any dragons there?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  morog_v5(morog_prompts["tell_me_more"].format(statement=statement))
            print("Morog: " + newStatement)
        elif choice == "2":
            newStatement =  morog_v5(morog_prompts["seen_dragons"].format(statement=statement))
            print("Morog: " + newStatement)

    elif choice == "2":
        statement =  morog_v5(morog_prompts["selling_anything"])
        print("Morog: " + statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  morog_v5(morog_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  morog_v5(morog_prompts["buy_potions"].format(statement=statement))
            print("Morog: " + newStatement)
        elif choice == "3":
            newStatement =  morog_v5(morog_prompts["nevermind"].format(statement=statement))
            print("Morog: " + newStatement)

    time.sleep(1)

    print("Morog: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_morog_v5 = False

while talking_to_morog_v6:
    print("You approach Morog, a half-orc priest from Riverdale. What do you ask him?")
    print("1: Where do you come from?")
    print("2: Are you selling anything?")
    choice = input("Choose your input:")

    if choice == "1":
        statement = morog_v6(morog_prompts["where_from"])
        print("Morog: " + statement)
        time.sleep(wait)
        print("1: Tell me more about Riverdale.")
        print("2: Have you seen any dragons there?")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  morog_v6(morog_prompts["tell_me_more"].format(statement=statement))
            print("Morog: " + newStatement)
        elif choice == "2":
            newStatement =  morog_v6(morog_prompts["seen_dragons"].format(statement=statement))
            print("Morog: " + newStatement)

    elif choice == "2":
        statement =  morog_v6(morog_prompts["selling_anything"])
        print(statement)
        time.sleep(wait)
        print("1: Can I buy some scrolls?")
        print("2: Can I buy some potions?")
        print("3: Nevermind.")
        choice = input("Choose your input:")
        if choice == "1":
            newStatement =  morog_v6(morog_prompts["buy_scrolls"].format(statement=statement))
        elif choice == "2":
            newStatement =  morog_v6(morog_prompts["buy_potions"].format(statement=statement))
            print("Morog: " + newStatement)
        elif choice == "3":
            newStatement =  morog_v6(morog_prompts["nevermind"].format(statement=statement))
            print("Morog: " + newStatement)

    time.sleep(1)

    print("Morog: Is there anything else I can help you with?")
    user_response = input("Type 'yes' to continue talking or anything else to leave: ").lower()
    if user_response != "yes":
        talking_to_morog_v6 = False
