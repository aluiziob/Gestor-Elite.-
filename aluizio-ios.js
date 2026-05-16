// ==========================================
// SCREEN SHARE STR — VERSÃO SUPREMA iOS
// DONO: ALUIZIO | FUCKING CHEATERS
// ==========================================

const ASSINATURAS = [
  "CHEAT", "BYPASS", "MODMENU", "INJECTOR", "REGEDIT", "AIMBOT", "WALLHACK", "REPLAY_PATCH", "SHADER_MOD",
  "HACK", "NO_RECOIL", "AIMLOCK", "AUTO_HEADSHOT", "ANTIBAN", "FLY_HACK", "TELEPORT", "SPEED_HACK",
  "GAME_GUARDIAN", "LULUBBOX", "PANDA_MOUSE", "OCTOPUS", "MT_MANAGER", "X8_SANDBOX", "VIRTUAL_BACKUP",
  "APKSIGNER", "LUCKY_PATCHER", "CHEAT_ENGINE", "GG_SCRIPT", "HACKERBOT", "FF_MOD", "MACRO_SPACE",
  "SU_BINARY", "MAGISK", "KERNELSU", "SUPERUSER", "BUSYBOX", "CYDIA", "SUBSTRATE", "ZEBRA", "SILEO",
  "LIBHOOKER", "FRIDA_SERVER", "XPOSED", "LSPOSED", "EDXPOSED", "ROOT_DETECT", "DAEMON_ADB",
  "COM.DTS.FREEFIRETH", "LIBAUTO.SO", "LIBANRK.SO", "METADATA.BIN", "GLOBAL-METADATA", "UNITY_PLAYER", 
  "SHADERS.BUNDLE", "ASSETS/BIN/DATA", "REPLAY/.JSON", "DOCUMENT_BYPASS", "LIBIL2CPP.SO"
];

let html = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body { background-color: #0d0d0d; color: #00ffff; font-family: 'Courier New', Courier, monospace; margin: 0; padding: 20px; text-align: center; }
    .container { border: 2px solid #00ffff; border-radius: 10px; padding: 15px; background: #141414; box-shadow: 0 0 15px rgba(0, 255, 255, 0.3); }
    .logo { color: #ffffff; font-weight: bold; font-size: 14px; margin-bottom: 10px; letter-spacing: 2px; }
    .sub { color: #666666; font-size: 11px; margin-bottom: 20px; letter-spacing: 2px; }
    .btn { background: transparent; color: #00ffff; border: 1px solid #00ffff; padding: 14px 20px; margin: 10px 0; width: 90%; font-family: inherit; font-size: 13px; cursor: pointer; border-radius: 5px; font-weight: bold; transition: 0.3s; }
    .btn:active { background: #00ffff; color: #000; }
    .progress-bar { width: 90%; background: #222; height: 20px; margin: 15px auto; border: 1px solid #00ffff; border-radius: 5px; overflow: hidden; display: none; }
    .progress-fill { height: 100%; width: 0%; background: #00ffff; }
    .status-box { margin-top: 20px; padding: 15px; border-radius: 5px; display: none; font-weight: bold; font-size: 13px; max-height: 150px; overflow-y: auto; }
    .sucesso { border: 1px solid #00ff00; color: #00ff00; background: #052105; }
    .perigo { border: 1px solid #ff0000; color: #ff0000; background: #210505; }
    .info-log { color: #ffffff; font-size: 12px; margin-top: 10px; }
  </style>
</head>
<body>
<div class="container">
  <div class="logo">● S C R E E N  S H A R E  S T R ●</div>
  <div class="sub">DONO: ALUIZIO | AUDITORIA DE SISTEMA</div>
  <button class="btn" onclick="Scriptable.withNotification('cloud')">1. VERIFICAR INTEGRIDADE DA NUVEM</button>
  <hr style="border: 0; border-top: 1px solid #222; margin: 25px 0;">
  <div style="font-size: 13px; margin-bottom: 15px; color: #ffffff; font-weight: bold;">MÓDULO 2: ESCANEAR ARQUIVOS DE LOG</div>
  <button class="btn" onclick="carregarLog()">📂 CARREGAR LOG / DOCUMENTO</button>
  <div class="progress-bar" id="pBar"><div class="progress-fill" id="pFill"></div></div>
  <div id="statusArea" class="status-box"></div>
</div>
<script>
  function carregarLog() {
    document.getElementById('statusArea').style.display = 'none';
    window.location.href = "scriptable://run?param=importar";
  }
  function animarEscanear() {
    document.getElementById('pBar').style.display = 'block';
    let fill = document.getElementById('pFill');
    let area = document.getElementById('statusArea');
    area.style.display = 'block';
    area.className = 'info-log';
    area.innerText = "🔍 MAPEANDO MEMÓRIA E PROCURANDO ASSINATURAS...";
    let progresso = 0;
    let intervalo = setInterval(() => {
      progresso += 10;
      fill.style.width = progresso + "%";
      if (progresso >= 100) {
        clearInterval(intervalo);
        document.getElementById('pBar').style.display = 'none';
        fill.style.width = "0%";
        window.location.href = "scriptable://run?param=analisar";
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
      area.innerHTML = "✅ STATUS: ESTRUTURA LIMPA<br><br><span style='font-size:11px; font-weight:normal;'>Nenhum padrão de trapaça encontrado no arquivo analisado.</span>";
    }
  }
</script>
</body>
</html>
`;

// Inicialização segura da WebView no iOS
let view = new WebView();
await view.loadHTML(html);

let arg = Args.string();

if (arg === "importar") {
  Speech.speak("Analisando");
  try {
    let doc = await DocumentPicker.open(["public.text", "public.data"]);
    if (doc && doc.length > 0) {
      let fm = FileManager.local();
      let texto = fm.readString(doc[0]).toUpperCase();
      Keychain.set("str_scan_data", texto);
      await view.loadHTML(html);
      view.present(true);
      await view.evaluateJavaScript("animarEscanear()");
    }
  } catch(e) {
    view.present(true);
  }
} else if (arg === "analisar") {
  let logTexto = Keychain.get("str_scan_data") || "";
  let achados = [];
  
  for (let termo of ASSINATURAS) {
    if (logTexto.includes(termo)) {
      achados.push(termo);
    }
  }
  
  await view.loadHTML(html);
  view.present(true);
  
  if (achados.length > 0) {
    Speech.speak("Análise suspeito");
    let msg = "Assinaturas de risco encontradas:<br>• " + achados.join("<br>• ");
    await view.evaluateJavaScript(`mostrarLaudo("PERIGO", "${msg}")`);
  } else {
    Speech.speak("Análise concluída");
    await view.evaluateJavaScript(`mostrarLaudo("SUCESSO", "")`);
  }
} else {
  view.present(true);
}
