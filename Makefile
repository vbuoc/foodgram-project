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
	docker-compose -f main-docker-compose.yaml up -d

dockerbuild: venv
	docker-compose -f main-docker-compose.yaml up -d --build

dockerdown: venv
	docker-compose down

dockerinit: venv
	docker-compose -f main-docker-compose.yaml up -d
	docker-compose -f main-docker-compose.yaml run --rm web python manage.py loaddata fixtures.json
	docker-compose -f main-docker-compose.yaml run --rm web python manage.py createsuperuser

git: venv
	git commit -a -m "(1) ci-cd bug fix" && git push
