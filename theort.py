class blocks:
    def __init__(self,cb):
        if cb[0]>cb[2] and cb[1]>cb[3]:
            self.upr=(cb[0],cb[1])
            self.downr=(cb[0],cb[3])
            self.upl=(cb[2],cb[1])
            self.downl=(cb[2],cb[3])
        if cb[0]>cb[2] and cb[1]<cb[3]:
            self.downr=(cb[0],cb[1])
            self.upr=(cb[0],cb[3])
            self.downl=(cb[2],cb[1])
            self.upl=(cb[2],cb[3])
        if cb[0]<cb[2] and cb[1]>cb[3]:
            self.upl=(cb[0],cb[1])
            self.upr=(cb[2],cb[1])
            self.downr=(cb[2],cb[3])
            self.downl=(cb[0],cb[3])
        if cb[0]<cb[2] and cb[1]<cb[3]:
            self.downl=(cb[0],cb[1])
            self.downr=(cb[2],cb[1])
            self.upl=(cb[0],cb[3])
            self.upr=(cb[2],cb[3])
    def centerofx(self):
        return (float(self.upl[0])+float(self.upr[0]))/2
def is_firmus(b1,b2):
 b1=blocks(b1)
 b2=blocks(b2)
 def bottomone(b1,b2):
     if b1.downr[1]<b2.downr[1]:
         return b1
     elif b1.downr[1]>b2.downr[1]:
         return b2
     else:
         if b1.upr[1]>b2.upr[1]:
            return b1 
         else:
            return b2
 if bottomone(b1,b2)==b1:
     upperone=b2
 else:
     upperone=b1
 def firstcrit(b1,b2):
     if type(bottomone(b1,b2))==str:
         return False
     if bottomone(b1,b2).downr[1]==0:
         return True
     else:
         return False
 def secondcrit(b1,b2):
     if upperone.downr[1]==bottomone(b1,b2).upr[1]:
         return True 
     else:
         return False 
 def thirdcrit(b1,b2):
      if float(upperone.centerofx()) < float(bottomone(b1,b2).upl[0]) or float(upperone.centerofx()) > float(bottomone(b1,b2).upr[0]):
          return False 
      else:
          return True
 def overlap(b1,b2):
     botleftx=bottomone(b1,b2).downl[0]
     botrightx=bottomone(b1,b2).downr[0]
     botupy=bottomone(b1,b2).upr[1]
     botdowny=bottomone(b1,b2).downr[1]
     upupy=upperone.upr[1]
     updowny=upperone.downr[1]
     uprightx=upperone.upr[0]
     upleftx=upperone.upl[0]
     centerofmassx=(botleftx+botrightx)/2
     centerofmassy=(botupy+botdowny)/2
     centerofblockx=(uprightx+upleftx)/2
     centerofblocky=(upupy+updowny)/2
     def closertocenterx(a,b):
         if abs(a-centerofmassx)<abs(b-centerofmassx):
             return a 
         else:
             return b
     def closertocentery(a,b):
         if abs(a-centerofmassy)<abs(b-centerofmassy):
             return a 
         else:
             return b
     if not (updowny<botdowny and upupy<botdowny or upupy>botupy and updowny>botupy or uprightx>botrightx and upleftx>botrightx or uprightx<botleftx and upleftx<botleftx):
         if centerofblockx>centerofmassx and centerofblocky>centerofmassy:  #1.bölge
             x11=upleftx
             x22=closertocenterx(uprightx,botrightx)
             y11=updowny
             y22=closertocentery(upupy,botupy)
         if centerofblockx<centerofmassx and centerofblocky>centerofmassy:  #2.bölge
             x11=uprightx
             x22=closertocenterx(upleftx,botleftx)
             y11=updowny
             y22=closertocentery(upleftx,botleftx)
         if centerofblockx<centerofmassx and centerofblocky<centerofmassy:  #3.bölge
             x11=uprightx
             x22=closertocenterx(upleftx,botleftx)
             y11=upupy
             y22=closertocentery(updowny,botdowny)
         if centerofblockx>centerofmassx and centerofblocky<centerofmassy:  #4.bölge
             x11=upleftx
             x22=closertocenterx(uprightx,botrightx)
             y11=upupy
             y22=closertocentery(updowny,botdowny)
         return (abs(x22-x11)*abs(y22-y11))
     else:
         return 0
 def lastf(b1,b2):
     global sharedarea
     if firstcrit(b1,b2)==True and secondcrit(b1,b2)==True:
         if thirdcrit(b1,b2)==True:
             return ["FIRMUS"] + [(float((float(b1.upr[1])-float(b1.downr[1])))*float((float(b1.upr[0])-float(b1.upl[0]))))+(float((float(b2.upr[1])-float(b2.downr[1])))*float((float(b2.upr[0])-float(b2.upl[0]))))]
         else:
             if float(upperone.centerofx())>float(bottomone(b1,b2).upr[0]): # sağında 
                 return ["ADDENDUM"] + [[upperone.downr[0],upperone.downr[1],(upperone.downr[0]+(2*(bottomone(b1,b2).upl[0]-upperone.centerofx()))),upperone.upr[1]]]
             if float(upperone.centerofx())<float(bottomone(b1,b2).upl[0]): # solunda
                 return ["ADDENDUM"] + [[upperone.downr[0],upperone.downr[1],(upperone.downr[0]+(2*(bottomone(b1,b2).upl[0]-upperone.centerofx()))),upperone.upr[1]]]
     else:
         return ["DAMNARE"] + [(float((float(b1.upr[1])-float(b1.downr[1])))*float((float(b1.upr[0])-float(b1.upl[0]))))+(float((float(b2.upr[1])-float(b2.downr[1])))*float((float(b2.upr[0])-float(b2.upl[0]))))-overlap(b1,b2)]
 return lastf(b1,b2)
print(is_firmus([0,10,-8.7,0],[-4,9,-1,14]))

