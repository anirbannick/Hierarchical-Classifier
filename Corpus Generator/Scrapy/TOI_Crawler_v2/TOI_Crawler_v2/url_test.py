'''
Created on Feb 21, 2013

@author: ayush
'''
import urllib
from url_generator import URL_gen

#===============================================================================
# urlgen = URL_gen(1, 1, 2001, 1, 2, 2001, 36892)
# x = urlgen.fetch()
# while not x is None:
#    try:
#        y = urllib.urlopen(x).read()
#        print "Success:", x
#    except:
#        print "Fail:", x
#    x = urlgen.fetch()
#===============================================================================
    
urlgen = URL_gen(1, 1, 2001, 1, 2, 2001, 36892)
t = urlgen.fetch_all()
y = urllib.urlopen(t[0]).read()
print y