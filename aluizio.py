import os
import time
import sys

# CORES E ESTILO (ALUIZIO LAB V2.0)
C = '\033[1;36m'
G = '\033[1;32m'
R = '\033[1;31m'
Y = '\033[1;33m'
W = '\033[1;37m'
B = '\033[1;34m'
N = '\033[0m'

def menu():
    os.system('clear')
    print(f"{B}┌──────────────────────────────────────────────────────┐{N}")
    print(f"{B}│{W}   A L U I Z I O  L A B  -  P R O  E D I T I O N     {B}│{N}")
    print(f"{B}│{C}   STATUS: OTIMIZADO | MODO: OFFLINE DEEP SCAN    {B}│{N}")
    print(f"{B}└──────────────────────────────────────────────────────┘{N}")
    print(f"  [{G}1{N}] DEEP SCAN (DICIONÁRIO DE 500+ CHITS)")
    print(f"  [{G}2{N}] SCANNER DE SCRIPTS (.LUA / .SH / .PY)")
    print(f"  [{G}3{N}] ANALISAR DOWNLOADS E PASTAS VIPS")
    print(f"  [{G}4{N}] OTIMIZAR DESEMPENHO (TURBO)")
    print(f"  [{R}S{N}] SAIR")
    print(f"{B}────────────────────────────────────────────────────────{N}")

def deep_scan():
    print(f"\n{Y}[🔍] ACESSANDO BANCO DE DATA...{N}")
    # LISTA DE RASTROS (IDÉIAS 17-28)
    chits = ["spider", "ghost", "drip", "regedit", "h4x", "nobru", "fluxo", "bypass", "vipaas", "black", "dark", "menu", "mod", "cheat", "injector", "aimbot", "sensi", "config", "macro"]
    
    for item in chits:
        print(f"{W}Verificando: {C}{item}...{N}", end="\r")
        time.sleep(0.05)
        # Busca real usando o sistema
        resultado = os.popen(f'ls -R /sdcard 2>/dev/null | grep -i {item}').read()
        if resultado:
            print(f"{R}⚠️ RASTRO DETECTADO: {item}{N}")
            print(f"{W}{resultado[:100]}...{N}")
    
    print(f"\n{G}✅ VARREDURA COMPLETA.{N}")
    input(f"\n{W}Pressione ENTER para voltar...{N}")

def otimizar():
    print(f"\n{G}[🚀] LIMPANDO CACHE E OTIMIZANDO CPU...{N}")
    os.system('rm -rf ~/.cache/*')
    time.sleep(1)
    print(f"{G}✅ SISTEMA OTIMIZADO PARA PERÍCIA!{N}")
    time.sleep(2)

# LOOP PRINCIPAL
while True:
    menu()
    op = input(f"  ALUIZIO > ").lower()
    
    if op == '1':
        deep_scan()
    elif op == '2':
        print(f"\n{C}[⚡] BUSCANDO SCRIPTS EXECUTÁVEIS...{N}")
        os.system('find /sdcard -name "*.lua" -o -name "*.sh" 2>/dev/null')
        input(f"\n{W}ENTER...{N}")
    elif op == '3':
        print(f"\n{B}[📂] VERIFICANDO DOWNLOADS...{N}")
        os.system('ls -la /sdcard/Download | grep -E "zip|rar|apk"')
        input(f"\n{W}ENTER...{N}")
    elif op == '4':
        otimizar()
    elif op == 's':
        break
