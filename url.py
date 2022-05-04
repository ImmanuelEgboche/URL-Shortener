import pyshorteners

user_url= input('input pls\n')

shorter = pyshorteners.Shortener()

small_url = shorter.tinyurl.short(user_url)

print('The url is ' + small_url)