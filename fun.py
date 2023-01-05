def start_conversation(lingua):
    if lingua == "pt" or lingua == "br":
        print("Bom dia. Daqui fala a escola AEG1. Em que podemos ser úteis.")
    elif lingua == "uk" or lingua == "us":
        print("Hello! This is from AEG1 school. How can I help you")
    elif lingua == "fr":
        print("Bonjour! On appelle de l'école AEG1. Comment peut on aidé?")
    elif lingua == "cn":
        print("早上好。这是AEG1学校。我们能提供什么帮助？")
    else:
        start_conversation("pt")

# start_conversation("pt")
# start_conversation("uk")
# start_conversation("fr")
start_conversation("cn")
