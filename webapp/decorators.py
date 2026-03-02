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