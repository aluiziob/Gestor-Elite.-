#!/bin/bash
# BLACK BOX V17.0 - BY DONO ALUIZIO
# VERSAO COMPATÍVEL COM TERMUX PLAY STORE

# Cores Elite
C='\033[1;36m' ; G='\033[1;32m' ; R='\033[1;31m' ; W='\033[1;37m' ; N='\033[0m' ; Y='\033[1;33m' ; B='\033[1;34m'

# [IDEIA 21] - Verificação de Dependências Automática
check_deps() {
    if ! command -v adb &> /dev/null; then
        echo -e "${Y}Instalando dependências...${N}"
        pkg update -y && pkg install android-tools openssl-tool curl -y
    fi
}

menu_conexao() {
    clear
    echo -e "${C}      ● BLACK BOX V17.0 - THE FUTURE ●${N}"
    echo -e "      STATUS: ${R}🔴 OFFLINE${N} | ${C}DONO: ALUIZIO${N}"
    echo -e "${W}──────────────────────────────────────${N}"
    # [IDEIA 42] - Cache de IP (Sugestão de uso do anterior)
    read -p "IP DO JOGADOR: " ip_alvo
    read -p "PORTA PAREAMENTO: " p1
    read -p "CÓDIGO (6 DÍGITOS): " c1
    echo -e "${G}[🔗] VINCULANDO...${N}"
    adb kill-server > /dev/null 2>&1
    adb pair $ip_alvo:$p1 $c1
    read -p "PORTA PRINCIPAL: " p2
    adb connect $ip_alvo:$p2
    
    check=$(adb devices | grep -w "device")
    if [ ! -z "$check" ]; then menu_pericia; else sleep 1; menu_conexao; fi
}

menu_pericia() {
    clear
    echo -e "${C}      ● BLACK BOX V17.0 - OFFICIAL ●${N}"
    echo -e "      STATUS: ${G}🟢 ONLINE${N} | ${C}DONO: ALUIZIO${N}"
    # [IDEIA 10] - Mostrar Bateria do Jogador
    bat=$(adb shell dumpsys battery | grep level | cut -d ':' -f2 | tr -d ' ')
    echo -e "      BATERIA ALVO: ${Y}${bat}%${N}"
    echo -e "${W}──────────────────────────────────────${N}"
    echo -e "[ ${G}1${N} ] VARREDURA PROFUNDA (ELITE)"
    echo -e "[ ${G}2${N} ] TIRAR PRINT DA TELA (REMOTO)"
    echo -e "[ ${R}V${N} ] VOLTAR / [ ${R}S${N} ] SAIR"
    read -p "SISTEMA > " opc

    if [ "$opc" == "1" ]; then
        clear
        echo -e "${C}      ● BLACK BOX V17.0 - ANALISE ●${N}"
        echo -e "${C}      DONO: ALUIZIO${N}"
        echo -e "${W}──────────────────────────────────────${N}"
        
        # [IDEIA 1] - Animação de Carregamento Dinâmica
        echo -ne "${Y}Buscando em DATA... [###-------] 30%\r${N}"; sleep 1
        res_data=$(adb shell "find /sdcard/Android/data -maxdepth 5 \( -iname '*headtrick*' -o -iname '*bypass*' -o -iname '*drip*' -o -iname '*h4x*' -o -iname '*rege*' -o -iname '*lua*' -o -iname '*spider*' \)" 2>/dev/null)
        
        echo -ne "${Y}Buscando em OBB...  [######----] 60%\r${N}"; sleep 1
        res_obb=$(adb shell "find /sdcard/Android/obb -maxdepth 5 \( -iname '*main*' -o -iname '*patch*' \)" 2>/dev/null)
        
        echo -ne "${Y}Buscando SYSTEM... [##########] 100%\r${N}"; sleep 1
        res_sys=$(adb shell "find /data/log /sdcard/Download -maxdepth 5 \( -iname '*plist*' -o -iname '*tracev3*' -o -iname '*proxy*' -o -iname '*pack*' \)" 2>/dev/null)

        echo -e "\n\n${W}📋 LAUDO TÉCNICO BLACK BOX:${N}"
        if [ ! -z "$res_data" ] || [ ! -z "$res_obb" ] || [ ! -z "$res_sys" ]; then
            # [IDEIA 2] - Status SUSPEITO
            echo -e "${R}STATUS: [ ⚠️ SUSPEITO DETECTADO ]${N}"
            echo -e "${W}──────────────────────────────────────${N}"
            
            # [IDEIA 3] - Explicação dos Rastros (Dicionário)
            if [[ "$res_sys" == *"plist"* || "$res_sys" == *"proxy"* ]]; then
                echo -e "${B}[!] INFO:${N} Perfil de rede/VPN detectado. Usado para injetar dados via Proxy."
            fi
            if [[ "$res_data" == *"headtrick"* || "$res_data" == *"bypass"* ]]; then
                echo -e "${B}[!] INFO:${N} Auxílio de Mira/Regedit detectado na pasta Data."
            fi

            echo -e "\n${W}EVIDÊNCIAS ENCONTRADAS:${N}"
            echo -e "$res_data\n$res_obb\n$res_sys" | grep -v "^$" | sed 's|.*/||' | sed "s|^| > |"
        else
            echo -e "${G}STATUS: [ ✅ JOGADOR LIMPO ]${N}"
        fi
        echo -e "${W}──────────────────────────────────────${N}"
        # [IDEIA 7] - Carimbo de Data/Hora
        echo -e "${C}DATA: $(date +'%d/%m/%Y, %H:%M:%S')${N}"
        read -p "APERTE ENTER PARA VOLTAR..."
        menu_pericia

    elif [ "$opc" == "2" ]; then
        # [IDEIA 26] - Print Screen Remoto
        echo -e "${Y}Capturando tela do jogador...${N}"
        adb shell screencap -p /sdcard/screen.png
        adb pull /sdcard/screen.png ~/screen_$(date +%H%M).png
        echo -e "${G}Print salvo na sua pasta principal do Termux!${N}"
        read -p "ENTER para voltar..."
        menu_pericia

    elif [[ "$opc" == "v" || "$opc" == "V" ]]; then adb disconnect > /dev/null 2>&1; menu_conexao;
    elif [[ "$opc" == "s" || "$opc" == "S" ]]; then exit; fi
}

check_deps
menu_conexao
