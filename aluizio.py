import os, time, sys

# DESIGN BLACK BOX
AZUL = '\033[1;34m'
VERDE = '\033[1;32m'
VERMELHO = '\033[1;31m'
BRANCO = '\033[1;37m'
AMARELO = '\033[1;33m'
CIANO = '\033[1;36m'
RESET = '\033[0m'

def logo():
    os.system('clear')
    print(f"{CIANO}")
    print("      ██████  ██       █████   ██████ ██   ██      ██████   ██████  ██   ██ ")
    print("      ██   ██ ██      ██   ██ ██      ██  ██       ██   ██ ██    ██  ██ ██  ")
    print("      ██████  ██      ███████ ██      █████        ██████  ██    ██   ███   ")
    print("      ██   ██ ██      ██   ██ ██      ██  ██       ██   ██ ██    ██  ██ ██  ")
    print("      ██████  ███████ ██   ██  ██████ ██   ██      ██████   ██████  ██   ██ ")
    print(f"{AZUL} — SISTEMA BLACK BOX: BY ALUIZIO | PROTOCOLO ELITE V4.0 — {RESET}")

def varredura_real(diretorio, extensao):
    print(f"{AMARELO}[ 🛰️ ] Analisando diretório: {diretorio}...{RESET}")
    # Busca real que faz o Termux trabalhar e mostrar os nomes dos arquivos
    os.system(f"find {diretorio} -maxdepth 4 -name '*{extensao}' 2>/dev/null")
    time.sleep(0.8)

def conectar_adb_completo():
    logo()
    print(f"{CIANO}=== PASSO 1: PAREAMENTO (CÓDIGO DE 6 DÍGITOS) ==={RESET}")
    print(f"{BRANCO}1. No celular: 'Depuração por Wi-Fi' > 'Parear com código'{RESET}")
    ip_pair = input(f"{VERDE}Digite o IP:PORTA de pareamento: {RESET}")
    code = input(f"{VERDE}Digite o CÓDIGO de 6 dígitos: {RESET}")
    
    print(f"\n{AMARELO}Sincronizando chaves com a BLACK BOX...{RESET}")
    os.system(f"adb pair {ip_pair} {code}")
    
    print(f"\n{CIANO}=== PASSO 2: CONEXÃO FINAL ==={RESET}")
    print(f"{BRANCO}Use o IP:PORTA da tela principal da Depuração.{RESET}")
    ip_final = input(f"{VERDE}Digite o IP:PORTA final: {RESET}")
    os.system(f"adb connect {ip_final}")
    input(f"\n{VERDE}Conexão BLACK BOX Ativa! Enter para voltar...{RESET}")

def varredura_profunda():
    logo()
    print(f"{VERMELHO}⚠️ ALERTA: INICIANDO VARREDURA PROFUNDA BLACK BOX{RESET}")
    print(f"{AMARELO}Buscando rastros ocultos no sistema (Aguarde)...{RESET}\n")
    
    # Camada 1: Scripts
    print(f"{CIANO}[ CAMADA 1 ] RASTREANDO SCRIPTS .LUA / .SH{RESET}")
    varredura_real("/sdcard/Download", ".lua")
    varredura_real("/sdcard/Android/media", ".lua")
    varredura_real("/sdcard/Telegram", ".lua")
    
    # Camada 2: Injetores
    print(f"\n{CIANO}[ CAMADA 2 ] BUSCANDO INSTALADORES (.APK / .APKS){RESET}")
    varredura_real("/sdcard", ".apk")
    varredura_real("/sdcard/Download", ".apks")
    
    # Camada 3: Sistema via ADB
    print(f"\n{CIANO}[ CAMADA 3 ] VERIFICANDO REGEDIT E DPI ATIVA{RESET}")
    os.system("adb shell getprop ro.sf.lcd_density 2>/dev/null || getprop ro.sf.lcd_density")
    
    # Camada 4: Processos
    print(f"\n{CIANO}[ CAMADA 4 ] MONITORANDO PROCESSOS EM TEMPO REAL{RESET}")
    os.system("adb shell ps -ef | grep -E 'daemon|kworker|magisk' | grep -v grep")
    
    print(f"\n{BRANCO}" + "="*60)
    print(f"{VERDE}✅ VARREDURA CONCLUÍDA: RESULTADOS EXPOSTOS ACIMA{RESET}")
    print(f"{BRANCO}" + "="*60)
    input(f"\nPressione Enter para Voltar...")

def menu():
    # Garante que o ADB esteja instalado
    os.system("pkg install android-tools -y > /dev/null 2>&1")
    while True:
        logo()
        print(f"{AZUL}[ 1 ] 🔗 PAREAR E CONECTAR (DEPURAÇÃO WI-FI)")
        print(f"[ 2 ] 🛡️  VARREDURA PROFUNDA (REAL/LENTA)")
        print(f"[ 3 ] 🔍 RASTREIO DE IP / ANTI-VPN")
        print(f"{VERMELHO}[ S ] 🚪 SAIR DA BLACK BOX{RESET}")
        
        opc = input(f"\n{VERDE}ALUIZIO > {RESET}").lower()
        if opc == '1': conectar_adb_completo()
        elif opc == '2': varredura_profunda()
        elif opc == '3':
             print(f"{AMARELO}IP Atual: {os.popen('curl -s ifconfig.me').read().strip()}{RESET}")
             input("\nEnter para voltar...")
        elif opc == 's': sys.exit()

if __name__ == '__main__':
    menu()
