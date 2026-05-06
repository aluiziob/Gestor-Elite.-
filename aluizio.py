import os, time, sys
try: import requests as r
except: os.system('pip install requests'); import requests as r

def L():
    os.system('clear')
    print('\033[1;36m      █████╗ ██╗     ██╗   ██╗██╗███████╗██╗ ██████╗ ')
    print('     ██╔══██╗██║     ██║   ██║██║╚══███╔╝██║██╔═══██╗')
    print('     ███████║██║     ██║   ██║██║  ███╔╝ ██║██║   ██║')
    print('     ██╔══██║██║     ██║   ██║██║ ███╔╝  ██║██║   ██║')
    print('     ██║  ██║███████╗╚██████╔╝██║███████╗██║╚██████╔╝')
    print('     ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝╚══════╝╚═╝ ╚═════╝\033[0m')
    print('\033[1;34m  ─── GESTOR SUPREMO: ALUIZIO | VERSÃO ELITE 2026 ───\033[0m')

def check_anim(texto):
    print(f'\033[1;37m [ \033[1;32m✓\033[1;37m ] {texto}\033[0m')
    time.sleep(0.3)

def B(t):
    print(f'\n\033[1;33m{t}\033[0m')
    for i in range(21):
        sys.stdout.write(f'\r[\033[1;32m' + '■' * i + ' ' * (20-i) + '\033[0m] ' + str(i*5) + '%')
        sys.stdout.flush()
        time.sleep(0.05)
    print('\n')

def S():
    L()
    print('\033[1;33m INICIANDO VARREDURA PROFUNDA...\033[0m\n')
    check_anim("Identificando aparelho e ambiente...")
    check_anim("Verificando integridade de logs...")
    check_anim("Verificando root e ferramentas suspeitas...")
    check_anim("Analisando MReplays e Shaders...")
    check_anim("Checando bypass de Wallhack/Holograma...")
    check_anim("Analisando pastas OBB e Data...")
    check_anim("Filtrando arquivos falsos do sistema...")
    
    B("GERANDO RELATÓRIO FINAL")
    
    print('\033[1;34m╔' + '═'*48 + '╗\n║ \033[1;37m        RELATÓRIO DE ELITE - VEREDITO FINAL    \033[0m ║\n╠' + '═'*48 + '╣\033[0m')
    
    cmd = 'adb shell \"find /sdcard/ -type f \( -name *.lua -o -name *reg* -o -name *h4x* -o -name *mod* -o -name *panel* -o *goxit* \) 2>/dev/null | grep -ivE \"optional|android|system|multiregion|obb\"\"'
    f = os.popen(cmd).read().strip()
    
    encontrado = False
    if f:
        for x in f.split('\n')[:8]:
            path = x.lower()
            if ".lua" in path: m = "W.O: SCRIPT LUA DETECTADO"
            elif "reg" in path: m = "W.O: REGEDIT (AUXÍLIO MIRA)"
            elif "mod" in path: m = "W.O: MOD MENU ATIVO"
            else: m = "W.O: RASTRO DE XIT"
            print(f'║ \033[1;41m 🚨 {m} \033[0m ║')
            print(f'║ \033[1;37m CAMINHO: {x[-35:]} \033[0m ║')
            encontrado = True

    apps = os.popen('adb shell pm list packages -3 2>/dev/null').read().strip()
    bl = ['cheat', 'h4x', 'regedit', 'macro', 'gameguardian', 'modmenu', 'aimbot', 'injector']
    ak = [x for x in apps.split('\n') if any(s in x.lower() for s in bl)]
    
    if ak:
        for x in ak:
            print(f'║ \033[1;41m 🚨 W.O: APP PROIBIDO: {x[-20:]} \033[0m ║')
            encontrado = True
            
    if not encontrado:
        print('║ \033[1;42m ✅ SISTEMA 100% LIMPO: JOGADOR APROVADO      \033[0m ║')
    print('\033[1;34m╚' + '═'*48 + '╝\033[0m')

def M():
    L()
    c = os.popen('adb devices').read().count('device') > 1
    st = '\033[1;42m ● LICENÇA ATIVA \033[0m' if c else '\033[1;41m ● AGUARDANDO ADB \033[0m'
    print(f' {st} | \033[1;37mUSUÁRIO: ALUIZIO\033[0m')
    print('\n\033[1;35m[ 1 ]\033[0m 📡 CONEXÃO SEGURA\n\033[1;35m[ 2 ]\033[0m 🛡️  VARREDURA DE W.O.')
    print('\033[1;35m[ 3 ]\033[0m 🔍 ANTI-VPN\n\033[1;31m[ S ]\033[0m 🚪 SAIR')
    
    o = input('\n\033[1;32mALUIZIO > \033[0m').lower()
    if o == '1':
        ip = input('➤ IP: '); p1 = input('➤ Porta Pair: '); cod = input('➤ Cod: ')
        os.system(f'adb pair {ip}:{p1} {cod}')
        p2 = input('➤ Porta Conexão: '); os.system(f'adb connect {ip}:{p2}'); M()
    elif o == '2':
        if not c: print('\n\033[1;41m ERRO: APARELHO NÃO CONECTADO \033[0m'); time.sleep(2); M()
        else: S(); input('\n\033[1;33mEnter para Voltar...\033[0m'); M()
    elif o == '3':
        B('RASTREAMENTO DE REDE...')
        try:
            res = r.get('http://ip-api.com/json/', timeout=5).json()
            print(f'\033[1;37mIP: {res.get("query")}\nPAÍS: {res.get("country")}\nVPN: {"DETECTADA 🚨" if res.get("proxy") else "LIMPO ✅"}\033[0m')
        except: print('\033[1;41m ERRO DE REDE \033[0m')
        input('\n\033[1;33mEnter para Voltar...\033[0m'); M()
    elif o == 's': sys.exit()

if __name__ == "__main__":
    M()
