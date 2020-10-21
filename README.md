Install python and pyodbc for sqlserver with ODBC 17

Tutorial para Ubuntu 18.04

apt-get update

apt-get upgrade

apt-get install python python-pip curl git nano

curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -

curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

apt-get update

ACCEPT_EULA=Y apt-get install msodbcsql17

ACCEPT_EULA=Y apt-get install mssql-tools

apt-get install mssql-tools unixodbc-dev -y

pip install pyodbc
