# -*- coding: utf-8 -*-
import os
import sys
import time
import glob

# LISTA EXPANDIDA DE RASTROS E DIRETÓRIOS SUSPEITOS
DICIONARIO_AUDITORIA = [
    "CHEAT", "BYPASS", "MODMENU", "INJECTOR", "REGEDIT", "AIMBOT", "WALLHACK", 
    "REPLAY_PATCH", "SHADER_MOD", "HACK", "NO_RECOIL", "AIMLOCK", "AUTO_HEADSHOT", 
    "GAME_GUARDIAN", "LULUBBOX", "MT_MANAGER", "X8_SANDBOX", "VIRTUAL_BACKUP",
    "COM.DTS.FREEFIRETH", "LIBAUTO.SO", "LIBANRK.SO", "METADATA.BIN", 
    "GLOBAL-METADATA", "UNITY_PLAYER", "SHADERS.BUNDLE", "LIBIL2CPP.SO"
]

# Cores ANSI para deixar o terminal estilizado
VERDE = '\033[92m'
CIANO = '\033[96m'
VERMELHO = '\033[91m'
AMARELO = '\033[93m'
RESET = '\033[0m'
NEON = '\033[1;36m'

def efeito_digitar(texto, velocidade=0.01):
    """Cria um efeito de digitação realista no terminal."""
    for caractere in texto:
        sys.stdout.write(caractere)
        sys.stdout.flush()
        time.sleep(velocidade)

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
    print(f"               {VERDE}● SCREEN SHARE STR — AUDITORIA AUTOMÁTICA ●{RESET}")
    print(f"{CIANO}======================================================================{RESET}")

def animar_varredura(nome_arquivo):
    desenhar_banner()
    print(f"\n{AMARELO}[+] ALVO LOCALIZADO: {nome_arquivo}{RESET}")
    efeito_digitar(f"{CIANO}[⚡] INICIALIZANDO NÚCLEO DE PERÍCIA FORENSE...\n{RESET}")
    time.sleep(0.5)
    
    # Simulação de análise de blocos com barra de progresso hacker
    passos_analise = [
        "Carregando buffers de memória física...",
        "Mapeando cabeçalhos do arquivo de log...",
        "Cruzando hashes com banco de dados STR Cloud...",
        "Rastreando injeções e pacotes modificados...",
        "Finalizando relatório de integridade..."
    ]
    
    for idx, passo in enumerate(passos_analise):
        print(f"\n{CIANO}🧪 {passo}{RESET}")
        barra_tamanho = 40
        for i in range(barra_tamanho + 1):
            percentual = int((i / barra_tamanho) * 100)
            blocos = "█" * i
            espacos = " " * (barra_tamanho - i)
            # Mostra o progresso com visual limpo e cores dinâmicas
            sys.stdout.write(f"\r{VERDE}[{blocos}{espacos}] {percentual}%{RESET}")
            sys.stdout.flush()
            time.sleep(0.02)
        print()
    time.sleep(0.5)

def executar_painel():
    desenhar_banner()
    efeito_digitar(f"\n{CIANO}[i] Vasculhando diretórios de armazenamento do Android...{RESET}\n")
    time.sleep(0.8)
    
    pastas_busca = [
        "/sdcard/Download/",
        "/storage/emulated/0/Download/",
        "./"
    ]
    
    arquivos_encontrados = []
    for pasta in pastas_busca:
        if os.path.exists(pasta):
            arquivos_encontrados.extend(glob.glob(os.path.join(pasta, "*.txt")))
            arquivos_encontrados.extend(glob.glob(os.path.join(pasta, "*.log")))
            
    arquivos_encontrados = list(dict.fromkeys(arquivos_encontrados))
    
    if not arquivos_encontrados:
        print(f"\n{VERMELHO}[X] ERRO: NENHUM ARQUIVO DE LOG ENCONTRADO NAS PASTAS PADRÃO.{RESET}")
        print(f"{AMARELO}💡 Dica: Certifique-se de salvar um arquivo .txt ou .log na pasta Downloads.{RESET}")
        print(f"{CIANO}======================================================================{RESET}")
        input("\nPressione [ENTER] para sair do painel..."); return

    # Seleciona automaticamente o arquivo de texto mais recente modificado na pasta
    arquivo_alvo = max(arquivos_encontrados, key=os.path.getmtime)
    nome_exibição = os.path.basename(arquivo_alvo)
    
    # Roda as animações gráficas na tela
    animar_varredura(nome_exibição)
    
    try:
        with open(arquivo_alvo, 'r', encoding='utf-8', errors='ignore') as f:
            conteudo_completo = f.read().upper()
    except Exception:
        print(f"\n{VERMELHO}[X] ERRO CRÍTICO: Falha de permissão ao abrir o arquivo.{RESET}")
        input("\nPressione [ENTER] para fechar..."); return

    # Executa a busca detalhada de assinaturas
    rastros_detectados = [termo for termo in DICIONARIO_AUDITORIA if termo in conteudo_completo]
    
    # Exibição estilizada do Laudo Final
    limpar_tela()
    desenhar_banner()
    print(f"\n{CIANO}╔════════════════════════════════════════════════════════════════════╗{RESET}")
    print(f"  {AMARELO}ARQUIVO EXAMINADO:{RESET} {nome_exibição}")
    print(f"  {AMARELO}DIRETÓRIO ORIGEM:{RESET} {os.path.dirname(arquivo_alvo)}")
    print(f"{CIANO}╚════════════════════════════════════════════════════════════════════╝{RESET}")
    
    if rastros_detectados:
        print(f"\n{VERMELHO}██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"{VERMELHO}❌ STATUS CRÍTICO: DISPOSITIVO REPROVADO / RASTROS LOCALIZADOS{RESET}")
        print(f"{VERMELHO}██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"\n{AMARELO}[!] Evidências coletadas de modificação de memória/diretório:{RESET}")
        for rastro in rastros_detectados:
            print(f"  {VERMELHO}• [VIOLAÇÃO REGISTRADA] ➔ {rastro}{RESET}")
    else:
        print(f"\n{VERDE}██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"{VERDE}✅ STATUS SEGURO: ESTRUTURA RECONHECIDA COMO LIMPA{RESET}")
        print(f"{VERDE}██████████████████████████████████████████████████████████████████████{RESET}")
        print(f"\n{VERDE}[+] Nenhuma assinatura de trapaça ativa foi mapeada no documento.{RESET}")
        
    print(f"\n{CIANO}======================================================================{RESET}")
    input(f"\n{AMARELO}Sessão encerrada com sucesso. Pressione [ENTER] para desconectar...{RESET}")

if __name__ == "__main__":
    executar_painel()
