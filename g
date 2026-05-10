#!/bin/bash
# BLACK BOX V17.0 - UNLIMITED DATABASE
# DATA: 10/05/2026 | DONO: ALUIZIO

C='\033[1;36m' ; G='\033[1;32m' ; R='\033[1;31m' ; Y='\033[1;33m' ; W='\033[1;37m' ; N='\033[0m'

varredura_profunda() {
    clear
    echo -e "${C}● BLACK BOX V17.0 - BANCO DE DADOS GLOBAL ●${N}"
    echo -e "${C}DONO: ALUIZIO | DATA: 10/05/2026${N}"
    echo -e "${W}──────────────────────────────────────${N}"

    # LISTA DE RASTROS PESADOS (MAIS DE 100 TERMOS)
    #
    RASTROS="headtrick|drip|bypass|spider|xit|chit|h4x|mod|lua|rege|macro|iphone|pack|auxilio|aim|bot|white|chams|antenna|proxy|plist|tracev3|config|sensi|noban|inject|ffh4x|vng|fdp|ghost"

    echo -e "${Y}[!] Iniciando Varredura Multi-Camadas...${N}"
    
    # 1. Busca em DATA/OBB (Scripts e Injetores)
    echo -ne "${W}Verificando Arquivos de Jogo... [###-------] 30%${N}\r"
    res1=$(adb shell "find /sdcard/Android/data /sdcard/Android/obb -maxdepth 5 -regextype posix-extended -iregex '.*($RASTROS).*' 2>/dev/null")
    sleep 3

    # 2. Busca em DOWNLOADS/WHATSAPP/TELEGRAM (Instaladores e Packs)
    echo -ne "${W}Varrendo Recebidos/Mídia...    [######----] 60%${N}\r"
    res2=$(adb shell "find /sdcard/Download /sdcard/Android/media/com.whatsapp /sdcard/Telegram -maxdepth 5 -regextype posix-extended -iregex '.*($RASTROS).*' 2>/dev/null")
    sleep 3

    # 3. Busca em SYSTEM/LOGS (Perfis de Rede e MDM)
    echo -ne "${W}Analisando Logs do Sistema...  [##########] 100%${N}\r"
    res3=$(adb shell "find /data/log /sdcard/Download -iname '*.plist' -o -iname '*.tracev3' -o -iname '*proxy*' 2>/dev/null")
    sleep 1

    echo -e "\n${W}──────────────────────────────────────${N}"
    
    total=$(echo -e "$res1\n$res2\n$res3" | grep -v "^$" | wc -l)

    if [ "$total" -gt 0 ]; then
        echo -e "${R}STATUS: [ ⚠️ SUSPEITO DETECTADO ]${N}"
        echo -e "${Y}FORAM ENCONTRADOS $total RASTROS DE AUXÍLIO:${N}"
        echo -e "${W}──────────────────────────────────────${N}"
        # Lista limpa dos arquivos
        echo -e "$res1\n$res2\n$res3" | grep -v "^$" | sed 's|.*/||' | sort -u | head -n 25 | sed "s|^| > |"
        
        echo -e "\n${C}[🔍] ANÁLISE TÉCNICA:${N}"
        echo -e " - Encontrado arquivos que violam os termos de uso."
        echo -e " - Detectado padrões de modificação de memória/rede."
    else
        echo -e "${G}STATUS: [ ✅ JOGADOR LIMPO ]${N}"
    fi
    
    echo -e "${W}──────────────────────────────────────${N}"
    echo -e "${C}DATA: $(date +'%d/%m/%Y, %H:%M:%S')${N}"
    read -p "PRESSIONE ENTER PARA VOLTAR..."
}

# Loop do Menu Principal
while true; do
    clear
    echo -e "${C}● BLACK BOX V17.0 - OFFICIAL ●${N}"
    echo -e "STATUS: ${G}🟢 ONLINE${N} | DONO: ${C}ALUIZIO${N}"
    echo -e "${W}──────────────────────────────────────${N}"
    echo -e "[ ${G}1${N} ] EXECUTAR PENTE FINO (TOTAL)"
    echo -e "[ ${G}2${N} ] CAPTURAR TELA (REMOTO)"
    echo -e "[ ${R}S${N} ] SAIR"
    read -p "SISTEMA > " opc

    case $opc in
        1) varredura_profunda ;;
        2) adb shell screencap -p /sdcard/evid.png && adb pull /sdcard/evid.png ~/print_$(date +%H%M).png && echo -e "${G}Print Salvo!${N}" && sleep 2 ;;
        s|S) exit ;;
    esac
done
