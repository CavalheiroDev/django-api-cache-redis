migrate:
	docker exec app python manage.py migrate

makemigrations:
	docker exec app python manage.py makemigrations