from django.shortcuts import render
from contacts.models import persons
import pyodbc
# Listaus
def getAllContacts(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=LAPTOP-UBQPUL3D\SQLEXSIMOSI;'
                        'Database=contacts;'
                        'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("select * from persons")
    result = cursor.fetchall()
    return render(request, 'Index.html',{'persons':result})

# Uuden lisäys
def addContact(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=LAPTOP-UBQPUL3D\SQLEXSIMOSI;'
                        'Database=contacts;'
                        'Trusted_Connection=yes;')
    
    if request.method=="POST":
        if request.POST.get('') and request.POST.get('') and request.POST.get('') and request.POST.get(''):
            new=insertdata()
            new.firstname=request.POST.get('')
            new.lastname=request.POST.get('')
            new.email=request.POST.get('')
            new.phone=request.POST.get('')
            cursor=conn.cursor()
            cursor.execute("insert into persons ")



        '''
                
                 result = cursor.fetchall()
                return render(request, 'Index.html',{'sqlserverconn':result})
        '''