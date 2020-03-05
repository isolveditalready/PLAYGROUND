#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
def is_isogram(string):
    masterList = []
    for letter in list(string):
        print(f"letter is {letter}")
        if ( letter in masterList ):
            print("false")
            return False
        else:
            masterList.append(letter)
    print("true")
            


is_isogram("shSit")