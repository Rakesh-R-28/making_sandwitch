
def make_sandwich(bread_type, filling, cheese="none", toasted=False):
    sentence = "Making a "

    # Handle toasted
    if toasted:
        sentence += "toasted "

    sentence += f"{bread_type} sandwich with {filling}"

    # Handle cheese
    if cheese != "none":
        sentence += f" and {cheese} cheese"

    sentence += "."

    return sentence
m1=make_sandwich("wheat", "turkey", "cheddar", True)
print(m1)
m2=make_sandwich("rye", "ham")
print(m2)
