# Created By Anirban Das
#  Date- 23 February 2013
#
#  The Database Schema :
#  Attributes( slNo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
#              relative_path  VARCHAR(200) NOT NULL,
#              broad_category  VARCHAR(20) NOT NULL,
#              sub_category    VARCHAR(20) NOT NULL,
#              predicted_broad_category  VARCHAR(20),
#              predicted_sub_category   VARCHAR(20),
#              set   VARCHAR(5) )
#
#



import MySQLdb as mdb
import sys
import os

conn= None

path=raw_input('\nenter absolute path of corpus :  ')
if path[-1]!='/':
	path=path+'/'
#if path[0]=='/':
#	path=path[1:]

if os.path.exists(path):
	
	host=raw_input('enter hostname  : ')
	host=host.strip()
	user=raw_input('enter username  :  ')
	user=user.strip()
	password=raw_input('enter password  :   ')
	password=password.strip()
	database=raw_input(' enter database name   :   ')
	database=database.strip()

	try :
		conn = mdb.connect(host,user,password,database)
		cur = conn.cursor()
		
		for d in os.listdir(path):
			if not d.startswith('.'):
				if os.path.isdir(d):
					relPath=path+'d/'
					for d1 in os.listdir(relPath):
						if not d1.startswith('.'):
							if os.path.isdir(relPath+d1+'/'):
								absPath=relPath+d1+'/'
								for f in os.listdir(absPath):
									cur.execute("INSERT INTO corpusInfo VALUES(absPath,d,d1,NULL,NULL,NULL)")
							
		
		print "\n\nDatabase Updated\n\n"
		if con:
			
			cur.close()
			conn.close()

	except mdb.Error, e:

		print "Error %d: %s" % (e.args[0],e.args[1])
		sys.exit(1)
	
	

		
else:
	print '\n\nPath Does Not Exists\n\n'
	sys.exit(1)
















