import requests

domain = input("Enter domain: ")
file = open('wordlist.txt','r')
content = file.read()

subdomains = content.splitlines()

for subdomain in subdomains:
        url = f"https://{subdomain}.{domain}"

        try:
                requests.get(url)
                print(f"Discovered URL: {url}")

        except requests.ConnectionError:
                pass
