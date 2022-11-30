from django.shortcuts import render
from . import Pool
import json
from django.http import JsonResponse
from urllib.parse import unquote  # url decode

def User_login(request):
    return render(request,"UserLogin.html")

emailid=''
username=''
def Check_User(request):
    try:
        DB, CMD = Pool.ConnectionPool()
        email = request.GET['email']
        global emailid
        global username
        emailid=email
        print("Email:",emailid)
        password = request.GET['password']

        Q = "select * from userregistration where email='{0}' and password='{1}'".format(email,password)
        CMD.execute(Q)
        print(Q)
        row = CMD.fetchone()
        username=row.get('firstname')+" "+row.get('lastname')
        print(username)
        #print(Q)
        print(row)
        DB.close()
        if(row):
            return render(request, 'dashboard.html',{'Userdata':row})
        else:
            return render(request, 'UserLogin.html', {'message': 'Invalid EmailId/Password'})

    except Exception as e:
        return render(request, 'UserLogin.html', {'message': 'Something Went Wrong'})

def Fetch_All_Survey(request):
    try:
        DB, CMD = Pool.ConnectionPool()
        Q = "select * from surveyrecord"
        CMD.execute(Q)
        record = CMD.fetchall()
        print(record)
        DB.close()
        return JsonResponse({'record': record}, safe=False)

    except Exception as e:
        print("Error : ",e)
        return render(request, 'dashboard.html', {'record': None})

def DisplaySurvey(request):
    record=unquote(request.GET['record'])
    record=json.loads(record)
    print("zzzzz",record,type(record))
    return render(request,"displaysurvey.html",{'record':record})

def Submit_Survey_Answers(request):
  try:
    DB,CMD=Pool.ConnectionPool()
    id=emailid
    print(id)
    a1 = request.GET['a1']
    a2 = request.GET['a2']
    a3 = request.GET['a3']
    a4 = request.GET['a4']
    title = request.GET['title']
    Q="insert into userfeedback(a1,a2,a3,a4,userid,title,username) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}')".format(a1,a2,a3,a4,id,title,username)
    #print(Q)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
    print("Error:",e)
    return JsonResponse({'result':False},safe=False)
