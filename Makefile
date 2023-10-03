install:
		#install commands
		pip install --upgrade pip &&\
		pip install -r requirements.txt

# install_gcloud:
# 	curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-448.0.0-linux-x86_64.tar.gz
# 	tar -zxvf google-cloud-cli-448.0.0-linux-x86_64.tar.gz -C ./
# 	./google-cloud-sdk/install.sh

format:
		#format code
		black ./ETLProject-1/*.py
lint:
	#flake8 or pylint
	pylint --disable=R,C ./ETLProject-1/*.py
test:
	#pytest
deploy:
		#deploy
all: install format lint test deploy
