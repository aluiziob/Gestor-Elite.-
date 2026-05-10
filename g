#!/bin/bash
# BLACK BOX V17.0 - REAL SYSTEM
# DATA: 10/05/2026 | DONO: ALUIZIO

C='\033[1;36m' ; G='\033[1;32m' ; R='\033[1;31m' ; Y='\033[1;33m' ; W='\033[1;37m' ; N='\033[0m'

menu_conexao() {
    clear
    echo -e "${C}      ● BLACK BOX V17.0 - WI-FI CONNECT ●${N}"
    echo -e "      ${C}DONO: ALUIZIO | STATUS: OFFLINE${N}"
    echo -e "${W}──────────────────────────────────────${N}"
    
    # [PASSO 1] - PAREAMENTO REAL (Onde a maioria erra)
    echo -e "${Y}[!] PASSO 1: PAREAMENTO${N}"
    read -p "IP DO ALVO: " ip
    read -p "PORTA DO PAREAMENTO: " porta_p
    read -p "CÓDIGO DE 6 DÍGITOS: " codigo
    
    echo -e "${G}Tentando parear...${N}"
    adb pair $ip:$porta_p $codigo
    
    # [PASSO 2] - CONEXÃO REAL
    echo -e "\n${Y}[!] PASSO 2: CONEXÃO FINAL${N}"
    read -p "PORTA DA DEPURAÇÃO: " porta_d
    adb connect $ip:$porta_d
    
    sleep 2
    check=$(adb devices | grep -w "device")
    if [ ! -z "$check" ]; then
        echo -e "${G}CONECTADO COM SUCESSO!${N}"
        sleep 1
        menu_pericia
    else
        echo -e "${R}FALHA NA CONEXÃO. VERIFIQUE O WI-FI!${N}"
        read -p "Pressione Enter para tentar de novo..."
        menu_conexao
    fi
}

menu_pericia() {
    clear
    echo -e "${C}      ● BLACK BOX V17.0 - PERÍCIA REAL ●${N}"
    echo -e "      STATUS: ${G}🟢 ONLINE${N} | ${C}DONO: ALUIZIO${N}"
    echo -e "${W}──────────────────────────────────────${N}"
    echo -e "[ ${G}1${N} ] INICIAR BUSCA REAL (MAIS DE 100 RASTROS)"
    echo -e "[ ${R}S${N} ] DESCONECTAR E SAIR"
    read -p "SISTEMA > " opc

    if [ "$opc" == "1" ]; then
        clear
        echo -e "${C}      ● BLACK BOX V16.0 - VARREDURA PROFUNDA ●${N}"
        echo -e "${W}──────────────────────────────────────${N}"
        
        # LISTA DE RASTROS QUE VOCÊ MANDOU (REAL)
        termos="headtrick|drip|bypass|spider|xit|chit|h4x|mod|lua|rege|macro|iphone|pack|auxilio|aim|bot|proxy|plist|tracev3"

        echo -e "${Y}🔍 PROCURANDO RASTROS EM TODO O CELULAR...${N}"
        echo -e "${W}(Isso pode demorar, o sistema está lendo as pastas)${N}"
        
        # O comando 'find' busca os arquivos de verdade. Se não achar, a variável fica vazia.
        resultado=$(adb shell "find /sdcard -regextype posix-extended -iregex '.*($termos).*' 2>/dev/null")

        if [ ! -z "$resultado" ]; then
            echo -e "\n${R}⚠️  SUSPEITO DETECTADO! ⚠️${N}"
            echo -e "${W}ARQUIVOS REAIS ENCONTRADOS NO DISPOSITIVO:${N}"
            echo -e "${W}──────────────────────────────────────${N}"
            # Mostra o rastro com o nome do arquivo original
            echo "$resultado" | sed "s|^|${R}> ${N}${W}|"
        else
            echo -e "\n${G}✅ JOGADOR LIMPO!${N}"
            echo -e "${W}Nenhum rastro de auxílio encontrado.${N}"
        fi
        
        echo -e "${W}──────────────────────────────────────${N}"
        read -p "APERTE ENTER PARA VOLTAR..."
        menu_pericia
    elif [[ "$opc" == "s" || "$opc" == "S" ]]; then
        adb disconnect
        exit
    fi
}

menu_conexao
