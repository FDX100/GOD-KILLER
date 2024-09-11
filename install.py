import os
choice = input('to install press (Y) to uninstall press (N) >> ')
run = os.system
if choice =='Y' or choice=='y':

    run('chmod 777 GOD-KILLER')
    run('mkdir /usr/share/god-killer')
    run('cp GOD-KILLER /usr/share/god-killer/GOD-KILLER')

    cmnd=(' #! /bin/sh \n exec /usr/share/god-killer/GOD-KILLER "$@"')
    with open('/usr/bin/GOD-KILLER','w')as file:
        file.write(cmnd)
    run('chmod +x /usr/bin/GOD-KILLER & chmod +x /usr/share/god-killer/GOD-KILLER')
    print('''\n\ncongratulation GOD-KILLER is installed successfully \nfrom now just type \x1b[6;30;42mGOD-KILLER\x1b[0m in terminal ''')
if choice=='N' or choice=='n':
    run('rm -r /usr/share/god-killer ')
    run('rm /usr/bin/GOD-KILLER ')
    print('[!] now GOD-KILLER has been removed successfully')
