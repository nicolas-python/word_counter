#word_counter

buchstaben = 0
woerter = 0
zahlen = 0
sonderzeichen = 0

def word_counter():
    global buchstaben
    global woerter
    global zahlen
    global sonderzeichen

    user_text = input("Welchen Text möchtest du Zerlegt haben?")

    for word in user_text.split():


        print("Sie haben Buchstaben:",buchstaben)
        print("Sie haben Woerter:",woerter)
        print("Sie haben Zahlen:",zahlen)
        print("Sie habven Sonderzeichen:",sonderzeichen)


word_counter()