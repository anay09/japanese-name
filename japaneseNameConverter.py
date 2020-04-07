print("_____________________________________________________")
print("|******************Japanese Names*******************|")
print("|---------------------------------------------------|")
print("|                                                   |")
englishName = input("|Please enter your name : ")
print("|                                                   |")
print("|---------------------------------------------------|")
print("|**********************RESULT***********************|")
print("|---------------------------------------------------|")
englishNameCapitalised = englishName.upper()
print("|                                                   |")
print("|Your English Name is : ", englishName.ljust(26, " "), "|")
print("|                                                   |")
lengthEnglishName = len(englishName)
japaneseName = ""
for i in range(lengthEnglishName):
    if englishNameCapitalised[i] == 'A':
        japaneseName += "ka"
    elif englishNameCapitalised[i] == 'B':
        japaneseName += "tu"
    elif englishNameCapitalised[i] == 'C':
        japaneseName += "mi"
    elif englishNameCapitalised[i] == 'D':
        japaneseName += "te"
    elif englishNameCapitalised[i] == 'E':
        japaneseName += "ku"
    elif englishNameCapitalised[i] == 'F':
        japaneseName += "lu"
    elif englishNameCapitalised[i] == 'G':
        japaneseName += "ji"
    elif englishNameCapitalised[i] == 'H':
        japaneseName += "ri"
    elif englishNameCapitalised[i] == 'I':
        japaneseName += "ki"
    elif englishNameCapitalised[i] == 'J':
        japaneseName += "zu"
    elif englishNameCapitalised[i] == 'K':
        japaneseName += "me"
    elif englishNameCapitalised[i] == 'L':
        japaneseName += "ta"
    elif englishNameCapitalised[i] == 'M':
        japaneseName += "rin"
    elif englishNameCapitalised[i] == 'N':
        japaneseName += "to"
    elif englishNameCapitalised[i] == 'O':
        japaneseName += "mo"
    elif englishNameCapitalised[i] == 'P':
        japaneseName += "no"
    elif englishNameCapitalised[i] == 'Q':
        japaneseName += "ke"
    elif englishNameCapitalised[i] == 'R':
        japaneseName += "shi"
    elif englishNameCapitalised[i] == 'S':
        japaneseName += "ari"
    elif englishNameCapitalised[i] == 'T':
        japaneseName += "chi"
    elif englishNameCapitalised[i] == 'U':
        japaneseName += "do"
    elif englishNameCapitalised[i] == 'V':
        japaneseName += "ru"
    elif englishNameCapitalised[i] == 'W':
        japaneseName += "mei"
    elif englishNameCapitalised[i] == 'X':
        japaneseName += "na"
    elif englishNameCapitalised[i] == 'Y':
        japaneseName += "fu"
    elif englishNameCapitalised[i] == 'Z':
        japaneseName += "zi"
print("|Your Japanese Name is : ", japaneseName.ljust(25, " "), "|")
print("|                                                   |")
print("|___________________________________________________|")