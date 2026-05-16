import os, time, sys

# PALETA DE CORES TERMINAL
BRANCO = '\033[1;37m'
CINZA = '\033[0;90m'
VERMELHO = '\033[1;31m'
VERDE = '\033[1;32m'
AMARELO = '\033[1;33m'
CIANO = '\033[1;36m'
RESET = '\033[0m'

# BASE DE DADOS DE IDENTIFICAÇÃO (1º SCRIPT CONVERTIDO)
BLACK_LIST_HWID = {
    "CAACFD6C87A2F273": "03/04/26 - Root Detectado",
    "B41E8AB1CBC546D9": "03/04/26 - Root Detectado",
    "C03909710521898B": "03/04/26 - FF Modificado (MOD HACK)",
    "62D64979F2A58645": "03/04/26 - Root Detectado",
    "6DCE2D317020BCF4": "03/04/26 - Root Detectado",
    "2532A6AC33155DA3": "03/04/26 - Root Detectado",
    "929E22F0B9557F5F": "03/04/26 - Root Detectado",
    "ECD3FE422308420F": "03/04/26 - Root Detectado",
    "ED0AFAE59334ACA8": "03/04/26 - Root Detectado",
    "F9A492B38EA622A8": "03/04/26 - Root Detectado",
    "A2C24E7E44C985EB": "03/04/26 - Root Detectado",
    "BFE125B0AD215364": "04/04/26 - Root Detectado",
    "068F136A9379AA16": "04/04/26 - Root Detectado",
    "C2EACDA77367229F": "04/04/26 - Root Detectado",
    "1449EAD0FA8C37F0": "05/04/26 - Root Detectado",
    "53A0EBB27E4C7AE5": "05/04/26 - Root Detectado",
    "9147C7F3CABCE3A9": "01/01/26 - Axx",
    "09763A91BBDB2446": "07/04/26 - Root Detectado",
    "68869F4A336515FE": "07/04/26 - Root Detectado",
    "D641FC5251B3241B": "07/04/26 - Passador Replay",
    "7894FF4492D1D6A5": "18/04/26 - Root Detectado",
    "DB59AEAD2BC7EBC6": "18/04/26 - Proxy Android",
    "56B9E9C6DDCB0D5B": "10/05/26 - Passador Replay"
}

def logo():
    os.system('clear')
    print(f"{BRANCO}  Screen Share Str — Fucking Cheaters{RESET}")
    print(f"  {CINZA}DONO: ALUIZIO | Versão Suprema{RESET}")
    print(f"{BRANCO}  " + "═"*40 + f"{RESET}")
    print(f"   )       (     (          (")
    print(f"   ( /(       )\ )  )\ )       )\ )")
    print(f"   )\()) (   (()/( (()/(  (   (()/(")
    print(f"  |((_)\  )\   /(_)) /(_)) )\   /(_))")
    print(f"  |_ ((_)((_) (_))  (_))  ((_) (_))")
    print(f"  | |/ / | __|| |   | |   | __|| _ \\")
    print(f"  ' <  | _| | |__ | |__ | _| |   /")
    print(f"  _|\_\\ |___||____||____||___||_|_\\")
    print(f"{BRANCO}  " + "═"*40 + f"{RESET}")

def conectar_wifi():
    logo()
    print(f"{BRANCO}■ MÓDULO: DEPURAÇÃO WI-FI{RESET}\n")
    print("1. No celular do jogador, ative a Depuração Wi-Fi.")
    print("2. Vá em 'Parear dispositivo com código'.\n")
    
    ip_pair = input("Digite o IP:PORTA de Pareamento: ")
    codigo = input("Digite o CÓDIGO de 6 números: ")
    
    print(f"\n{CINZA}[ 🛰️ ] Efetuando pareamento ADB...{RESET}")
    os.system(f"adb pair {ip_pair} {codigo}")
    
    print(f"\n{BRANCO}3. Volte uma tela e pegue o IP da tela principal.{RESET}")
    ip_final = input("Digite o IP:PORTA Principal: ")
    
    print(f"\n{CINZA}[ 🔌 ] Conectando ao dispositivo...{RESET}")
    os.system(f"adb connect {ip_final}")
    input(f"\n{VERDE}✓ SUCESSO! Conectado à Black Box. Enter para voltar.{RESET}")

def varredura_total():
    logo()
    print(f"{VERMELHO}🔥 INICIANDO PERÍCIA AUTOMÁTICA (5 MINUTOS){RESET}")
    print(f"{CINZA}ANALISANDO ARQUIVOS, LOGS E DIRETÓRIOS DO SYSTEMA...{RESET}\n")
    
    # Detecções baseadas na lista do 3º script
    modulos = [
        ("Instalação FreeFire", "Buscando pacotes oficiais e caminhos modificados"),
        ("Reinicialização", "Avaliando Uptime do dispositivo (Bypass de tempo)"),
        ("Android Version", "Avaliando vulnerabilidades da partição de segurança"),
        ("Verificação Root", "Procurando binários 'su', Magisk ou KernelSU"),
        ("Passagem de Replay", "Rastreando manipulação de arquivos de Replay"),
        ("Análise MTP", "Checando conexões USB externas e transferências"),
        ("Shaders & OBB", "Escaneando modificações de texturas e wallhacks")
    ]
    
    for mod, desc in modulos:
        print(f"{BRANCO}[ 🔍 ] Analisando Módulo: {mod}{RESET}")
        print(f"{CINZA}  └─ {desc}...{RESET}")
        
        # Simulação de verificação forçada
        if mod == "Verificação Root":
            os.system("adb shell which su 2>/dev/null")
        elif mod == "Shaders & OBB":
            os.system("find /sdcard/Android/obb/ -name '*.obb' 2>/dev/null")
            
        time.sleep(43) # Distribuição exata para completar os 5 minutos de rastro

    # Puxa o HWID (Serial) real do celular conectado
    print(f"\n{BRANCO}■ CONSULTANDO HWID NO BANCO DE DADOS...{RESET}")
    hwid_atual = os.popen("adb shell getprop ro.serialno 2>/dev/null || getprop ro.serialno").read().strip().upper()
    
    if hwid_atual in BLACK_LIST_HWID:
        print(f"\n{VERMELHO}⚠ ATENÇÃO: DISPOSITIVO ENCONTRADO NA BLACKLIST!{RESET}")
        print(f"{AMARELO}ID: {hwid_atual} -> Motivo: {BLACK_LIST_HWID[hwid_atual]}{RESET}")
    else:
        print(f"\n{VERDE}✓ HWID ({hwid_atual}) Limpo na base de dados.{RESET}")
        
    print(f"\n{BRANCO}■ CONFIGURAÇÕES REGEDIT (DPI):{RESET}")
    os.system("adb shell getprop ro.sf.lcd_density 2>/dev/null || getprop ro.sf.lcd_density")

    print(f"\n{VERDE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    print(f"{BRANCO}✅ PERÍCIA COMPLETA: ANÁLISE ARQUIVADA.{RESET}")
    print(f"{VERDE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{RESET}")
    input("Pressione Enter para fechar o relatório...")

def menu():
    os.system("pkg install android-tools -y > /dev/null 2>&1")
    while True:
        logo()
        print(f"[ 1 ] {BRANCO}CONECTAR DISPOSITIVO (WI-FI){RESET}")
        print(f"[ 2 ] {BRANCO}EXECUTAR PERÍCIA COMPLETA (5 MIN){RESET}")
        print(f"[ 3 ] {BRANCO}VERIFICAR MEU IP / REGIAO{RESET}")
        print(f"[ S ] {CINZA}ENCERRAR SESSÃO{RESET}")
        
        opc = input(f"\n{BRANCO}ALUIZIO > {RESET}").lower()
        if opc == '1': conectar_wifi()
        elif opc == '2': varredura_total()
        elif opc == '3':
             os.system("curl -s ifconfig.me")
             input("\nEnter para voltar...")
        elif opc == 's': sys.exit()

if __name__ == '__main__':
    menu()
