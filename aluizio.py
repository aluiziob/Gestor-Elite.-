import os, time, sys

# CORES OFICIAIS
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
    print("Abra 'Depuração por Wi-Fi' > 'Parear com código'.")
    ip_pair = input("IP:PORTA DO CÓDIGO: ")
    codigo = input("CÓDIGO DE 6 DÍGITOS: ")
    
    print(f"\n{CINZA}Sincronizando chaves...{RESET}")
    os.system(f"adb pair {ip_pair} {codigo}")
    
    print(f"\n{BRANCO}PASSO 2: CONEXÃO DE DADOS{RESET}")
    print("Volte uma tela e pegue o IP:PORTA principal.")
    ip_final = input("IP:PORTA FINAL: ")
    os.system(f"adb connect {ip_final}")
    
    # Validação Real
    check = os.popen("adb devices").read()
    if "device" in check.split('\n')[1]:
        print(f"\n{VERDE_BG} ✅ DISPOSITIVO VINCULADO! {RESET}")
    else:
        print(f"\n{VERMELHO_BG} ❌ ERRO NA CONEXÃO ADB! {RESET}")
    input("\nEnter para voltar...")

def varredura_total():
    logo()
    # Bloqueio de varredura falsa
    check = os.popen("adb devices").read()
    if "device" not in check.split('\n')[1]:
        print(f"{VERMELHO_BG} ERRO: NENHUM CELULAR CONECTADO! {RESET}")
        input("\nConecte na Opção 1 antes. Enter...")
        return

    print(f"{AMARELO}☢️ INICIANDO PENTE FINO (VARREDURA PROFUNDA) ☢️{RESET}")
    print("ANALISANDO ARQUIVOS, LOGS E REDE. AGUARDE...\n")
    
    provas = []
    # Termos pesados para buscar tudo (incluindo MDM e Proxy do print)
    termos = ["lua", "h4x", "mod", "cheat", "xit", "rege", "v7a", "inject", "proxy", "mdm", "plist", "tracev3"]
    pastas = ["/sdcard/Android/data", "/sdcard/Android/obb", "/sdcard/Download", "/data/local/tmp"]

    for pasta in pastas:
        print(f"{CINZA}[🔍] Periciando: {pasta}...{RESET}")
        for t in termos:
            # O SEGREDO: adb shell find busca DENTRO do celular do cara
            cmd = f"adb shell find {pasta} -iname '*{t}*' 2>/dev/null"
            resultado = os.popen(cmd).read().strip()
            if resultado:
                for linha in resultado.split('\n'):
                    if linha:
                        print(f"{AMARELO}⚠ ACHADO: {linha[-50:]}{RESET}")
                        provas.append(linha)
        # FORÇA A LENTIDÃO: Isso evita o erro de 1 segundo
        time.sleep(4)

    # BUSCA DE PROXY (DUMPSYS)
    print(f"\n{CINZA}[🌐] Analisando túneis de IP e MDM...{RESET}")
    proxy = os.popen("adb shell dumpsys connectivity | grep -E 'Proxy|mHttpProxy'").read().strip()
    if proxy:
        provas.append(f"Proxy Detectado: {proxy}")

    logo()
    print(f"{BRANCO}LAUDO PERICIAL FINALIZADO{RESET}")
    print(f"{CINZA}──────────────────────────────────────{RESET}")
    modelo = os.popen("adb shell getprop ro.product.model").read().strip()
    print(f" APARELHO : {modelo}")
    
    if provas:
        print(f"\n STATUS   : {VERMELHO_BG}   W.O. DETECTADO   {RESET}")
        print(f"\n{BRANCO}EVIDÊNCIAS (Pode subir o W.O.):{RESET}")
        print(f"Foram encontrados {len(provas)} rastros suspeitos.")
    else:
        print(f"\n STATUS   : {VERDE_BG}      LIMPO       {RESET}")
        print(f"\n{BRANCO}Dispositivo verificado com sucesso.{RESET}")

    print(f"\n{CINZA}──────────────────────────────────────{RESET}")
    input("Pressione Enter para fechar...")

def menu():
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
