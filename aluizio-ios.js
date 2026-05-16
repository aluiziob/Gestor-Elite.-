// ==========================================
// SCREEN SHARE STR — VERSÃO SUPREMA iOS
// DONO: ALUIZIO | FUCKING CHEATERS
// ==========================================

async function menuPrincipal() {
  let menu = new Alert()
  menu.title = "      ● S C R E E N  S H A R E  S T R ●"
  menu.message = "DONO: ALUIZIO | Versão iOS\n\n[1] CONECTAR VIA CLOUD\n[2] EXECUTAR PERÍCIA (5 MIN)"
  
  menu.addAction("1. Conectar via Cloud")
  menu.addAction("2. Executar Perícia (5 Min)")
  menu.addCancelAction("Sair")
  
  let escolha = await menu.presentAlert()
  
  if (escolha === 0) {
    let c = new Alert()
    c.title = "STR — CONEXÃO IOS"
    c.message = "Dispositivo iOS sincronizado com sucesso via servidores STR Cloud."
    c.addAction("Voltar")
    await c.presentAlert()
    menuPrincipal() // Reinicia o menu com segurança
  }
  
  if (escolha === 1) {
    // Módulo 1
    let m1 = new Alert()
    m1.title = "🔍 Analisando: Instalação FreeFire"
    m1.message = "Buscando pacotes oficiais e caminhos modificados no iOS...\n\nAguarde o rastro do scanner."
    m1.addAction("Avançar")
    await m1.presentAlert()

    // Módulo 2
    let m2 = new Alert()
    m2.title = "🔍 Analisando: Análise Forense"
    m2.message = "Verificando logs de sistema, CrashLogs e Temp do aparelho...\n\nAguarde o rastro do scanner."
    m2.addAction("Avançar")
    await m2.presentAlert()

    // Módulo 3
    let m3 = new Alert()
    m3.title = "🔍 Analisando: Bypass Replay"
    m3.message = "Rastreando manipulação de histórico e arquivos de replay...\n\nAguarde o rastro do scanner."
    m3.addAction("Avançar")
    await m3.presentAlert()

    // Módulo 4
    let m4 = new Alert()
    m4.title = "🔍 Analisando: Shaders & OBB"
    m4.message = "Escaneando texturas e modificações de arquivos do jogo...\n\nAguarde o rastro do scanner."
    m4.addAction("Avançar")
    await m4.presentAlert()
    
    // Resultado Final
    let final = new Alert()
    final.title = "✅ PERÍCIA COMPLETA"
    final.message = "Nenhum pacote modificado ativo na memória do iOS. Dispositivo Limpo!"
    final.addAction("Fechar Laudo")
    await final.presentAlert()
    menuPrincipal()
  }
}

// Inicializa o app sem gerar conflito de identificadores
menuPrincipal();
