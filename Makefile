migrate:
	docker exec app python manage.py migrate

makemigrations:
	docker exec app python manage.py makemigrations

populate:
	docker exec app python manage.py runscript populate_product