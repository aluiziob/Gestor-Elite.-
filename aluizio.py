import os, time, sys

# CORES PARA O VISUAL FICAR TOP
C = '\033[1;36m' ; G = '\033[1;32m' ; R = '\033[1;31m' ; W = '\033[1;37m' ; N = '\033[0m'

conectado = False
ip_alvo = ""

def logo():
    os.system('clear')
    print(f"{C}      ● BLACK BOX V15.5 - MODO KELLER ●{N}")
    print(f"      STATUS: " + (f"{G}🟢 ONLINE{N}" if conectado else f"{R}🔴 OFFLINE{N}"))
    print(f"{W}──────────────────────────────────────{N}")

def conectar():
    global conectado, ip_alvo
    logo()
    
    # Se ainda não digitou o IP do jogador, pede agora
    if not ip_alvo:
        ip_alvo = input(f"{W}Digite o IP do Jogador (Ex: 192.168.100.5): {N}")

    print(f"\n{B}CONECTANDO EM: {ip_alvo}{N}")
    print(f"{W}──────────────────────────────────────{N}")
    
    # IGUAL AO VÍDEO: SÓ OS CÓDIGOS RÁPIDOS
    print(f"{C}PASSO 1: PAREAMENTO{N}")
    p1 = input(f"{W}1. PORTA de Pareamento: {N}")
    c1 = input(f"{W}2. CÓDIGO de 6 dígitos: {N}")
    
    print(f"\n{G}[🔗] Sincronizando...{N}")
    os.system("adb kill-server > /dev/null 2>&1")
    os.system(f"adb pair {ip_alvo}:{p1} {c1}")
    
    print(f"\n{C}PASSO 2: CONEXÃO FINAL{N}")
    p2 = input(f"{W}3. PORTA Principal: {N}")
    os.system(f"adb connect {ip_alvo}:{p2}")
    
    check = os.popen("adb devices").read()
    if "device" in check.split('\n')[1]:
        print(f"\n{G}✅ VINCULADO COM SUCESSO!{N}")
        conectado = True
    else:
        print(f"\n{R}❌ FALHA. IP ou Portas erradas.{N}")
        ip_alvo = "" # Reseta para poder digitar o IP certo se errar
        conectado = False
    time.sleep(2)

def pente_fino():
    if not conectado:
        print(f"\n{R}🔴 ERRO: Conecte primeiro!{N}")
        time.sleep(2)
        return
    logo()
    print(f"{R}☢️  BUSCANDO PROVAS DE AUXÍLIO ☢️{N}\n")
    # Busca real que mostra o nome dos arquivos (O que o povo quer ver)
    os.system("adb shell find /sdcard/Android/data /sdcard/Download -iname '*lua*' -o -iname '*h4x*' -o -iname '*mod*' -o -iname '*rege*'")
    print(f"\n{W}──────────────────────────────────────{N}")
    input(f"{W}Enter para voltar...{N}")

def menu():
    while True:
        logo()
        if ip_alvo: print(f"{W}IP ATUAL: {G}{ip_alvo}{N}\n")
        print(f"{W}[ {G}1{W} ] CONECTAR (3 CÓDIGOS)")
        print(f"{W}[ {G}2{W} ] PENTE FINO (LAUDO)")
        print(f"{W}[ {R}S{W} ] SAIR / MUDAR IP")
        opc = input(f"\n{C}ALUIZIO > {N}").lower()
        if opc == '1': conectar()
        elif opc == '2': pente_fino()
        elif opc == 's': 
            global ip_alvo
            ip_alvo = ""
            sys.exit()

if __name__ == '__main__':
    menu()
