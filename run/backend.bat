@echo off
setlocal

:: Verificar se existe a pasta venv, se não existir deverá ser criada!!
set "diretorio=%~dp0"

:: Verifica se a pasta especificada dentro do diretório atual existe
set "diretorioVerificar=%diretorioAtual%..\backend\"

if not exist "%diretorioVerificar%venv" (
    
    ::echo A pasta existe.
    python -m venv venv
) 

cd /d "%diretorioVerificar%"

pip install -r requirements.txt

python app.py

pause

endlocal
