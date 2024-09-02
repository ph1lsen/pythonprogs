import feedparser
import os

# Deine RSS-Feed URL
rss_feed_url = 'ENTER URL'

# RSS-Feed parsen
feed = feedparser.parse(rss_feed_url)

# URLs der Posts extrahieren
urls = [entry.link for entry in feed.entries]

# Aktuelles Verzeichnis abrufen
aktuelles_verzeichnis = os.getcwd()

# Datei zum speichern der URLs
datei_name = os.path.join(aktuelles_verzeichnis, 'extrahierte-urls.txt')

# URLs in die Datei schreiben
with open(datei_name, 'w') as datei:
    for url in urls:
        datei.write(url + '\n')


print(f'Die URLs wurden erfolgreich in die Datei "{datei_name}" gespeichert.')