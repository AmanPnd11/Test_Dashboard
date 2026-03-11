from django.shortcuts import redirect
from django.contrib import messages

def admin_required(view_func):
    def wrapper(request, *args, **kwargs):

        admin_id = request.session.get("admin_id")

        if not admin_id:
            messages.error(request, "Please login first")
            return redirect("adminlogin")

        return view_func(request, *args, **kwargs)

    return wrapper


def subadmin_required(view_func):
    def wrapper(request, *args, **kwargs):

        subadmin_id = request.session.get("subadmin_id")

        if not subadmin_id:
            messages.error(request, "Please login first")
            return redirect("subadminlogin")

        return view_func(request, *args, **kwargs)

    return wrapper


def student_required(view_func):
    def wrapper(request, *args, **kwargs):

        student_id = request.session.get("student_id")

        if not student_id:
            messages.error(request, "Please login first")
            return redirect("studentlogin")

        return view_func(request, *args, **kwargs)

    return wrapper