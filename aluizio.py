import os, time, subprocess

# Cores
R, G, W, B, D, N = '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;34m', '\033[1;30m', '\033[0m'

def header():
    os.system('clear')
    print(f"{R} ■ BLACK BOX SYSTEM v3.0 ■{N}")
    print(f"{D}──────────────────────────────────────────{N}")
    try:
        check = subprocess.check_output("adb devices", shell=True).decode()
        if "device\n" in check:
            print(f" STATUS: {G}DISPOSITIVO CONECTADO{N}")
        else:
            print(f" STATUS: {R}AGUARDANDO CONEXÃO...{N}")
    except:
        print(f" STATUS: {R}ERRO NO ADB{N}")
    print(f"{D}──────────────────────────────────────────{N}")

def scan_deep():
    print(f"\n{B}[🔍] INICIANDO PERÍCIA AVANÇADA...{N}")
    # Lista de rastros que você enviou (Dicionário de Elite)
    termos = [
        "headtrick", "drip", "spider", "ghost", "h4x", "chit", "xit", "shuhari", 
        "vng", "bypass", "inject", "mod", "menu", "aimbot", "aimlock", "magic", 
        "rege", "regedit", "noban", "antiban", "hs", "capa", "sensi", "fluxo", 
        "black", "white", "ruok", "zeus", "odin", "DripClient", "SpiderV7", 
        "BypassMobile", "Auxilio_Mira", "Gringo_XP", "Cheat_Global", "proxy.config",
        "mdm_bypass", "dns_changer", "packet_injector", ".lua"
    ]
    
    # Pastas Críticas
    pastas = [
        "/sdcard/Download", 
        "/sdcard/Android/data", 
        "/sdcard/WhatsApp/Media/WhatsApp\ Documents",
        "/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp\ Documents",
        "/sdcard/Telegram/Telegram\ Documents"
    ]

    encontrados = 0
    for termo in termos:
        print(f"{D}Buscando: {termo}...{N}", end="\r")
        for pasta in pastas:
            # Comando shell para buscar sem travar o script
            cmd = f"adb shell find {pasta} -name '*{termo}*' 2>/dev/null"
            res = subprocess.getoutput(cmd)
            if res:
                print(f"{R}⚠️ DETECTADO: {W}{termo}{N}")
                print(f"{D}{res}{N}")
                encontrados += 1
    
    if encontrados == 0:
        print(f"\n{G}✅ NENHUM RASTRO ENCONTRADO NAS PASTAS CRÍTICAS.{N}")
    else:
        print(f"\n{R}🚨 TOTAL DE {encontrados} RASTROS IDENTIFICADOS.{N}")
    input(f"\n{D}Pressione Enter para voltar...{N}")

while True:
    header()
    print(f" [{R}01{N}] {W}PAREAR (CODE 6 DÍGITOS){N}")
    print(f" [{R}02{N}] {W}CONECTAR (IP:PORTA){N}")
    print(f" [{R}03{N}] {W}SCANNER DE LOGS (REAL-TIME){N}")
    print(f" [{R}04{N}] {W}PERÍCIA DE PASTAS (DICIONÁRIO BLACK BOX){N}")
    print(f" [{R}05{N}] {W}DESCONECTAR E RESETAR{N}")
    print(f" [{R}00{N}] {W}SAIR{N}")
    print(f"{D}──────────────────────────────────────────{N}")
    
    op = input(f" {R}BLACK_BOX > {N}")

    if op == '1':
        ip = input(f"\n {W}IP:Porta de Pareio: {N}")
        code = input(f" {W}Código: {N}")
        os.system(f"adb pair {ip} {code}")
        input(f"\n{D}Pressione Enter...{N}")
    elif op == '2':
        ip = input(f"\n {W}IP:Porta de Conexão: {N}")
        os.system(f"adb connect {ip}")
        input(f"\n{D}Pressione Enter...{N}")
    elif op == '3':
        print(f"\n{B}[🔍] ANALISANDO LOGCAT...{N}")
        os.system('adb shell logcat -d | grep -iE "cheat|mod|menu|injector|h4x|regedit"')
        input(f"\n{D}Fim dos Logs. Enter...{N}")
    elif op == '4':
        scan_deep()
    elif op == '5':
        os.system("adb disconnect && adb kill-server && adb start-server")
        print(f"\n{G}Sistema Resetado.{N}")
        time.sleep(2)
    elif op == '0':
        break
