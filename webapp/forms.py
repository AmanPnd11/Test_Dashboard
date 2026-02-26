from django.forms import ModelForm

from .models import TblSuperAdmin, Department, TblSubAdmin, studentregistration, Subject, Test, Question, StudentResult

class TblSuperAdmin(ModelForm):
    class Meta:
        model = TblSuperAdmin # Ensure this is a single model, not a tuple
        fields = "__all__"

class Department(ModelForm):
    class Meta:
        model = Department # Ensure this is a single model, not a tuple
        fields = "__all__"

class TblSubAdmin(ModelForm):
    class Meta:
        model = TblSubAdmin # Ensure this is a single model, not a tuple
        fields = "__all__"


class studentregistration(ModelForm):
    class Meta:
        model = studentregistration # Ensure this is a single model, not a tuple
        fields = "__all__"

     
   
class Subject(ModelForm):
    class Meta:
        model = Subject # Ensure this is a single model, not a tuple
        fields = "__all__"

class Test(ModelForm):
    class Meta:
        model = Test # Ensure this is a single model, not a tuple
        fields = "__all__"

class Question(ModelForm):
    class Meta:
        model = Question # Ensure this is a single model, not a tuple
        fields = "__all__"

class StudentResult(ModelForm):
    class Meta:
        model = StudentResult
        fields = "__all__"