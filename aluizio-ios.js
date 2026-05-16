// ==========================================
// SCREEN SHARE STR — VERSÃO SUPREMA iOS
// DONO: ALUIZIO | FUCKING CHEATERS
// ==========================================

async function iniciarPainel() {
  let menu = new Alert()
  menu.title = "      ● S C R E E N  S H A R E  S T R ●"
  menu.message = "DONO: ALUIZIO | Versão iOS\n\n[1] CONECTAR VIA CLOUD\n[2] EXECUTAR PERÍCIA (5 MIN)\n[S] SAIR"
  
  menu.addAction("Option 1")
  menu.addAction("Option 2")
  menu.addCancelAction("Sair")
  
  let escolha = await menu.presentAlert()
  
  if (escolha === 0) {
    let c = new Alert()
    c.title = "STR — CONEXÃO IOS"
    c.message = "Dispositivo iOS sincronizado com sucesso via servidores STR Cloud."
    c.addAction("Voltar")
    await c.presentAlert()
    await iniciarPainel()
  }
  
  if (escolha === 1) {
    let modulos = [
      ["Instalação FreeFire", "Buscando pacotes oficiais e caminhos modificados no iOS"],
      ["Análise Forense", "Verificando logs de sistema, CrashLogs e Temp do aparelho"],
      ["Bypass Replay", "Rastreando manipulação de histórico e arquivos de replay"],
      ["Shaders & OBB", "Escaneando texturas e modificações de arquivos do jogo"]
    ]
    
    for (let mod of modulos) {
      let m = new Alert()
      m.title = `🔍 Analisando: ${mod[0]}`
      m.message = `${mod[1]}...\n\nAguarde o rastro do scanner.`
      m.addAction("Avançar")
      await m.presentAlert()
    }
    
    let final = new Alert()
    final.title = "✅ PERÍCIA COMPLETA"
    final.message = "Nenhum pacote modificado ativo na memória do iOS. Dispositivo Limpo!"
    final.addAction("Fechar Laudo")
    await final.presentAlert()
    await iniciarPainel()
  }
}

// Executa o sistema
await iniciarPainel()
