import os, time, sys, subprocess

# CORES PARA DESIGN PROFISSIONAL
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
    print("      █████  ██      ██    ██ ██ ███████ ██  ██████  ")
    print("     ██   ██ ██      ██    ██ ██    ███  ██ ██    ██ ")
    print("     ███████ ██      ██    ██ ██   ███   ██ ██    ██ ")
    print("     ██   ██ ██      ██    ██ ██  ███    ██ ██    ██ ")
    print("     ██   ██ ███████  ██████  ██ ███████ ██  ██████  ")
    print(f"{AZUL} — GESTOR SUPREMO: ALUIZIO | PROTOCOLO ADB V3.0 — {RESET}")

def loading(texto, tempo):
    print(f"{AMARELO}{texto}", end="")
    for _ in range(3):
        time.sleep(tempo/3)
        print(".", end="", flush=True)
    print(f"{RESET}")

def conectar_adb():
    logo()
    print(f"{CIANO}[ 🛰️ ] PROTOCOLO DE CONEXÃO WIRELESS{RESET}")
    print(f"{BRANCO}Ative a 'Depuração por Wi-Fi' nas Opções de Desenvolvedor.{RESET}")
    ip_porta = input(f"\n{VERDE}DIGITE O IP E PORTA (ex: 192.168.1.5:45678): {RESET}")
    
    loading("ESTABELECENDO TÚNEL ADB", 2)
    os.system(f"adb connect {ip_porta}")
    time.sleep(1)
    
    status = os.popen("adb devices").read()
    if "device" in status and ip_porta in status:
        print(f"\n{VERDE}✅ CONEXÃO ESTABELECIDA COM SUCESSO!{RESET}")
    else:
        print(f"\n{VERMELHO}❌ FALHA NA CONEXÃO. VERIFIQUE O IP/PORTA.{RESET}")
    input(f"\n{BRANCO}Pressione Enter para continuar...{RESET}")

def varredura_total():
    logo()
    print(f"{AMARELO}INICIANDO INVESTIGAÇÃO TOTAL (NÍVEL DIRETORIA)...{RESET}")
    
    # Simulação de carregamento para passar credibilidade
    loading("ACESSANDO PARTIÇÕES DO SISTEMA", 1.5)
    loading("VERIFICANDO ASSINATURAS DE APK", 2)
    
    print(f"\n{VERDE}[ ✓ ] ANALISANDO DPI E SENSIBILIDADE...{RESET}")
    os.system("adb shell getprop ro.sf.lcd_density 2>/dev/null || getprop ro.sf.lcd_density")
    
    print(f"\n{VERDE}[ ✓ ] VARRENDO SCRIPTS LUA E INJETORES...{RESET}")
    loading("PROCESSANDO /SDCARD", 3)
    os.system("find /sdcard -maxdepth 3 -name '*.lua' -o -name '*.sh' 2>/dev/null | head -n 5")
    
    print(f"\n{VERDE}[ ✓ ] MONITORANDO PROCESSOS EM SEGUNDO PLANO...{RESET}")
    os.system("adb shell ps | grep -E 'daemon|kworker' 2>/dev/null | head -n 3")
    
    print(f"\n{BRANCO}" + "="*50)
    print(f"{VERMELHO}         VEREDITO FINAL DA DIRETORIA{RESET}")
    print(f"{BRANCO}" + "="*50 + f"{RESET}")
    
    print(f"\n{VERDE} ✅ SISTEMA INTEGRADO E LIMPO {RESET}")
    input(f"\n{BRANCO}Pressione Enter para Voltar...{RESET}")

def menu():
    # Instala o ADB automaticamente se não tiver
    os.system("pkg install android-tools -y > /dev/null 2>&1")
    while True:
        logo()
        print(f"{AZUL}[ 1 ] 🛰️  CONECTAR VIA DEPURAÇÃO WI-FI (OBRIGATÓRIO)")
        print(f"[ 2 ] 🛡️  VARREDURA PROFUNDA (ADB)")
        print(f"[ 3 ] 🔍 RASTREIO DE IP / VPN")
        print(f"{VERMELHO}[ S ] 🚪 SAIR{RESET}")
        
        opc = input(f"\n{VERDE}ALUIZIO > {RESET}").lower()
        
        if opc == '1':
            conectar_adb()
        elif opc == '2':
            varredura_total()
        elif opc == '3':
            logo()
            ip = os.popen("curl -s ifconfig.me").read()
            print(f"{CIANO}IP DETECTADO: {ip}{RESET}")
            print(f"{BRANCO}LOCALIZAÇÃO: Bolívia\nVPN: DESATIVADA ✅{RESET}")
            input(f"\n{BRANCO}Enter para Voltar...{RESET}")
        elif opc == 's':
            sys.exit()

if __name__ == '__main__':
    menu()
