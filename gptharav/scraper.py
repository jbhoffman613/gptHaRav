import scrapy
from bs4 import BeautifulSoup

# Get the text 
# The response to get the English: response.css("span.co_verse").getall()[4]
html_content = ""
soup = BeautifulSoup(html_content, 'html.parser')
text = soup.get_text(separator=' ', strip=True)
print(text)
