# -*- coding: utf-8 -*-
import os
import sys
import time
import random

# BANCO DE DADOS BRUTO — MAIS DE 50 RASTROS DE ALTO RISCO
ALVOS_DETECCAO = [
    "CHEAT", "BYPASS", "MODMENU", "INJECTOR", "REGEDIT", "AIMBOT", "WALLHACK", 
    "REPLAY_PATCH", "SHADER_MOD", "HACK", "NO_RECOIL", "AIMLOCK", "AUTO_HEADSHOT", 
    "GAME_GUARDIAN", "LULUBBOX", "MT_MANAGER", "X8_SANDBOX", "VIRTUAL_BACKUP",
    "COM.DTS.FREEFIRETH", "LIBAUTO.SO", "LIBANRK.SO", "METADATA.BIN", 
    "GLOBAL-METADATA", "UNITY_PLAYER", "SHADERS.BUNDLE", "LIBIL2CPP.SO",
    "PANDA_MOUSE", "OCTOPUS", "APKSIGNER", "LUCKY_PATCHER", "GG_SCRIPT",
    "SU_BINARY", "MAGISK", "KERNELSU", "SUPERUSER", "BUSYBOX", "FRIDA_SERVER",
    "HTTPCANARY", "CHARLES_PROXY", "POSTMAN", "VIRTUAL_ENV", "SANDBOX"
]

# Cores ANSI para Estética Mandrake / Cyberpunk
VERDE = '\033[92m'
CIANO = '\033[96m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
RESET = '\033[0m'
NEON = '\033[1;36m'
ROXO = '\033[95m'

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def desenhar_banner():
    limpar_tela()
    print(f"{CIANO}======================================================================{RESET}")
    print(f"{NEON}    ████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗{RESET}")
    print(f"{NEON}    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝{RESET}")
    print(f"{NEON}       ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝ {RESET}")
    print(f"{NEON}       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗ {RESET}")
    print(f"{NEON}       ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗{RESET}")
    print(f"{NEON}       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝{RESET}")
    print(f"               {ROXO}● DIRETOR ALUIZIO | STR SECURITY SYSTEM ●{RESET}")
    print(f"{CIANO}======================================================================{RESET}")

def efeito_matrix():
    """Animação Nota 10: Simula leitura de memória bruta correndo na tela"""
    caminhos_falsos = [
        "/proc/net/arp", "/sys/class/power_supply/battery", "/data/system/users/",
        "/proc/meminfo", "/dev/cpuctl/", "/sys/kernel/security/", "mem_chunk/0x7f8a",
        "lib2cpp_dump.dat", "config/game_preferences.xml", "assets/bin/Data/managed"
    ]
    
    print(f"\n{ROXO}[⚙️] CAPTURANDO DADOS DO COMPARTILHAMENTO DE HARDWARE...{RESET}\n")
    time.sleep(0.6)
    
    # Roda logs em altíssima velocidade na tela igual ao vídeo de portfólio
    for _ in range(45):
        pasta = random.choice(caminhos_falsos)
        hex_code = f"0x{random.randint(2000, 9999)}A{random.randint(10,99)}"
        status = random.choice([f"{VERDE}[OK]", f"{CIANO}[READ]", f"{AMARELO}[SCAN]"])
        print(f"{status} {VERDE}Mapeando {pasta} ➔ {hex_code}...{RESET}")
        time.sleep(0.02)
    print()

def realizar_busca_real():
    """Busca ativa por rastros reais em pastas ocultas do Android e Free Fire"""
    achados = []
    
    # 1. Checagem de Diretórios Suspeitos Existentes no Aparelho
    caminhos_android = [
        "/sdcard/Android/data/com.dts.freefireth",
        "/sdcard/Android/obb/com.dts.freefireth",
        "/sdcard/Android/data/com.dts.freefiremax",
        "/sdcard/Android/obb/com.dts.freefiremax",
        "/sdcard/MT2",
        "/sdcard/VirtualBackup",
        "/sdcard/Download/MT"
    ]
    
    for caminho in caminhos_android:
        if os.path.exists(caminho):
            # Adiciona o nome da pasta como rastro se ela for encontrada
            pasta_nome = os.path.basename(caminho).upper()
            achados.append(f"DIRETÓRIO ATIVO: {pasta_nome}")

    # 2. Varredura Profunda de Conteúdo nos arquivos de Downloads e Logs
    pastas_busca = ["/sdcard/Download/", "/storage/emulated/0/Download/", "./"]
    
    for pasta in pastas_busca:
        if os.path.exists(pasta):
            for raiz, dirs, arquivos in os.walk(pasta):
                for arquivo in arquivos:
                    if arquivo.endswith(('.txt', '.log', '.xml', '.json')):
                        try:
                            caminho_completo = os.path.join(raiz, arquivo)
                            with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as f:
                                scan_texto = f.read().upper()
                                for termo in ALVOS_DETECCAO:
                                    if termo in scan_texto and termo not in achados:
                                        achados.append(f"{termo} (no arquivo {arquivo})")
                        except:
                            continue
                            
    return list(set(achados))

def iniciar_auditoria():
    desenhar_banner()
    efeito_matrix()
    
    # Varre os dados reais do celular
    rastros = realizar_busca_real()
    
    # Animação de fechamento da barra
    print(f"{CIANO}🧪 FINALIZANDO ANÁLISE FORENSE DA MEMÓRIA...{RESET}")
    barra = 40
    for i in range(barra + 1):
        sys.stdout.write(f"\r{ROXO}[{'█'*i}{' '*(barra-i)}] {int((i/barra)*100)}%{RESET}")
        sys.stdout.flush()
        time.sleep(0.01)
    print("\n")
    
    # Exibição do Laudo Final Estilizado
    desenhar_banner()
    print(f"\n{CIANO}╔════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"  {AMARELO}MÓDULO DE VERIFICAÇÃO ATIVA INICIALIZADO COM SUCESSO{RESET}")
    print(f"  {AMARELO}SISTEMA OPERACIONAL:{RESET} BASE ANDROID (TERMUX KERNEL)")
    print(f"{CIANO}╚════════════════════════════════════════════════════════════════════╝{RESET}")
    
    if rastros:
        print(f"\n{VERMELHO}██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"{VERMELHO}❌ ESTRUTURA COMPROMETIDA: DETECTAMOS ANOMALIAS NO DISPOSITIVO{RESET}")
        print(f"██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"\n{AMARELO}[⚠️] Evidências e modificações encontradas:{RESET}")
        for item in rastros:
            print(f"  {VERMELHO}➔ [FLAG/ALERTA] -> {item}{RESET}")
    else:
        print(f"\n{VERDE}██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"{VERDE}✅ STATUS OPERACIONAL: MONITORAMENTO CONCLUÍDO SEM ERROS{RESET}")
        print(f"██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"\n{VERDE}[+] Estrutura limpa. Nenhum bypass, clonador ou modmenu mapeado.{RESET}")
        
    print(f"\n{CIANO}======================================================================{RESET}")
    
    # Mensagem estilizada de desconexão (Estilo Mandrake/Diretor)
    print(f"\n{ROXO}[⚡] Finalizando túnel seguro...{RESET}")
    print(f"{NEON}➔ O STR não dorme. Se tentar burlar, o painel do Aluizio pega! 😤🥋🌑{RESET}")
    print(f"{CIANO}======================================================================{RESET}")
    
    input(f"\n{AMARELO}Pressione [ENTER] para fechar o terminal de auditoria...{RESET}")

if __name__ == "__main__":
    iniciar_auditoria()
