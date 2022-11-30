"""surveymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import AdminController
from . import UserController
urlpatterns = [
    path('admin/', admin.site.urls),
    path('userinterface/',AdminController.UserInterface),
    path('recordsubmit/',AdminController.SubmitRecord),
    path('displayuser/',AdminController.displayUserList),
    path('displaysurveyrecord/',AdminController.displaySurveyList),
    path('surveyinterface/',AdminController.SurveyInterface),
    path('insertsurveyquestion/',AdminController.SurveyQuestionInterface),
    path('surveyrecordsubmit/',AdminController.SubmitSurveyRecord),
    path('submitsurveyquestion/',AdminController.Submit_Survey_Question),
    path('viewsurveyquestion/',AdminController.ViewSurveyQuestion),
    path('userlogin',UserController.User_login),
    path('logincheck/',UserController.Check_User),
    path('fetch_all_survey/',UserController.Fetch_All_Survey),
    path('displaysurvey',UserController.DisplaySurvey),
    path('submitsurveyanswer/',UserController.Submit_Survey_Answers),
    path('displayuserfeedback/',AdminController.displayUserFeedback),
    
    
]
