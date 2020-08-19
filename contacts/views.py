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
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('phone'):
            new=Insert()
            new.firstname=request.POST.get('')
            new.lastname=request.POST.get('')
            new.email=request.POST.get('')
            new.phone=request.POST.get('')
            cursor=conn.cursor()
            cursor.execute('''insert into persons values ('"+new.firstname+"','"+new.lastname+"','"+new.email+"','"+new.phone+"') ''')
            cursor.commit()
            return render(request, 'AddNew.html')
    else:
            return render(request, 'AddNew.html')
