build:
	sudo docker-compose build

up:
	sudo docker-compose up -d

down:
	sudo docker-compose down

terminal:
	sudo docker-compose run back bash

mysql:
	sudo docker-compose exec db mysql -uadminuser -pfantastic
