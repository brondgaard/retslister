import re
import bleach
from BeautifulSoup import BeautifulSoup
from mechanize import Browser

br = Browser()

f = open("byretterscrapet.txt", "w")

#Åbner en streng med urls til byretternes oversigt over retslister (to forskellige dirs)

#PC1
byreturls = open("C:/Users/kba/Desktop/byrettenurls.txt", "r").read()

#PC2
#byreturls = open("C:/Documents and Settings/Mensberg/Dokumenter/Google Drive/Python/Retslister/byretter.txt", "r").read()

#Strengen deles til en liste

byretter = byreturls.splitlines()

for byret in byretter:
    retslister = BeautifulSoup(br.open(byret))
    retsliste = [x["href"] for x in retslister.findAll("a", href=re.compile("[Uu]ge\d+"))]
    for ugeoversigt in retsliste:
        ugeoversigt.replace('u', "")
        ugeoversigtsoup = BeautifulSoup(br.open(ugeoversigt))
        retssager = [ugeoversigtsoup.findAll('div', id=re.compile('contentcontainer'))]
        ren = bleach.clean(retssager, tags=[], strip=True)
        print >> f, unicode(ren).encode("utf-8")

#bornholm

bornholm = br.open("http://www.domstol.dk/Bornholm/retslister/Pages/default.aspx").read()

bornholmsuppe = BeautifulSoup(bornholm)

for link in bornholmsuppe.findAll('a', href=re.compile('http://www.domstol.dk/Bornholm/retslister/')):
    bhretsliste = br.open(link['href'])
    html = BeautifulSoup(bhretsliste)
    oversigt = [html.findAll('div', id=re.compile('contentcontainer'))]
    renbornholm = bleach.clean(oversigt, tags=[], strip=True)
    print >> f, unicode(renbornholm).encode("utf-8")

f.close()
    
