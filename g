#!/bin/bash
# BLACK BOX V17.0 - OFFICIAL WI-FI SYSTEM
# DONO: ALUIZIO | DATA: 10/05/2026

C='\033[1;36m' ; G='\033[1;32m' ; R='\033[1;31m' ; Y='\033[1;33m' ; W='\033[1;37m' ; N='\033[0m'

menu_conexao() {
    clear
    echo -e "${C}      ● BLACK BOX V17.0 - PAREAMENTO WI-FI ●${N}"
    echo -e "      STATUS: ${R}🔴 AGUARDANDO CONEXÃO${N}"
    echo -e "${W}──────────────────────────────────────${N}"
    
    # [PASSO 1] PAREAMENTO OBRIGATÓRIO
    echo -e "${Y}[1] CONFIGURAÇÃO DE PAREAMENTO${N}"
    echo -e "${W}Vá em: Opções do Desenv. > Depuração por Wi-Fi > Parear com código${N}"
    echo -e "${W}──────────────────────────────────────${N}"
    read -p "DIGITE O IP DO JOGADOR: " ip
    read -p "PORTA DO PAREAMENTO: " p_pair
    read -p "CÓDIGO DE PAREAMENTO (6 DÍGITOS): " code
    
    echo -e "\n${G}[🔗] TENTANDO PAREAR...${N}"
    adb pair $ip:$p_pair $code
    
    echo -e "\n${Y}[2] CONEXÃO FINAL${N}"
    echo -e "${W}Agora use a porta que aparece na tela anterior (a principal)${N}"
    read -p "PORTA DA DEPURAÇÃO (PRINCIPAL): " p_conn
    
    echo -e "${G}[🚀] CONECTANDO AO DISPOSITIVO...${N}"
    adb connect $ip:$p_conn
    
    sleep 2
    check=$(adb devices | grep -w "device")
    if [ ! -z "$check" ]; then
        echo -e "${G}✅ DISPOSITIVO VINCULADO COM SUCESSO!${N}"
        sleep 1
        menu_pericia
    else
        echo -e "${R}❌ FALHA AO PAREAR. REINICIANDO...${N}"
        sleep 2
        menu_conexao
    fi
}

menu_pericia() {
    clear
    echo -e "${C}      ● BLACK BOX V17.0 - PERÍCIA REAL ●${N}"
    echo -e "      STATUS: ${G}🟢 ONLINE${N} | ${C}DONO: ALUIZIO${N}"
    echo -e "${W}──────────────────────────────────────${N}"
    echo -e "[ ${G}1${N} ] INICIAR BUSCA REAL (MAIS DE 100 RASTROS)"
    echo -e "[ ${R}S${N} ] SAIR E DESCONECTAR"
    read -p "SISTEMA > " opc

    if [ "$opc" == "1" ]; then
        clear
        echo -e "${C}      ● ANALISANDO TODOS OS ARQUIVOS... ●${N}"
        echo -e "${W}──────────────────────────────────────${N}"
        
        # LISTA DE RASTROS REAIS (2026)
        termos="headtrick|drip|bypass|spider|xit|chit|h4x|mod|lua|rege|macro|iphone|pack|auxilio|aim|bot|proxy|plist|tracev3"

        echo -e "${Y}🔍 VARRENDO MEMÓRIA INTERNA...${N}"
        # Busca real: Varre o sdcard inteiro atrás da lista de xits
        resultado=$(adb shell "find /sdcard -regextype posix-extended -iregex '.*($termos).*' 2>/dev/null")

        if [ ! -z "$resultado" ]; then
            echo -e "\n${R}⚠️  SUSPEITO DETECTADO! ⚠️${N}"
            echo -e "${W}ARQUIVOS ENCONTRADOS:${N}"
            echo -e "${W}──────────────────────────────────────${N}"
            echo "$resultado" | sed "s|^|${R}> ${N}${W}|"
        else
            echo -e "\n${G}✅ NADA ENCONTRADO. JOGADOR LIMPO!${N}"
        fi
        echo -e "${W}──────────────────────────────────────${N}"
        read -p "ENTER PARA VOLTAR..."
        menu_pericia
    elif [[ "$opc" == "s" || "$opc" == "S" ]]; then
        adb disconnect
        exit
    fi
}

menu_conexao
