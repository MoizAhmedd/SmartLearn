from django.shortcuts import render, redirect,reverse
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.http import HttpResponse, HttpRequest
from rest_framework.decorators import api_view
import os
import pyrebase
import json
import requests
from .authentication import config, survey_monkey_key

ids = {}
class HomePageView(TemplateView):
    template_name = 'index.html'
class LoginView(TemplateView):
    def get(self,request,*args,**kwargs):
        email= request.GET.get('uname')
        password = request.GET.get('psw')
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'smartlearn-51f0a-firebase-adminsdk-c8k6r-104d23d108.json')
        
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        if email and password:
            #try:
            role = db.child("users")
            print(role)
            user = auth.sign_in_with_email_and_password(email, password)
            trye = role.child(email[:email.index('@')]).child("role").get().val()
            if trye.lower() == 'teacher':
                #url = '{}?{}'.format('t-dashboard',email[:email.index('@')])
                #base_url = reverse('t-dashboard')  # 1 /products/
                #query_string =  urlencode({'teacher': email[:email.index('@')]})  # 2 category=42
                url = '{}{}'.format('teacher/', email[:email.index('@')])  # 3 /products/?category=42
                return redirect(url)  # 4
            if trye.lower() == 'student':
                url = '{}{}'.format('student/', email[:email.index('@')])
                return redirect(url)
            #except:
            #    return redirect('fail')
        return render(request, "login.html", context={})

class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        email= request.GET.get('email')
        password = request.GET.get('password')
        role = request.GET.get('type')
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'smartlearn-51f0a-firebase-adminsdk-c8k6r-104d23d108.json')
        #print(filename)
       
        if role == 'student':
            data = {"email": email, "role": role, "enrolled": ['hello']}
        elif role == 'teacher':
            data = {"email": email, "role": role}
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        if email and password:
            auth.create_user_with_email_and_password(email, password)
            #user = auth.sign_in_with_email_and_password(email, password)
            #id_token = user['idToken']
            db.child("users").child(email[:email.index('@')]).set(data)
            # db.child("youtube_code").set('1')
            # db.child("surveymonkey_code").set('1')
            # array = ['math']
            # array.append('english')
            # db.child("users").child(email[:email.index('@')]).child('enrolled').set(array)
        return render(request, "registration.html", context={})

class TeacherDashboardView(View):
    def get(self, request, teacher_name):
        #teacher_name= request.GET.get('teacher_name')
        print("Teacher Name:{}".format(teacher_name))
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'smartlearn-51f0a-firebase-adminsdk-c8k6r-104d23d108.json')
        #print(filename)
      
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        data = {
            "teacher" : "try"
        }
        #db.child("courses").child("math").set(data)
        list_of_courses = db.child("courses").get().val()
        print("Courses:{}{}".format(list_of_courses,type(list_of_courses)))
        courses = []
        for key in list_of_courses:
            if teacher_name in list_of_courses[key]['teacher']:
                courses.append(list_of_courses[key])
        print(courses)
        return render(request, "t_dashboard.html", context={'teacher_name':teacher_name,'courses':courses})
    #template_name = 't_dashboard.html'

class StudentDashboardView(TemplateView):
    def get(self, request, student_name):
        #teacher_name= request.GET.get('teacher_name')
        print("Teacher Name:{}".format(student_name))
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'smartlearn-51f0a-firebase-adminsdk-c8k6r-104d23d108.json')
        #print(filename)
    
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        #db.child("courses").child("math").set(data)
        list_of_courses = db.child("users").child(student_name).child("enrolled").get().val()
        print(list_of_courses)
        courses = []
        for key in list_of_courses:
            courses.append(key)
        print(courses)
        return render(request, "s_dashboard.html", context={'student_name':student_name,'courses':courses,'course_codes':['BIO900','MAT190']})


################33CREATE VIEW
class CreateView(TemplateView):
    def create_survey(self,data,uri,headers):
        request_survey = requests.post(uri,data=json.dumps(data),headers=headers)
        to_json = request_survey.json()
        survey_id = to_json['id']
        return survey_id 
    def create_page(self,data,uri,headers):
        response = requests.post(uri,data=json.dumps(data),headers=headers)
        to_json = response.json()
        page_id = to_json['id']
        return page_id
    def get(self, request, teacher_name):
        #teacher_name= request.GET.get('teacher_name')
        course_code = request.GET.get('course_code')
        course_name = request.GET.get('course_name')
        description = request.GET.get('description')
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'smartlearn-51f0a-firebase-adminsdk-c8k6r-104d23d108.json')
        #print(filename)
      
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        if teacher_name and course_code and course_name and description:
            data = {
                "teacher" : teacher_name,
                "code": course_code,
                "name": course_name,
                "description": description
            }
            db.child("courses").child(course_name.lower()).set(data)
            headers = {
                "Authorization": "bearer %s" % + survey_monkey_key,
                "Content-Type": "application/json"
            }
            survey_data = {
                "title": course_code + " Survey"
            }
            HOST = "https://api.surveymonkey.net"   
            CREATE_SURVEY_ENDPOINT = "/v3/surveys"
            uri = "%s%s" % (HOST, CREATE_SURVEY_ENDPOINT)
            survey_id = self.create_survey(survey_data,uri,headers)
            
            page_data = {}
            CREATE_PAGE_ENDPOINT = "/v3/surveys/" + survey_id + "/pages"
            page_uri = "%s%s" % (HOST, CREATE_PAGE_ENDPOINT)
            page_id = self.create_page(page_data,page_uri,headers)
            #TO FIX: Put survey_id, page_id in Firebase, rather than global dict
            
            #ids[course_code] = [survey_id, page_id]
            data["survey_id"] = survey_id
            data["page_id"] = page_id
            db.child("courses").child(course_name.lower()).set(data)
            #list_of_courses = db.child("courses").get().val()
            # courses = []
            # for key in list_of_courses:
            #     if type(key) == dict:
            #         if teacher_name in key:
            #             courses.append(key)
            # print(courses)
            # print("Courses:{}{}".format(list_of_courses,list_of_courses[0]))
        return render(request, "add_course.html", context={'teacher_name':teacher_name})

class CourseDetailsView(View):
    def create_question(self,data,uri,headers):
        response = requests.post(uri, data=json.dumps(data), headers=headers)
    def get(self,request,course_code):
        headers = {
            "Authorization": "bearer %s" % + survey_monkey_key,
            "Content-Type": "application/json"
        }
        question = request.GET.get('question')
        ans_1 = request.GET.get('ans-1')
        ans_2 = request.GET.get('ans-2')
        ans_3 = request.GET.get('ans-3')
        ans_4 = request.GET.get('ans-4')
        youtube = request.GET.get('youtube')
        survey = request.GET.get('survey')
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'smartlearn-51f0a-firebase-adminsdk-c8k6r-104d23d108.json')

        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        db.child("youtube_code").set(youtube)
        db.child("surveymonkey_code").set(survey)
        correct = request.GET.get('correct')
        correct_answer = ''
        if correct == 'A':
            correct_answer = ans_1
        elif correct == 'B':
            correct_answer = ans_2
        elif correct == 'C':
            correct_answer = ans_3
        elif correct == 'D':
            correct_answer = ans_4
        client = requests.session()
        HOST = "https://api.surveymonkey.net"
        question_data = {
        "headings": [

        {
     
        "heading": question
        }
        ],
        "family": "single_choice",
        "subtype": "vertical",
        "answers": {
        "choices": [
        {
        "text": ans_1,
        "visible": True,
        "position": 1
        },
        {
        "text": ans_2,
        "visible": True,
        "position": 2
        },
        {
        "text": ans_3,
        "visible": True,
        "position": 3
        }
        ]
        },
        "position": 3
        }
        course_name = ""
        courses = db.child("courses").get().val()
        for course in courses.keys():
            key = course
            value = courses[course]["code"]
            if value == course_code:
                course_name = key

        print(courses.keys())
        survey_id = db.child("courses").child(course_name).child("survey_id").get().val()
        page_id =  db.child("courses").child(course_name).child("page_id").get().val()
        CREATE_QUESTION_ENDPOINT = "/v3/surveys/" + survey_id + "/pages/" + page_id + "/questions"
        question_uri = "%s%s" % (HOST, CREATE_QUESTION_ENDPOINT)
        self.create_question(question_data,question_uri,headers)
        #requests.post(uri,data=data,headers=headers)
        print(correct_answer)
        return render(request, "details.html", context={'course_code':course_code})


class LiveView(View):
    def get(self,request,course_code):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'smartlearn-51f0a-firebase-adminsdk-c8k6r-104d23d108.json')
        #print(filename)
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        #db.child("youtube_code").set(youtube)
        youtube_embed = db.child("youtube_code").get().val()
        survey_embed = db.child("surveymonkey_code").get().val()
        return render(request, "live_stream.html", context={'youtube_embed':youtube_embed,'survey_embed':survey_embed,'course_code':course_code})

class StudentLiveView(View):
    def get(self,request,course_code):
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'smartlearn-51f0a-firebase-adminsdk-c8k6r-104d23d108.json')
        #print(filename)
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        #db.child("youtube_code").set(youtube)
        youtube_embed = db.child("youtube_code").get().val()
        survey_embed = db.child("surveymonkey_code").get().val()
        return render(request, "student_stream.html", context={'youtube_embed':youtube_embed,'survey_embed':survey_embed})

@api_view(['GET', 'POST'])
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world!"})

class AllCoursesView(TemplateView):
    def get(self, request, student_name):
        #teacher_name= request.GET.get('teacher_name')
        #print("Teacher Name:{}".format(teacher_name))
        #print(name)
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'smartlearn-51f0a-firebase-adminsdk-c8k6r-104d23d108.json')
        #print(filename)
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        #db.child("courses").child("math").set(data)
        list_of_courses = db.child("courses").get().val()
        #print("Courses:{}{}".format(list_of_courses,type(list_of_courses)))
        courses = []
        for key in list_of_courses:
            courses.append(list_of_courses[key])
        print(courses)
        return render(request, "all_courses.html", context={'student_name':student_name,'courses':courses})

class EnrollView(TemplateView):
    def get(self, request, student_name):
        #teacher_name= request.GET.get('teacher_name')
        course_code = request.GET.get('course_code')
        course_name = request.GET.get('course_name')
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'smartlearn-51f0a-firebase-adminsdk-c8k6r-104d23d108.json')
        #print(filename)
        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        db = firebase.database()
        if student_name and course_code and course_name:
            data = {
                "student" : student_name,
                "code": course_code,
                "name": course_name,
            }
            array = [course_code]
            db.child("users").child(student_name).child('enrolled').set(array)
        return render(request, "enroll.html", context={})
class SuccessView(TemplateView):
    template_name = 'success.html'

class FailView(TemplateView):
    template_name = 'fail.html'