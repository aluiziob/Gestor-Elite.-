#!/bin/bash
# BLACK BOX V16.0 - THE FUTURE
C='\033[1;36m' ; G='\033[1;32m' ; R='\033[1;31m' ; W='\033[1;37m' ; N='\033[0m'

menu_conexao() {
    clear
    echo -e "${C}      ● BLACK BOX V16.0 - OFFICIAL ●${N}"
    echo -e "      STATUS: ${R}🔴 OFFLINE${N}"
    echo -e "      ${C}DONO: ALUIZIO${N}"
    echo -e "${W}──────────────────────────────────────{N}"
    read -p "$(echo -e "${W}IP DO JOGADOR: ${N}")" ip_alvo
    echo -e "\n${C}[1] SINCRONIZAÇÃO INSTANTÂNEA${N}"
    read -p "PORTA PAREAMENTO: " p1
    read -p "CÓDIGO (6 DÍGITOS): " c1
    echo -e "${G}[🔗] VINCULANDO...${N}"
    adb kill-server > /dev/null 2>&1
    adb pair $ip_alvo:$p1 $c1
    echo -e "\n${C}[2] CONEXÃO FINAL${N}"
    read -p "PORTA PRINCIPAL: " p2
    adb connect $ip_alvo:$p2
    
    check=$(adb devices | grep -w "device")
    if [ ! -z "$check" ]; then
        menu_pericia
    else
        echo -e "${R}❌ ERRO NA CONEXÃO. REINICIANDO...${N}"
        sleep 1
        menu_conexao
    fi
}

menu_pericia() {
    clear
    echo -e "${C}      ● BLACK BOX V16.0 - OFFICIAL ●${N}"
    echo -e "      STATUS: ${G}🟢 ONLINE${N}"
    echo -e "      ${C}DONO: ALUIZIO${N}"
    echo -e "${W}──────────────────────────────────────{N}"
    echo -e "[ ${G}1{N} ] EXECUTAR PENTE FINO (W.O.)"
    echo -e "[ ${R}S{N} ] DESCONECTAR / SAIR"
    echo -e "${W}──────────────────────────────────────{N}"
    read -p "SISTEMA > " opc

    if [ "$opc" == "1" ]; then
        echo -e "\n${R}☢️  ESCANEANDO DISPOSITIVO... ☢️${N}"
        # Busca silenciosa e direta
        provas=$(adb shell find /sdcard/Android/data /sdcard/Download /sdcard/Telegram -maxdepth 4 \( -iname "*lua*" -o -iname "*h4x*" -o -iname "*mod*" -o -iname "*rege*" -o -iname "*white*" \) 2>/dev/null)
        
        echo -e "\n${W}📋 RESULTADO DA VARREDURA:${N}"
        if [ ! -z "$provas" ]; then
            echo -e "${R}STATUS: [ W.O. DETECTADO ]${N}"
            echo -e "${W}JOGADOR DESCLASSIFICADO.${N}"
        else
            echo -e "${G}STATUS: [ JOGADOR LIMPO ]${N}"
        fi
        echo -e "${W}──────────────────────────────────────{N}"
        read -p "ENTER PARA VOLTAR..."
        menu_pericia
    elif [[ "$opc" == "s" || "$opc" == "S" ]]; then
        adb disconnect > /dev/null 2>&1
        exit
    else
        menu_pericia
    fi
}

menu_conexao
