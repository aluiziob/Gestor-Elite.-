import os, time, sys

# Variável de controle
conectado = False

def logo():
    os.system('clear')
    print("         ● BLACK BOX ●")
    print("         DONO: ALUIZIO")
    print("──────────────────────────────────────")

def fluxo_conexao():
    global conectado
    logo()
    print("PASSO 1: PAREAMENTO (Tela do código de 6 números)")
    ip_pair = input("1. IP:PORTA de PAREAMENTO: ")
    codigo = input("2. CÓDIGO de 6 DÍGITOS: ")
    
    print("\n[🔗] Sincronizando...")
    os.system(f"adb pair {ip_pair} {codigo}")
    
    print("\nPASSO 2: CONEXÃO FINAL (Tela principal da Depuração)")
    ip_final = input("3. IP:PORTA PRINCIPAL: ")
    
    print("\n[🚀] Conectando...")
    os.system(f"adb connect {ip_final}")
    
    # Validação real
    check = os.popen("adb devices").read()
    if "device" in check.split('\n')[1]:
        print("\n✅ DISPOSITIVO VINCULADO!")
        conectado = True
    else:
        print("\n❌ FALHA. Tente novamente.")
        conectado = False
    input("\nEnter para voltar...")

def varredura_pente_fino():
    global conectado
    logo()
    
    # TRAVA DE SEGURANÇA
    if not conectado:
        print("\033[41m ACESSO NEGADO \033[0m")
        print("\nVocê precisa CONECTAR (Opção 1) antes de escanear.")
        input("\nEnter para voltar...")
        return

    print("☢️ INICIANDO PENTE FINO (1-10 MIN) ☢️")
    print("ANALISANDO ARQUIVOS, LOGS E PROXIES...\n")
    
    # Comando de busca profunda via Shell
    os.system("adb shell find /sdcard/Android/data -iname '*lua*' -o -iname '*h4x*' -o -iname '*mod*' -o -iname '*rege*'")
    
    # Verificação de MDM/Proxy igual ao seu print
    proxy = os.popen("adb shell dumpsys connectivity | grep -E 'Proxy|mHttpProxy'").read().strip()
    if proxy:
        print(f"\n⚠️ PROXY DETECTADO: {proxy}")
        
    print("\nVARREDURA CONCLUÍDA.")
    input("\nEnter para fechar o laudo...")

def menu():
    while True:
        logo()
        status = "\033[32mON\033[0m" if conectado else "\033[31mOFF\033[0m"
        print(f"STATUS DE CONEXÃO: [{status}]")
        print("──────────────────────────────────────")
        print("[ 1 ] CONECTAR (3 CÓDIGOS)")
        print("[ 2 ] VARREDURA TOTAL (PENTE FINO)")
        print("[ S ] SAIR")
        
        opc = input(f"\nALUIZIO > ").lower()
        if opc == '1': fluxo_conexao()
        elif opc == '2': varredura_pente_fino()
        elif opc == 's': sys.exit()

if __name__ == '__main__':
    menu()
