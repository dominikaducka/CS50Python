def main():
    answer = input("Tell me something ")
    convert(answer)

def convert(input):
    #converting emoticons to emoji
    newstr = input.replace(':)', '🙂').replace(':(','🙁')
    print(newstr)

main()

