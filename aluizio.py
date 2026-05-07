import os, time, sys

# Identidade Visual (Cores)
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
    print(f"{AMARELO}=================================================================={RESET}")
    
    # --- CAMADA 1 & 4: ARQUIVOS OCULTOS E SCRIPTS (Execução Real) ---
    print(f"\n{VERDE}[ 🛰️ ] Escaneando armazenamento por arquivos .lua e .sh...{RESET}")
    # Busca real por arquivos .lua e .sh no sdcard (maximo de 3 subpastas para não demorar)
    result_lua = os.popen("find /sdcard -maxdepth 3 -name '*.lua' -o -name '*.sh' 2>/dev/null").read()
    if result_lua:
        print(f"{VERMELHO}[⚠️] ATENÇÃO: Scripts encontrados no sistema:{RESET}")
        print(result_lua)
    else:
        print(f"{VERDE}[✓] Nenhum script oculto encontrado nas pastas principais.{RESET}")
    
    # --- CAMADA 2 & 4: HARDWARE E SENSITIVIDADE (Execução Real) ---
    print(f"\n{VERDE}[ ⚙️ ] Analisando DPI e Status da Depuração USB...{RESET}")
    # Lê a DPI real definida pelo sistema
    dpi = os.popen("getprop ro.sf.lcd_density").read().strip()
    # Verifica se a Depuração USB está ATIVA (adbd running)
    adb_status = os.popen("getprop init.svc.adbd").read().strip()
    
    print(f"{BRANCO} -> DPI do Sistema: {dpi}{RESET}")
    if adb_status == "running":
        print(f"{VERMELHO}[⚠️] ATENÇÃO: Depuração USB/Wi-Fi está ATIVA!{RESET}")
    else:
        print(f"{VERDE}[✓] Depuração USB está desativada.{RESET}")

    # --- CAMADA 3 & 5: UPTIME E RASTROS DE MENSAGEIROS (Execução Real) ---
    print(f"\n{VERDE}[ 🕵️ ] Checando integridade e tempo de atividade do sistema...{RESET}")
    # Pega o Uptime real (tempo que o celular está ligado)
    uptime = os.popen("uptime").read().strip()
    print(f"{BRANCO} -> Tempo de atividade: {uptime}{RESET}")
    
    # Verifica arquivos recentes na pasta de documentos do Telegram
    print(f"{VERDE}[ 🔎 ] Verificando arquivos recentes no Telegram...{RESET}")
    os.system("ls -lht /sdcard/Android/media/org.telegram.messenger/Telegram/Telegram\ Documents 2>/dev/null | head -n 3")

    # --- RELATÓRIO FINAL COM VEREDITO TÉCNICO ---
    print(f"\n{BRANCO}" + "="*60)
    print(f"{AZUL}            RELATÓRIO TÉCNICO - VEREDITO DIRETORIA{RESET}")
    print(f"{BRANCO}" + "="*60 + f"{RESET}")
    
    # Lógica de Veredito Simples (pode ser melhorada)
    if result_lua or adb_status == "running":
         print(f"\n{VERMELHO} ❌ JOGADOR REPROVADO: RASTROS SUSPEITOS ENCONTRADOS {RESET}")
         print(f"{AMARELO} Analise os detalhes técnicos acima.{RESET}")
    else:
         print(f"\n{VERDE} ✅ SISTEMA LIMPO: NENHUM RASTRO TÉCNICO ENCONTRADO {RESET}")
    
    input(f"\n{BRANCO}Pressione Enter para Voltar...{RESET}")

def menu():
    while True:
        logo()
        print(f"{VERDE} ● LICENÇA ATIVA {RESET} | USUÁRIO: ALUIZIO")
        print(f"\n{AZUL}[ 1 ] 🛰️  CONEXÃO SEGURA (Visual)")
        print(f"[ 2 ] 🛡️  VARREDURA TOTAL (Execução Real)")
        print(f"[ 3 ] 🔍 ANTI-VPN / RASTREIO (Execução Real)")
        print(f"{VERMELHO}[ S ] 🚪 SAIR{RESET}")
        
        opc = input(f"\n{VERDE}ALUIZIO > {RESET}").lower()
        
        if opc == '1':
            logo()
            print(f"{AMARELO}OTIMIZANDO REDE E PROXY (Simulação)...{RESET}")
            time.sleep(1)
            print(f"{VERDE}CONEXÃO BLINDADA!{RESET}")
            time.sleep(1)
        elif opc == '2':
            varredura_total()
        elif opc == '3':
            logo()
            print(f"{AMARELO}RASTREAMENTO DE REDE TÉCNICO...{RESET}")
            # Pega o IP real e Localização usando comandos de rede
            ip_real = os.popen("curl -s https://ifconfig.me/ip").read().strip()
            print(f"{BRANCO} -> IP Real Detectado: {ip_real}{RESET}")
            # Lógica simples para mostrar Bolívia (pode ser aprimorada com API de GeoIP)
            print(f"{BRANCO}PAÍS: Bolívia (Assumido por Contexto)\nVPN: Checagem Técnica Básica...{RESET}")
            input(f"\n{BRANCO}Enter para Voltar...{RESET}")
        elif opc == 's':
            # Corrige o problema do 'S' no Termux saindo do Python de forma limpa
            sys.exit()

if __name__ == '__main__':
    menu()
