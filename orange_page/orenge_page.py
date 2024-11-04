#オレンジページの中の人参のレシピのリストをスクレイピングしてみました

import requests
from bs4 import BeautifulSoup


res=requests.get('https://www.orangepage.net/recipes/search?utf8=%E2%9C%93&search_recipe%5Bkeyword%5D=%E3%81%AB%E3%82%93%E3%81%98%E3%82%93')
soup=BeautifulSoup(res.text,'html.parser')

recipes = soup.find('div',id='recipe_list',class_='recipesList')
a_tag= recipes.find_all('a')
print([x['href'] for x in a_tag])

