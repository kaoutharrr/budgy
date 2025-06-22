
build:
	docker-compose build

startproject:
	docker-compose run web django-admin startproject budget_backend .

up:
	docker-compose up
down:
	docker-compose down

migrate:
	docker-compose run web python manage.py migrate

superuser:
	docker-compose run web python manage.py createsuperuser


shell:
	docker-compose run web python manage.py shell

clean:
	docker-compose down -v --rmi all --remove-orphans
