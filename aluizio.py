import os, time, sys, socket

ip_memoria = ""
conectado = False

def logo():
    os.system('clear')
    print("      ● BLACK BOX V15.0 - AGILIDADE ●")
    print("      STATUS: " + ("ON" if conectado else "OFF"))
    print("--------------------------------------")

def conectar():
    global conectado, ip_memoria
    logo()
    if not ip_memoria:
        ip_memoria = input("IP do jogador (Ex: 192.168.100.5): ")
    
    print(f"\nCONECTANDO EM: {ip_memoria}")
    print("--------------------------------------")
    porta_p = input("Porta pareamento (5 num): ")
    cod_p = input("Codigo pareamento (6 num): ")
    
    print("\n[🔗] Sincronizando...")
    os.system("adb kill-server > /dev/null 2>&1")
    os.system(f"adb pair {ip_memoria}:{porta_p} {cod_p}")
    
    porta_c = input("\nPorta conexao final (5 num): ")
    os.system(f"adb connect {ip_memoria}:{porta_c}")
    
    check = os.popen("adb devices").read()
    if "device" in check.split('\n')[1]:
        print("\n✅ CONECTADO!")
        conectado = True
    else:
        print("\n❌ FALHA. Verifique o Wi-Fi.")
        conectado = False
    time.sleep(2)

def pente_fino():
    if not conectado:
        print("\n🔴 Erro: Conecte primeiro!")
        time.sleep(2)
        return
    logo()
    print("🔍 BUSCANDO ARQUIVOS SUSPEITOS...\n")
    termos = ["lua", "h4x", "mod", "cheat", "rege", "sensi", "macro"]
    pastas = ["/sdcard/Android/data", "/sdcard/Download"]
    provas = []
    for pasta in pastas:
        for t in termos:
            res = os.popen(f"adb shell find {pasta} -iname '*{t}*' 2>/dev/null").read().strip()
            if res:
                for line in res.split('\n'): provas.append(line)
    if provas:
        print(f"🔴 W.O. DETECTADO! ({len(provas)} provas)")
        for p in provas: print(f" > {p.split('/')[-1]}")
    else:
        print("🟢 JOGADOR LIMPO")
    input("\nEnter para voltar...")

def menu():
    while True:
        logo()
        print("[ 1 ] CONECTAR (SÓ PORTAS)")
        print("[ 2 ] PENTE FINO")
        print("[ S ] SAIR")
        opc = input("\nALUIZIO > ").lower()
        if opc == '1': conectar()
        elif opc == '2': pente_fino()
        elif opc == 's': sys.exit()

if __name__ == '__main__':
    menu()
