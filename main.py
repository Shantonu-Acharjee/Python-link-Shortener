import pyshorteners

link=input('Enter The Big Ling For Short : ')
shortener=pyshorteners.Shortener()
x=shortener.tinyurl.short(link)

print('\n\n\nThe Short Link Is : ',x)