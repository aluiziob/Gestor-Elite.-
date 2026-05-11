import os, time

# CORES BLACK BOX
R, W, D, N = '\033[1;31m', '\033[1;37m', '\033[1;30m', '\033[0m'

def menu():
    os.system('clear')
    print(f"{D}██████╗ ██╗      █████╗  ██████╗██╗  ██╗    ██████╗  ██████╗ ██╗  ██╗{N}")
    print(f"{R}██████╔╝██║     ███████║██║     █████╔╝     ██████╔╝██║   ██║ ╚███╔╝ {N}")
    print(f"{D}██████╔╝███████╗██║  ██║╚██████╗██║  ██╗    ██████╔╝╚██████╔╝██╔╝ ██╗{N}")
    print(f"   {W}DESENVOLVIDO POR: {R}ALUIZIO {W}| SERVIDOR: {R}BLACK BOX{N}")
    print(f"{D}──────────────────────────────────────────────────────────────────────{N}")
    print(f"  [{R}01{N}] {W}PAREAR DISPOSITIVO (CÓDIGO DE 6 DÍGITOS){N}")
    print(f"  [{R}02{N}] {W}CONECTAR AO DISPOSITIVO (IP E PORTA){N}")
    print(f"  [{R}03{N}] {W}VER STATUS DA CONEXÃO{N}")
    print(f"  [{R}04{N}] {W}SCANNER DE LOGS (BUSCAR CHITS){N}")
    print(f"  [{R}05{N}] {W}DESCONECTAR TUDO{N}")
    print(f"  [{R}06{N}] {W}SAIR{N}")
    print(f"{D}──────────────────────────────────────────────────────────────────────{N}")

while True:
    menu()
    op = input(f" {R}BLACK BOX > {N}")
    if op == '1':
        print(f"\n{R}[!] {W}PASSO 1: PAREAMENTO (Pairing){N}")
        ip = input(f" {W}Digite IP:Porta de Pareamento: {N}")
        code = input(f" {W}Digite o Código de 6 dígitos: {N}")
        os.system(f'adb pair {ip} {code}')
        input(f"\n{D}Pressione ENTER para continuar...{N}")
    elif op == '2':
        print(f"\n{R}[!] {W}PASSO 2: CONEXÃO (Connect){N}")
        ip_port = input(f" {W}Digite IP:Porta de Conexão: {N}")
        os.system(f'adb connect {ip_port}')
        input(f"\n{D}Pressione ENTER para voltar...{N}")
    elif op == '3':
        os.system('adb devices')
        input(f"\n{D}ENTER...{N}")
    elif op == '4':
        print(f"\n{R}[🔍] {W}ANALISANDO REGISTROS DO SISTEMA...{N}")
        # Busca logs específicos de atividades de menus e cheats
        os.system('adb shell logcat -d | grep -iE "cheat|mod|menu|injector|h4x"')
        input(f"\n{D}Fim da análise. ENTER...{N}")
    elif op == '5':
        os.system('adb disconnect')
        print(f"\n{R}[!] {W}Dispositivo desconectado.{N}")
        time.sleep(2)
    elif op == '6':
        break
