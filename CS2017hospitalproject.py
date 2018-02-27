from pickle import *
import os
import datetime
f=open("no.txt","w")
f.write('00001')
f.close()

class hopital:  
    def input(self,p_id):
        
        '''To input new patient's details'''
        
        l=[]
        self.p_id=p_id
        self.p_name=raw_input('Enter Patient\'s Name: ')
        self.comments,self.feedback="",""		#entered while follow-up
        
        while True:
            	x=raw_input("Enter Gender: F/M:  ")
            	if x.upper() in ["M","F"]:
            		break



else:
            		print "Enter a valid option"
            		
        self.p_gen=x
        while True:
            	x=raw_input("Enter Contact Number  :")
            	
            	if len(x)==10 or len(x)==8:
            		break
            	else: 
            		print "Invalid Number, Enter again”
        self.p_num=x	
        x=raw_input('Enter date of birth in \'DD/MM/YYYY\': ')
        while not validdate(x):
            	x=raw_input('Invalid date. Enter date of birth in \’DD/MM/YYYY’)   
        self.p_dob=x   
        self.p_doc=self.doc_assign() 
        x=raw_input('Enter Registration date in \'DD/MM/YYYY\': ')
        while not self.validdate(x):
            	x=raw_input('Enter date in \'DD/MM/YYYY\': ')
        self.p_rdate=x
    def validdate(self,date):
        try:
            ld=date.split('/')
            d,m,y=int(ld[0].lstrip('0')),int(ld[1].lstrip('0')),int(ld[2])
            a=0
            if y<100:
                return false
            elif y%4==0 or y%100==0 and y%400==0 and m==2:
                if d<=29:
                    a=1
            else:            
                if m in (1,3,5,7,8,10,12):
                        if d<=31:
                            a=1
                else:
                    if d<=30 and m<=12:
                        a=1
            if a==1:
                return True
            else:
                return False
        except:
            return False
    def doc_assign(self):
        l=[]
        while True:
            dept=raw_input('Enter corresponding Department: [oncology, cardiology, gynaecology, neurology, accidental and emergency, checkup, pediatrics] : ')
            
            if dept.lower()=="oncology":
                l=["Dr. Anjali Sharma","Dr. Reeta Saxena","Dr. B.R. House"] 
                print l
                a=raw_input("Enter consulting Doctor: ")
                if a in l:
                    return a
                    break
                    
            elif dept.lower()=="cardiology":
                l=['Dr. Reeta Singh','Dr. Priti Singhal', 'Dr. Virat Mehta ','Dr. Narayana']  
                print l
                a=raw_input("Enter consulting Doctor: ")
                if a in l :
                    return a
                    

            elif dept.lower()=="neurology":
                l=['Dr. Jatin Aggarwal','Dr. Ishwar Sharma', 'Dr. Dimitri ','Dr. Eshaan Rao']
                print l
                a=raw_input("Enter consulting doctor")
                if a in l:
                    return a
                    
            elif dept.lower()=="accidental and emergency":
                l=['Dr. Joell Nath','Dr. Vineeta Singhal', 'Dr. Geeta Mehta ','Dr. Phoebe Buffay']
                print l
                a=raw_input("Enter Consulting doctor")
                if a in l :
                    return a
                    

            elif dept.lower()=="checkup":
                l=['Dr. R.K. Gupta','Dr. Jatin Sehgal', 'Dr. Anand Sharma ','Dr. S.K. Swami']
                print l
                a=raw_input("Enter Consulting doctor")
                if a in l :
                    return a
                    
            elif dept.lower()=="gynaecology":
                l=['Dr. Preeti Sharma','Dr. John Noe', 'Dr. Virath Kohli','Dr. P.K. Goel']
                print l
                a=raw_input("Enter Consulting doctor")
l=['Dr. Emma G.','Dr. R. Maheshwari', 'Dr. Smriti Vadhwa','Dr. Prakashana']
print l
 a=raw_input("Enter Consulting doctor")
if a in l :
return a    
else:
print "invalid department. Enter again”       
    
def disp(self):
 print "Registration Number: ",self.p_id
print "Patient\'s Name: ", self.p_name
print "Gender: ", self.p_gen
print "Contact Number: ",self.p_num
print "Registration Date: ",self.p_rdate
print "Discharge Date: ",self.p_ddate
print 'Consulting Doctor:',self.p_doc, '\n'      

def create():
f1=open("hop.dat","wb")
h1=hopital()
f2=open('no.txt','r')
ID=int(f2.read())
f2.close()
while True:
h1.input(ID)
dump(h1,f1)
ch=raw_input('Continue?')
if ch.upper()!='Y':
break
f1.close()
f2=open('no.txt','w')
f2.write(str(ID))
f2.close()

def add():
f1=open("hop.dat","ab+")
h1=hopital()
f2=open('no.txt','r')
ID=int(f2.read())
f2.close()
while True:
ID+=1
h1.input(ID)
dump(h1,f1)
ch=raw_input('Continue?')
if ch.upper()!='Y':
 break
f1.close()
f2=open('no.txt','w')
f2.write(str(ID))
f2.close()    

def modify():
    
   if not os.path.isfile('hop.dat'):
              print 'sorry file can\'t be found'
       else:
                f=open('hop.dat','rb+')
                f1=open("temp.dat","wb")
                h1=hopital()
                ad=input('Enter patient ID: ')
                nm=raw_input('Enter patient name')
                doc=raw_input("Enter new consultant")
                while True:
                    x=raw_input("Enter new Contact Number  :")
                    
                    if len(x)==10 or len(x)==8:
                            break
                    else: 
                            print "Invalid Number, Enter again"
                try:
                      fl=0
                      while True:
                          h1=load(f)
                          if h1.p_id==ad:
                                    fl=1
                                    h1.p_name=nm
                                    h1.p_num=x
                                    h1.p_doc=doc
                                    dump(h1,f1)
                                    break
                          else:
                                dump(h1,f1)
                except EOFError:
                     if fl==0:
                            print "sorry record not found"
                finally:
                     f.close()
                     f1.close()
                     os.remove("hop.dat")
                     os.rename("temp.dat","hop.dat")

def follow_up():
    print "--- Previous Patient history ---"
    search()
    if not os.path.isfile('hop.dat'):
        print '404 ERROR: File Not Found.'
    else:
        f=open("hop.dat","rb")
        flag=0
        h1=hopital()
        pid=input('Enter the ID of the patient: ')
        try:
            while True:
                h1=load(f)
                if h1.p_id==pid:
                    h1.comments=raw_input("Enter special comments: ")
                    h1.feedback=raw_input("Enter customer feedback: ")
                    flag=1
        except EOFError:
            if flag==0:
                print "Patient record not found."
        except:
      print ""
        finally:
      f.close()



def display():
    if not os.path.isfile('hop.dat'):
        print '404 ERROR: File Not Found.'
    else:
        f=open("hop.dat","rb")
        flag=0
        
h1=hopital()
        try:
            while True:
                h1=load(f)
                flag=1
                h1.disp()
        except EOFError:
            if flag==0:
                print "No record found."
        except: print "An error occurred."
        finally: f.close()
        
def search():
    #by patient, dates
    if not os.path.isfile('hop.dat'):
        print '404 ERROR: File Not Found.'
    else:
        f=open("hop.dat","rb")
        flag=0
        h1=hopital()
        pid=input('Enter the ID of the patient being seeked: ')
        try:
            while True:
                h1=load(f)
                if h1.p_id==pid:
                    h1.disp()
                    flag=1
        except EOFError:
            if flag==0:
                print "Patient record not found."
        except:
            print ""
        finally: f.close()

def delete():
    if not os.path.isfile('hop.dat'):
        print '404 ERROR: File not found.'
    else:
        flag=1
        f1=open('hop.dat','rb')
        f2=open('temp.dat','wb')
        h1=hopital()
        pid=input("Enter the ID of the patient to be discharged: ")
        try:
            while True:
                h1=load(f1)
                if h1.p_id==pid:
                    flag=0
                else:
                    dump(h1,f2)
        except EOFError:
            if flag==1:
                print "Patient record not found."
        except:print "An error occurred."
        finally:
            f1.close()
            f2.close()
        os.remove('hop.dat')
        os.rename('temp.dat','hop.dat')

def review():
    if not os.path.isfile('hop.dat'):
        print '404 ERROR: File Not Found.'
    else:
        f=open("hop.dat","rb")
        h1=hopital()
        now= datetime.datetime.now()
        flag = 0
        print "Records for review on", now
        try:
            while True:
                h1=load(f)
                if h1.p_ddate==( "%s-%s-%s" % (now.day, now.month, now.year) ):
                   flag+=1
        h1.disp()

                   ch=raw_input('Do you want to discharge this patient? Y\N: ').upper()
                   if ch=='Y':
                       delete()      
        except EOFError: 
	        if flag==0:
		print "No records to be reviewed today"
        except: print "An error occurred."
        finally: f.close()
while True:
    print '''                       Welcome to Seattle Grace Mercy West Hospital
                                                Seattle, Washington
                                                
1. Create                                                            
2. Add
3. Display
4. Modify
5. Follow up
6. Search
7. Review
8. Delete
9. Exit'''

    
    ch=raw_input('Enter Choice: ')
    if ch=='1':
        create()
    elif ch=='2':
        add()
    elif ch=='3':
        display()
    elif ch=='4':
        modify()
    elif ch=='5':
        follow_up()
    elif ch=='6':
        search()
    elif ch=='7':
        review()
    elif ch=='8':
        delete()
    elif ch=='9':
        print "--- Have a nice day ---"
        break
