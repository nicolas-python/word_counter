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

    woerter = len(user_text.split())

    for zeichen in user_text:

        if zeichen.isalpha():
            buchstaben += 1

        elif zeichen.isdigit():
            zahlen += 1

        elif zeichen == " ":        # Leerzeichen sollen nicht als Sonderzeichen zählen
            pass

        else:
            sonderzeichen += 1

    print("Sie haben Buchstaben:",buchstaben)
    print("Sie haben Woerter:",woerter)
    print("Sie haben Zahlen:",zahlen)
    print("Sie haben Sonderzeichen:",sonderzeichen)


#Ausführung Programm
word_counter()