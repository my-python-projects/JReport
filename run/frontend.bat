@echo off
setlocal

:: Verificar se existe a pasta venv, se não existir deverá ser criada!!
set "diretorio=%~dp0"

:: Verifica se a pasta especificada dentro do diretório atual existe
set "diretorioVerificar=%diretorioAtual%..\frontend\"

cd /d "%diretorioVerificar%"

cmd /c npm install

cmd /c npm run serve

pause

endlocal
