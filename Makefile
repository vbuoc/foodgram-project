freeze: venv
	pip freeze -> requirements.txt

migrate: venv
	python manage.py makemigrations
	python manage.py migrate

static: venv
	python manage.py collectstatic --noinput --clear

dump: venv
	python manage.py dumpdata --exclude auth.permission --exclude contenttypes > fixtures.json

dockerup: venv
	docker-compose -f docker-compose.yaml up -d

dockerdown: venv
	docker-compose down

dockerinit: venv
	docker-compose -f docker-compose.yaml up -d
	docker-compose -f docker-compose.yaml run --rm web python manage.py createsuperuser
	docker-compose -f docker-compose.yaml run --rm web python manage.py loaddata fixtures.json

gitpush: venv
	git commit -a -m "bugfix docker and settings, fix .env" && git push
