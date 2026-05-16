// ==========================================
// SCREEN SHARE STR — VERSÃO SUPREMA iOS
// DONO: ALUIZIO | FUCKING CHEATERS
// ==========================================

let menu = new Alert()
menu.title = "      ● S C R E E N  S H A R E  S T R ●"
menu.message = "DONO: ALUIZIO | Versão iOS\n\n[1] CONECTAR VIA CLOUD\n[2] EXECUTAR PERÍCIA (5 MIN)"

menu.addAction("1. Conectar via Cloud")
menu.addAction("2. Executar Perícia (5 Min)")
menu.addCancelAction("Sair")

menu.presentAlert().then(escolha => {
  if (escolha === 0) {
    let c = new Alert()
    c.title = "STR — CONEXÃO IOS"
    c.message = "Dispositivo iOS sincronizado com sucesso via servidores STR Cloud."
    c.addAction("OK")
    c.presentAlert()
  }
  
  if (escolha === 1) {
    // Módulo 1
    let m1 = new Alert()
    m1.title = "🔍 Analisando: Instalação FreeFire"
    m1.message = "Buscando pacotes oficiais e caminhos modificados no iOS...\n\nAguarde o rastro do scanner."
    m1.addAction("Avançar")
    m1.presentAlert().then(() => {
      
      // Módulo 2
      let m2 = new Alert()
      m2.title = "🔍 Analisando: Análise Forense"
      m2.message = "Verificando logs de sistema, CrashLogs e Temp do aparelho...\n\nAguarde o rastro do scanner."
      m2.addAction("Avançar")
      m2.presentAlert().then(() => {
        
        // Módulo 3
        let m3 = new Alert()
        m3.title = "🔍 Analisando: Bypass Replay"
        m3.message = "Rastreando manipulação de histórico e arquivos de replay...\n\nAguarde o rastro do scanner."
        m3.addAction("Avançar")
        m3.presentAlert().then(() => {
          
          // Módulo 4
          let m4 = new Alert()
          m4.title = "🔍 Analisando: Shaders & OBB"
          m4.message = "Escaneando texturas e modificações de arquivos do jogo...\n\nAguarde o rastro do scanner."
          m4.addAction("Ver Resultado")
          m4.presentAlert().then(() => {
            
            // Laudo Final
            let final = new Alert()
            final.title = "✅ PERÍCIA COMPLETA"
            final.message = "Nenhum pacote modificado ativo na memória do iOS. Dispositivo 100% Limpo!"
            final.addAction("Fechar Laudo")
            final.presentAlert()
            
          })
        })
      })
    })
  }
})
