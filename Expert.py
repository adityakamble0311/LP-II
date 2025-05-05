def ask_question(question):
    response = input(question + ": ").lower().strip()[0]
    return response == "y"

def diagnose_allergies():
    return ask_question("Kya aapko kaanpne ya soojan ho rahi hai?") or ask_question("Aapke aankhon se paani aa raha hai ya laal ho gayi hain?")

def diagnose_fever():
    return ask_question("Kya aapka temperature 37.5°C se zyada hai?") or ask_question("Kya aapko thand lag rahi hai ya kaafi jalan ho rahi hai?")

def diagnose_cold():
    return ask_question("Kya aapko naak band hai ya beh rahi hai?") or ask_question("Kya aap baar baar chhink rahe ho?")

def diagnose_flu():
    return (
        ask_question("Kya aapke sharir mein dard ho raha hai?")
        and ask_question("Kya aapko thakan mehsoos ho rahi hai?")
        and ask_question("Kya aapka temperature 38°C se zyada hai?")
    )

def diagnose_strep_throat():
    return ask_question("Kya aapko gale mein dard ho raha hai?") and ask_question("Kya aapke tonsils sujan ho gaye hain?")

def diagnose_food_poisoning():
    return (
        ask_question("Kya aapko ulti aayi hai?")
        and ask_question("Kya aapko dast ho rahe hain?")
        and ask_question("Kya aapko jalan ho rahi hai ya ghabrahat mehsoos ho rahi hai?")
    )

def diagnose_appendicitis():
    return ask_question("Kya aapko peet mein zyada dard ho raha hai?") and ask_question("Kya aapka bhukh bilkul band ho gaya hai?")

print("Bhai, yeh system aapke bimari diagnose karne ke liye hai")

if diagnose_allergies():
    print("Aapko allergies ho sakti hain")
if diagnose_fever():
    print("Aapko bukhar ho sakta hai")
if diagnose_cold():
    print("Aapko zukam ho sakta hai")
if diagnose_flu():
    print("Aapko flu ho sakta hai")
if diagnose_strep_throat():
    print("Aapko strep throat ho sakta hai")
if diagnose_food_poisoning():
    print("Aapko food poisoning ho sakti hai")
if diagnose_appendicitis():
    print("Aapko appendicitis ho sakti hai")
