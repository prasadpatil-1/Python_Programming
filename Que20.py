def CheckVowel(ch):

    vowel = ['a','e','i','o','u']


    if ch in vowel:
        return True
    else:
        return False

def main():
   
    char = str(input("Enter character :"))
    CheckVowel(char)

    if CheckVowel(char):
        print("Vowel")
    else:
        print("Not Vowel")


   

if __name__ == "__main__":
    main()