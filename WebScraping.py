#webbrowser Comes with Python and opens a browser to a specific page.
#requests Downloads files and web pages from the internet.
#bs4 Parses HTML, the format that web pages are written in.
#selenium Launches and controls a web browser. The selenium module is able to fill
#in forms and simulate mouse clicks in this browser.

import webbrowser, sys
webbrowser.open('https://inventwithpython.com/')

sys.argv
#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

# TODO: Get address from clipboard.