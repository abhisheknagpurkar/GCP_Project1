install:
		#install commands
		pip install --upgrade pip &&\
		pip install -r requirements.txt
		
install-mysqlclient:
				sudo apt-get update
				sudo apt-get install mysql-client

# install_gcloud:
# 	curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-448.0.0-linux-x86_64.tar.gz
# 	tar -zxvf google-cloud-cli-448.0.0-linux-x86_64.tar.gz -C ./
# 	./google-cloud-sdk/install.sh

format:
		#format code
		black /workspaces/GCP_Project1/SF_bike-sharing/ETL/Orchestration/*.py /workspaces/GCP_Project1/SF_bike-sharing/ETL/Ingestion/*.py /workspaces/GCP_Project1/SF_bike-sharing/ETL/Load/*.py
lint:
	#flake8 or pylint
	pylint --disable=R,C /workspaces/GCP_Project1/SF_bike-sharing/ETL/Orchestration/*.py /workspaces/GCP_Project1/SF_bike-sharing/ETL/Ingestion/*.py /workspaces/GCP_Project1/SF_bike-sharing/ETL/Load/*.py
test:
	#pytest
deploy:
		#deploy
all: install format lint test deploy
