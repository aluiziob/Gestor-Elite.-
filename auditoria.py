# -*- coding: utf-8 -*-
import os
import sys
import time

# DICIONÁRIO DE EXEMPLO - PALAVRAS CHAVE COMUNS EM LOGS DE AUDITORIA
TERMOS_SUSPEITOS = [
    "CHEAT", "BYPASS", "MODMENU", "INJECTOR", "REGEDIT", 
    "AIMBOT", "WALLHACK", "GAME_GUARDIAN", "MT_MANAGER",
    "COM.DTS.FREEFIRETH", "LIBAUTO.SO", "LIBANRK.SO"
]

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def animar_carregamento(mensagem):
    print(f"\n{mensagem}")
    barra_tamanho = 30
    for i in range(barra_tamanho + 1):
        percentual = int((i / barra_tamanho) * 100)
        blocos = "█" * i
        espacos = " " * (barra_tamanho - i)
        sys.stdout.write(f"\r[{blocos}{espacos}] {percentual}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

def executar_varredura():
    limpar_tela()
    print("==================================================")
    print("        ● S C R E E N  S H A R E  S T R ●         ")
    print("         PAINEL DE AUDITORIA DE SISTEMA           ")
    print("==================================================")
    
    # Solicita o caminho do arquivo de log que foi exportado ou gerado
    print("\n[!] Certifique-se de que o arquivo de log está na memória interna.")
    arquivo_alvo = input("Digite o nome ou caminho do arquivo de log (ex: log.txt): ").strip()
    
    # Caminhos comuns onde o arquivo pode estar no Android
    caminhos_busca = [
        arquivo_alvo,
        f"/sdcard/{arquivo_alvo}",
        f"/sdcard/Download/{arquivo_alvo}",
        f"/storage/emulated/0/Download/{arquivo_alvo}"
    ]
    
    conteudo = None
    caminho_encontrado = None
    
    # Tenta localizar e ler o arquivo
    for caminho in caminhos_busca:
        if os.path.exists(caminho) and os.path.isfile(caminho):
            try:
                with open(caminho, 'r', encoding='utf-8', errors='ignore') as f:
                    conteudo = f.read().upper()
                    caminho_encontrado = caminho
                    break
            except Exception:
                continue
                
    if not conteudo:
        print("\n[X] ERRO: Arquivo não localizado ou sem permissão de leitura.")
        print("Certifique-se de digitar o nome correto e dar permissão ao Termux.")
        input("\nPressione Enter para voltar..."); return

    animar_carregamento("🔍 PROCESSANDO ARQUIVO E MAPEANDO REGISTROS...")
    
    # Varredura de strings
    achados = [termo for termo in TERMOS_SUSPEITOS if termo in conteudo]
    
    print("==================================================")
    print("                 LAUDO DA PERÍCIA                 ")
    print("==================================================")
    print(f"Arquivo analisado: {os.path.basename(caminho_encontrado)}")
    
    if achados:
        print("\n❌ STATUS: DISPOSITIVO SUSPEITO / REPROVADO")
        print("Assinaturas ou caminhos modificados encontrados:")
        for item in achados:
            print(f" • [FLAG] -> {item}")
    else:
        print("\n✅ STATUS: DISPOSITIVO LIMPO / APROVADO")
        print("Nenhum padrão de modificação conhecido foi detectado neste arquivo.")
        
    print("==================================================")
    input("\nVarredura finalizada. Pressione Enter para sair...")

if __name__ == "__main__":
    executar_varredura()
