import regex as re
import pandas as pd
import requests
from datetime import datetime
from bs4 import BeautifulSoup

Make = "Tesla"

# Test access to the Edmunds website
url = 'https://www.edmunds.com//'
url = url[:24] + Make + url[24:]
print(url)
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
try:
    status = response.status_code
    print(status)
except Exception as e:
    print(e)

soup = BeautifulSoup(response.content, 'html.parser')

#print(soup.get_attribute_list('name'))

html_string = soup.prettify()
pattern = r'"(\d{4}\s'+ Make + '[^"]*)"'


matches = re.findall(pattern, html_string)

unique_matches = list(set(matches))

short_list = [item for item in unique_matches if item.count(" ") <= 5]
new_list = [item for item in short_list if ':' not in item]

#for match in new_list:
#    print(match)
threshold = datetime.now().year -1
cars_df = pd.DataFrame(new_list, columns=['Car Extraction'])
cars_df['Model Year'] = cars_df['Car Extraction'].str[:4]
cars_df = cars_df[cars_df['Model Year'].astype(int) >= threshold]
cars_df['Make'] = cars_df['Car Extraction'].str.split().str[1]
cars_df['Type'] = cars_df['Car Extraction'].str.split().str[-1]
cars_df['Model'] = cars_df['Car Extraction'].str.split().str[1:-1].str.join(' ')

print(cars_df)
"""
if matches:
    for match in matches:
        print(match)
else:
    print("No matches found.")
"""
#if isinstance(matches, list): print("Yes list")
#print(matches)
#for row in soup.find_all('a'):
#    print(row)

#file_path = 'Output.txt'
#file = open(file_path, 'w')

#file.write(html_string)

#file.close()

