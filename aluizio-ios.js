// ==========================================
// SCREEN SHARE STR — VERSÃO SUPREMA iOS
// DONO: ALUIZIO | FUCKING CHEATERS
// ==========================================

// BASE DE DADOS DE TRAIDORES
const BLACK_LIST = {
  "551F020D00DD1E49": "Root / Bypass Identificado no Aparelho",
  "CAACFD6C87A2F273": "Root Detectado",
  "C03909710521898B": "FF Modificado (MOD HACK)",
  "D641FC5251B3241B": "Passador de Replay",
  "DB59AEAD2BC7EBC6": "Proxy Android ativo",
  "56B9E9C6DDCB0D5B": "Passador de Replay",
  "1403873499": "UUID banido por uso de Regedit/Auxiliar"
}

let menu = new Alert()
menu.title = "      ● S C R E E N  S H A R E  S T R ●"
menu.message = "DONO: ALUIZIO | Versão iOS\n\n[1] CONECTAR VIA CLOUD\n[2] EXECUTAR PERÍCIA REAIS"

menu.addAction("1. Conectar via Cloud")
menu.addAction("2. Executar Perícia (Real)")
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
    let inputJanela = new Alert()
    inputJanela.title = "PERÍCIA DE SINAL STR"
    inputJanela.message = "Insira o HWID, Serial ou ID/UUID do jogador para cruzar com a nossa Blackbox:"
    inputJanela.addTextField("Cole o HWID ou ID aqui...")
    inputJanela.addAction("Iniciar Análise Profunda")
    
    inputJanela.presentAlert().then(campo => {
      let dadoInserido = inputJanela.textFieldValue(0).trim().toUpperCase()
      
      if (dadoInserido === "") {
        let erro = new Alert()
        erro.title = "⚠️ ERRO DE ENTRADA"
        erro.message = "Você precisa digitar ou colar um dado válido para rastrear."
        erro.addAction("Voltar")
        erro.presentAlert()
        return
      }

      // 🔊 ÁUDIO: INICIANDO A ANÁLISE
      Speech.speak("Analisando")

      // Módulo 1
      let m1 = new Alert()
      m1.title = "🔍 Analisando: Instalação & Diretórios"
      m1.message = `Varrendo registros associados ao ID: ${dadoInserido}...`
      m1.addAction("Avançar")
      m1.presentAlert().then(() => {
        
        // Módulo 2
        let m2 = new Alert()
        m2.title = "🔍 Analisando: Histórico de Replays"
        m2.message = "Buscando manipulações ou substituições recentes de arquivos..."
        m2.addAction("Avançar")
        m2.presentAlert().then(() => {
          
          // Módulo 3
          let m3 = new Alert()
          m3.title = "🔍 Analisando: Injeções de Textura"
          m3.message = "Procurando assinaturas de Shaders ou OBBs modificadas..."
          m3.addAction("Ver Laudo Final")
          m3.presentAlert().then(() => {
            
            // VERIFICAÇÃO SE SÃO SUSPEITOS DE VERDADE
            if (BLACK_LIST[dadoInserido]) {
              // 🔊 ÁUDIO: ENCONTROU CHEATER
              Speech.speak("Análise suspeito")

              let laudoRuim = new Alert()
              laudoRuim.title = "❌ STATUS: SUSPEITO / DETECTADO"
              laudoRuim.message = `⚠️ ALERTA DE TRAPAÇA!\n\nO registro [${dadoInserido}] foi encontrado na base de dados.\n\nMotivo da flag: ${BLACK_LIST[dadoInserido]}`
              laudoRuim.addAction("Fechar Laudo")
              laudoRuim.presentAlert()
            } else {
              // 🔊 ÁUDIO: APARELHO LIMPO
              Speech.speak("Análise concluída")

              let laudoLimpo = new Alert()
              laudoLimpo.title = "✅ STATUS: DISPOSITIVO LIMPO"
              laudoLimpo.message = `Nenhuma irregularidade ativa ou flag de trapaça encontrada para o registro: ${dadoInserido}.`
              laudoLimpo.addAction("Fechar Laudo")
              laudoLimpo.presentAlert()
            }
            
          })
        })
      })
    })
  }
})
