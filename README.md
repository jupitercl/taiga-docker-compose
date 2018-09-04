### TAIGA DOCKER COMPOSE

Project management web application with scrum in mind! Built on top of Django and AngularJS

## STEP by STEP

- git clone https://github.com/jupitercl/taiga-docker-compose.git
- cd taiga-docker-compose
- docker-compose build
- docker-compose up -d
- docker-compose exec taigaback bash -c "sh /initial_data.sh"
- Go to http://localhost:8000
