import argparse


def bruteUser():
    pass

def brutePassword():
    pass

def main():
    parser = argparse.ArgumentParser(description="Script for resolve lab 1 of Autentication PortSwigger labs")
    
    #ARGUMENTS
    parser.add_argument("option", help ="Choose option user or password to bruteforce")
    parser.add_argument("url", help ="Especfic the URL for attack")
    parser.add_argument("file", help="Specific file for bruteforce")
    parser.add_argument("-user", help="Specific user for bruteforce password")

    #PARSER IN CREATED ARGUMENTS
    args = parser.parse_args()
    print(parser.parse_args())

    if (args.option == "user"):
        
        bruteUser()

    elif (args.option == "password"):
        
        if (not args.user):
            print("Please input flag -u sampleuser")
        else:
            brutePassword()

if __name__=="__main__":
    main()