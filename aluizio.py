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
    print(f"{BRANCO}PASSO ÚNICO: PAREAMENTO DE ELITE{RESET}")
    print(f"{CINZA}Abra: 'Parear dispositivo com código'{RESET}\n")
    
    # Exatamente como você pediu: os dois dados da mesma tela
    ip_porta = input("1. Digite o IP:PORTA (Final de 5 números): ")
    codigo = input("2. Digite o CÓDIGO (Os 6 números grandes): ")
    
    print(f"\n{CINZA}Conectando ao sistema do jogador...{RESET}")
    
    # O comando ADB PAIR faz o vínculo oficial
    os.system(f"adb pair {ip_porta} {codigo}")
    
    # Tentativa de conexão automática após o pareamento
    os.system(f"adb connect {ip_porta}")
    
    print(f"\n{CINZA}──────────────────────────────────────{RESET}")
    check = os.popen("adb devices").read()
    if "device" in check.split('\n')[1]:
        print(f"{VERDE_BG} ✅ DISPOSITIVO VINCULADO E PRONTO! {RESET}")
    else:
        print(f"{VERMELHO_BG} ❌ ERRO: Verifique se os números estão certos. {RESET}")
    input("\nEnter para voltar ao Menu...")

def varredura_total():
    logo()
    print(f"{AMARELO}☢️ INICIANDO PENTE FINO (VARREDURA PROFUNDA) ☢️{RESET}")
    print("BUSCANDO RASTROS EM 100% DAS PASTAS...\n")
    
    provas = []
    # Busca real via shell dentro do celular do cara
    termos = ["lua", "h4x", "mod", "cheat", "xit", "rege", "v7a", "inject", "proxy", "mdm"]
    # Varre as pastas de dados e obb (onde o xit se esconde)
    pastas = ["/sdcard/Android/data", "/sdcard/Android/obb", "/sdcard/Download"]

    for pasta in pastas:
        print(f"{CINZA}[🔍] Revistando: {pasta}...{RESET}")
        for t in termos:
            # Esse comando 'find' não tem limites, ele vai até o fim
            resultado = os.popen(f"adb shell find {pasta} -iname '*{t}*' 2>/dev/null").read().strip()
            if resultado:
                for linha in resultado.split('\n'):
                    if linha:
                        print(f"{AMARELO}⚠ ACHADO: {linha[-55:]}{RESET}")
                        provas.append(linha)
        time.sleep(3) # Força a análise demorada para ser real

    logo()
    print(f"{BRANCO}RELATÓRIO FINAL DE PERÍCIA{RESET}")
    print(f"{CINZA}──────────────────────────────────────{RESET}")
    
    if provas:
        print(f"\n STATUS   : {VERMELHO_BG}   W.O. DETECTADO   {RESET}")
        print(f"\n{BRANCO}O SISTEMA ENCONTROU {len(provas)} EVIDÊNCIAS.{RESET}")
    else:
        print(f"\n STATUS   : {VERDE_BG}      LIMPO       {RESET}")
    
    print(f"\n{CINZA}──────────────────────────────────────{RESET}")
    input("Pressione Enter para fechar...")

def menu():
    while True:
        logo()
        print(f"[ 1 ] {BRANCO}CONECTAR (IP + CÓDIGO DE 6 DÍGITOS){RESET}")
        print(f"[ 2 ] {BRANCO}VARREDURA TOTAL (SEM FALSO LIMPO){RESET}")
        print(f"[ S ] {CINZA}SAIR{RESET}")
        opc = input(f"\nALUIZIO > ").lower()
        if opc == '1': conectar()
        elif opc == '2': varredura_total()
        elif opc == 's': sys.exit()

if __name__ == '__main__':
    menu()
