#!/bin/bash
# BLACK BOX V16.0 - BY DONO ALUIZIO
C='\033[1;36m' ; G='\033[1;32m' ; R='\033[1;31m' ; W='\033[1;37m' ; N='\033[0m' ; Y='\033[1;33m'

menu_conexao() {
    clear
    echo -e "${C}      ● BLACK BOX V16.0 - OFFICIAL ●${N}"
    echo -e "      STATUS: ${R}🔴 OFFLINE${N} | ${C}DONO: ALUIZIO${N}"
    echo -e "${W}──────────────────────────────────────${N}"
    read -p "IP DO JOGADOR: " ip_alvo
    read -p "PORTA PAREAMENTO: " p1
    read -p "CÓDIGO (6 DÍGITOS): " c1
    adb kill-server > /dev/null 2>&1
    adb pair $ip_alvo:$p1 $c1
    read -p "PORTA PRINCIPAL: " p2
    adb connect $ip_alvo:$p2
    
    check=$(adb devices | grep -w "device")
    if [ ! -z "$check" ]; then menu_pericia; else sleep 1; menu_conexao; fi
}

menu_pericia() {
    clear
    echo -e "${C}      ● BLACK BOX V16.0 - OFFICIAL ●${N}"
    echo -e "      STATUS: ${G}🟢 ONLINE${N} | ${C}DONO: ALUIZIO${N}"
    echo -e "${W}──────────────────────────────────────${N}"
    echo -e "[ ${G}1${N} ] INICIAR VARREDURA COMPLETA (SEM PRESSA)"
    echo -e "[ ${R}V${N} ] VOLTAR / [ ${R}S${N} ] SAIR"
    read -p "SISTEMA > " opc

    if [ "$opc" == "1" ]; then
        clear
        echo -e "${C}      ● BLACK BOX V16.0 - ANALISE PROFUNDA ●${N}"
        echo -e "${W}──────────────────────────────────────${N}"
        
        # 1. Feedback visual de onde está procurando
        echo -e "${Y}🔍 BUSCANDO EM: /sdcard/Android/data...${N}"
        data_res=$(adb shell "find /sdcard/Android/data -maxdepth 5 \( -iname '*lua*' -o -iname '*h4x*' -o -iname '*rege*' -o -iname '*mod*' -o -iname '*inject*' \)" 2>/dev/null)
        
        echo -e "${Y}🔍 BUSCANDO EM: /sdcard/Android/obb...${N}"
        obb_res=$(adb shell "find /sdcard/Android/obb -maxdepth 5 \( -iname '*main*' -o -iname '*patch*' \)" 2>/dev/null)
        
        echo -e "${Y}🔍 BUSCANDO PERFIS MDM / PROXY...${N}"
        sys_res=$(adb shell "find /data/log /sdcard/Download -maxdepth 5 \( -iname '*plist*' -o -iname '*tracev3*' -o -iname '*proxy*' \)" 2>/dev/null)

        echo -e "\n${W}📋 RELATÓRIO TÉCNICO (ENTENDA O RASTRO):${N}"
        if [ ! -z "$data_res" ] || [ ! -z "$obb_res" ] || [ ! -z "$sys_res" ]; then
            echo -e "${R}STATUS: [ ⚠️ SUSPEITO DETECTADO ]${N}"
            echo -e "${W}──────────────────────────────────────${N}"
            
            # Explicação do que foi achado para o perito não ficar perdido
            if [ ! -z "$sys_res" ]; then
                echo -e "${Y}[!] PERFIL DE REDE:${N} Arquivos .plist/.trace detectados. Indica uso de VPN/Proxy para burlar o ping ou injetar dados via rede."
            fi
            if [ ! -z "$data_res" ]; then
                echo -e "${Y}[!] SCRIPTS LUA/H4X:${N} Arquivos modificados na pasta DATA que alteram a sensibilidade ou mira."
            fi
            if [ ! -z "$obb_res" ]; then
                echo -e "${Y}[!] OBB MODIFICADA:${N} Arquivo principal do jogo foi alterado (comum em antiarena/corpo branco)."
            fi
            
            echo -e "\n${W}ARQUIVOS ENCONTRADOS:${N}"
            echo -e "$data_res\n$obb_res\n$sys_res" | grep -v "^$" | sed 's|.*/||' | sed "s|^| > |"
        else
            echo -e "${G}STATUS: [ ✅ JOGADOR LIMPO ]${N}"
        fi
        echo -e "${W}──────────────────────────────────────${N}"
        echo -e "${C}DATA: $(date +'%d/%m/%Y, %H:%M:%S')${N}"
        read -p "PRESSIONE ENTER PARA VOLTAR..."
        menu_pericia
    elif [[ "$opc" == "v" || "$opc" == "V" ]]; then adb disconnect > /dev/null 2>&1; menu_conexao;
    elif [[ "$opc" == "s" || "$opc" == "S" ]]; then exit; fi
}
menu_conexao
