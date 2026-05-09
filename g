#!/bin/bash
# BLACK BOX V15.5 - MODO AGILIDADE TOTAL
clear
echo -e "\033[1;36m      ● BLACK BOX V15.5 - ELITE ●\033[0m"
echo -e "\033[1;37m──────────────────────────────────────\033[0m"

# 1. Pega o IP rápido
read -p "$(echo -e "\033[1;37mIP do Jogador: \033[0m")" ip_alvo

# 2. Pareamento Instantâneo (Igual ao KellerSS)
echo -e "\n\033[1;36m[1] PAREAMENTO\033[0m"
read -p "Porta: " p1
read -p "Código: " c1
echo -e "\033[1;32m[🔗] Sincronizando...\033[0m"
adb kill-server > /dev/null 2>&1
adb pair $ip_alvo:$p1 $c1

# 3. Conexão Final
echo -e "\n\033[1;36m[2] CONEXÃO\033[0m"
read -p "Porta Final: " p2
adb connect $ip_alvo:$p2

# 4. Verificação e Menu de Perícia
echo -e "\n\033[1;32m✅ DISPOSITIVO VINCULADO!\033[0m"
echo -e "\033[1;37m──────────────────────────────────────\033[0m"
echo -e "[ 1 ] GERAR LAUDO DE W.O."
echo -e "[ S ] SAIR"
read -p "ALUIZIO > " opc

if [ "$opc" == "1" ]; then
    echo -e "\n\033[1;31m☢️  BUSCANDO PROVAS... ☢️\033[0m"
    adb shell find /sdcard/Android/data /sdcard/Download -iname '*lua*' -o -iname '*h4x*' -o -iname '*mod*'
    echo -e "\033[1;37m──────────────────────────────────────\033[0m"
    read -p "Enter para concluir..."
fi
