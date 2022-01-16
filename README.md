Redis Cache:
	Lessons: 
		- Cache can be integrated and used for both full blown pages or explicity for custom data storage
		- Implicit cache is established by adding middleware
		- Due to automatic setup of implicit cache, it was caching the page and did not let the code run
	Challenges:
		- figure out if a page resulted from a cache or not

MySQL DB:
	Lessons:
		- MySQL base image has all the ingredients to set itself up from key environment variables. 
		- Do not use the default root username, otherwise the container does not fire up
		- The port settings is automatic and does not need to be mentioned everywhere as default port is 3306. Since Docker containers share the network everything works fine
	Challenges:
		- Repeat with MariaDB

Django:
	Lessons:
		- Image: use the appropriate image with the django version. the alpine image alone is currently 3.10 and django 3.2 although officially supports 3.10 but I got issues of backports.zoneinfo
		- The package manager is called 'apk' in alpine and some key libraries would be needed for python development
		- To see the stdout and stderr output on the screen, use environment variable pythonunbuffered, so it flushes out all the output to the console immidiately. Obviously this setting is meant for development alone
		- If django runserver does not connect to the database, the container network environment is not set and hence results in unreachable container from the web browser
		- migrations are run one off after the containers start
	Links:
		- Useful Medium article. https://medium.com/@minghz42/docker-setup-for-django-on-mysql-1f063c9d16a0
		- Useful Django Deployment. https://www.digitalocean.com/community/tutorials/how-to-build-a-django-and-gunicorn-application-with-docker
	Challenges:
		- How to produce migrations. Make migration had to be run again outside the containers in a different environment. How does making new migrations work in development? the issue is that the migrations require the setup of the django environment, however, django environment is a container and any migrations produced result in migration inside the container?
		- Also, django development does not seem easy with Docker, what if we need to change the settings, would it recompile the project?

Docker:
	Lessons:
		- Docker has a huge issue with containers that may depend on eachother and there is not a clear way to solve it. In our case the django runserver depended on the db connection to run successfully and hence result in a useless container as db container independently takes time to set up. There does not seem to be a good solution for this. I saw this on docker https://docs.docker.com/compose/startup-order/ which is a third party script to make the app server wait for the db-server to get started
	Challenges:
		- Not sure what 'depends_on' does as it did not help me with docker-compose
		- The problem of docker container dependency may not be a problem if we utilize a production web server like gunicorn/apache rather the runserver which is a development server
	Links:
		- Similar db container ready challenge with postgress https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
