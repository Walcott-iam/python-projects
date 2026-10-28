import requests

browse = requests.get('https://dataslid.com.ng')
print(browse.text)

with open('mysite.html', 'w') as mysite_file:
    mysite_file.write(browse.text)
    