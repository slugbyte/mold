build:
	Pipenv build

install: 
	Pipenv install 

dev:
	Pipenv shell

clean:
	rm -rf build dot.egg-info dot/__pycache__

