import os, time, sys

# PALETA DE CORES DARK (SÉRIA)
BRANCO = '\033[1;37m'
CINZA = '\033[0;90m'
AZUL_DARK = '\033[0;34m'
VERMELHO_ERRO = '\033[0;31m'
RESET = '\033[0m'

def logo():
    os.system('clear')
    print(f"{BRANCO}")
    print("      ▪️ BLACK BOX ▪️")
    print(f"{CINZA}      ━━━━━━━━━━━━━━━")
    print(f"      [ PERÍCIA TÉCNICA ]")
    print(f"      DESENVOLVIDO POR: ALUIZIO")
    print(f"      ━━━━━━━━━━━━━━━{RESET}")

def varredura_pericial(caminho, alvo):
    print(f"{CINZA}[ ANALISANDO ] > {caminho}{RESET}")
    # O comando find agora é mais lento e mostra exatamente o que está sendo lido
    os.system(f"find {caminho} -name '*{alvo}' 2>/dev/null")
    time.sleep(1.2) # Delay pericial para conferência

def conectar_black_box():
    logo()
    print(f"{BRANCO}■ PROTOCOLO DE ACESSO WIRELESS{RESET}")
    print(f"{CINZA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{BRANCO}1. PAREAMENTO (6 DÍGITOS){RESET}")
    pair_target = input(f"{CINZA}IP:PORTA PAREAR: {RESET}")
    pair_code = input(f"{CINZA}CÓDIGO PAREAR: {RESET}")
    os.system(f"adb pair {pair_target} {pair_code}")
    
    print(f"\n{BRANCO}2. CONEXÃO DE DADOS{RESET}")
    final_target = input(f"{CINZA}IP:PORTA FINAL: {RESET}")
    os.system(f"adb connect {final_target}")
    input(f"\n{CINZA}Acesso Estabelecido. Enter para Continuar...{RESET}")

def analise_profunda():
    logo()
    print(f"{BRANCO}■ INICIANDO EXTRAÇÃO DE DADOS (DEEP SCAN){RESET}")
    print(f"{CINZA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    
    # Busca real e técnica
    varredura_pericial("/sdcard/Download", ".lua")
    varredura_pericial("/sdcard/Android/media", ".lua")
    varredura_pericial("/sdcard/Android/data", ".sh")
    varredura_pericial("/sdcard/Telegram", ".apk")
    
    print(f"\n{BRANCO}■ PROPRIEDADES DE HARDWARE{RESET}")
    print(f"{CINZA}DPI ATUAL:{RESET}", end=" ")
    os.system("adb shell getprop ro.sf.lcd_density 2>/dev/null || getprop ro.sf.lcd_density")
    
    print(f"\n{BRANCO}■ PROCESSOS EM EXECUÇÃO (SUSPEITOS){RESET}")
    os.system("adb shell ps -ef | grep -iE 'cheat|mod|injector|daemon' | grep -v grep")
    
    print(f"\n{CINZA}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{BRANCO}ANÁLISE FINALIZADA.{RESET}")
    input(f"{CINZA}Pressione Enter para Sair do Relatório...{RESET}")

def menu():
    os.system("pkg install android-tools -y > /dev/null 2>&1")
    while True:
        logo()
        print(f"{BRANCO}[ 1 ] CONECTAR ACESSO REMOTO")
        print(f"[ 2 ] EXECUTAR BLACK BOX (ANALISE)")
        print(f"[ 3 ] STATUS DE REDE / IP")
        print(f"{CINZA}[ S ] LOGOUT{RESET}")
        
        opc = input(f"\n{BRANCO}ALUIZIO > {RESET}").lower()
        if opc == '1': conectar_black_box()
        elif opc == '2': analise_profunda()
        elif opc == '3':
             ip = os.popen("curl -s ifconfig.me").read().strip()
             print(f"\n{CINZA}IP DETECTADO: {ip}{RESET}")
             input("\nEnter para voltar...")
        elif opc == 's': sys.exit()

if __name__ == '__main__':
    menu()
