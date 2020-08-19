from django.shortcuts import render
from contacts.models import sqlserverconn
import pyodbc

def connsql(request):
    conn=pyodbc.connect('Driver={sql server};'
                        'Server=LAPTOP-UBQPUL3D\SQLEXSIMOSI;'
                        'Database=contacts;'
                        'Trusted_Connection=yes;')
    cursor=conn.cursor()
    cursor.execute("select * from persons")
    result = cursor.fetchall()
    return render(request, 'Index.html',{'sqlserverconn':result})