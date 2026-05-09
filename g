#!/bin/bash
# Instala as ferramentas se não tiver
pkg install python android-tools curl -y
# Baixa o seu script novo
curl -sL https://raw.githubusercontent.com/aluiziob/Gestor-Elite.-/main/aluizio.py -o aluizio.py
# Abre o sistema
python aluizio.py
