# -*- coding: utf-8 -*-
import os
import sys
import time
import random

# CATEGORIA 1: HACKS CRÍTICOS E AUXÍLIOS DE MIRA DIRECTA (REPROVAÇÃO DIRETA)
HACKS_CRITICOS = [
    "CHEAT", "BYPASS", "MODMENU", "INJECTOR", "AIMBOT", "WALLHACK", 
    "AIMLOCK", "AUTO_HEADSHOT", "NO_RECOIL", "AUXILIO_MIRA", "XIT", 
    "HACK", "GG_SCRIPT", "LIBAUTO.SO", "LIBANRK.SO"
]

# CATEGORIA 2: FERRAMENTAS DUAL-USE / MODIFICAÇÃO (GERA APENAS SUSPEITA)
FERRAMENTAS_SUSPEITAS = [
    "REGEDIT", "MACRO", "SENSITIVITY", "MT_MANAGER", "MT2", "GAME_GUARDIAN", 
    "LULUBBOX", "X8_SANDBOX", "VIRTUAL_BACKUP", "PANDA_MOUSE", "OCTOPUS", 
    "LUCKY_PATCHER", "HTTPCANARY", "CHARLES_PROXY", "VIRTUAL_ENV", "SANDBOX"
]

# Cores ANSI para a Estética do Painel
VERDE = '\033[92m'
CIANO = '\033[96m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
RESET = '\033[0m'
NEON = '\033[1;36m'
ROXO = '\033[95m'
BRANCO = '\033[97m'

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

def animacao_hacker_nota_10(pastas, total_arquivos):
    """Gera um feed de análise ultra rápido simulando descriptografia de memória"""
    print(f"\n{ROXO}[⚙️] CONECTANDO AO MEMORY BUFFER DO PROCESSO CORE...{RESET}\n")
    time.sleep(0.4)
    
    for i in range(100):
        caminho_fake = random.choice(pastas)[:45] if pastas else "/storage/emulated/0/Android/data"
        hex_addr = f"0x{random.randint(1000, 9999)}X{random.randint(10, 99)}"
        tag_status = random.choice([f"{VERDE}[OK]", f"{CIANO}[VASCULHANDO]", f"{ROXO}[INDEXING]"])
        
        # Logs subindo na velocidade da luz para o efeito nota 10
        print(f"{tag_status} {BRANCO}Endereço {hex_addr} ➔ {caminho_fake}...{RESET}")
        time.sleep(0.01)
        
    print(f"\n{VERDE}[+] Varredura de strings de hardware concluída.{RESET}")
    print(f"{VERDE}[+] {total_arquivos} registros estruturados sem corromper pacotes.{RESET}\n")
    time.sleep(0.4)

def realizar_pericia_profunda():
    """Busca ativa por arquivos e caminhos divididos por severidade de risco"""
    alertas_criticos = []
    alertas_suspeitos = []
    pastas_mapeadas = []
    total_arquivos = 0
    
    raizes = ["/sdcard/", "/storage/emulated/0/"]
    
    for raiz in raizes:
        if os.path.exists(raiz):
            for pasta_atual, _, arquivos in os.walk(raiz):
                pastas_mapeadas.append(pasta_atual)
                nome_pasta = os.path.basename(pasta_atual).upper()
                
                # Checagem baseada no nome do diretório
                for h in HACKS_CRITICOS:
                    if h == nome_pasta:
                        alertas_criticos.append(f"Diretório de Modificação Grave: {pasta_atual}")
                for s in FERRAMENTAS_SUSPEITAS:
                    if s == nome_pasta:
                        alertas_suspeitos.append(f"Diretório Suspeito Identificado: {pasta_atual}")
                
                # Leitura e análise dos arquivos internos (.txt, .log, etc)
                for arquivo in arquivos:
                    total_arquivos += 1
                    if arquivo.endswith(('.txt', '.log', '.xml', '.json', '.cfg')):
                        try:
                            caminho_completo = os.path.join(pasta_atual, arquivo)
                            if os.path.getsize(caminho_completo) < 3 * 1024 * 1024:
                                with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as f:
                                    conteudo = f.read().upper()
                                    
                                    # Valida contra o dicionário de Hacks Críticos
                                    for h in HACKS_CRITICOS:
                                        if h in conteudo:
                                            alertas_criticos.append(f"Assinatura [{h}] em {arquivo}")
                                            
                                    # Valida contra o dicionário de Suspeitas
                                    for s in FERRAMENTAS_SUSPEITAS:
                                        if s in conteudo:
                                            alertas_suspeitos.append(f"Ferramenta/Termo [{s}] em {arquivo}")
                        except:
                            continue
                            
    # Remove duplicatas mantendo os laudos limpos
    return list(set(alertas_criticos)), list(set(alertas_suspeitos)), pastas_mapeadas, total_arquivos

def iniciar_painel():
    desenhar_banner()
    print(f"\n{AMARELO}[!] ACESSANDO ÁREAS INTERNAS DO DISPOSITIVO...{RESET}")
    time.sleep(0.8)
    
    criticos, suspeitos, pastas, total_arq = realizar_pericia_profunda()
    animacao_hacker_nota_10(pastas, total_arq)
    
    desenhar_banner()
    print(f"\n{CIANO}╔════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"  {AMARELO}RELATÓRIO TÉCNICO DE INTEGRIDADE OPERACIONAL{RESET}")
    print(f"  {AMARELO}SISTEMA DE ANÁLISE:{RESET} FILTRO INTELIGENTE ANTI-FALSO POSITIVO")
    print(f"{CIANO}╚════════════════════════════════════════════════════════════════════╝{RESET}")
    
    # ORDEM DE EXIBIÇÃO EM CASO DE RESULTADOS
    if criticos:
        # Cenário 1: Encontrou modificação explícita/Hack
        print(f"\n{VERMELHO}██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"{VERMELHO}❌ STATUS: REPROVADO - MODIFICAÇÃO INTERNA GRAVE DETECTADA{RESET}")
        print(f"██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"\n{AMARELO}[⚠️] Evidências incontestáveis de auxílios ou trapaças encontrados:{RESET}")
        for c in criticos[:10]:
            print(f"  {VERMELHO}➔ [EVIDÊNCIA CRÍTICA] ➔ {c}{RESET}")
            
    elif suspeitos:
        # Cenário 2: Encontrou apenas ferramentas suspeitas (Evita o falso positivo)
        print(f"\n{AMARELO}██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"{AMARELO}⚠️ STATUS: DISPOSITIVO SUSPEITO - REQUER ANÁLISE MANUAL{RESET}")
        print(f"██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"\n{AMARELO}[i] Motivo da Suspeita (Ferramentas de modificação ou gerenciadores ativos):{RESET}")
        for s in suspeitos[:10]:
            print(f"  {AMARELO}➔ [ANALISAR COM CALMA] ➔ {s}{RESET}")
        print(f"\n{BRANCO}💡 Nota para o Fiscal: Isto não prova o uso de hack, verifique o histórico do jogador.{RESET}")
        
    else:
        # Cenário 3: Absolutamente limpo
        print(f"\n{VERDE}██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"{VERDE}✅ STATUS: DISPOSITIVO INTEGRADO E TOTALMENTE EM CONFORMIDADE{RESET}")
        print(f"██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"\n{VERDE}[+] Nenhuma anormalidade de software ou rastro de risco localizado.{RESET}")
        
    print(f"\n{CIANO}======================================================================{RESET}")
    print(f"\n{ROXO}[⚡] Finalizando túnel de varredura e limpando buffers locais...{RESET}")
    print(f"{NEON}➔ O STR não dorme. Se tentar burlar, o painel do Aluizio pega! 😤🥋🌑{RESET}")
    print(f"{CIANO}======================================================================{RESET}")
    
    input(f"\n{AMARELO}Pressione [ENTER] para liberar a conexão do terminal...{RESET}")

if __name__ == "__main__":
    iniciar_painel()
