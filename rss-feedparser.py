import feedparser


# URL del feed RSS de JotDown
url_base = 'https://www.jotdown.es/feed/'

# Parseo del feed RSS
feed = feedparser.parse(url_base)

print(feed.feed.link)
print('Titulo del feed: ', feed.feed.title)
print('Descripcion del feed: ', feed.feed.description)


for entry in feed.entries:
    print('Titulo de la entrada: ', entry.title)
    print('link de la entrada: ', entry.link)
    print('Fecha de la entrada: ', entry.published)
    print('Descripcion de la entrada: ', entry.description)
    print('que hace: ', entry.published_parsed)
    print('-' * 40)