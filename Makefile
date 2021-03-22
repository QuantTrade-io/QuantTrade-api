start:
	git pull origin master &&
	docker-compose up --build

migrate:
	docker-compose run --rm app sh -c "python manage.py migrate"

migrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations"

test:
	docker-compose run --rm app sh -c "black qt qt_core qt_auth && python manage.py test && flake8"
