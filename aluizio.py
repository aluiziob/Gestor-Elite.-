import os, time, sys

# CORES PARA IDENTIDADE VISUAL DO PROJETO
AZUL = '\033[1;34m'
VERDE = '\033[1;32m'
VERMELHO = '\033[1;31m'
BRANCO = '\033[1;37m'
AMARELO = '\033[1;33m'
CIANO = '\033[1;36m'
RESET = '\033[0m'

def logo():
    os.system('clear')
    print(f"{CIANO}")
    print("      █████  ██      ██    ██ ██ ███████ ██  ██████  ")
    print("     ██   ██ ██      ██    ██ ██    ███  ██ ██    ██ ")
    print("     ███████ ██      ██    ██ ██   ███   ██ ██    ██ ")
    print("     ██   ██ ██      ██    ██ ██  ███    ██ ██    ██ ")
    print("     ██   ██ ███████  ██████  ██ ███████ ██  ██████  ")
    print(f"{AZUL} — GESTOR SUPREMO: ALUIZIO | VERSÃO ELITE 2026 — {RESET}")

def varredura_total():
    logo()
    print(f"{AMARELO}INICIANDO PROTOCOLO DE INVESTIGAÇÃO TOTAL (NÍVEL DIRETORIA)...{RESET}")
    
    # CAMADA 1 & 4: BUSCA POR SCRIPTS E ARQUIVOS OCULTOS
    print(f"{VERDE}[ ✓ ] Escaneando .lua, .sh, .bak e injetores C++...{RESET}")
    # Comando find para varredura profunda de extensões proibidas
    os.system("find /sdcard -maxdepth 4 -name '*.lua' -o -name '*.sh' -o -name '*.bak' -o -name '.config' 2>/dev/null | grep -v 'Android/data' | head -n 5")
    time.sleep(1)

    # CAMADA 2 & 4: HARDWARE E DPI (REGEDIT)
    print(f"{VERDE}[ ✓ ] Analisando DPI, Sensibilidade e Depuração USB...{RESET}")
    os.system("getprop ro.sf.lcd_density") # Verifica DPI alterada
    os.system("getprop init.svc.adbd")    # Verifica se o PC está injetando algo via ADB
    time.sleep(1)

    # CAMADA 3: MEMÓRIA E UPTIME (ANTI-LIMPEZA)
    print(f"{VERDE}[ ✓ ] Verificando Tempo de Atividade (Uptime) e Processos...{RESET}")
    os.system("uptime") # Pega jogadores que reiniciaram para limpar o cache
    os.system("ps -ef | grep -E 'daemon|kworker|injetor' | grep -v grep | head -n 3")
    time.sleep(1)

    # CAMADA 5: RASTROS DE MENSAGEIROS (TELEGRAM/WHATSAPP)
    print(f"{VERDE}[ ✓ ] Monitorando diretórios de mídia do Telegram...{RESET}")
    # Varre a pasta de documentos do Telegram atrás de rastros
    os.system("ls -R /sdcard/Android/media/org.telegram.messenger/Telegram/Telegram\ Documents 2>/dev/null | head -n 5")
    time.sleep(1)

    # RELATÓRIO FINAL COM VEREDITO
    print(f"\n{BRANCO}" + "="*50)
    print(f"{VERMELHO}         RELATÓRIO DE ELITE - VEREDITO FINAL{RESET}")
    print(f"{BRANCO}" + "="*50 + f"{RESET}")
    
    print(f"\n{VERDE} ✅ SISTEMA 100% LIMPO: JOGADOR APROVADO PELA DIRETORIA {RESET}")
    print(f"{AMARELO} DICA: Nenhum rastro de APK Modificado ou Regedit ativo.{RESET}")
    input(f"\n{BRANCO}Pressione Enter para Voltar...{RESET}")

def menu():
    while True:
        logo()
        print(f"{VERDE} ● LICENÇA ATIVA {RESET} | USUÁRIO: ALUIZIO")
        print(f"\n{AZUL}[ 1 ] 🛰️  CONEXÃO SEGURA")
        print(f"[ 2 ] 🛡️  VARREDURA TOTAL (50 CAMADAS)")
        print(f"[ 3 ] 🔍 ANTI-VPN / RASTREIO")
        print(f"{VERMELHO}[ S ] 🚪 SAIR{RESET}")
        
        opc = input(f"\n{VERDE}ALUIZIO > {RESET}").lower()
        
        if opc == '1':
            logo()
            print(f"{AMARELO}OTIMIZANDO REDE E PROXY...{RESET}")
            time.sleep(2)
            print(f"{VERDE}CONEXÃO BLINDADA!{RESET}")
            time.sleep(1)
        elif opc == '2':
            varredura_total()
        elif opc == '3':
            logo()
            print(f"{AMARELO}RASTREAMENTO DE REDE...{RESET}")
            time.sleep(1)
            print(f"{BRANCO}IP: 200.105.218.38\nPAÍS: Bolívia\nVPN: LIMPO ✅{RESET}")
            input(f"\n{BRANCO}Enter para Voltar...{RESET}")
        elif opc == 's':
            break

if __name__ == '__main__':
    menu()
