from tokenize import String
import requests
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'

URL_Efood = "https://www.e-food.gr/?__cf_chl_jschl_tk__=3a9d2b8d5da4e58b1b3f102e03774aac76e35d11-1622244863-0-ARiv60aYGNlpN5UEyJlCkjDiJ9TTxevB9Syaxt3wEfBAb9CRDw6lL-8tr7b_qIk6AYcqQvCppLyPh4GWZZGY93ZC7i2pyzQuap9mF0UCBl4mf_Csww9f3nuybQQHRaTMKjcVu9apOpiV7fUwLUohOQTOm5urOG8diBB47imD3MX3LfNf1Cd8Y0il546Ai8TNZDsk8YPDyZnUjITUSlaaMuoMyqCwL0BjytRZvpdy27pMEDSH4rzbo5jSs_vajrGI-YB9tyMrB2a3cZ0JFWIau1SCMbKQ4pqV1GH_ktCIqXORatrnbwipGZ-9K-CMx_VMREp-wCFK4N9aiM8uiKFTseXz3ywWwdoQE_ZPKVlmKWAYXMr1WoT1W1UlfSlCXST9BglxR-WnFlKP_aRzMqDjwv_f9EQNbOmwyD7jtqIix3vVwOITziBbV0BFKcW-CT64cyK_Xbn4f_34zQBdNbLEIao"

page = requests.get(URL_Efood)

soup = BeautifulSoup(page.content, 'html.parser')


results = soup.find_all('h2',string='Athens')

def new_func(results):
    strResults = String(results)
    return strResults

strResults = new_func(results)
print("Hello "+strResults)

#results = soup.find(id='ResultsContainer')
#job_elems = results.find_all('section', class_='card-content')
#print(results)
#python_jobs = results.find_all('h2', string='Python Developer')

#print(python_jobs)
