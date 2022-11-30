from django.shortcuts import render
from . import Pool
import json
from django.http import JsonResponse
from urllib.parse import unquote  # url decode

def UserInterface(request):
    return render(request,"UserInterface.html")

def SubmitRecord(request):
    try:
        DB,CMD=Pool.ConnectionPool()
        fname = request.GET['fname']
        lname = request.GET['lname']
        email = request.GET['email']
        gender = request.GET['gender']
        number= request.GET['number']
        password = request.GET['password']
        cpassword = request.GET['cpassword']
        address= request.GET['address']
        Q = "insert into userregistration(firstname,lastname,phone,gender,password,cpassword,email,address) values('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}')".format(fname,lname,number,gender,password,cpassword,email,address)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'UserInterface.html', {'message': 'Record Submitted'})
    except Exception as e:
        print("Error", e)
        return render(request, 'UserInterface.html', {'message': 'Fail to Submit record'})
        
def displayUserList(request):
    try:
        DB,CMD=Pool.ConnectionPool()
        Q = "select * from userregistration"
        CMD.execute(Q)
        records=CMD.fetchall()
        print(records)
        DB.close()
        return render(request, 'DisplayUser.html', {'record':records})
    except Exception as e:
        print("Error", e)
        return render(request, 'DisplayUser.html')
       
def SubmitSurveyRecord(request):
    try:
        DB,CMD=Pool.ConnectionPool()
        sdate = request.GET['sdate']
        edate = request.GET['edate']
        description = request.GET['description']
        title = request.GET['title']
        Q = "insert into surveyrecord(sdate,edate,description,title) values('{0}','{1}','{2}','{3}')".format(sdate,edate,description,title)
        CMD.execute(Q)
        DB.commit()
        DB.close()
        return render(request, 'SurveyInterface.html', {'message': 'Record Submitted'})
    except Exception as e:
        print("Error", e)
        return render(request, 'SurveyInterface.html', {'message': 'Fail to Submit record'})
        
def displayUserList(request):
    try:
        DB,CMD=Pool.ConnectionPool()
        Q = "select * from userregistration"
        CMD.execute(Q)
        records=CMD.fetchall()
        print(records)
        DB.close()
        return render(request, 'DisplayUser.html', {'record':records})
    except Exception as e:
        print("Error", e)
        return render(request, 'DisplayUser.html')
       
def displaySurveyList(request):
    try:
        DB,CMD=Pool.ConnectionPool()
        Q = "select * from surveyrecord"
        CMD.execute(Q)
        records=CMD.fetchall()
        # print(records)
        DB.close()
        return render(request, 'displaySurveyRecord.html', {'record':records})
    except Exception as e:
        print("Error", e)
        return render(request, 'displaySurveyRecord.html')
       
        
def SurveyInterface(request):
    return render(request,"SurveyInterface.html")       

def SurveyQuestionInterface(request):
    return render(request,"surveyquestioninterface.html")

def ViewSurveyQuestion(request):
    return render(request,"ViewsurveyQuestion.html")
       
def Submit_Survey_Question(request):
  try:
    DB,CMD=Pool.ConnectionPool()
    id=request.GET['surveyid']
    q1 = request.GET['q1']
    q2 = request.GET['q2']
    q3 = request.GET['q3']
    q4 = request.GET['q4']

    Q="update surveyrecord set q1='{0}',q2='{1}',q3='{2}',q4='{3}' where  surveyid={4}".format(q1,q2,q3,q4,id)
    #print(Q)
    CMD.execute(Q)
    DB.commit()
    DB.close()
    return JsonResponse({'result':True},safe=False)
  except Exception as e:
    print("Error:",e)
    return JsonResponse({'result':False},safe=False)

       
def displayUserFeedback(request):
    try:
        DB,CMD=Pool.ConnectionPool()
        Q = "select * from userfeedback"
        CMD.execute(Q)
        records=CMD.fetchall()
        # print(records)
        DB.close()
        return render(request, 'DisplayUserfeedback.html', {'record':records})
    except Exception as e:
        print("Error", e)
        return render(request, 'DisplayUserfeedback.html')
       