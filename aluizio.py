import os, time, sys, socket

# CORES PARA O VISUAL FICAR TOP
R = '\033[1;31m' # Vermelho
G = '\033[1;32m' # Verde
B = '\033[1;34m' # Azul
W = '\033[1;37m' # Branco
C = '\033[1;36m' # Ciano
N = '\033[0m'    # Reset

ip_memoria = ""
conectado = False

def logo():
    os.system('clear')
    print(f"{C}      ● BLACK BOX V15.0 - ELITE ●{N}")
    print(f"      STATUS: " + (f"{G}🟢 ONLINE{N}" if conectado else f"{R}🔴 OFFLINE{N}"))
    print(f"{W}──────────────────────────────────────{N}")

def conectar():
    global conectado, ip_memoria
    logo()
    
    # Captura automática de IP para agilizar
    if not ip_memoria:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            base = ".".join(s.getsockname()[0].split('.')[:-1]) + "."
            s.close()
            print(f"{B}[ℹ️] Rede: {base}X{N}")
            final = input(f"{W}Final do IP (ou Enter para {base}5): {N}")
            ip_memoria = base + (final if final else "5")
        except:
            ip_memoria = input(f"{W}IP Completo: {N}")

    print(f"\n{B}ALVO: {ip_memoria}{N}")
    print(f"{W}──────────────────────────────────────{N}")
    
    print(f"{C}[1] PAREAMENTO{N}")
    porta_p = input("Porta (5 num): ")
    cod_p = input("Código (6 num): ")
    
    print(f"\n{G}[🔗] Sincronizando...{N}")
    os.system("adb kill-server > /dev/null 2>&1")
    os.system(f"adb pair {ip_memoria}:{porta_p} {cod_p}")
    
    print(f"\n{C}[2] CONEXÃO{N}")
    porta_c = input("Porta Final: ")
    os.system(f"adb connect {ip_memoria}:{porta_c}")
    
    check = os.popen("adb devices").read()
    if "device" in check.split('\n')[1]:
        print(f"\n{G}✅ DISPOSITIVO VINCULADO!{N}")
        conectado = True
    else:
        print(f"\n{R}❌ FALHA NA SINCRONIZAÇÃO.{N}")
        conectado = False
    time.sleep(2)

def pente_fino():
    if not conectado:
        print(f"\n{R}🔴 ERRO: Conecte primeiro!{N}")
        time.sleep(2)
        return
    logo()
    print(f"{R}☢️  BUSCANDO PROVAS DE USO DE AUXÍLIO ☢️{N}\n")
    termos = ["lua", "h4x", "mod", "cheat", "rege", "sensi", "macro", "bypass"]
    pastas = ["/sdcard/Android/data", "/sdcard/Download", "/sdcard/Telegram"]
    provas = []
    for pasta in pastas:
        for t in termos:
            res = os.popen(f"adb shell find {pasta} -iname '*{t}*' 2>/dev/null").read().strip()
            if res:
                for line in res.split('\n'): provas.append(line)
    
    logo()
    print(f"{W}📋 RESULTADO DA PERÍCIA{N}")
    if provas:
        print(f"STATUS: {R}W.O. DETECTADO{N}")
        print(f"Evidências encontradas: {len(provas)}")
        for p in provas: print(f" {R}>{N} {p.split('/')[-1]}")
    else:
        print(f"STATUS: {G}🟢 JOGADOR LIMPO{N}")
    input(f"\n{W}Pressione Enter para voltar...{N}")

def menu():
    while True:
        logo()
        print(f"{W}[ {G}1{W} ] CONECTAR (MODO AGILIDADE)")
        print(f"{W}[ {G}2{W} ] PENTE FINO (GERAR LAUDO)")
        print(f"{W}[ {R}S{W} ] SAIR")
        opc = input(f"\n{C}ALUIZIO > {N}").lower()
        if opc == '1': conectar()
        elif opc == '2': pente_fino()
        elif opc == 's': sys.exit()

if __name__ == '__main__':
    menu()
