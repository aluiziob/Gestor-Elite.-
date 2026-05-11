import os, time

# Cores limpas para não bugar no Termux
R = '\033[1;31m'
W = '\033[1;37m'
D = '\033[1;30m'
G = '\033[1;32m'
N = '\033[0m'

def menu():
    os.system('clear')
    print(f"{R}  ____  _        _    ____ _  __  ____   ______   __ {N}")
    print(f"{R} | __ )| |      / \  / ___| |/ / | __ ) / _ \ \ / / {N}")
    print(f"{W} |  _ \| |     / _ \| |   | ' /  |  _ \| | | \ V /  {N}")
    print(f"{W} | |_) | |___ / ___ \ |___| . \  | |_) | |_| / ^ \  {N}")
    print(f"{D} |____/|_____/_/   \_\____|_|\_\ |____/ \___/_/ \_\ {N}")
    print(f"{D}──────────────────────────────────────────────────────{N}")
    print(f" {W}DEV: {R}ALUIZIO {N}| {W}SERVER: {R}BLACK BOX{N}")
    print(f"{D}──────────────────────────────────────────────────────{N}")
    print(f" [{R}01{N}] {W}PAREAR DISPOSITIVO (PAIRING CODE){N}")
    print(f" [{R}02{N}] {W}CONECTAR AO DISPOSITIVO (IP:PORTA){N}")
    print(f" [{R}03{N}] {W}DISPOSITIVOS ATIVOS{N}")
    print(f" [{R}04{N}] {W}BUSCAR RASTROS (LOGCAT DEEP SCAN){N}")
    print(f" [{R}05{N}] {W}DESCONECTAR TUDO{N}")
    print(f" [{R}06{N}] {W}SAIR{N}")
    print(f"{D}──────────────────────────────────────────────────────{N}")

while True:
    menu()
    op = input(f" {R}BLACK BOX > {N}")
    
    if op == '1':
        print(f"\n{R}[!] PAREAMENTO{N}")
        ip_pair = input(f" {W}IP:PORTA DE PAREIO: {N}")
        code = input(f" {W}CODIGO DE 6 DIGITOS: {N}")
        os.system(f'adb pair {ip_pair} {code}')
        input(f"\n{D}ENTER para voltar...{N}")
    
    elif op == '2':
        print(f"\n{R}[!] CONEXÃO{N}")
        ip_conn = input(f" {W}IP:PORTA DE CONEXÃO: {N}")
        os.system(f'adb connect {ip_conn}')
        input(f"\n{D}ENTER para voltar...{N}")
        
    elif op == '3':
        print(f"\n{G}[+] STATUS ATUAL:{N}")
        os.system('adb devices')
        input(f"\n{D}ENTER...{N}")
        
    elif op == '4':
        print(f"\n{R}[🔍] PERICIANDO REGISTROS DO ANDROID...{N}")
        # O segredo do KellerSS: ele filtra o logcat por palavras-chave
        os.system('adb shell logcat -d | grep -iE "cheat|mod|menu|injector|h4x|ffh4x|regedit"')
        print(f"\n{G}Análise de Logs concluída.{N}")
        input(f"\n{D}ENTER...{N}")
        
    elif op == '5':
        os.system('adb disconnect')
        print(f"\n{R}Desconectado com sucesso.{N}")
        time.sleep(2)
        
    elif op == '6':
        break
