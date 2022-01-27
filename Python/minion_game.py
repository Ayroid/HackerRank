def minion_game(string):

    vowels="AEIOU"
    Stuart=0
    Kevin=0

    for i in range(len(string)):
        if string[i] in vowels:
            Kevin+=len(string)-i
        else:
            Stuart+=len(string)-i

    if Kevin==Stuart:
        print("Draw")
    elif Kevin<Stuart:
        print("Stuart",Stuart)
    else:
        print("Kevin",Kevin)


if __name__ == '__main__':
    s = input()
    minion_game(s)
