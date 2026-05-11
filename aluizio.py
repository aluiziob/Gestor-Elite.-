import os, time, subprocess

# Cores
R, G, W, B, D, N = '\033[1;31m', '\033[1;32m', '\033[1;37m', '\033[1;34m', '\033[1;30m', '\033[0m'

def header():
    os.system('clear')
    print(f"{R} ■ BLACK BOX SYSTEM v4.0 ■{N}")
    print(f"{D}──────────────────────────────────────────{N}")
    try:
        check = subprocess.getoutput("adb devices")
        if "device\n" in check:
            print(f" STATUS: {G}DISPOSITIVO CONECTADO{N}")
        else:
            print(f" STATUS: {R}AGUARDANDO CONEXÃO...{N}")
    except:
        print(f" STATUS: {R}ERRO NO MOTOR ADB{N}")
    print(f"{D}──────────────────────────────────────────{N}")

def barra_progresso(tarefa):
    print(f"\n{W}[+]{N} {tarefa}")
    for i in range(0, 101, 2):
        print(f" {B}[{N}{'#' * (i // 5)}{' ' * (20 - (i // 5))}{B}]{N} {i}%", end="\r")
        time.sleep(0.03)
    print(f"\n{G}[!] {tarefa} CONCLUÍDO.{N}\n")

def scan_deep():
    header()
    barra_progresso("ESCANEANDO MEMÓRIA E LOGS")
    
    # Dicionário explicativo de rastros reais
    rastros = {
        "headtrick": "Mod de auxílio de mira (Aimbot/HS)",
        "drip": "Injetor de funções VIP (Drip Client)",
        "spider": "Menu de trapaça atravessa parede/voar",
        "h4x": "Abreviatura comum para hacks/trapaças",
        "regedit": "Modificação de registro para sensibilidade apelona",
        "bypass": "Script para burlar o Anti-Cheat do jogo",
        "aimlock": "Trava de mira automática no inimigo",
        "lua": "Script de execução externa (Executor Script)",
        "config.xml": "Pode conter modificações de textura ou antena",
        "mdm_bypass": "Perfil para esconder apps instalados",
        "proxy.config": "Usado para desviar tráfego e esconder o IP"
    }
    
    pastas = ["/sdcard/Download", "/sdcard/Android/data", "/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp\ Documents"]
    achados = []

    print(f"{D}Pesquisando por evidências...{N}")
    for termo, motivo in rastros.items():
        for pasta in pastas:
            cmd = f"adb shell find {pasta} -name '*{termo}*' 2>/dev/null"
            res = subprocess.getoutput(cmd)
            if res:
                achados.append(f"{R}ALERTA:{N} {W}{termo}{N}\n{D}LOCAL:{N} {res.splitlines()[0]}\n{Y}MOTIVO:{N} {motivo}\n")

    if not achados:
        print(f"\n{G}✅ NENHUM RASTRO REAL ENCONTRADO NO DISPOSITIVO.{N}")
    else:
        print(f"\n{R}🚨 RELATÓRIO DE PERÍCIA:{N}\n")
        for item in achados:
            print(item)
            print(f"{D}---{N}")
    
    input(f"\n{W}Pressione ENTER para voltar ao menu...{N}")

while True:
    header()
    print(f" [{R}01{N}] {W}PAREAR (CÓDIGO WIRELESS){N}")
    print(f" [{R}02{N}] {W}CONECTAR (IP:PORTA){N}")
    print(f" [{R}03{N}] {W}DEEP SCAN (LOGS + MEMÓRIA){N}")
    print(f" [{R}04{N}] {W}DESCONECTAR E RESETAR{N}")
    print(f" [{R}00{N}] {W}SAIR{N}")
    print(f"{D}──────────────────────────────────────────{N}")
    
    op = input(f" {R}BLACK_BOX > {N}")

    if op == '1':
        ip = input(f"\n IP:Porta: "); code = input(f" Código: ")
        os.system(f"adb pair {ip} {code}"); input("\nENTER...")
    elif op == '2':
        ip = input(f"\n IP:Porta: ")
        os.system(f"adb connect {ip}"); input("\nENTER...")
    elif op == '3':
        scan_deep()
    elif op == '4':
        os.system("adb disconnect && adb kill-server && adb start-server")
        print(f"\n{G}Sistema Resetado.{N}"); time.sleep(2)
    elif op == '0':
        break
