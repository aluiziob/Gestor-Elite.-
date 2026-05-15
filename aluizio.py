import os, time, subprocess

# Paleta de Cores
R, G, W, B, D, Y, N = '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;34m', '\033[1;30m', '\033[1;33m', '\033[0m'

def header():
    os.system('clear')
    print(f"{B} ■ SCREEN SHARE STR v1.0 ■{N}")
    print(f"{D}──────────────────────────────────────────{N}")
    try:
        # Verifica se o ADB está ativo e dispositivos conectados
        check = subprocess.getoutput("adb devices")
        if "device\n" in check:
            print(f" STATUS: {G}DISPOSITIVO CONECTADO{N}")
        else:
            print(f" STATUS: {R}AGUARDANDO CONEXÃO...{N}")
    except:
        print(f" STATUS: {R}ERRO NO MOTOR ADB{N}")
    print(f" {W}DEV: {B}ALUIZIO {N}| {W}SISTEMA: {B}UNIVERSAL{N}")
    print(f"{D}──────────────────────────────────────────{N}")

def barra_progresso(tempo):
    for i in range(0, 101, 2):
        print(f" {B}[{N}{'#' * (i // 5)}{' ' * (20 - (i // 5))}{B}]{N} {i}%", end="\r")
        time.sleep(tempo)
    print("\n")

def scan_pericia():
    header()
    print(f"{W}[+]{N} INICIANDO VARREDURA ESTRUTURAL...")
    barra_progresso(0.04)
    
    # Banco de dados de rastros reais que você passou
    rastros = {
        "headtrick": "Aimbot/HS - Modificação de mira",
        "drip": "Drip Client - Injetor de funções VIP",
        "spider": "SpiderV7 - Travessia de paredes",
        "ghost": "Ghost Mod - Invisibilidade",
        "bypass": "Bypass - Burlar Anti-Cheat",
        "regedit": "Regedit VIP - Ajuste de sensibilidade",
        "aimlock": "Trava de Mira - Fixação automática",
        "lua": "Script Externo - Executor .lua",
        "shuhari": "Shuhari Injector - Modificação de arquivos",
        "zeus": "Odin/Zeus - Painel de controle",
        "mdm_bypass": "Perfil Oculto - Ocultação de apps",
        "proxy.config": "Proxy/VPN - Desvio de tráfego"
    }
    
    pastas = [
        "/sdcard/Download", 
        "/sdcard/Android/data", 
        "/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp\ Documents",
        "/sdcard/Telegram/Telegram\ Documents",
        "/sdcard/Android/obb"
    ]
    
    achados = []

    print(f"{D}Analisando logs e diretórios...{N}")
    for rastro, info in rastros.items():
        print(f" {W}Buscando:{N} {D}{rastro}{N}", end="\r")
        for pasta in pastas:
            # Comando find para busca real via ADB
            cmd = f"adb shell find {pasta} -name '*{rastro}*' 2>/dev/null"
            res = subprocess.getoutput(cmd)
            if res and "/" in res:
                for line in res.splitlines():
                    if line.strip() and not "denied" in line:
                        achados.append(f"{R}ALERTA:{N} {W}{rastro}{N}\n{D}LOCAL:{N} {line}\n{Y}MOTIVO:{N} {info}")

    header()
    if not achados:
        print(f"{G}✅ RESULTADO: DISPOSITIVO LIMPO.{N}")
    else:
        print(f"{R}🚨 EVIDÊNCIAS ENCONTRADAS:{N}")
        print(f"{D}──────────────────────────────────────────{N}")
        for item in achados:
            print(item)
            print(f"{D}---{N}")
        print(f"{B}TOTAL:{N} {len(achados)} rastros.")
    
    input(f"\n{W}Pressione ENTER para sair...{N}")

while True:
    header()
    print(f" [{B}01{N}] {W}PAREAR (CODE WIRELESS){N}")
    print(f" [{B}02{N}] {W}CONECTAR (IP:PORTA){N}")
    print(f" [{B}03{N}] {W}DEEP SCAN (PERÍCIA){N}")
    print(f" [{B}04{N}] {W}LIMPAR ADB / RESET{N}")
    print(f" [{B}00{N}] {W}SAIR{N}")
    print(f"{D}──────────────────────────────────────────{N}")
    
    op = input(f" {B}STR > {N}")

    if op == '1':
        ip = input(f"\n IP:Porta: "); code = input(f" Código: ")
        os.system(f"adb pair {ip} {code}")
        input("\nClique Enter...")
    elif op == '2':
        ip = input(f"\n IP:Porta: ")
        os.system(f"adb connect {ip}")
        input("\nClique Enter...")
    elif op == '3':
        scan_pericia()
    elif op == '4':
        os.system("adb disconnect && adb kill-server && adb start-server")
        print(f"\n{G}Reset concluído.{N}"); time.sleep(1)
    elif op == '0':
        break
