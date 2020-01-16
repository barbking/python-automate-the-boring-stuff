import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
# <class 'requests.models.Response'>
print(res.status_code == requests.codes.ok)
# True
print(len(res.text))
# 178978
print(res.text[:250])

# raise error if bad request
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
# ensure that a program halts if a bad download occurs, or wrap in exception to cont run
res.raise_for_status()

# using exception
import requests
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# write webpage to file
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
res.raise_for_status()
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()

# for more info on requests
# requests.readthedoc.org
# good when know url, not good for logging into webpage