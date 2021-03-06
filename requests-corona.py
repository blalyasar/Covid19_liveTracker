import requests
import bs4
import argparse

def covid19(country):
    
    res = requests.get("https://www.worldometers.info/coronavirus/#countries")
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    index = -1
    data=soup.select('tr td')
    for i in range(len(data)):
        if data[i].text.lower()==country.lower():
            index=i
            break

    for i in range(7):
        if i == 0:
            print("\nCountry name: "+str(data[i+index].text))
        elif i == 1:
            print("Total cases: "+str(data[i+index].text))
        elif i == 2:
            if data[i+index].text == '':
                print("New cases: 0")
            else:
                print("New cases: "+str(data[i+index].text))
        elif i == 3:
            print("Total deaths: "+str(data[i+index].text))
        elif i == 4:
            if data[i+index].text == '':
                print("New deaths: 0")
            else:
                print("New deaths: "+str(data[i+index].text))
        elif i == 5:
            print("Total Recovered: "+str(data[i+index].text))
        elif i == 6:
            print("Active cases: "+str(data[i+index].text),end='\n\n')
        else:
            print("This country doesn't exist")


if __name__ == '__main__' :
    parser = argparse. ArgumentParser(
            description="Add CountryName")
    
    parser.add_argument('-c' ,
                         help='Country Name' ,
                         type=str,
                         default="turkey")

    args = parser.parse_args()
    covid19(args.c)
