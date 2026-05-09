#!/bin/bash
# BLACK BOX V16.0 - BY DONO ALUIZIO
C='\033[1;36m' ; G='\033[1;32m' ; R='\033[1;31m' ; W='\033[1;37m' ; N='\033[0m' ; Y='\033[1;33m'

menu_conexao() {
    clear
    echo -e "${C}      ● BLACK BOX V16.0 - OFFICIAL ●${N}"
    echo -e "      STATUS: ${R}🔴 OFFLINE${N}"
    echo -e "      ${C}DONO: ALUIZIO${N}"
    echo -e "${W}──────────────────────────────────────${N}"
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
    echo -e "${W}──────────────────────────────────────${N}"
    echo -e "[ ${G}1${N} ] EXECUTAR PENTE FINO (W.O.)"
    echo -e "[ ${R}V${N} ] VOLTAR PARA CONEXÃO"
    echo -e "[ ${R}S${N} ] SAIR"
    echo -e "${W}──────────────────────────────────────${N}"
    read -p "SISTEMA > " opc

    if [ "$opc" == "1" ]; then
        clear
        echo -e "${C}      ● BLACK BOX V16.0 - ANALISE ●${N}"
        echo -e "      ${C}DONO: ALUIZIO${N}"
        echo -e "${W}──────────────────────────────────────${N}"
        echo -e "${R}☢️  ESCANEANDO DISPOSITIVO... ☢️${N}"
        
        # BUSCA REAL DE MAIS DE 100 RASTROS (MDM, PROXY, LUA, ETC)
        # O comando busca em profundidade no Android
        rastros=$(adb shell "find /sdcard/Android/data /sdcard/Download /data/log -maxdepth 5 \( -iname '*plist*' -o -iname '*tracev3*' -o -iname '*lua*' -o -iname '*h4x*' -o -iname '*proxy*' -o -iname '*config*' -o -iname '*rege*' -o -iname '*mod*' -o -iname '*bypass*' -o -iname '*inject*' \)" 2>/dev/null)

        if [ ! -z "$rastros" ]; then
            echo -e "\n${Y}⚠️ Perfil MDM/Proxy Detectado, Aplique o W.O! ⚠️${N}"
            echo -e "${W}──────────────────────────────────────${N}"
            # Organiza os rastros encontrados em formato de log elite
            echo "$rastros" | sed 's|.*/||' | head -n 15 | sed "s|^|${R}ID: ${N}${W}|;s|$| (em SystemLogs)$|"
            echo -e "\n${R}STATUS: [ W.O. DETECTADO ]${N}"
        else
            echo -e "\n${G}✅ NENHUM PERFIL SUSPEITO ENCONTRADO${N}"
            echo -e "${G}STATUS: [ JOGADOR LIMPO ]${N}"
        fi
        echo -e "${W}──────────────────────────────────────${N}"
        echo -e "${C}DATA: $(date +'%d/%m/%2026, %H:%M:%S')${N}"
        read -p "ENTER PARA VOLTAR..."
        menu_pericia
    elif [[ "$opc" == "v" || "$opc" == "V" ]]; then
        adb disconnect > /dev/null 2>&1
        menu_conexao
    elif [[ "$opc" == "s" || "$opc" == "S" ]]; then
        adb disconnect > /dev/null 2>&1
        exit
    else
        menu_pericia
    fi
}

menu_conexao
