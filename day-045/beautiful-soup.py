from bs4 import BeautifulSoup
# 1. get the contents of the HTML file in the form of a string
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup)   # print raw html
# print(soup.prettify()) # format with tabs
print(soup.title)   # get title
print(soup.title.name)
print(soup.title.string)

print(soup.p) # get first paragraph

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)  # list of all anchor tags
# get texts of anchor tags
for tag in all_anchor_tags:
    print(tag.getText())
# list all hrefs (websites)
for tag in all_anchor_tags:
    print(tag.get("href"))

# get first h1 with id = name
heading = soup.find(name="h1", id="name")
print(heading)

# get first h3 with class = heading
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.name)     # get tag name
print(section_heading.get("class"))  # get class name

class_is_heading = soup.find_all(class_="heading")
print(class_is_heading)  # get all items with class = heading

# get all h3 with class = heading
h3_heading = soup.find_all("h3", class_="heading")
print(h3_heading)
# select a specific nested element by tag i.e. p.a
company_url = soup.select_one(selector="p a")
print(company_url)
# get item by id
name = soup.select_one("#name")
print(name)
# get item by class
headings = soup.select(".heading")
print(headings)