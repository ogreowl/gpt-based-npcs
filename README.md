# GPT Based NPCs With Dialogue Trees

## Description

This repository houses a Python-based interactive dialogue system that simulates conversations with iconic characters such as Dracula, Gandalf, and a new addition named Morog. It aims to demonstrate the power of prompt engineering and fine-tuning with GPT-3 to create immersive experiences within conversational agents (in this case, NPCs) when combined with traditional dialogue trees. 

It also tests how GPT performs when handling different types of characters. Dracula is a character within our cultural collective lore; Gandalf is a character within a specific IP; Morog is a new character, but based on well-defined fantasy archetypes. And, it allows users to experience those characters among different GPT-3 configurations.

## Dependencies

- Python 3.x
- OpenAI Python package

### Functions
- `dracula_v1` to `dracula_v6`, `gandalf_v1`, `morog_v1`: Functions simulate conversations with the characters using different GPT-3 model configurations.

### Dictionaries
- `character_prompts`: A dictionary containing the base prompts for the NPCs.

### Booleans
- `talking_to_character_v1` to `talking_to_character_v6`: Booleans to manage which version of the character the user is currently talking to.

