def main():
    speak = input("Tell me something ")
    speak_slower(speak)

def speak_slower(speak):
    #seperating words
    sep = speak.rsplit(sep = " ")

    #adding pouse
    pouse = "..."
    slower = [words + pouse for words in sep]

    #joining all words back together
    slower = ''.join(slower)
    print(slower)

main()

