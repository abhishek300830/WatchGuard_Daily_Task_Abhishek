from bs4 import BeautifulSoup

SIMPLE_HTML = '''<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p class="subtitle">My first paragraph.</p>

<p>My second paragraph.</p>

<ul>
    <li>Abhi</li>
    <li>Kunal</li>
    <li>Kushagra</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


def find_list_items():
    list_items = simple_soup.find_all('li')
    list_items = [li.string for li in list_items]
    print(list_items)


def find_subtitle():
    subtitle = simple_soup.find('p', {"class": "subtitle"})
    print(subtitle)


def find_other_paragraph():
    paragraph = simple_soup.findAll('p')
    other_paragraph = [p for p in paragraph if 'subtitle' not in p.attrs.get('class',[])]
    # in p.attrs.get() if we not found any class it return None or we change it to List
    print(other_paragraph)


find_title()
find_list_items()
find_subtitle()
find_other_paragraph()
