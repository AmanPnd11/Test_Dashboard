from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
     # path('admin/', admin.site.urls),
    
    # LANDING PAGE URLS
    path('', views.base, name='base'),  
    
    
    # SUPER ADMIN DASHBOARD URLS
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('forgotadmin/', views.forgotadmin, name='forgotadmin'),
    path('forgotadminprofile/', views.forgotadminprofile, name='forgotadminprofile'),

    path('adminprofile/', views.adminprofile, name='adminprofile'),
    path('updaterec/<str:email>/', views.updaterec, name='updaterec'),
    path('students/', views.students, name='students'),
    path('Results/', views.studentresult, name='studentresult'),
    path('subadmins/', views.subadmins, name='subadmins'),
#     path('Department_update/', views.Department_update, name='Department_update'),
    path('dept_update/', views.dept_update, name='dept_update'),
    path('Department_view/', views.Department_view, name='Department_view'),

    path('updatestudent/', views.updatestudent, name='updatestudent'),
    path('updatestudent1/<str:mail>/', views.updatestudent1, name='updatestudent1'),
    path('subadminreg/', views.subadminreg, name='subadminreg'),
    path('updatesubadmin/<int:id>/',views.updatesubadmins,name='updatesubadmins'),
#     path('edit_subadmin/<int:id>/',views.edit_subadmin,name='edit_subadmin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('view_department_result/<int:id>/', views.view_department_result, name='view_department_result'),
#     path('department-performance/', views.department_performance, name='department_performance'),


    # SUBADMINS DASHBOARD URLS
            path('subadminlogin/', views.subadminlogin, name='subadminlogin'),
            path('forgotsubadmin/', views.forgotsubadmin, name='forgotsubadmin'),
            path('subadmindashboard/', views.subadmindashboard, name='subadmindashboard'),
            path('subadminprofile/', views.subadminprofile, name='subadminprofile'),
            path('deptstudent/', views.deptstudent, name='deptstudent'),
            path('updstu/<int:id>/', views.updstu, name='updstu'),
            path('subject_test_creation/', views.subject_test_creation, name='subject_test_creation'),
            path('upload_question/<int:test_id>/', views.upload_question, name='upload_question'),
            path('result_view/', views.result_view, name='result_view'),
            path('subadminlogout/', views.subadminlogout, name='subadminlogout'),
            path('forgotsubadminprofile/', views.forgotsubadminprofile, name='forgotsubadminprofile'),
            path('subadmin_upd/<str:email>/', views.subadmin_upd, name='subadmin_upd'),
            path('update_test/<int:test_id>/', views.update_test, name='update_test'),
            path('delete_test/<int:test_id>', views.delete_test, name='delete_test'),



    # STUDENTS DASHBOARD URLS
        path('studentregistration/', views.studregistration, name='studregistration'),
        path('studentlogin/',views.studentlogin, name='studentlogin'),
        path('studentdashboard/', views.studentdashboard, name='studentdashboard'),
        path('studentprofile/', views.studentprofile, name='studentprofile'),
        path('test/', views.test, name='test'),
        path('Result/', views.Result, name='Result'),
        path('forgotstudent/', views.forgotstudent, name='forgotstudent'),
        path('test_start/<int:test_id>/', views.test_start, name='test_start'),
        path('test_submit/<int:test_id>/', views.test_submit, name='test_submit'),
        
    



]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#  test_dash
#  test_dash
#   test_dash_786