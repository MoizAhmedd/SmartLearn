from django.urls import path
from . import views
video_id = 'eor44398'
urlpatterns = [
    path('',views.HomePageView.as_view(),name='home'),
    path('login',views.LoginView.as_view(),name='login'),
    path('registration',views.RegistrationView.as_view(),name = 'registration'),
    path('success',views.SuccessView.as_view(),name='success'),
    path('fail',views.FailView.as_view(),name='fail'),
    path('teacher/<str:teacher_name>',views.TeacherDashboardView.as_view(),name='t-dashboard'),
    path('create/<str:teacher_name>',views.CreateView.as_view(),name='create'),
    path('details/<str:course_code>',views.CourseDetailsView.as_view(),name='course-details'),
    path('live/<str:course_code>',views.LiveView.as_view(),name='live-stream'),
    path('student/<str:student_name>',views.StudentDashboardView.as_view(),name='s-dashboard'),
    path('all_courses/<str:student_name>',views.AllCoursesView.as_view(),name='all_courses'),
    path('enroll/<str:student_name>',views.EnrollView.as_view(),name='enrol_in_course'),
    path('studentlive/<str:course_code>',views.StudentLiveView.as_view(),name='student-live')
]
