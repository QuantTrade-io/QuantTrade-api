start:
	git pull origin master &&
	docker-compose up --build

test:
	docker-compose run --rm app sh -c "python manage.py test && flake8"