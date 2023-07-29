from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .forms import CommentForm, ProblemForm
from .models import Problems, Comment


def problems_list(request):
    problems = Problems.objects.all()

    context = {
        'problems':problems
    }
    return render(request,'problem/problem_list.html',context)


def problems_detail(request, problems_id):
    problem = Problems.objects.get(id=problems_id)
    comment_form = CommentForm()
    context = {
        'problem': problem,
        'comment_form':comment_form
    }
    return render(request,'problem/problem_detail.html',context)


def problem_add(request):
    if request.method == "POST":
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            problem.user = request.user

            problem.save()

            return HttpResponseRedirect('/problems/')
    else:
        form = ProblemForm()
    context = {"form": form}
    return render(request, 'problem/problem_add.html', context)


def comment_add(request,problems_id):
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user

        comment.save()

        return HttpResponseRedirect(f"/problems/{comment.problem.id}")


@require_POST
def comment_delete(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    if comment.user == request.user:
        comment.delete()
        return HttpResponseRedirect(f"/problems/{comment.problem.id}/")
    else:
        return HttpResponseForbidden("이 댓글을 삭제할 권한이 없습니다.")


