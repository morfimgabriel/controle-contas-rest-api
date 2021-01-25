build:
	sudo docker-compose up --build

test:
	sudo docker-compose exec web coverage run -m pytest -v --cov=./contas --cov-report=term --cov-report=html

