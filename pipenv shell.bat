cd /d %~dp0
@echo off
cd %

@echo off
cls

echo Coloque esto después de ejecutado el ambiente virtual: pipenv run numberLocation.py
echo Abriendo ambiente virtual...

pipenv shell

echo END
PAUSE