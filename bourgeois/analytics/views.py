from django.shortcuts import render
import cx_Oracle as ora
import json
from django.http import JsonResponse

# Create your views here.

################# 오라클 클라우드 사전 절차 진행 후 주석 해제할것
# oracle db연결 (클라우드)

def connections():
    try:
        # instantclient경로
        # conn = ora.connect(user='ADMIN으로 고정', password='데이터베이스 비밀번호', dsn='데이터베이스이름_high') #windows
        # conn = ora.connect(user='ADMIN', password='Epdlxjqpdltm1!', dsn='db01_high') #windows (예제)
        conn = ora.connect(user='ADMIN', password='Epdlxjqpdltm1!', dsn='db_high') #windows (예제)
        # conn = ora.connect(user='ADMIN', password='Epdlxjqpdltm1!', dsn='db01_high') #mac
    except:
        print('error')
        
    return conn   

def makeDictFactory(cursor):
    columnNames = [d[0] for d in cursor.description] 
    def createRow(*args):
        return dict(zip(columnNames,args))   
    return createRow 

#################

def chart_data(request):
    conn = connections()
    cursor = conn.cursor() 
    cursor.execute("select * from project_category_analytics")
    
    # list(튜플)형태를 dic타입으로 변경
    cursor.rowfactory = makeDictFactory(cursor)
    
    rows = cursor.fetchall()
    conn.close()
    context ={'aList':rows}
    
    return JsonResponse(context,safe=False)

def inner(request):
    return render(request, 'inner.html')

