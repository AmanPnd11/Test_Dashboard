from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import TblSuperAdmin, Department, TblSubAdmin, studentregistration, Test, Subject, Question, StudentResult
from django.contrib.auth import authenticate, login, logout




# Create your views here.

# LANDING PAGE URLS

def base(request):

    return render(request, 'landingpage/base.html')





# SUPERADMIN DASHBOARD VIEWS FUNCTIONS.-------------------------------------------------------------------

def index(request):
    supadms = TblSuperAdmin.objects.get()
    Depts = Department.objects.count()
    students = studentregistration.objects.count()
    adms = TblSubAdmin.objects.count()
    context = {
        "supadms":supadms,
        "Depts": Depts,
        "students": students,
        "adms":adms,
    }
    return render(request, 'superadmin/index.html', context
    )


def about(request):
  
    return render(request, 'superadmin/about.html')

def adminprofile(request):
    admins= TblSuperAdmin.objects.all()
    context = {
        "admins": admins,
    }
    return render(request, 'superadmin/adminprofile.html', context)

def updaterec(request,email):
    admin = get_object_or_404(TblSuperAdmin, Email=email)

    if request.method == "POST":
        admin.AdminName = request.POST.get('AdminName')
        admin.UserName = request.POST.get('UserName')
        admin.Email = request.POST.get('Email')
        admin.MobileNumber = request.POST.get('MobileNumber')
        admin.Role = request.POST.get('Role')

        admin.save()
        messages.success(request, "Profile updated successfully")
        return redirect('adminprofile')

    return redirect('adminprofile')

    

def students(request):
    students = studentregistration.objects.all()
    context= {
        "students": students,
    }
    return render(request, 'superadmin/students.html', context)


def studentresult(request):
  
    return render(request, 'superadmin/studentresult.html')

def subadmins(request):

    subs= TblSubAdmin.objects.all()
    depts = Department.objects.all()
    context ={
        "subs": subs,
        "depts": depts
    }
    return render(request, 'superadmin/Subadmins.html', context)



def Department_view(request):
    if request.method == "POST":
        Deptname = request.POST.get("Deptname")
        Deptcode = request.POST.get("Deptcode")

        if Department.objects.filter(Deptname=Deptname).exists():
            messages.error(request, "Department name already exists")
        elif Department.objects.filter(Deptcode=Deptcode).exists():
            messages.error(request, "Department code already exists")
        else:
            Department.objects.create(
                Deptname=Deptname,
                Deptcode=Deptcode
            )
            messages.success(request, "Department created successfully")
            return redirect("Department_view")

    departs= Department.objects.all()
    context = {
        "departs": departs,
    }
    return render(request, "superadmin/Department_view.html", context)



# def Department_update(request):

#     departs= Department.objects.all()
#     context = {
#         "departs": departs,
#     }
#     return render(request, 'superadmin/Department_update.html', context)



def dept_update(request):
    dept = get_object_or_404(Department, id=request.POST.get('id'))

    if request.method == "POST":
        dept.id = request.POST.get('id')
        dept.Deptname = request.POST.get('Deptname')
        dept.Deptcode= request.POST.get('Deptcode')

        dept.save()
        messages.success(request, "Department updated successfully")
        return redirect('Department_view')
    return redirect('Department_view')



from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import TblSuperAdmin

if not TblSuperAdmin.objects.filter(Role='SUPER_ADMIN').exists():
    admin = TblSuperAdmin(
        AdminName="Aman",
        UserName="Admin",
        Email="amanpande416@gmail.com",
        MobileNumber="8484061360",
        Password=make_password("aman_7868"),
        Role="SUPER_ADMIN"
    )
    admin.save()

def adminlogin(request):
     if request.method == "POST":
        Email = request.POST.get("Email", "").strip()  
        Password = request.POST.get("Password", "").strip()  

        try:
            admin = TblSuperAdmin.objects.get(Email=Email, Role='SUPER_ADMIN')
            if check_password(Password, admin.Password):
                request.session["admin_id"] = admin.id
                messages.success(request, "What's Up SuperAdmin")
                return redirect("index")
                # messages.success(request,"What's Up SuperAdmin")
            else:
                messages.error(request, "Invalid Password")
        except TblSuperAdmin.DoesNotExist:
            messages.error(request, "Invalid Username")
     return render(request, 'superadmin/adminlogin.html')


# def forgotadmin(request):
#     admin_id = request.session.get("admin_id")

#     if not admin_id:
#         messages.error(request, "Please login first")
#         return redirect("adminlogin")

#     admin = TblSuperAdmin.objects.get(id=admin_id)

#     if request.method == "POST":
#         email = request.POST.get("Email")
#         new_password = request.POST.get("new_password")
#         confirm_password = request.POST.get("confirm_password")

#         if not check_password(old_password, admin.Password):
#             messages.error(request, "Old password is incorrect")
#             return redirect("forgotadmin")

#         if new_password != confirm_password:
#             messages.error(request, "Passwords do not match")
#             return redirect("forgotadmin")

#         admin.Password = make_password(new_password)
#         admin.save()

#         messages.success(request, "Password changed successfully")
#         return redirect("index")

#     return render(request, 'superadmin/forgotadmin.html')


def forgotadmin(request):

    if request.method == "POST":
        email = request.POST.get("Email").strip()
        new_password = request.POST.get("new_password").strip()
        confirm_password = request.POST.get("confirm_password").strip()

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("forgotadmin")

        try:
            admin = TblSuperAdmin.objects.get(
                Email=email,
                Role="SUPER_ADMIN"
            )

            admin.Password = make_password(new_password)
            admin.save()

            messages.success(request, "Password changed successfully!")
            return redirect("adminlogin")

        except TblSuperAdmin.DoesNotExist:
            messages.error(request, "Email not found!")
            return redirect("forgotadmin")

    return render(request, "superadmin/forgotadmin.html")



def updatestudent(request):
    stus = studentregistration.objects.all()   
    context = {
        "stus": stus
    }
    return render(request, 'superadmin/updatestudent.html', context)



def updatestudent1(request, mail):
    stu = get_object_or_404(studentregistration, mail=mail)
    departments = Department.objects.all()

    if request.method == "POST":
        stu.username = request.POST.get('user')
        stu.mail = request.POST.get('email')
        stu.RollNo = request.POST.get('Rollno')
        stu.Department.Deptcode = request.POST.get('Department.Deptcode')
        stu.MobileNo = request.POST.get('Mobileno')
        stu.save()
        messages.success(request, "Student Profile Updated successfully")
        return redirect('students')

    context = {
        'stu': stu,
        'departments': departments
    }

    return render(request, 'superadmin/updatestudent.html', context)






def updatesubadmins(request, id):
    subadmin = get_object_or_404(TblSubAdmin, id=id)
    departments = Department.objects.all()

    if request.method == "POST":
        subadmin.Subadminfirstname = request.POST.get('firstname')
        subadmin.Subadminlastname = request.POST.get('lastname')
        subadmin.Subadminemail = request.POST.get('email')
        subadmin.Subadminmobile = request.POST.get('mobile')
        subadmin.Subadminpassword = request.POST.get('password')
        subadmin.Department_id = request.POST.get('department')
        subadmin.IsActive = request.POST.get('is_active') == 'on'

        subadmin.save()

        messages.success(request, "SubAdmin Profile Updated Successfully!")
        return redirect('subadmins')

    context = {
        'subadmin': subadmin,
        'departments': departments
    }

    return render(request, 'superadmin/updatesubadmins.html', context)





# SUBADMIN REGISTRATION VIEW FUCTION----------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------
def subadminreg(request):
    
    if request.method == "POST":

        firstname = request.POST.get("Subadminfirstname")
        lastname = request.POST.get("Subadminlastname")
        email = request.POST.get("Subadminemail")
        mobile = request.POST.get("Subadminmobile")
        password = request.POST.get("Subadminpassword")
        department_id = request.POST.get("Department")

        if not department_id:
            messages.error(request, "Please select a department")
            return redirect("subadminreg")

        try:
            department_obj = Department.objects.get(id=department_id)
        except Department.DoesNotExist:
            messages.error(request, "Invalid Department selected")
            return redirect("subadminreg")

        if TblSubAdmin.objects.filter(Subadminemail=email).exists():
            messages.error(request, "Email already exists")
            return redirect("subadminreg")

        if TblSubAdmin.objects.filter(Department=department_obj).exists():
            messages.error(request, "Department already assigned")
            return redirect("subadminreg")

        TblSubAdmin.objects.create(
            Subadminfirstname=firstname,
            Subadminlastname=lastname,
            Subadminemail=email,
            Subadminmobile=mobile,
            Subadminpassword=make_password(password),
            Department=department_obj,
        )

        messages.success(request, "SubAdmin Registered Successfully")
        return redirect("subadmins")

    departments = Department.objects.all()
    return render(request, "superadmin/Subadmins.html",{"depts": departments})   



def subadminlogin(request):
     if request.method == "POST":
        Subadminfirstname = request.POST.get("Subadminfirstname")
        Subadminpassword = request.POST.get("Subadminpassword")
        dept_code = request.POST.get("department")

        try:
            department = Department.objects.get(Deptcode=dept_code)
        except Department.DoesNotExist:
            messages.error(request, "Invalid Department Code")
            return redirect("subadminlogin")

        try:
            subadmin = TblSubAdmin.objects.get(
                Subadminfirstname=Subadminfirstname,
                Subadminpassword=Subadminpassword,
                Department=department
            )
        except TblSubAdmin.DoesNotExist:
            messages.error(request, "Invalid login credentials")
            return redirect("subadminlogin")

        
        request.session["subadmin_id"] = subadmin.id
        request.session["department_id"] = department.id

        messages.success(request, "What's Up Subadmin")
        return redirect("subadmindashboard")
     return render(request,'subadmin/subadminlogin.html')





# def updatesubadmins(request):
#     subads = TblSubAdmin.objects.all()
#     context = {
#         "subads": subads,
#     }
#     return render(request, 'subadmin/updatesubadmins.html', context)



def subadmindashboard(request):
    subadmin_id = request.session.get("subadmin_id")
    department_id = request.session.get("department_id")

    if not subadmin_id:
        return redirect("subadminlogin")

    subadmin = TblSubAdmin.objects.get(id=subadmin_id)
    department = Department.objects.get(id=department_id)
    students = studentregistration.objects.filter(Department=department)

    return render(request, "subadmin/subadmindashboard.html", {
        "subadmin": subadmin,
        "department": department,
        "students": students
    })


def forgotsubadmin(request):

    return render(request, 'subadmin/forgotsubadmin.html')



def deptquestions(request):

    return render(request,'subadmin/deptquestions.html')



def deptstudent(request):
    students = studentregistration.objects.filter(Department_id=request.session.get("department_id"))
    context = {
        "students": students,
    }
    return render(request, 'subadmin/deptstudent.html', context)


def updstu(request):
    studs= studentregistration.objects.filter(Department_id=request.session.get("department_id"))
    context ={
        "studs": studs,
    }
    return render(request, 'subadmin/updstu.html', context)



def subadminprofile(request):
    subadmins = TblSubAdmin.objects.get(Department_id=request.session.get("department_id"))
    context= {
        "subadmins" : subadmins,
    }
    return render(request, 'subadmin/subadminprofile.html', context)


from .models import TblSubAdmin

def get_subadmin(request):
    subadmin_id = request.session.get('subadmin_id')
    if not subadmin_id:
        return None
    try:
        return TblSubAdmin.objects.get(id=subadmin_id)
    except TblSubAdmin.DoesNotExist:
        return None


# def subject_test_creation(request):
#     subadmin = get_subadmin(request)
#     if not subadmin:
#         return redirect('subadmin_login')


#     subjects = Subject.objects.filter(Department=subadmin.Department)

#     if request.method == "POST":
#         subject_name = request.POST.get('subject_name')
#         test_name = request.POST.get('test_name')
#         duration = request.POST.get('duration')

#         subject, created = Subject.objects.get_or_create(
#             Subjectname=subject_name,
#             Department=subadmin.Department
#         )

#         test = Test.objects.create(
#             test_name=test_name,
#             Subjectname=Subjectname,
#             duration=duration,
#             Department=subadmin.Department,
#             created_by=subadmin
#         )

#         return redirect('upload_question', test.id)

#     return render(request, 'subadmin/subject_test_creation.html', {
#         'subjects': subjects
#     })

    
def subject_test_creation(request):
    subadmin = get_subadmin(request)
    if not subadmin:
        return redirect('subadmin_login')

    subjects = Subject.objects.filter(Department=subadmin.Department)

    if request.method == "POST":
        subject_name = request.POST.get('subject_name')
        test_name = request.POST.get('test_name')
        duration = request.POST.get('duration')

        subject, created = Subject.objects.get_or_create(
            Subjectname=subject_name,
            Department=subadmin.Department
        )

        test = Test.objects.create(
            test_name=test_name,
            Subject=subject,               
            duration=int(duration),         
            Department=subadmin.Department,
            created_by=subadmin
        )

        return redirect('upload_question', test.id)

    return render(request, 'subadmin/subject_test_creation.html', {
        'subjects': subjects
    })


def upload_question(request, test_id):
    test = get_object_or_404(Test, id=test_id)

    if request.method == "POST":
        Question.objects.create(
            Test=test,
            question_text=request.POST['question_text'],
            option_a=request.POST['option_a'],
            option_b=request.POST['option_b'],
            option_c=request.POST['option_c'],
            option_d=request.POST['option_d'],
            correct_option=request.POST['correct_option'],
            marks=request.POST.get('marks', 1)
        )
        return redirect('upload_question', test_id=test.id)

    return render(request, 'subadmin/upload_question.html', {
        'test': test
    })


def result_view(request):
    subadmin = get_subadmin(request)
    if not subadmin:
        return redirect('subadmin_login')

    results = StudentResult.objects.filter(
        Test__Department=subadmin.Department
    )

    return render(request, 'subadmin/result_view.html', {
        'results': results
    })




# STUDENTS DASHBOARD VIEWS FUNCTIONS-----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------
def studregistration(request):
    if request.method == "POST":
        username = request.POST.get("username")
        mail = request.POST.get("mail")
        RollNo = request.POST.get("RollNo")
        MobileNo = request.POST.get("MobileNo")
        CreatePassword = request.POST.get("CreatePassword")
        Deptcode = request.POST.get("Department")

        if studentregistration.objects.filter(mail=mail).exists():
            message.error(request, "Email already exists")
        elif studentregistration.objects.filter(RollNo=RollNo).exists():
            message.error(request, "Email already exists")
        else:
             department_obj = Department.objects.get(id=Deptcode)

             studentregistration.objects.create(
                 username=username,
                 mail=mail,
                 RollNo=RollNo,
                 MobileNo=MobileNo,
                 CreatePassword=CreatePassword,
                 Department=department_obj
             )

             messages.success(request," Student Registered Successfully")
             return redirect("studentlogin")
    
    departments = Department.objects.all()
    return render(request, "student/studregistration.html", {"departments": departments})



def studentlogin(request):
    if request.method == "POST":
        mail = request.POST.get("mail")
        CreatePassword = request.POST.get("CreatePassword")

        try:
            student = studentregistration.objects.get(mail=mail)

            if student.CreatePassword == CreatePassword:
                request.session["student_id"] = student.id

                request.session["dept_id"] = student.Department.id
                request.session["dept_code"] = student.Department.Deptcode

                messages.success(request, "Welcome")
                return redirect("studentdashboard")

            else:
                messages.error(request, "Invalid Password")

        except studentregistration.DoesNotExist:
            messages.error(request, "Invalid Email")

    return render(request, 'student/studentlogin.html')



def studentdashboard(request):
    student = studentregistration.objects.get(id=request.session.get("student_id"))
    context = {
        "student": student,
    }
    return render(request, 'student/studentdashboard.html', context)


def studentprofile(request):
    st = studentregistration.objects.get(id=request.session.get("student_id"))
    context ={
        "st" : st,
    }
    return render(request, 'student/studentprofile.html', context)


def test(request):
    tets = Test.objects.filter(Department_id=request.session.get("dept_id"))
    context = {
        "tets": tets,
    }
    return render(request, 'student/test.html', context)


def Result(request):
    
    return render(request, 'student/Result.html')


def forgotstudent(request):

    if request.method == "POST":

        email = request.POST.get("mail")
        new_password = request.POST.get("CreatePassword")
        confirm_password = request.POST.get("ConfirmPassword")

        if new_password != confirm_password:
            return render(request, "student/forgotstudent.html", {
                "error": "Passwords do not match!"
            })

        try:
            student = studentregistration.objects.get(mail=email)

            student.CreatePassword = new_password
            student.save()

            return redirect("studentlogin")

        except studentregistration.DoesNotExist:
            return render(request, "student/forgotstudent.html", {
                "error": "Email not found!"
            })

    return render(request, "student/forgotstudent.html")


def test_start(request, test_id):
    test = Test.objects.get(id=test_id)
    questions = Question.objects.filter(Test_id=test_id)

    context = {
        "test": test,
        "questions": questions,
    }
    return render(request, 'student/test_start.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from .models import Test, Question, StudentResult
from .models import studentregistration


def test_submit(request, test_id):

    test = get_object_or_404(Test, id=test_id)
    questions = Question.objects.filter(Test=test)

    if request.method == "POST":

        obtained_marks = 0
        total_marks = 0

        for question in questions:

            selected_answer = request.POST.get(str(question.id))

            total_marks += question.marks

            if selected_answer == question.correct_option:
                obtained_marks += question.marks

        total_questions = questions.count()

        percentage = (
            obtained_marks / total_marks * 100
            if total_marks > 0 else 0
        )

        status = "Pass" if percentage >= 40 else "Fail"

        student_obj = studentregistration.objects.get(id=request.session.get("student_id"))
        StudentResult.objects.create(
            studentregistration=student_obj,
            Test=test,
            total_questions=total_questions,
            total_marks=total_marks,
            obtained_marks=obtained_marks,
            percentage=percentage,
            status=status
        )

        return redirect("test_submit", test_id)

    return redirect("test")
