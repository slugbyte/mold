build:
	Pipenv build

install: 
	Pipenv install 

clean:
	rm -rf build mold.egg-info mold/__pycache__ dev-root

