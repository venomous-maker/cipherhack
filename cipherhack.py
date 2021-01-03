import base64
print('    C   I   P   H   E   R   S    H    A    C   K')

print("""\
CODED BY:
  .___.     ..___ .___.___   .      ..___.   ..___..    .
  |    \   / |   \|   |    |  \    / |   |\  ||   ||\  /|
  |     \ /  |———/|———|———/    \  /  |———| \ ||   || \/ |
  |____  |   |___/|___|    \    \/   |___|  \||___||    |.
         @cybervenomous on telegram
         https://darktelegramvenomous my channel
""""")
print('''\
       WHAT DO YOU WANT?
       > ENCODING CHOOSE 1
       > DECODING CHOOSE 2
       > REVERSE CIPHER CHOOSE 3
''')
n = int(input("Enter your option: "))
if n==1:
    print('      E    N    C   O    D    E')
    message = input("Enter text: ")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print('''\
     ....................................................
     Your Encoded Text Is:
    ''')
    print('          '+base64_message)
    print('''\
     ....................................................
    ''')
    print('''\
___________________________________________________________
___________________________________________________________
       T H A N K    Y O U    F O R   U S I N G    M E !
                  To be updated soon
                  Copy with credits
___________________________________________________________
___________________________________________________________
''')
elif n==2:
    print('      D    E    C   O    D    E')
    base64_message = input('Input coded text:  ')
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('ascii')
    print('''\
     ....................................................
     Your Decoded Text Is:
    ''')
    print('          '+message)
    print('''\
     ....................................................
    ''')
    print('''\
___________________________________________________________
___________________________________________________________
       T H A N K    Y O U    F O R   U S I N G    M E !
                  To be updated soon
                   Copy with credits
___________________________________________________________
___________________________________________________________
    ''')
elif n==3:
    print('  R    E    V    E   R    S    E')
    message = input('Type or paste the cipher here:''  ')
    if len(message)==0:
        print('          YOU MUST INSERT A VALID CIPHER!!')
        message = input('Type a valid message  ')
        translated = ''
    else:
        translated = ''

    i = len(message) - 1
    while i >= 0:
        translated = translated + message[i]
        i = i - 1
    if len(message)>0:
        print('''\
     ....................................................
     Your Encrypted Text Is:
    ''')
        print("      "+translated)
        print('     ....................................................')
    else:
        print('      NO CIPHER INSERTED')

    print('''\
___________________________________________________________
___________________________________________________________
       T H A N K    Y O U    F O R   U S I N G    M E !
                  To be updated soon
                   Copy with credits
___________________________________________________________
___________________________________________________________
''')
else:
    print('''\
     ....................................................
     INPUT EITHER 1 OR 2 OR 3
    ''')
    print('       TRY AGAIN')
    print('''\
     ....................................................
   ''')
    print('''\
___________________________________________________________
___________________________________________________________
       T H A N K    Y O U    F O R   U S I N G    M E !
                  To be updated soon
                   Copy with credits
___________________________________________________________
___________________________________________________________
''')
