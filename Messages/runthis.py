import os
import time
import string
import pandas as pd

#string.punctuations list 
table = str.maketrans('','',string.punctuation)
#
def fault(i):
    return(i.translate(table))

#first for the spam objects
def spam(path):
    os.chdir(path)
    spamwordsdict={}
    changedirectory=os.chdir("Spam/")
    spamfolder=os.listdir(".")
    for i in spamfolder:
        f=open(str(i),"r")
        for j in f:
            words=list(map(str,j.strip().split(' ')))
            for k in words:
                if(k.isalnum()==False):
                    k=fault(k)
                if k in spamwordsdict:
                    spamwordsdict[k]=spamwordsdict[k]+1
                else:
                    spamwordsdict[k]=1
    return spamwordsdict

def genuine(path):
    os.chdir(path)
    genuine={}
    changedirectory=os.chdir("Ham/")
    genuinefolder=os.listdir(".")
    for i in genuinefolder:
        f=open(str(i),"r")
        for j in f:
            words=list(map(str,j.strip().split(' ')))
            for k in words:
                if(k.isalnum()==False):
                    k=fault(k)
                if k in genuine:
                    genuine[k]=genuine[k]+1
                else:
                    genuine[k]=1
    return genuine

def testa(spamwordshai,genuine,path):
    os.chdir(path)
    genuinecount=0
    spamcount=0
    os.chdir("NLP-Spam-detection/SpamDirTest")
    testfolder=os.listdir(".")
    for i in testfolder:
        f=open(str(i),"r")
        for j in f:
            words=list(map(str,j.strip().split(' ')))
            for k in words:
                if(k.isalnum()==False):
                    k=fault(k)
                if k in spamwordshai and k in genuine:
                    spamcount+=spamwordshai[k]
                    genuinecount+=genuine[k]
                elif k in spamwordshai:
                    spamcount+=spamwordshai[k]
                elif k in genuine:
                    genuinecount+=genuinewords[k]
        print('file is:',str(i))
        print('spam count is:',spamcount)
        print('genuine count is:',genuinecount)
        if(spamcount>genuinecount):
            print('it is a spam')
            print('spam percent:',(spamcount/(spamcount+genuinecount))*100)
        else:
            print('it is genuine')
            print('genuine percent:',(genuinecount/(spamcount+genuinecount))*100)
        print()
        print()
        

if __name__=="__main__":
    counter=0
    t=time.time()
    path2=os.getcwd()
    f=open("spamandham.csv","r+")
    os.chdir("SpamDir")
    path=os.getcwd()
    for i in f:
        if(counter>0 and counter<500):
            counter+=1
            if(i[0]=='s'):
                if not os.path.exists("Spam"):
                    os.mkdir("Spam")
                os.chdir("Spam")
                f=open("spam"+str(counter),"w+")
                newcounter=0
                for j in i:
                    if(newcounter>4):
                        f.write(j)
                    else:
                        newcounter+=1
                f.close()
                os.chdir(path)
            else:
                if not os.path.exists("Ham"):
                    os.mkdir("Ham")
                os.chdir("Ham")
                f=open("ham"+str(counter),"w+")
                newcounter=0
                for j in i:
                    if(newcounter>4):
                        f.write(j)
                    else:
                        newcounter+=1
                f.close()
                os.chdir(path)           
        else:
            counter+=1
    spamwords={}
    spamwords=spam(path)
    genuinewords={}
    genuinewords=genuine(path)
    testa(spamwords,genuinewords,path2)
    
    
    
        
