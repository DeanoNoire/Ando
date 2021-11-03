import requests
from bs4 import BeautifulSoup
 
def scrap():
    page = requests.get('http://nightingales.clanweb.eu/pureStates.php') # Getting page HTML through request
    soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup
    
    gate = soup.find(id = "sgate") 
    garage = soup.find(id = "sgarage") 
    return(gate.text,garage.text)