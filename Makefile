builddev:
	docker-compose -f docker-compose.dev.yml build

startdev:
	docker-compose -f docker-compose.dev.yml up

migrate:
	docker-compose run --rm app sh -c "python manage.py migrate"

migrations:
	docker-compose run --rm app sh -c "python manage.py makemigrations"

unittest:
	docker-compose run --rm app sh -c "black qt qt_core qt_auth && python manage.py test && flake8"

flake:
	docker-compose -f docker-compose.dev.yml run --rm api sh -c "flake8 ."

black:
	docker-compose -f docker-compose.dev.yml run --rm api sh -c "black ."