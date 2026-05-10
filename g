#!/bin/bash
# BLACK BOX V17.0 - DINAMIC SYSTEM
# DONO: ALUIZIO | DATA: AUTOMÁTICA

C='\033[1;36m' ; G='\033[1;32m' ; R='\033[1;31m' ; Y='\033[1;33m' ; W='\033[1;37m' ; N='\033[0m'

# [BANCO DE DATA MASSIVO ATUALIZADO]
DATABASE="headtrick|drip|spider|ghost|h4x|xit|chit|vng|bypass|inject|mod|menu|aim|rege|macro|iphone|pack|auxilio|bot|proxy|plist|tracev3|sensi|hs|capa|noban|fluxo|black|white|ruok|odin|zeus|gringo|vip|regedit|aimlock|magic|antenna|chams|wall|fly|speed|config|shuhari|fdp|force|kill|death|expert|pvt|privado|internal|external|sh|lua|dex|xml|json|log|bin|apk|zip|rar|tar|7z|exe|dll"

varredura_overkill() {
    clear
    # AQUI A DATA ATUALIZA SOZINHA
    DATA_ATUAL=$(date +'%d/%m/%Y')
    HORA_ATUAL=$(date +'%H:%M:%S')

    echo -e "${C}● BLACK BOX V17.0 - MODO OVERKILL ATIVADO ●${N}"
    echo -e "${C}DONO: ALUIZIO | DATA: $DATA_ATUAL${N}"
    echo -e "${W}──────────────────────────────────────${N}"
    echo -e "${Y}[🔍] INICIANDO VARREDURA PROFUNDA EM TODOS OS SETORES...${N}"
    
    setores=(
        "/sdcard/Android/data:DADOS_DE_APPS"
        "/sdcard/Android/obb:ARQUIVOS_OBB"
        "/sdcard/Download:DOWNLOADS"
        "/sdcard/Android/media/com.whatsapp:WHATSAPP"
        "/sdcard/Telegram:TELEGRAM"
        "/data/local/tmp:TEMPORARIOS"
    )

    for setor in "${setores[@]}"; do
        path=$(echo $setor | cut -d: -f1)
        name=$(echo $setor | cut -d: -f2)
        
        echo -e "\n${W}➜ SETOR: ${C}$name${N}"
        echo -ne "${Y}   [##########----------] Analisando pastas...\r${N}"
        
        find_res=$(adb shell "find $path -maxdepth 5 -regextype posix-extended -iregex '.*($DATABASE).*' 2>/dev/null")
        resultado_total+="$find_res"$'\n'
        
        sleep 2 # O carregamento que você curtiu
        echo -ne "${G}   [####################] CONCLUÍDO!           \n${N}"
    done

    echo -e "${W}──────────────────────────────────────${N}"
    
    evidencias=$(echo -e "$resultado_total" | grep -v "^$" | sort -u)
    total=$(echo "$evidencias" | wc -l)

    if [ "$total" -gt 1 ]; then
        echo -e "${R}STATUS: [ ⚠️ SUSPEITO DETECTADO ]${N}"
        echo -e "${Y}EVIDÊNCIAS ENCONTRADAS ($total):${N}"
        echo -e "${W}──────────────────────────────────────${N}"
        echo "$evidencias" | head -n 40 | sed "s|^| ${R}> ${N}${W}|"
    else
        echo -e "${G}STATUS: [ ✅ JOGADOR LIMPO ]${N}"
    fi
    
    echo -e "${W}──────────────────────────────────────${N}"
    echo -e "${C}RELATÓRIO GERADO EM: $DATA_ATUAL ÀS $HORA_ATUAL${N}"
    read -p "ENTER PARA VOLTAR..."
}
# ... (resto do código de conexão Wi-Fi igual)
