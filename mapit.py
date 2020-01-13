import webbrowser, sys, pyperclip

sys.argv

# check if command line arg were passed
if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St']
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)