import requests

file =open('C:/Users/ramaz/Desktop/urls/external.txt', 'r') 
lines = file.readlines()
writer = open('C:/Users/ramaz/Desktop/urls/bad_status.txt', 'w')
for line in lines:
    urls = line.strip()
    request = requests.head(urls, verify=True)
    response = request.status_code
    print(urls, response)
    if response != 200:
        writer.write(urls)
        writer.write('\n')
file.close()
writer.close()