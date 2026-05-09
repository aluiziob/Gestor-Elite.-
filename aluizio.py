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

def varredura_total():
    logo()
    print(f"{VERMELHO_BG} ⚠️  VARREDURA SEM LIMITE DE PROFUNDIDADE  {RESET}")
    print(f"{AMARELO}AGUARDE... O SISTEMA VAI ATÉ O FIM.{RESET}\n")
    
    alertas = 0
    motivos = []

    # Dicionário de busca pesada
    termos = ["v7a", "v8a", "lib", "mod", "cheat", "xit", "rege", "h4x", "inject", "lua", "sh", "bypass", "proxy", "mdm"]
    
    # Raízes de busca (Caminhos onde o Android esconde arquivos)
    caminhos = ["/sdcard", "/data/media/0", "/storage/emulated/0"]

    for pasta in caminhos:
        if os.path.exists(pasta):
            print(f"{CINZA}[🔍] Escaneando raiz: {pasta}{RESET}")
            for t in termos:
                # O comando 'find' sem '-maxdepth' varre TUDO até o final
                # Buscamos por nome e também dentro de arquivos de texto se necessário
                cmd = f"find {pasta} -iname '*{t}*' 2>/dev/null"
                resultado = os.popen(cmd).read().strip()
                
                if resultado:
                    alertas += 1
                    # Mostra o caminho completo na tela pro ADM ver a prova
                    print(f"{AMARELO}ACHADO: {resultado}{RESET}")
                    if "Arquivos Suspeitos" not in motivos:
                        motivos.append("Arquivos/Pastas de trapaça detectados")

    # Checagem de Proxy (Igual ao seu print de W.O.)
    print(f"\n{CINZA}[🌐] Checando Túnel de Rede...{RESET}")
    proxy = os.popen("adb shell dumpsys connectivity | grep -E 'Proxy|mHttpProxy'").read().strip()
    if proxy:
        alertas += 1
        motivos.append("IP/MDM Proxy Detectado")

    # RELATÓRIO FINAL
    logo()
    print(f"{BRANCO}LAUDO PERICIAL FINALIZADO{RESET}")
    print(f"{CINZA}──────────────────────────────────────{RESET}")
    print(f" APARELHO : {os.popen('getprop ro.product.model').read().strip()}")
    
    if alertas > 0:
        print(f"\n STATUS   : {VERMELHO_BG}   W.O. DETECTADO   {RESET}")
        print(f"\n{BRANCO}LISTA DE PROVAS:{RESET}")
        for m in motivos:
            print(f" > {m}")
    else:
        print(f"\n STATUS   : {VERDE_BG}      LIMPO       {RESET}")
        print(f"\n{BRANCO}Dispositivo verificado em profundidade total.{RESET}")

    print(f"\n{CINZA}──────────────────────────────────────{RESET}")
    input("Pressione Enter para fechar...")

def menu():
    os.system("pkg install android-tools -y > /dev/null 2>&1")
    while True:
        logo()
        print("[ 1 ] CONECTAR CELULAR (ADB)")
        print("[ 2 ] VARREDURA TOTAL (SEM LIMITES)")
        print("[ S ] SAIR")
        
        opc = input(f"\nALUIZIO > ").lower()
        if opc == '1':
            ip = input("IP:PORTA: ")
            cod = input("CÓDIGO: ")
            os.system(f"adb pair {ip} {cod} && adb connect {ip}")
            input("\nPronto! Enter...")
        elif opc == '2':
            varredura_total()
        elif opc == 's': sys.exit()

if __name__ == '__main__':
    menu()
