print("Het is eindelijk weekend. Je wordt wakker en kijkt naar de wekker en ziet dat het 9:30 is. Wil je blijven liggen of opstaan ?")
choice = input()
if choice == 'opstaan':
    print("Rise and shine! Je maag heeft aandacht nodig!")
elif choice == 'blijven liggen':
    print("Niemand die je stoort en je heb alle tijd. Kan jou het scheeelennnn zzzz...")
else:
    print(choice, " sorry?")

print("Even opstarten en naar de keuken lopen. Even denken... brood of cerial ?")
choice = input()
if choice == 'brood':
    print("Beetje hageslag erop en... eet smakelijk!")
elif choice == 'cerial':
    print("je heb geen zin in brood smeren. Makelijk wat cerial in een bakje gooiien en doe er wat melk bij. Niet slecht!")
else:
    print(choice, " Ben je wakker? Je moet eten!")

print("Okay! Uh... wat nu? Je heb een Nintendo Switch en een PlayStation 5. Je heb nog games die je nog niet heb uitgespeeld. Dus... Switch of PS5?")
choice = input()
if choice == 'switch':
    print("Metroid Dread moet je nog uitspelen. Het is net uit maar je heb al een hoop lol! Nog even voorbereiden voor het gevecht tegen die E.M.M.I robots. Ew...")
elif choice == 'PS5':
    print("Spider Man: Miles Morales! Het heeft al snel een grote indruk gemaakt! Het mag misschien een kleine game zijn maar de open wereld en spannende gevechten blijven geweldig!")
else:
    print(choice, " Alles goed? Switch of PS5?")

print("Oké dat is wel genoeg van dat. Wil je even naar buiten of misschien nog iets doen op jouw PC?")
choice = input()
if choice == 'naar buiten':
    print("Even goede kleren aandoen en even een rondje lopen. Even zwaaien naar de buurman die zijn tuin mooimaakt. Misschien laat iemand jou wel zijn of haar hond aaien in het park...")
elif choice == 'PC':
    print("Nog even wat vechtgames spelen en oefenen. Het is lastig maar gelukkig is het internet de beste plek om iets te leren. Misschien kun je een keer meedoen aan een toernooi...")
else:
    print(choice, " Wet je zeker dat je wakker bent?")

print("Tijd vliegt en het is bijna avond. Wil je vroeg naar bed of wil je nog TV kijken?")
choice = input()
if choice == 'naar bed':
    print("Weltrusten!")
elif choice == 'TV':
    print("Maakt het niet te laat!")
else:
    print(choice, " wat?")