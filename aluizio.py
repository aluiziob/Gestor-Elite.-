import os, time, sys

# Cores Dark Mode
B = '\033[1;37m' # Branco
C = '\033[0;90m' # Cinza
V = '\033[41;1;37m' # Vermelho BG
G = '\033[42;1;37m' # Verde BG
A = '\033[1;33m' # Amarelo
R = '\033[0m' # Reset

conectado = False

def logo():
    os.system('clear')
    print(f"{B}         ● BLACK BOX V13.5 ●{R}")
    print(f"{B}         DONO: ALUIZIO{R}")
    print(f"{C}──────────────────────────────────────{R}")

def conectar():
    global conectado
    logo()
    # Reset inicial para evitar erro de protocolo
    os.system("adb kill-server > /dev/null 2>&1")
    os.system("adb start-server > /dev/null 2>&1")
    
    print(f"{B}PASSO 1: PAREAMENTO{R}")
    print(f"{C}(Tela com o código de 6 números){R}\n")
    ip_pair = input("1. IP:PORTA de PAREAMENTO: ")
    codigo = input("2. CÓDIGO de 6 DÍGITOS: ")
    
    print(f"\n{C}[🔗] Pareando...{R}")
    pair_cmd = os.popen(f"adb pair {ip_pair} {codigo}").read()
    
    if "Successfully paired" in pair_cmd or "connected" in pair_cmd.lower():
        print(f"{G} PAREAMENTO OK! {R}")
        print(f"\n{B}PASSO 2: CONEXÃO FINAL{R}")
        print(f"{C}(IP da tela principal da Depuração){R}\n")
        ip_final = input("3. IP:PORTA PRINCIPAL: ")
        os.system(f"adb connect {ip_final}")
        
        # Validação se ficou ONLINE
        check = os.popen("adb devices").read()
        if "device" in check.split('\n')[1]:
            print(f"\n{G} ✅ STATUS: ONLINE {R}")
            conectado = True
        else:
            print(f"\n{V} ❌ FALHA NA CONEXÃO FINAL {R}")
            conectado = False
    else:
        print(f"\n{V} ❌ FALHA NO PAREAMENTO {R}")
        print(f"{A}Dica: Verifique se estão no mesmo Wi-Fi!{R}")
        conectado = False
    input("\nEnter para voltar...")

def pente_fino():
    global conectado
    logo()
    if not conectado:
        print(f"{V} ACESSO NEGADO: CONECTE PRIMEIRO (OPÇÃO 1) {R}")
        input("\nEnter para voltar...")
        return

    print(f"{A}☢️ VARREDURA PROFUNDA INICIADA (1-10 MIN) ☢️{R}")
    # Busca real usando SHELL no celular do player
    termos = ["lua", "h4x", "mod", "cheat", "xit", "rege", "v7a", "proxy", "mdm"]
    pastas = ["/sdcard/Android/data", "/sdcard/Android/obb", "/sdcard/Download"]
    
    provas = []
    for p in pastas:
        print(f"{C}[🔍] Periciando: {p}...{R}")
        for t in termos:
            cmd = f"adb shell find {p} -iname '*{t}*' 2>/dev/null"
            res = os.popen(cmd).read().strip()
            if res:
                for line in res.split('\n'):
                    print(f"{A}⚠ ACHADO: {line[-50:]}{R}")
                    provas.append(line)
        time.sleep(3) # Garante que a varredura não seja instantânea e falsa

    logo()
    print(f"{B}RESULTADO DA PERÍCIA{R}")
    if provas:
        print(f"\n STATUS: {V} W.O. DETECTADO {R}")
        print(f"Evidências encontradas: {len(provas)}")
    else:
        print(f"\n STATUS: {G} LIMPO {R}")
    input("\nEnter para concluir...")

def menu():
    while True:
        logo()
        st = f"{G}[ON]{R}" if conectado else f"{V}[OFF]{R}"
        print(f" CONEXÃO: {st}")
        print(f"{C}──────────────────────────────────────{R}")
        print(f"[ 1 ] {B}CONECTAR (3 CÓDIGOS){R}")
        print(f"[ 2 ] {B}VARREDURA (PENTE FINO){R}")
        print(f"[ S ] {C}SAIR{R}")
        opc = input(f"\nALUIZIO > ").lower()
        if opc == '1': conectar()
        elif opc == '2': pente_fino()
        elif opc == 's': sys.exit()

if __name__ == '__main__':
    menu()
