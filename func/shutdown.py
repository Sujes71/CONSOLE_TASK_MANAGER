import datetime
import os
import keyboard

def shutdown(time):
    done = True
    timeset = str(time)
    timeset = time.replace(':', '').strip()

    if len(timeset) == 4:
        timeset = timeset + "00"
        
    while True:
        currenttime = datetime.datetime.now().strftime('%H%M%S')
        
        if done:
            done = False

            if len(timeset) == 6 and timeset.isnumeric() and int(timeset) >= 000000 and int(timeset) <= 235959:
                t = ':'.join(timeset[i:i+2] for i in range(0, len(timeset), 2))
                print(f'[+] shutdown configured at {t}')

            else:
                print(f'[!] error: arg1 [{time}]: expected one valid arg1' )
                print("""
                arg1 = time to shutdown HH:MM:SS or HH:MM
                """ )
                break
                
        if currenttime == timeset:
            os.system("shutdown /s /t 1")
            break
        
        elif keyboard.is_pressed('supr'):
            print('[-] shutdown cancelled')
            break