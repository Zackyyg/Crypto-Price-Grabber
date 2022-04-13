import requests
from bs4 import BeautifulSoup

## searchs crypto.com
def search(coin):
    print "Searching for your coin"
    url = 'https://crypto.com/price?page=1'
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    pages = int(soup.findAll(attrs={'class':'chakra-button css-1k8y4zd'})[-1].text)
    for i in xrange(1, pages):
        print "searching the top %d"%(50*i)
        url = 'https://crypto.com/price?page=%d' % i
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        for row in soup.findAll(attrs={'class':'css-7sv28d'}):
            abbv = str(row.find(attrs={'class':'chakra-text css-ft1qn5'}).text.encode("utf-8"))
            n = str(row.find(attrs={'class':'chakra-text css-1mrk1dy'}).text.encode("utf-8"))
            p = str(row.find(attrs={'class':'css-1vyy4qg'}).div.text.encode("utf-8"))[1:]
            if abbv == coin:
                print "\n%s \n------------ \nName: %s \nPrice: %s \n" % (abbv, n, p)
                return
        
## UI
print "Welcome to Crypto Currency Grabber"
while True:
    print "What would you like to do?"
    print "1: Grab a Crypto Currency off of Crypto.com"
    print "2: Exit"

    user = raw_input("> ")
    if user == "1":
        print "Enter a Crpyto Abbreviation"
        print "Example: 'BTC'"
        user_coin = raw_input("> ").upper()
        search(user_coin)
    elif user == "2":
        break
    else:
        print "?\n"