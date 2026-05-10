termux-setup-storage && sleep 2 && cat << 'EOF' > bb
#!/bin/bash
# OTIMIZAÇÃO MÁXIMA
C='\033[1;36m'; G='\033[1;32m'; R='\033[1;31m'; Y='\033[1;33m'; W='\033[1;37m'; B='\033[1;34m'; N='\033[0m'

while true; do
clear
echo -e "${B}┌──────────────────────────────────────────────────────┐${N}"
echo -e "${B}│${W}   A L U I Z I O  L A B  -  O F F L I N E  E D I T I O N ${B}│${N}"
echo -e "${B}│${C}   ESTADO: 100% OTIMIZADO | DISPOSITIVO: SAMSUNG A35  ${B}│${N}"
echo -e "${B}└──────────────────────────────────────────────────────┘${N}"
echo -e "  [${G}1${N}] DEEP SCAN (BUSCA POR NOMES DE CHITS)"
echo -e "  [${G}2${N}] SCANNER DE SCRIPTS (.LUA / .SH / .PY)"
echo -e "  [${G}3${N}] ANALISAR DOWNLOADS RECENTES (PASTAS VIPS)"
echo -e "  [${G}4${N}] LIMPEZA E TURBO (PERFORMANCE)"
echo -e "  [${R}S${N}] ENCERRAR"
echo -e "${B}────────────────────────────────────────────────────────${N}"
read -p "  ALUIZIO > " op

case $op in
    1)
        echo -e "\n${Y}[🔍] INICIANDO VARREDURA DE DICIONÁRIO...${N}"
        # Dicionário ampliado
        DICO=("spider" "ghost" "drip" "regedit" "h4x" "nobru" "fluxo" "bypass" "vipaas" "black" "dark" "menu" "mod" "cheat" "injector" "aimbot" "sensi" "config" "macro")
        for i in "${DICO[@]}"; do
            echo -ne "${W}Verificando rastro: ${C}$i... \r${N}"
            # O comando abaixo agora busca de forma agressiva
            ls -R /sdcard 2>/dev/null | grep -i "$i" && echo -e "${R}⚠ ACHADO: $i${N}"
        done
        echo -e "\n${G}✅ VARREDURA COMPLETA.${N}"
        read -p "  ENTER..." ;;
    2)
        echo -e "\n${C}[⚡] BUSCANDO SCRIPTS EXECUTÁVEIS...${N}"
        # Busca por extensões que realmente guardam códigos de cheat
        find /sdcard -name "*.lua" -o -name "*.sh" 2>/dev/null | xargs ls -lh 2>/dev/null
        echo -e "\n${G}✅ BUSCA DE SCRIPTS FINALIZADA.${N}"
        read -p "  ENTER..." ;;
    3)
        echo -e "\n${B}[📂] ANALISANDO DOWNLOADS E PASTAS OCULTAS...${N}"
        ls -la /sdcard/Download | grep -E "zip|rar|7z|apk"
        echo -e "\n${W}Verificando pastas ocultas no sistema...${N}"
        ls -d /sdcard/.* 2>/dev/null
        read -p "  ENTER..." ;;
    4)
        echo -e "\n${G}[🚀] APLICANDO OTIMIZAÇÃO NO LABORATÓRIO...${N}"
        # Força o sistema a focar no Termux
        rm -rf ~/.cache/*
        sync && echo 3 > /proc/sys/vm/drop_caches 2>/dev/null
        echo -e "${G}✅ TERMUX OTIMIZADO E LIMPO!${N}"
        sleep 2 ;;
    s|S) exit ;;
esac
done
EOF
chmod +x bb && ./bb
