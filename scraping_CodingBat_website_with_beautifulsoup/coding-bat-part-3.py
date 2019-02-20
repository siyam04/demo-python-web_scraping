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


# part 2

for link in all_links:
    inner_page = requests.get(link,headers={'user-agent':user_agent.chrome})
    inner_soup = BeautifulSoup(inner_page.content,'lxml')
    div = inner_soup.find('div',class_='tabc')
    question_links = [base_url + td.a['href'] for td in div.table.find_all('td')]


# part 3

    for question_link in question_links:
        final_page = requests.get(question_link)
        final_soup = BeautifulSoup(final_page.content, 'lxml')
        indent_div = final_soup.find('div', attrs={'class':'indent'})
        problem_statement = indent_div.table.div.string


        siblings_of_statement = indent_div.table.div.next_siblings

        examples = [sibling for sibling in siblings_of_statement if sibling.string is not None]

        print(problem_statement)
        for example in examples:
            print(example)

        print('\n\n\n')
