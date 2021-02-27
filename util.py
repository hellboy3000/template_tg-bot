import requests
from bs4 import BeautifulSoup 

# parsing the exchange rate
def bitcoin_to_usd():
    link = 'https://www.calc.ru/Bitcoin-k-dollaru-online.html'
    r = requests.get(link).text

    soup = BeautifulSoup(r, 'lxml')
    block = soup.find('div', {'class': 't18'})
    usd = block.find_all('b')[1].text
    # print('1 BTC =', x) 
    message = f'1 BTC = {usd}'
    return message



        
        

     
    
