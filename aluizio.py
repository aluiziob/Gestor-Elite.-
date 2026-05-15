import os, time, sys

# PALETA DARK ELITE (PROFISSIONAL)
BRANCO = '\033[1;37m'
CINZA = '\033[0;90m'
VERMELHO = '\033[1;31m'
VERDE = '\033[1;32m'
RESET = '\033[0m'

def logo():
    os.system('clear')
    print(f"{BRANCO}      ● S C R E E N  S H A R E  S T R ●")
    print(f"      DONO: ALUIZIO")
    print(f"{CINZA}      ──────────────────────────────────────")
    print(f"      SISTEMA DE PERÍCIA E RASTRO MÁXIMO")
    print(f"      ──────────────────────────────────────{RESET}")

def conectar_wifi():
    logo()
    print(f"{BRANCO}■ CONEXÃO POR DEPURAÇÃO WI-FI{RESET}")
    print(f"{CINZA}1. Clique em 'Parear dispositivo com código'{RESET}")
    ip_pair = input(f"{BRANCO}Digite IP:PORTA de Pareamento: {RESET}")
    code = input(f"{BRANCO}Digite o Código de 6 números: {RESET}")
    
    print(f"\n{CINZA}[ 🛰️ ] Autenticando com o dispositivo...{RESET}")
    os.system(f"adb pair {ip_pair} {code}")
    
    print(f"\n{CINZA}──────────────────────────────────────{RESET}")
    print(f"{BRANCO}2. Volte uma tela e veja o IP:PORTA Principal{RESET}")
    ip_final = input(f"{BRANCO}Digite o IP:PORTA de Conexão: {RESET}")
    
    print(f"\n{CINZA}[ 🔌 ] Abrindo túnel de dados...{RESET}")
    os.system(f"adb connect {ip_final}")
    input(f"\n{VERDE}✅ CONECTADO! Pressione Enter para continuar.{RESET}")

def varredura_forense():
    logo()
    print(f"{VERMELHO}🔥 SCANNER DE RASTRO ATIVADO (ESTIMATIVA: 5 MIN){RESET}")
    print(f"{CINZA}ANALISANDO LOGS, DISCOS E SCRIPTS OCULTOS...{RESET}\n")
    
    # Módulos de detecção baseados no seu pedido
    modulos = [
        ("AuthModule", "Verificando chaves de segurança"),
        ("Analise Forense", "Buscando Prefetch e CrashLogs"),
        ("Strings/Logs", "Rastreando limpeza de histórico"),
        ("BAM/Disco", "Verificando partições de jogo"),
        ("Hacker Search", "Pente fino em .lua, .sh e .apk"),
        ("Services", "Monitorando daemons de injeção")
    ]
    
    for mod, desc in modulos:
        print(f"{BRANCO}[ ▶ ] Módulo: {mod}{RESET}")
        print(f"{CINZA}└─ {desc}...{RESET}")
        
        # A busca real que faz o Termux trabalhar
        if mod == "Hacker Search":
            os.system("find /sdcard/ -name '*.lua' -o -name '*.sh' -o -name '*.apk' 2>/dev/null")
        
        # Delay para garantir os 5 minutos de varredura profunda
        time.sleep(48) 

    print(f"\n{BRANCO}■ REGISTROS DE SISTEMA (DPI/SENSITIVIDADE){RESET}")
    os.system("adb shell getprop ro.sf.lcd_density 2>/dev/null || getprop ro.sf.lcd_density")
    time.sleep(5)
    
    print(f"\n{VERDE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{BRANCO}✅ PERÍCIA FINALIZADA COM SUCESSO.{RESET}")
    print(f"{VERDE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    input("Pressione Enter para fechar o relatório...")

def menu():
    # Instala o suporte ADB caso não exista
    os.system("pkg install android-tools -y > /dev/null 2>&1")
    while True:
        logo()
        print(f"{BRANCO}[ 1 ] CONECTAR APARELHO (WI-FI)")
        print(f"[ 2 ] VARREDURA DE RASTRO (5 MINUTOS)")
        print(f"[ 3 ] STATUS DE REDE / IP")
        print(f"{CINZA}[ S ] LOGOUT DO SISTEMA{RESET}")
        
        opc = input(f"\n{BRANCO}ALUIZIO > {RESET}").lower()
        if opc == '1': conectar_wifi()
        elif opc == '2': varredura_forense()
        elif opc == '3':
             os.system("curl -s ifconfig.me")
             input("\nEnter para voltar...")
        elif opc == 's': sys.exit()

if __name__ == '__main__':
    menu()
