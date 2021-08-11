

f = open('urls/links.txt', 'r')
google = []
yandex = []

for link in f:
	if 'yandex.ru/maps' in link or 'yandex.ru/profile' in link or 'yandex.ru/Maps' in link:
		yandex.append(link)
	if 'www.google.ru/maps' in link or 'www.google.com/maps' in link or 'goo.gl/maps' in link:
		google.append(link)
f.close()

f = open('urls/google.txt', 'w')
for g in google:
	f.write(g)
f.close()

f = open('urls/yandex.txt', 'w')
for y in yandex:
	f.write(y)
f.close()