start:
	git pull origin master &&
	docker-compose up --build

test:
	docker-compose run --rm app sh -c "black qt qt_core qt_auth && python manage.py test && flake8"
