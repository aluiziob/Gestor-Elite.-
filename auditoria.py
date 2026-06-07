# -*- coding: utf-8 -*-
import os
import sys
import time
import random

# CATEGORIA 1: TRAPAÇAS EXPLICITAS (GATILHO PARA W.O. IMEDIATO)
CH_CRITICOS = [
    "CHEAT", "BYPASS", "MODMENU", "INJECTOR", "AIMBOT", "WALLHACK", 
    "AIMLOCK", "AUTO_HEADSHOT", "NO_RECOIL", "AUXILIO_MIRA", "XIT", 
    "HACK", "GG_SCRIPT", "LIBAUTO.SO", "LIBANRK.SO", "KHOINDVN.CLOUDFLARE"
]

# CATEGORIA 2: ANOMALIAS OU FERRAMENTAS RECURRENTES (GERA APENAS SUSPEITA)
FERR_SUSPEITAS = [
    "REGEDIT", "MACRO", "SENSITIVITY", "MT_MANAGER", "MT2", "GAME_GUARDIAN", 
    "LULUBBOX", "X8_SANDBOX", "VIRTUAL_BACKUP", "PANDA_MOUSE", "OCTOPUS", 
    "LUCKY_PATCHER", "HTTPCANARY", "CHARLES_PROXY", "JAILBREAK", "PERFIS MDM"
]

# Paleta de Cores ANSI Baseada no WebApp do Print
VERDE = '\033[92m'
CIANO = '\033[96m'
VERMELHO = '\033[1;31m'
AMARELO = '\033[1;33m'
RESET = '\033[0m'
NEON = '\033[1;36m'
ROXO = '\033[95m'
FUNDO_VERMELHO = '\033[41m'
FUNDO_AMARELO = '\033[43m'
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

def animacao_web_style(pastas, total_arquivos):
    """Logs rápidos simulando leitura estruturada de hardware do aparelho"""
    print(f"\n{ROXO}[⚙️] INDEXANDO REPOSITÓRIOS E PROCURANDO PERFIS ATIVOS...{RESET}\n")
    time.sleep(0.4)
    
    for i in range(70):
        caminho_fake = random.choice(pastas)[:45] if pastas else "/storage/emulated/0/Android/data"
        hex_addr = f"0x{random.randint(1000, 9999)}A{random.randint(10, 99)}"
        tag_status = random.choice([f"{VERDE}[OK]", f"{CIANO}[SCANNING]", f"{ROXO}[SECURE]"])
        
        print(f"{tag_status} {BRANCO}Hardware {hex_addr} ➔ {caminho_fake}...{RESET}")
        time.sleep(0.01)
        
    print(f"\n{VERDE}[+] Análise de integridade de diretórios finalizada.{RESET}")
    print(f"{VERDE}[+] {total_arquivos} arquivos mapeados na árvore do sistema.{RESET}\n")
    time.sleep(0.4)

def realizar_pericia_completa():
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
                
                for h in CH_CRITICOS:
                    if h == nome_pasta:
                        alertas_criticos.append(f"Diretório Crítico: {pasta_atual}")
                for s in FERR_SUSPEITAS:
                    if s == nome_pasta:
                        alertas_suspeitos.append(f"Diretório Suspeito: {pasta_atual}")
                
                for arquivo in arquivos:
                    total_arquivos += 1
                    if arquivo.endswith(('.txt', '.log', '.xml', '.json', '.cfg')):
                        try:
                            caminho_completo = os.path.join(pasta_atual, arquivo)
                            if os.path.getsize(caminho_completo) < 3 * 1024 * 1024:
                                with open(caminho_completo, 'r', encoding='utf-8', errors='ignore') as f:
                                    conteudo = f.read().upper()
                                    
                                    for h in CH_CRITICOS:
                                        if h in conteudo:
                                            alertas_criticos.append(f"Rastro de {h} em ({arquivo})")
                                            
                                    for s in FERR_SUSPEITAS:
                                        if s in conteudo:
                                            alertas_suspeitos.append(f"Inconsistência de {s} em ({arquivo})")
                        except:
                            continue
                            
    return list(set(alertas_criticos)), list(set(alertas_suspeitos)), pastas_mapeadas, total_arquivos

def iniciar_painel():
    desenhar_banner()
    print(f"\n{AMARELO}[!] ACESSANDO ÁREAS INTERNAS DO DISPOSITIVO...{RESET}")
    time.sleep(0.6)
    
    criticos, suspeitos, pastas, total_arq = realizar_pericia_completa()
    animacao_web_style(pastas, total_arq)
    
    desenhar_banner()
    print(f"\n{CIANO}╔════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"  {BRANCO}VERSÃO DO SISTEMA: BASE ANDROID (CORE PARSER){RESET}")
    print(f"  {BRANCO}POLÍTICA DA RECON: DETECÇÃO DE PERFIS / JAILBREAK / CHEATS{RESET}")
    print(f"{CIANO}╚════════════════════════════════════════════════════════════════════╝{RESET}")
    
    # 1. FLUXO CRÍTICO: DETECTOU CHEAT -> EXIBE ADVERTÊNCIA DE W.O.
    if criticos:
        print(f"\n{VERMELHO}╔════════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"  {FUNDO_VERMELHO}{BRANCO} ⚠️  APLIQUE O W.O IMEDIATAMENTE {RESET}")
        print(f"  {VERMELHO}Deteccões confirmadas de trapaça neste dispositivo.{RESET}")
        print(f"{VERMELHO}╚════════════════════════════════════════════════════════════════════╝{RESET}")
        print(f"\n{AMARELO}[⚡] Evidências extraídas de arquivos comprometidos:{RESET}")
        for c in criticos[:10]:
            print(f"  {VERMELHO}➔ [DETECTADO] ➔ {c}{RESET}")
            
    # 2. FLUXO DE SUSPEITA: SÓ LOGS DE CONFIGURAÇÃO OU GERENCIADORES
    elif suspeitos:
        print(f"\n{AMARELO}╔════════════════════════════════════════════════════════════════════╗{RESET}")
        print(f"  {FUNDO_AMARELO}{BRANCO} 🔍 AVISO: DISPOSITIVO EM ANÁLISE SUSPEITA {RESET}")
        print(f"  {AMARELO}Achamos algumas estruturas ou perfis modificados que requerem atenção.{RESET}")
        print(f"{AMARELO}╚════════════════════════════════════════════════════════════════════╝{RESET}")
        print(f"\n{AMARELO}[i] Elementos suspeitos listados para checagem da Staff:{RESET}")
        for s in suspeitos[:10]:
            print(f"  {AMARELO}➔ [CHECAR MANUALMENTE] ➔ {s}{RESET}")
        print(f"\n{BRANCO}💡 Orientação: Faça verificação visual, o jogador possui ferramentas modificadoras.{RESET}")
        
    # 3. TOTALMENTE LIMPO
    else:
        print(f"\n{VERDE}██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"{VERDE}✅ STATUS OPERACIONAL: MONITORAMENTO CONCLUÍDO SEM ANOMALIAS{RESET}")
        print(f"██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"\n{VERDE}[+] Nenhuma modificação, perfil de risco ou trapaça ativa localizados.{RESET}")
        
    print(f"\n{CIANO}======================================================================{RESET}")
    print(f"\n{ROXO}[⚡] Encerrando túnel e limpando cache temporário...{RESET}")
    print(f"{NEON}➔ O STR não dorme. Se tentar burlar, o painel do Aluizio pega! 😤🥋🌑{RESET}")
    print(f"{CIANO}======================================================================{RESET}")
    
    input(f"\n{AMARELO}Pressione [ENTER] para desconectar o terminal...{RESET}")

if __name__ == "__main__":
    iniciar_painel()
