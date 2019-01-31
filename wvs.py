import subprocess
import os

class wvs:
    def __init__(self,website):
        self.exePath = u"C:\Program Files (x86)\Acunetix\Web Vulnerability Scanner 10\wvs_console.exe"
        self.website = website
        self.logdir = u"d:\\awvs_temp\\"
        
    def scan(self):
        cmd = self.exePath + ' /Crawl ' + self.website + ' /Save /SaveFolder ' + self.logdir
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def listurl(self,filename):
        res = []
        for line in open(self.logdir + filename):
            if 'Added request for URL' in line:
                res.append( line.split('Added request for URL')[-1].strip())
        res = list(set(res))

        return res
        
    def view(self):
        res = []
        for i in os.listdir(self.logdir):
            if i.split('.')[-1] == 'csv':
                res.append(i)
        return res
    

    def delete(self,filename):
        cmd = 'cmd /c del ' + self.logdir + filename
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
                

    
