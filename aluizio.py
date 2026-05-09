import os, time, sys, socket

# Memória do script para agilizar
ip_memoria = ""
conectado = False

def pegar_ip_rede():
    # Tenta descobrir o IP do seu Wi-Fi automaticamente
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        meu_ip = s.getsockname()[0]
        s.close()
        # Sugere a base da rede (ex: 192.168.100.)
        return ".".join(meu_ip.split('.')[:-1]) + "."
    except:
        return "192.168.100."

def logo():
    os.system('clear')
    print("      ● BLACK BOX V15.0 - MODO AGILIDADE ●")
    print("      STATUS: " + ("🟢 ONLINE" if conectado else "🔴 OFFLINE"))
    print("──────────────────────────────────────")

def conectar():
    global conectado, ip_memoria
    logo()
    
    # Se ainda não temos o IP do jogador, pegamos a base da rede
    if not ip_memoria:
        base = pegar_ip_rede()
        print(f"Rede detectada: {base}X")
        final = input(f"Complete o IP do jogador (ou Enter para {base}5): ")
        ip_memoria = final if "." in final else (base + (final if final else "5"))

    print(f"\nCONECTANDO EM: {ip_memoria}")
    print("──────────────────────────────────────")
    
    # IGUAL AO VÍDEO: SÓ AS PORTAS E CÓDIGOS
    print("[1] PAREAMENTO")
    porta_p = input("Porta de pareamento (ex: 34525): ")
    cod_p = input("Código de pareamento (6 dígitos): ")
    
    print(f"\n{C}[🔗] Sincronizando chaves...{R}")
    # Limpa o ADB antes para evitar erro de protocolo dos prints antigos
    os.system("adb kill-server > /dev/null 2>&1")
    os.system(f"adb pair {ip_memoria}:{porta_p} {cod_p}")
    
    print("\n[2] CONEXÃO")
    porta_c = input("Porta de conexão (ex: 40667): ")
    os.system(f"adb connect {ip_memoria}:{porta_c}")
    
    # Validação final
    check = os.popen("adb devices").read()
    if "device" in check.split('\n')[1]:
        print("\n✅ DISPOSITIVO CONECTADO!")
        conectado = True
    else:
        print("\n❌ FALHA NA CONEXÃO. Verifique o Wi-Fi.")
        conectado = False
    time.sleep(2)

def pente_fino():
    if not conectado:
        print("\n🔴 ERRO: Use a Opção 1 primeiro!")
        time.sleep(2)
        return

    logo()
    print("☢️  VARREDURA PENTE FINO (BUSCA DE PROVAS) ☢️\n")
    
    # Lista de termos suspeitos para o laudo não vir vazio
    termos = ["lua", "h4x", "mod", "cheat", "rege", "sensi", "macro", "bypass"]
    pastas = ["/sdcard/Android/data", "/sdcard/Download", "/sdcard/Telegram"]
    provas = []

    for pasta in pastas:
        print(f"🔍 Analisando: {pasta}...")
        for t in termos:
            # Busca real por arquivos que contenham os termos
            cmd = f"adb shell find {pasta} -iname '*{t}*' 2>/dev/null"
            res = os.popen(cmd).read().strip()
            if res:
                for line in res.split('\n'):
                    provas.append(line)
        time.sleep(0.5)

    logo()
    print("📋 LAUDO DE EVIDÊNCIAS")
    print("──────────────────────────────────────")
    if provas:
        print("STATUS: 🔴 W.O. DETECTADO")
        print(f"\nARQUIVOS SUSPEITOS ENCONTRADOS ({len(provas)}):")
        for p in provas:
            # Mostra o nome do arquivo para provar o que é (ex: rege.lua)
            print(f" > {p.split('/')[-1]} (Local: {p})")
    else:
        print("STATUS: 🟢 JOGADOR LIMPO")
    
    print("──────────────────────────────────────")
    input("\nEnter para voltar...")

def menu():
    while True:
        logo()
        print("[ 1 ] CONECTAR (SÓ PORTAS/CÓDIGO)")
        print("[ 2 ] PENTE FINO (VER LAUDO)")
        print("[ S ] SAIR / RESETAR IP")
        opc = input("\nALUIZIO > ").lower()
        if opc == '1': conectar()
        elif opc == '2': pente_fino()
        elif opc == 's': 
            global ip_memoria
            ip_memoria = ""
            sys.exit()

if __name__ == '__main__':
    menu()
