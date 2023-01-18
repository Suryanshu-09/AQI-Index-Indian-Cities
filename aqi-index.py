import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import *
print('1. Find the Pollution Index of Indian city\n2. Find the top ten polluted cities in India\n3 Find the top ten cleanest cities of India\n')
s=int(input('Enter What You would like to do. (1-2-3): '))
if s not in (1,2,3):
    print('choose a valid option')
class location():
    def __init__(self,
                 state='',
                 city='',
                 url=''):
        self.state = state
        self.city = city
        self.url=url

location2=location()
location1=location()
if s==1:
    location1.state=input('Enter the State: ')
    location1.city=input('Enter the City: ')
    if len(location1.state.split(' '))>1:
        location1.state=(location1.state.split(' '))[0]+'-'+(location1.state.split(' '))[1]
    if len(location1.city.split(' '))>1:
        location1.city=(location1.city.split(' '))[0]+'-'+(location1.city.split(' '))[1]
    url1='https://www.aqi.in/in/dashboard/india/'+(location1.state).lower()+'/'+(location1.city).lower()+'/'
    reqs = requests.get(url1)
    soup = bs(reqs.text, 'html.parser')
    desc=[]
    for statement in soup.find_all('meta'):
        desc.append(statement.get('content'))
    try:
        print('\n',desc[8],'\n')
    except:
        print('\n Please Enter A Valid Location.')
    finally:
        print('\n Tips to protect you and your family from poor air quality:')
        print('1. Check the AQI daily')
        print('2. Wear a mask when outdoors')
        print('3. Plant air-purifying plants in your home')
        print('4. Avoid outdoor activities')
        print('5. Inculcate healthy eating')
url2='https://www.iqair.com/in-en/india'
reqs2 = requests.get(url2)
soup2 = bs(reqs2.text, 'html.parser')
worst=[]
worst_places=[]
for statement in soup2.find_all('a'):
    worst.append(statement.get('href'))
for x in worst:
    if worst.index(x) in range(4,14):
        worst_places.append(x[13:])
for x in worst_places:
    y=x.split('/')
    worst_places[worst_places.index(x)]=y
for x in worst_places:
    for y in x:
        worst_places[worst_places.index(x)][x.index(y)]=y.capitalize()
best=[]
best_places=[]
for statement in soup2.find_all('a'):
    best.append(statement.get('href'))
for x in best:
    if best.index(x) in range(17,28):
        best_places.append(x[13:])
for x in best_places:
    y=x.split('/')
    best_places[best_places.index(x)]=y
for x in best_places:
    for y in x:
        best_places[best_places.index(x)][x.index(y)]=y.capitalize()
if s==2:
    print('\n Most Polluted Cities In India: ')
    for x in worst_places:
        print(str(worst_places.index(x)+1),x[0],x[1],sep='  ',end='\n')
elif s==3:
    print('\n Cleanest Cities In India: ')
    for x in best_places:
        print(str(best_places.index(x)+1),x[0],x[1],sep='  ',end='\n')
