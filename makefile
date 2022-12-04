reload:
	make stop; make build; make run
	# make stop; make build; make run-d; make superuser; make logs

run:
	docker-compose up
logs:
	docker-compose logs -f
run-d:
	docker-compose up -d

watch-emails:
	 docker-compose exec    notification_service  python3 utils/consumer.py

stop:
	docker-compose down

clean:
	docker-compose down --remove-orphans --volumes

setup:
	make build; make run

build:
	docker-compose build

test:
	docker-compose exec -T main  python manage.py test  --keepdb

format_with_black:
	black ./main

flake8:
	flake8 ./main --count --select=E9,F63,F7,F82 --show-source --statistics --exclude venv; flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --exclude venv

sort_imports:
	isort .; isort --check --diff .

checks:
	make format_with_black; make flake8; make sort_imports; make test
logs_web:
	docker-compose logs web --tail 10 --follow
build_service_registry:
	cd service_registry; make build; cd ..
grep:
	docker-compose logs web --follow | grep -i $(keyword)




