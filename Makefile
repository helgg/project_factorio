kill-port:
	lsof -ti :8000 | xargs kill -9 || true

tailwind-start: 
	python manage.py tailwind start

django-runserver:
	python manage.py runserver

go: kill-port
	make -j 2 tailwind-start django-runserver
