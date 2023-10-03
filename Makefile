install:
		#install commands
format:
		#format code
lint:
	#flake8 or pylint
test:
	#pytest
deploy:
		#deploy
all: install format lint test deploy
