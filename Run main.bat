echo Ubicacion Carpeta
cd /d %~dp0
@echo off
echo:
@echo on
pipenv shell
echo Ahora ejecuta lo siguiente
pipenv run numberLocation.py
PAUSE