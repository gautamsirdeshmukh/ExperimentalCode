def create():
    import sys
    # words = open(sys.argv[1], "r")
    words = open("lowerwords.txt")
    words = [w[:-1].upper() for w in words if len(w) == 6]
    ret = []
    for word in words:
        yes = True
        while yes:
            for letter in word:
                if word.count(letter) > 2:
                    yes = False
            break
        if yes:
            ret.append(word)
        else:
            continue
    return ret

def spaces(letter, option):
    print("\n_ _ _ _ _")
    print("1 2 3 4 5\n")
    if option == "yellow":
        print(f"\n- - - Enter what NUMBER SPACES the yellow letter '{letter.upper()}' CANNOT be at - - -\n")
    else:
        print(f"\n- - - Enter what NUMBER SPACES the green letter '{letter.upper()}' is at - - -\n")
    space = input("Enter spaces [i.e. 23] or press return to move on: ")
    print("\n")
    return list(set([int(sp) for sp in space]))

def gray():
    print("\n- - - Enter GRAY Letters - - -\n")
    letters = input("Enter letters [i.e. asdf] or press return to move on: ").upper()
    print("\n")
    return list(set([let for let in letters]))


def yellow():
    print("\n- - - Enter YELLOW Letters - - -\n")
    ret = {}
    while True:
        letter = "AA"
        while (len(str(letter)) != 0) and letter not in "abcdefghijklmnopqrsztuvwxyz".upper():
            letter = input("Enter letter [A-Z] or press return to move on: ").upper()
        if len(letter) == 0:
            print("\n")
            return ret
        else:
            ret[letter] = spaces(letter, "yellow")

def green():
    print("\n- - - Enter GREEN Letters - - -\n")
    ret = {}
    while True:
        letter = "AA"
        while (len(str(letter)) != 0) and letter not in "abcdefghijklmnopqrsztuvwxyz".upper():
            letter = input("Enter letter [A-Z] or press return to move on: ").upper()
        if len(letter) == 0:
            print("\n")
            return ret
        else:
            ret[letter] = spaces(letter, "green")

def solve():
    words = create()
    grays = gray()
    yellows = yellow()
    greens = green()
    possible = []
    for word in words:
        def checkGray():
            if len(set(list(word)).intersection(set(grays))) != 0:
                return False
            return True
        def checkYellow():
            for letter in yellows.keys():
                if letter not in word:
                    return False
                else:
                    for i in range(len(word)):
                        if word[i] == letter:
                            if i in [y-1 for y in yellows[letter]]:
                                return False
            return True
        def checkGreen():
            for letter in greens.keys():
                if letter not in word:
                    return False
                else:
                    for i in range(len(word)):
                        if word[i] == letter:
                            if i not in [g-1 for g in greens[letter]]:
                                return False
            return True
        pos = (checkGray() and checkYellow() and checkGreen())
        if pos:
            possible.append(word)
        else:
            continue

    for choice in possible:
        print(choice,)

if __name__ == "__main__":
    while True:
        play = input("Press enter to start or type anything to quit: ")
        if len(play) == 0:
            solve()
            print("\n")
        else:
            break