import re
import bleach
from BeautifulSoup import BeautifulSoup, SoupStrainer
from mechanize import Browser
br = Browser()

suppe = BeautifulSoup(br.open("http://www.domstol.dk/oestrelandsret/retslister/Pages/default.aspx"))

rloversigt = suppe.findAll('a')

links = rloversigt(id=re.compile('TO210612'))
print links

    f = open("sagerilandretten.txt", "w")
	
listemedlandsretten = open("C:/Users/kba/Google Drive/Python/Retslister/landsretter.txt", "r").read()

landsretten = listemedlandsretten.splitlines()

for landsret in landsretten:
    retslister = BeautifulSoup(br.open(landsret))
    openrl = [y["href"] for y in retslister.findAll("a", href=re.compile("[Uu]ge"))]
    for x in openrl:
        #renset = x.replace('u', "")
        renset = x
        print renset
        print type(renset)
        retssager = BeautifulSoup(br.open(renset))
        overskueligt = [retssager.findAll('div', id=re.compile('contentcontainer'))]
        ren = bleach.clean(overskueligt, tags=[], strip=True)
        print ren
    
                          
#ugeoversigt.replace('u', "")

rlsoup = BeautifulSoup(br.open("http://www.domstol.dk/oestrelandsret/retslister/Pages/default.aspx"))

#test = BeautifulSoup(br.open("http://www.domstol.dk/oestrelandsret/retslister/Retslister/MA051112.HTM"))

#print bleach.clean(test, tags=[], strip=True)


rl = [y["href"] for y in rlsoup.findAll("a", href=re.compile("[0-9]{5}"))]
for rlmedwww in rl[30:40]:
    #rlmedwww.replace('u', "")
    #print "www.domstol.dk"+rlmedwww.replace('u', "")
    suppe = BeautifulSoup(br.open("www.domstol.dk"+rlmedwww.replace('u', "")))