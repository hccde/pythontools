import urllib
import os, sys
 

pid = os.fork()
if pid > 0:
    sys.exit(0)
 

os.chdir("/Users/admos/Downloads/testdown")

os.setsid()

os.umask(0)
 
pid = os.fork()
if pid > 0:
    sys.exit(0)

sys.stdout.flush()
sys.stderr.flush()
si = file("/dev/null", 'r')
so = file("/dev/null", 'a+')
se = file("/dev/null", 'a+', 0)
os.dup2(si.fileno(), sys.stdin.fileno())
os.dup2(so.fileno(), sys.stdout.fileno())
os.dup2(se.fileno(), sys.stderr.fileno())

while True:
	fs = open('test.txt');
	prog = 0
	def callback(a,b,c):
		global prog
		progress = 100.0*a*b/c
		if progress-prog >= 1:
			per = '%.2f' %progress
			mesg = "alreay download:"+per+'%';
			prog = progress;
			print(mesg)
	global index
	index = 1
	for m in fs.readlines():
		name = '%d' %index;
		urllib.urlretrieve(m,name+'.mp4',callback)
		index = index+1
	fs.close()