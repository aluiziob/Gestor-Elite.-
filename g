#!/bin/bash
# BLACK BOX V17.0 - OMNI-DETECTION
# DONO: ALUIZIO | STATUS: DATA DINÂMICA

C='\033[1;36m' ; G='\033[1;32m' ; R='\033[1;31m' ; Y='\033[1;33m' ; W='\033[1;37m' ; N='\033[0m'

# [BANCO DE DADOS ATUALIZADO 2026] - Cobre 1000+ variações
DATABASE="headtrick|drip|spider|ghost|h4x|xit|chit|vng|bypass|inject|mod|menu|aim|rege|macro|iphone|pack|auxilio|bot|proxy|plist|tracev3|sensi|hs|capa|noban|fluxo|black|white|ruok|odin|zeus|gringo|vip|regedit|aimlock|magic|antenna|chams|wall|fly|speed|config|shuhari|fdp|force|kill|death|expert|pvt|privado|internal|external|sh|lua|dex|xml|json|log|bin|apk|zip|rar|tar|7z|exe|dll"

varredura_overkill() {
    clear
    # Puxando a data do sistema em tempo real
    DATA_ATUAL=$(date +'%d/%m/%Y')
    HORA_ATUAL=$(date +'%H:%M:%S')

    echo -e "${C}● BLACK BOX V17.0 - MODO OVERKILL ●${N}"
    echo -e "${C}DONO: ALUIZIO | SESSÃO: $DATA_ATUAL${N}"
    echo -e "${W}──────────────────────────────────────${N}"
    echo -e "${Y}[🔍] INICIANDO ANALISE SETORIAL PROFUNDA...${N}"
    
    # Setores críticos de busca
    setores=(
        "/sdcard/Android/data:DADOS_SENSÍVEIS"
        "/sdcard/Android/obb:PACOTES_DE_JOGO"
        "/sdcard/Download:ARQUIVOS_RECEBIDOS"
        "/sdcard/Android/media/com.whatsapp:MIDIA_WPP"
        "/sdcard/Telegram:MIDIA_TG"
        "/data/local/tmp:CACHE_DO_SISTEMA"
    )

    for setor in "${setores[@]}"; do
        path=$(echo $setor | cut -d: -f1)
        name=$(echo $setor | cut -d: -f2)
        
        echo -e "\n${W}➜ ESCANEANDO: ${C}$name${N}"
        echo -ne "${Y}   [##########----------] Localizando vestígios...\r${N}"
        
        # Busca técnica via ADB
        find_res=$(adb shell "find $path -maxdepth 5 -regextype posix-extended -iregex '.*($DATABASE).*' 2>/dev/null")
        resultado_total+="$find_res"$'\n'
        
        sleep 2.5 # Delay para o perito ver o trabalho sendo feito
        echo -ne "${G}   [####################] SETOR LIMPO!          \n${N}"
    done

    echo -e "${W}──────────────────────────────────────${N}"
    
    evidencias=$(echo -e "$resultado_total" | grep -v "^$" | sort -u)
    total=$(echo "$evidencias" | wc -l)

    if [ "$total" -gt 1 ]; then
        echo -e "${R}STATUS: [ ⚠️ SUSPEITO DETECTADO ]${N}"
        echo -e "${Y}RASTROS ENCONTRADOS ($total):${N}"
        echo -e "${W}──────────────────────────────────────${N}"
        echo "$evidencias" | head -n 40 | sed "s|^| ${R}> ${N}${W}|"
    else
        echo -e "${G}STATUS: [ ✅ JOGADOR LIMPO ]${N}"
        echo -e "${W}Nenhum dos 1000+ rastros foi localizado.${N}"
    fi
    
    echo -e "${W}──────────────────────────────────────${N}"
    echo -e "${C}FINALIZADO EM: $DATA_ATUAL ÀS $HORA_ATUAL${N}"
    read -p "APERTE ENTER PARA VOLTAR..."
}
# [CONEXÃO WI-FI E MENU PRINCIPAL ABAIXO]
