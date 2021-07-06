from django.shortcuts import render

from app.models import CustomUser, Staff


def example(request):
    staffs = Staff.objects.get(user=request.user)
    return render(request, 'staffs.html', {'staffs': staffs})
