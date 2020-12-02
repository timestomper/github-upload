import webbrowser, sys, pyperclip
#sys.argv maps.py

#check if cli args were passed

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()


webbrowser.open('https://www.google.com/maps/place/' + address)
