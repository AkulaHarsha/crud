from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.db.models import Q
from .models import *  # Assuming you have a models.py file with the Student model

def first(request):
    data = Student.objects.all()  # Get all students initially
    query = ""
    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            Student.objects.create(name=name, email=email)
            messages.success(request, "Student Added successfully")
        elif "update" in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name')
            email = request.POST.get('email')
            update_student = Student.objects.get(id=id)
            update_student.name = name
            update_student.email = email
            update_student.save()
            messages.success(request, "Student Updated successfully")
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.get(id=id).delete()
            messages.success(request, "Student deleted successfully")
        elif "search" in request.POST:
            query = request.POST.get('searchquery')
            if query:  # Check if a search query is provided
                data = Student.objects.filter(Q(name__icontains=query) | Q(email__icontains=query))
            else:  # If no search query, display all students
                data = Student.objects.all()
                messages.success(request, f"Search results for '{query}'")  # Update success message

    context = {'result': data, 'query': query}
    return render(request, 'index.html', context=context)
