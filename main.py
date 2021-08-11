from threading import Thread


def yandex_maps():
	import y


def google_maps():
	import g


t1 = Thread(target=yandex_maps)
t2 = Thread(target=google_maps)
t1.start()
t2.start()
t1.join()
t2.join()