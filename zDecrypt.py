import zipfile
import optparse
from threading import thread

FLAG = 0
counter = 0

def extractFile(zFile, password):
	global FLAG
	try:
		zFile.extractall(pwd=password)
		print '[+] Found password => ' +password
		print '[+] Files extracted\n'
		FLAG = 1
		return
	except: 
		return

def main():
	global FLAG
	global counter
	parser = optparse.OptionParser("usage: \nusage: prog -f <zipfile> -d <dictionary>\n")
	parser.add_option('-f', dest='zname', type='string', help='specify zip file')
	parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
	(options, args) = parser.parse_args()
	
	if (options.zname == None) | (options.dname == None):
		print parser.usage
		return
	else:
		zname = options.zname
		dname = options.dname

	zFile = zipfile.ZipFile(zname)
	passfile = open(dname)
	print 'Running dictionary attack on targeted Zip'
	for line in passfile.readlines():
		if FLAG: return
		if counter %10000 == 0:
			print 'Passwords attempted %d'%counter
		password = line.strip('\n')
		counter += 1
		t =threading.Thread(target=extractFile, args=(zFile,password))
		t.start()
		if FLAG:
			return

if __name__ == '__main__':
	main()
