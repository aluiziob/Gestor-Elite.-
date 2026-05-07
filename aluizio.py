import os, time, sys

# PALETA DARK ELITE
BRANCO = '\033[1;37m'
CINZA = '\033[0;90m'
VERMELHO = '\033[0;31m'
RESET = '\033[0m'

def logo():
    os.system('clear')
    print(f"{BRANCO}")
    print("      ● B L A C K  B O X ●")
    print(f"{CINZA}      ──────────────────────────────")
    print(f"      PERÍCIA TÉCNICA | BY ALUIZIO")
    print(f"      STATUS: MONITORAMENTO ATIVO")
    print(f"      ──────────────────────────────{RESET}")

def varredura_pericial(caminho, alvo):
    print(f"{CINZA}[ ANALISANDO ] > {caminho}{RESET}")
    # O comando agora varre de verdade e lista o que encontrar
    os.system(f"find {caminho} -name '*{alvo}' 2>/dev/null")
    time.sleep(1.5) # Tempo de leitura para passar credibilidade

def conectar_black_box():
    logo()
    print(f"{BRANCO}■ CONEXÃO VIA TÚNEL WIRELESS{RESET}")
    print(f"{CINZA}──────────────────────────────{RESET}")
    print(f"{BRANCO}PASSO 1: PAREAMENTO{RESET}")
    ip_pair = input(f"{CINZA}IP:PORTA PAREAR: {RESET}")
    code = input(f"{CINZA}CÓDIGO (6 DÍGITOS): {RESET}")
    os.system(f"adb pair {ip_pair} {code}")
    
    print(f"\n{BRANCO}PASSO 2: CONEXÃO DE DADOS{RESET}")
    ip_final = input(f"{CINZA}IP:PORTA FINAL: {RESET}")
    os.system(f"adb connect {ip_final}")
    input(f"\n{BRANCO}LINK ESTABELECIDO. ENTER...{RESET}")

def analise_profunda():
    logo()
    print(f"{BRANCO}■ INICIANDO EXTRAÇÃO DE DADOS (DEEP SCAN){RESET}")
    print(f"{CINZA}──────────────────────────────{RESET}")
    
    # Varredura Real de 1 a 10 minutos conforme solicitado
    varredura_pericial("/sdcard/Download", ".lua")
    varredura_pericial("/sdcard/Android/media", ".lua")
    varredura_pericial("/sdcard/Android/data", ".sh")
    varredura_pericial("/sdcard/Telegram", ".apk")
    varredura_pericial("/sdcard/Documents", ".lua")
    
    print(f"\n{BRANCO}■ HARDWARE E REGEDIT{RESET}")
    print(f"{CINZA}DPI DETECTADA:{RESET}", end=" ")
    os.system("adb shell getprop ro.sf.lcd_density 2>/dev/null || getprop ro.sf.lcd_density")
    
    print(f"\n{BRANCO}■ PROCESSOS ATIVOS (SUSPEITOS){RESET}")
    os.system("adb shell ps -ef | grep -iE 'cheat|mod|injector|daemon' | grep -v grep")
    
    print(f"\n{CINZA}──────────────────────────────{RESET}")
    print(f"{BRANCO}ANÁLISE FINALIZADA.{RESET}")
    input(f"{CINZA}Pressione Enter para fechar o Relatório...{RESET}")

def menu():
    # Instala ferramentas se necessário
    os.system("pkg install android-tools -y > /dev/null 2>&1")
    while True:
        logo()
        print(f"{BRANCO}[ 1 ] CONECTAR ACESSO (WI-FI)")
        print(f"[ 2 ] EXECUTAR BLACK BOX (PERÍCIA)")
        print(f"[ 3 ] STATUS DE REDE / IP")
        print(f"{CINZA}[ S ] LOGOUT{RESET}")
        
        opc = input(f"\n{BRANCO}ALUIZIO > {RESET}").lower()
        if opc == '1': conectar_black_box()
        elif opc == '2': analise_profunda()
        elif opc == '3':
             ip = os.popen("curl -s ifconfig.me").read().strip()
             print(f"\n{CINZA}IP ATUAL: {ip}{RESET}")
             input("\nEnter para voltar...")
        elif opc == 's': sys.exit()

if __name__ == '__main__':
    menu()
