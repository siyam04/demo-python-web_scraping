import requests
from fake_useragent import UserAgent



url = 'http://www.consumerreports.org/cro/a-to-z-index/products/index.htm'                    # input your url here
file_name = 'consumer_reports.txt'              # output file name

user_agent = UserAgent()

page = requests.get(url,headers={'user-agent':user_agent.chrome})
with open(file_name,'w') as file:
    file.write(page.content.decode('utf-8')) if type(page.content) == bytes else file.write(page.content)