import os, time, sys

# CORES
BRANCO = '\033[1;37m'
CINZA = '\033[0;90m'
VERMELHO_BG = '\033[41;1;37m'
VERDE_BG = '\033[42;1;37m'
AMARELO = '\033[1;33m'
RESET = '\033[0m'

def logo():
    os.system('clear')
    print(f"{BRANCO}         ● BLACK BOX ●{RESET}")
    print(f"{BRANCO}         DONO: ALUIZIO{RESET}")
    print(f"{CINZA}──────────────────────────────────────{RESET}")

def conectar():
    logo()
    print(f"{BRANCO}PASSO 1: PAREAMENTO{RESET}")
    print("No celular do player: 'Parear dispositivo com código'")
    ip_pair = input("Digite o IP:PORTA do código: ")
    codigo = input("Digite o CÓDIGO de 6 números: ")
    
    print(f"\n{CINZA}Sincronizando...{RESET}")
    os.system(f"adb pair {ip_pair} {codigo}")
    
    print(f"\n{BRANCO}PASSO 2: CONEXÃO DE DADOS{RESET}")
    print("Agora volte uma tela e veja o IP:PORTA principal.")
    ip_final = input("Digite o IP:PORTA da tela inicial: ")
    os.system(f"adb connect {ip_final}")
    
    # Verifica se conectou de verdade antes de seguir
    check = os.popen("adb devices").read()
    if "device" in check.split('\n')[1]:
        input(f"\n{VERDE_BG} ✅ CELULAR VINCULADO COM SUCESSO! {RESET}\nENTER...")
    else:
        input(f"\n{VERMELHO_BG} ❌ FALHA NA CONEXÃO. TENTE NOVAMENTE. {RESET}")

def varredura_total():
    logo()
    # Verifica se tem algum dispositivo conectado
    check = os.popen("adb devices").read()
    if "device" not in check.split('\n')[1]:
        print(f"{VERMELHO_BG} ERRO: NENHUM CELULAR CONECTADO VIA ADB! {RESET}")
        print("Conecte primeiro na Opção 1 antes de procurar.")
        input("\nEnter para voltar...")
        return

    print(f"{AMARELO}☢️ INICIANDO PENTE FINO NO SISTEMA DO JOGADOR...{RESET}")
    print("ISSO VAI DEMORAR. NÃO CANCELE.\n")
    
    provas = []
    
    # BUSCA POR ARQUIVOS (Agora usando ADB SHELL para entrar no Android do cara)
    # Procuramos por nomes e extensões que xitado usa
    termos = ["lua", "mod", "cheat", "xit", "rege", "v7a", "inject", "proxy", "mdm", "bypass", "aim", "bot"]
    pastas = ["/sdcard", "/storage/emulated/0/Android/data", "/storage/emulated/0/Android/obb"]

    for p in pastas:
        print(f"{CINZA}[🔍] Entrando em: {p}...{RESET}")
        for t in termos:
            # O comando 'adb shell find' é o segredo. Ele vasculha o celular do outro.
            comando = f"adb shell find {p} -iname '*{t}*' 2>/dev/null"
            resultado = os.popen(comando).read().strip()
            
            if resultado:
                # Se achou algo, a gente quebra em linhas e adiciona às provas
                for linha in resultado.split('\n'):
                    if linha:
                        print(f"{AMARELO}⚠ DETECTADO: {linha[-60:]}{RESET}")
                        provas.append(linha)
        # Pausa para o processamento não ser instantâneo e falso
        time.sleep(3)

    # BUSCA POR PROXY ATIVO (Igual ao seu print de W.O.)
    print(f"\n{CINZA}[🌐] Verificando túneis de rede (Proxy/VPN)...{RESET}")
    proxy = os.popen("adb shell dumpsys connectivity | grep -E 'Proxy|mHttpProxy'").read().strip()
    if proxy:
        provas.append(f"PROXY ATIVO: {proxy}")

    logo()
    print(f"{BRANCO}RELATÓRIO FINAL DE PERÍCIA{RESET}")
    print(f"{CINZA}──────────────────────────────────────{RESET}")
    modelo = os.popen("adb shell getprop ro.product.model").read().strip()
    print(f" APARELHO : {modelo}")
    
    if provas:
        print(f"\n STATUS   : {VERMELHO_BG}   W.O. DETECTADO   {RESET}")
        print(f"\n{BRANCO}PROVAS (Vejas os prints da busca):{RESET}")
        print(f"Total de rastros: {len(provas)}")
    else:
        print(f"\n STATUS   : {VERDE_BG}      LIMPO       {RESET}")
        print(f"\n{BRANCO}Nenhum rastro encontrado no dispositivo.{RESET}")

    print(f"\n{CINZA}──────────────────────────────────────{RESET}")
    input("Pressione Enter para fechar...")

def menu():
    # Instalação rápida sem frescura
    os.system("pkg install android-tools -y > /dev/null 2>&1")
    while True:
        logo()
        print(f"[ 1 ] {BRANCO}CONECTAR NO CELULAR (PASSO A PASSO){RESET}")
        print(f"[ 2 ] {BRANCO}VARREDURA TOTAL (SEM FALSO LIMPO){RESET}")
        print(f"[ S ] {CINZA}SAIR{RESET}")
        opc = input(f"\nALUIZIO > ").lower()
        if opc == '1': conectar()
        elif opc == '2': varredura_total()
        elif opc == 's': sys.exit()

if __name__ == '__main__':
    menu()
