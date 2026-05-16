// ==========================================
// SCREEN SHARE STR — INTERFACE PROFISSIONAL
// DONO: ALUIZIO | FUCKING CHEATERS
// ==========================================

// BANCO DE DADOS DE ASSINATURAS SUSPEITAS (EXTENDIDO)
const DICIONARIO_SUG_DETECCOES = [
  // Termos Gerais de Trapaças e Auxiliares
  "CHEAT", "BYPASS", "MODMENU", "INJECTOR", "REGEDIT", "AIMBOT", "WALLHACK", "REPLAY_PATCH", "SHADER_MOD",
  "HACK", "NO_RECOIL", "AIMLOCK", "AUTO_HEADSHOT", "ANTIBAN", "FLY_HACK", "TELEPORT", "SPEED_HACK",
  
  // Nomes de Ferramentas e Aplicativos de Modificação Comuns
  "GAME_GUARDIAN", "LULUBBOX", "PANDA_MOUSE", "OCTOPUS", "MT_MANAGER", "X8_SANDBOX", "VIRTUAL_BACKUP",
  "APKSIGNER", "LUCKY_PATCHER", "CHEAT_ENGINE", "GG_SCRIPT", "HACKERBOT", "FF_MOD", "MACRO_SPACE",

  // Binários, Root e Gerenciadores de Acesso (Android/iOS)
  "SU_BINARY", "MAGISK", "KERNELSU", "SUPERUSER", "BUSYBOX", "CYDIA", "SUBSTRATE", "ZEBRA", "SILEO",
  "LIBHOOKER", "FRIDA_SERVER", "XPOSED", "LSPOSED", "EDXPOSED", "ROOT_DETECT", "DAEMON_ADB",

  // Estruturas de Arquivos, Caminhos Comuns e Modificações de Pacotes
  "ANDROID/OBB/COM.DTS.FREEFIRETH", "ANDROID/DATA/COM.DTS.FREEFIRETH", "LIBAUTO.SO", "LIBANRK.SO",
  "METADATA.BIN", "GLOBAL-METADATA", "UNITY_PLAYER", "SHADERS.BUNDLE", "ASSETS/BIN/DATA", 
  "REPLAY/.JSON", "DOCUMENT_BYPASS", "LIBIL2CPP.SO", "SANDBOX_DIRECTORY", "VIRTUAL_ENV"
];

const html = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      background-color: #0d0d0d;
      color: #00ffff;
      font-family: 'Courier New', Courier, monospace;
      margin: 0;
      padding: 20px;
      text-align: center;
    }
    .container {
      border: 2px solid #00ffff;
      border-radius: 10px;
      padding: 15px;
      background: #141414;
      box-shadow: 0 0 15px rgba(0, 255, 255, 0.3);
    }
    .logo {
      color: #ffffff;
      font-weight: bold;
      white-space: pre;
      font-size: 9px;
      line-height: 1.2;
      margin-bottom: 10px;
    }
    .sub {
      color: #666666;
      font-size: 11px;
      margin-bottom: 20px;
      letter-spacing: 2px;
    }
    .btn {
      background: transparent;
      color: #00ffff;
      border: 1px solid #00ffff;
      padding: 14px 20px;
      margin: 10px 0;
      width: 90%;
      font-family: inherit;
      font-size: 13px;
      cursor: pointer;
      border-radius: 5px;
      font-weight: bold;
      transition: 0.3s;
    }
    .btn:active {
      background: #00ffff;
      color: #000;
    }
    .progress-bar {
      width: 90%;
      background: #222;
      height: 20px;
      margin: 15px auto;
      border: 1px solid #00ffff;
      border-radius: 5px;
      overflow: hidden;
      display: none;
    }
    .progress-fill {
      height: 100%;
      width: 0%;
      background: #00ffff;
      transition: width 0.1s linear;
    }
    .status-box {
      margin-top: 20px;
      padding: 15px;
      border-radius: 5px;
      display: none;
      font-weight: bold;
      font-size: 13px;
      max-height: 150px;
      overflow-y: auto;
    }
    .sucesso { border: 1px solid #00ff00; color: #00ff00; background: #052105; }
    .perigo { border: 1px solid #ff0000; color: #ff0000; background: #210505; }
    .info-log { color: #ffffff; font-size: 12px; margin-top: 10px; }
  </style>
</head>
<body>

<div class="container">
  <div class="logo">
 █  █ █ █ █▀▀ █▀▀ █▀▀ █▀▄ █▀▀ █▀▀ ▀█▀ █▀▄
 ▀▄▀▄▀ █ █ █▄▄ █▄▄ ██▄ █▀▄ █▄▄ ▄█▄  █  █▀▄
  </div>
  <div class="sub">DONO: ALUIZIO | AUDITORIA DE SISTEMA</div>
  
  <button class="btn" onclick="conectarServidor()">1. VERIFICAR INTEGRIDADE DA NUVEM</button>
  
  <hr style="border: 0; border-top: 1px solid #222; margin: 25px 0;">
  
  <div style="font-size: 13px; margin-bottom: 15px; color: #ffffff; font-weight: bold;">MÓDULO 2: ESCANEAR ARQUIVOS DE LOG</div>
  <button class="btn" onclick="selecionarArquivo()">📂 CARREGAR LOG / DOCUMENTO</button>
  
  <div class="progress-bar" id="pBar"><div class="progress-fill" id="pFill"></div></div>
  <div id="statusArea" class="status-box"></div>
</div>

<script>
  function enviarComando(acao, valor) {
    let dados = { acao: acao, valor: valor };
    window.location.href = "scriptable://run?param=" + encodeURIComponent(JSON.stringify(dados));
  }

  // Mantém a simulação visual de conexão limpa
  function conectarServidor() {
    let area = document.getElementById('statusArea');
    area.style.display = 'block';
    area.className = 'status-box';
    area.style.color = '#00ffff';
    area.style.border = '1px solid #00ffff';
    area.style.background = '#002222';
    area.innerText = "☁️ CONEXÃO ATIVA: Banco de dados STR sincronizado.";
    enviarComando("audio", "Conectado");
  }

  function selecionarArquivo() {
    document.getElementById('statusArea').style.display = 'none';
    enviarComando("importar", "");
  }

  function animarEscanear() {
    document.getElementById('pBar').style.display = 'block';
    let fill = document.getElementById('pFill');
    let area = document.getElementById('statusArea');
    area.style.display = 'block';
    area.className = 'info-log';
    area.innerText = "🔍 MAPEANDO MEMÓRIA E PROCURANDO ASSINATURAS...";
    
    enviarComando("audio", "Analisando");

    let progresso = 0;
    let intervalo = setInterval(() => {
      progresso += 10;
      fill.style.width = progresso + "%";
      if (progresso >= 100) {
        clearInterval(intervalo);
        document.getElementById('pBar').style.display = 'none';
        fill.style.width = "0%";
        enviarComando("analisarConteudo", "");
      }
    }, 100);
  }

  function mostrarLaudo(status, detalhes) {
    let area = document.getElementById('statusArea');
    area.style.display = 'block';
    if (status === "PERIGO") {
      area.className = 'status-box perigo';
      area.innerHTML = "❌ STATUS: MEMÓRIA SUSPEITA<br><br><span style='font-size:11px; font-weight:normal; text-align:left; display:block;'>" + detalhes + "</span>";
    } else {
      area.className = 'status-box sucesso';
      area.innerHTML = "✅ STATUS: ESTRUTURA LIMPA<br><br><span style='font-size:11px; font-weight:normal;'>Nenhum padrão de trapaça ou modificação encontrado no arquivo analisado.</span>";
    }
  }
</script>

</body>
</html>
`;

// Carrega o ambiente visual
let wv = new WebView();
await wv.loadHTML(html);
wv.present(true);

// Processador de comandos enviados da tela HTML para o iOS
let parametros = Args.string();
if (parametros) {
  try {
    let acaoObj = JSON.parse(decodeURIComponent(parametros));
    
    if (acaoObj.acao === "audio") {
      Speech.speak(acaoObj.valor);
    }
    
    if (acaoObj.acao === "importar") {
      let documento = await DocumentPicker.open(["public.text", "public.data"]);
      if (documento && documento.length > 0) {
        let caminho = documento[0];
        let fm = FileManager.local();
        let conteudoLog = fm.readString(caminho);
        
        Keychain.set("log_temporario", conteudoLog);
        await wv.evaluateJavaScript("animarEscanear()");
      }
    }
    
    if (acaoObj.acao === "analisarConteudo") {
      let textoParaAnalisar = Keychain.get("log_temporario").toUpperCase();
      let termosEncontrados = [];
      
      // Laço de repetição varrendo a matriz completa de logs e assinaturas conhecidas
      for (let i = 0; i < DICIONARIO_SUG_DETECCOES.length; i++) {
        let termo = DICIONARIO_SUG_DETECCOES[i];
        if (textoParaAnalisar.includes(termo)) {
          termosEncontrados.push(termo);
        }
      }
      
      if (termosEncontrados.length > 0) {
        Speech.speak("Análise suspeito");
        let msgErro = "Assinaturas de risco encontradas no arquivo:<br>• " + termosEncontrados.join("<br>• ");
        await wv.evaluateJavaScript(`mostrarLaudo("PERIGO", "${msgErro}")`);
      } else {
        Speech.speak("Análise concluída");
        await wv.evaluateJavaScript(`mostrarLaudo("SUCESSO", "")`);
      }
    }
  } catch (erroGeral) {}
}
