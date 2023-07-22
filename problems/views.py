from django.shortcuts import render, get_object_or_404
from .models import Problems, Comment


def problems_list(request):
    problems = Problems.objects.all()

    context = {
        'problems':problems
    }
    return render(request,'problem/problem_list.html',context)


def problems_detail(request, problems_id):
    problem = Problems.objects.get(id=problems_id)
    context = {
        'problem': problem,
    }
    return render(request,'problem/problem_detail.html',context)
