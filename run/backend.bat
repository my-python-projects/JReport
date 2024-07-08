@echo off
setlocal

:: Verificar se existe a pasta venv, se não existir deverá ser criada!!
set "diretorio=%~dp0"

:: Verifica se a pasta especificada dentro do diretório atual existe
set "diretorioVerificar=%diretorio%..\backend\"

if not exist "%diretorioVerificar%venv" (
    python -m venv "%diretorioVerificar%venv"
) 

cd /d "%diretorioVerificar%"

:: 
call venv\Scripts\activate

pip install --no-deps -r requirements.txt

python app.py

:: Mantém a janela aberta após a execução do script
pause

endlocal
pause
