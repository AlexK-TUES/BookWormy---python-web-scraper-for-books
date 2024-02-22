from bs4 import BeautifulSoup as bS
import requests

ciela_url = 'https://www.ciela.com/knigi'

main_page_text = requests.get(ciela_url).text
soup = bS(main_page_text, 'lxml')
for book in soup.find_all('li', class_ = 'item product product-item'):
    book_url = book.find('span', class_ = 'clever-link')['data-link']
    book_price = float(book.find('span', class_ = 'price').text.replace(' лв.','').replace(',','.'))
    book_html = requests.get(book_url).text
    soup = bS(book_html,'lxml')
    info_table = soup.find('table', class_ = 'data table additional-attributes')
    for element in info_table.find_all('td'):
        value = element.text
        key = element.get('data-th')
        print(f"{key}:{value}")
    print("\n")
        

    