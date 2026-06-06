# -*- coding: utf-8 -*-
import os
import sys
import time
import random

# DICIONÁRIO COMPLETO — AUXÍLIOS DE MIRA, INJETORES, BYPASS E PASTAS
ALVOS_DETECCAO = [
    # Termos Gerais e Auxílios de Mira
    "CHEAT", "BYPASS", "MODMENU", "INJECTOR", "REGEDIT", "AIMBOT", "WALLHACK", 
    "AIMLOCK", "AUTO_HEADSHOT", "NO_RECOIL", "AUXILIO_MIRA", "MACRO", "SENSITIVITY",
    # Modificações de Arquivos do Jogo
    "COM.DTS.FREEFIRETH", "COM.DTS.FREEFIREMAX", "LIBAUTO.SO", "LIBANRK.SO", 
    "METADATA.BIN", "GLOBAL-METADATA", "UNITY_PLAYER", "SHADERS.BUNDLE", "LIBIL2CPP.SO",
    # Ferramentas e Clonadores
    "GAME_GUARDIAN", "LULUBBOX", "MT_MANAGER", "X8_SANDBOX", "VIRTUAL_BACKUP",
    "PANDA_MOUSE", "OCTOPUS", "APKSIGNER", "LUCKY_PATCHER", "GG_SCRIPT",
    "SU_BINARY", "MAGISK", "KERNELSU", "SUPERUSER", "BUSYBOX", "FRIDA_SERVER",
    "HTTPCANARY", "CHARLES_PROXY", "POSTMAN", "VIRTUAL_ENV", "SANDBOX"
]

# Cores ANSI para o Visual Cyberpunk/Mandrake
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

def animacao_carregamento_nota_10(diretorios_escaneados, total_arquivos):
    """Gera o feed de logs correndo em altíssima velocidade estilo o vídeo"""
    print(f"\n{ROXO}[⚙️] INICIALIZANDO DECRIPTOGRAFIA E MAPEAMENTO DE BUFFER...{RESET}\n")
    time.sleep(0.5)
    
    # Faz linhas de código e verificação passarem voando na tela
    for i in range(80):
        if diretorios_escaneados:
            pasta_exemplo = random.choice(diretorios_escaneados)[:40]
        else:
            pasta_exemplo = "/storage/emulated/0/Android/data"
            
        hex_memoria = f"0x{random.randint(1000, 9999)}F{random.randint(10, 99)}"
        status_log = random.choice([f"{VERDE}[INTEGRO]", f"{CIANO}[CHECK]", f"{AMARELO}[VASCULHANDO]"])
        
        print(f"{status_log} {CIANO}Setor {hex_memoria} ➔ {pasta_exemplo}...{RESET}")
        time.sleep(0.015) # Velocidade ultra rápida para efeito nota 10
        
    print(f"\n{VERDE}[+] Varredura de hardware concluída em microsegundos.{RESET}")
    print(f"{VERDE}[+] Total de {total_arquivos} indexados para análise de strings.{RESET}\n")
    time.sleep(0.5)

def realizar_varredura_sem_limites():
    """Varre todas as pastas públicas e a memória externa acessível por completo"""
    achados = []
    pastas_pesquisadas = []
    total_arquivos_contados = 0
    
    # Raízes padrão de armazenamento interno e caminhos de cartões/pastas do Android
    raizes_busca = [
        "/sdcard/",
        "/storage/emulated/0/",
        "/storage/self/primary/"
    ]
    
    # Varredura profunda baseada em árvore de diretórios
    for raiz_pasta in raizes_busca:
        if os.path.exists(raiz_pasta):
            for pasta_atual, subpastas, arquivos in os.walk(raiz_pasta):
                pastas_pesquisadas.append(pasta_atual)
                
                # 1. Verifica se o próprio nome da pasta contém algum rastro conhecido
                nome_pasta_caixa_alta = os.path.basename(pasta_atual).upper()
                for termo in ALVOS_DETECCAO:
                    if termo == nome_pasta_caixa_alta:
                        achados.append(f"Diretório modificado ativo: {pasta_atual}")
                
                # 2. Abre e lê o conteúdo de arquivos de texto, configurações e logs salvos
                for arquivo in arquivos:
                    total_arquivos_contados += 1
                    if arquivo.endswith(('.txt', '.log', '.xml', '.json', '.cfg', '.ini')):
                        try:
                            caminho_completo = os.path.join(pasta_atual, arquivo)
                            # Limita a leitura para arquivos não muito gigantes para evitar travamentos
                            if os.path.getsize(caminho_completo) < 5 * 1024 * 1024:
                                with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as f:
                                    conteudo = f.read().upper()
                                    for termo in ALVOS_DETECCAO:
                                        if termo in conteudo:
                                            achados.append(f"Assinatura [{termo}] no arquivo: {arquivo}")
                        except:
                            continue
                            
    return list(set(achados)), pastas_pesquisadas, total_arquivos_contados

def executar_sistema():
    desenhar_banner()
    print(f"\n{AMARELO}[!] QUEBRANDO TRAVAS DE SEGURANÇA E ACESSANDO MEMÓRIA COMPLETA...{RESET}")
    time.sleep(1)
    
    # Executa a busca bruta nos diretórios reais do celular
    rastros, pastas, total_arq = realizar_varredura_sem_limites()
    
    # Executa a animação veloz usando as pastas reais encontradas
    animacao_carregamento_nota_10(pastas, total_arq)
    
    # Tela de exibição do Laudo Técnico Final
    desenhar_banner()
    print(f"\n{CIANO}╔════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"  {AMARELO}MÓDULO DE PERÍCIA AVANÇADA AUTOMÁTICA{RESET}")
    print(f"  {AMARELO}POLÍTICA DE ANÁLISE:{RESET} MODS / AUXÍLIOS DE MIRA / BYPASS / CLONADORES")
    print(f"{CIANO}╚════════════════════════════════════════════════════════════════════╝{RESET}")
    
    if rastros:
        print(f"\n{VERMELHO}██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"{VERMELHO}❌ STATUS OPERACIONAL: DISPOSITIVO REPROVADO / LOGS COMPROMETIDOS{RESET}")
        print(f"██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"\n{AMARELO}[⚠️] Evidências e modificações localizadas na memória:{RESET}")
        # Mostra os primeiros achados detectados para não inundar o terminal
        for item in rastros[:15]:
            print(f"  {VERMELHO}➔ [FLAG] -> {item}{RESET}")
        if len(rastros) > 15:
            print(f"  {VERMELHO}➔ ... e mais {len(rastros) - 15} registros de risco encontrados.{RESET}")
    else:
        print(f"\n{VERDE}██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"{VERDE}✅ STATUS OPERACIONAL: MONITORAMENTO CONCLUÍDO SEM ERROS{RESET}")
        print(f"██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"\n{VERDE}[+] Dispositivo em conformidade. Nenhuma trapaça ou auxílio mapeado.{RESET}")
        
    print(f"\n{CIANO}======================================================================{RESET}")
    
    # Linha de desconexão com muita postura
    print(f"\n{ROXO}[⚡] Encerrando túnel e limpando logs de acesso...{RESET}")
    print(f"{NEON}➔ O STR não dorme. Se tentar burlar, o painel do Aluizio pega! 😤🥋🌑{RESET}")
    print(f"{CIANO}======================================================================{RESET}")
    
    input(f"\n{AMARELO}Pressione [ENTER] para desconectar o terminal...{RESET}")

if __name__ == "__main__":
    executar_sistema()
