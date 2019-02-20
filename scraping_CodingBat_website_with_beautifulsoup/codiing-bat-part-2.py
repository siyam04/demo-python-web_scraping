import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


user_agent = UserAgent()
main_url = 'http://codingbat.com/java'
page = requests.get(main_url,headers={'user-agent':user_agent.chrome})
soup = BeautifulSoup(page.content,'lxml')

base_url = 'http://codingbat.com'

all_divs = soup.find_all('div',class_='summ')

all_links = [base_url + div.a['href'] for div in all_divs]

for link in all_links:
    inner_page = requests.get(link,headers={'user-agent':user_agent.chrome})
    inner_soup = BeautifulSoup(inner_page.content,'lxml')
    div = inner_soup.find('div',class_='tabc')
    question_links = [base_url + td.a['href'] for td in div.table.find_all('td')]



