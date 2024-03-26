from bs4 import BeautifulSoup

with open("index.html") as file:
  contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# soup.find_all(name="li") # returns a list of all the li tags

for elm in soup.ul.children:
  print(elm.string)

heading = soup.find(name="h1", id="name")
print(heading)

h3 = soup.find(name="h3", class_="sub_heading")
print(h3)

company_url1 = soup.select_one(selector="p a")
print(company_url1)

company_url2 = soup.select_one(selector="#name")
print(company_url2)

names = soup.select(selector=".name")
print(names)
