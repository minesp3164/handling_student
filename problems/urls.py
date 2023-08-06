from django.urls import path
from .views import problems_list, problem_detail, comment_add, comment_delete, problem_add, problem_edit, problem_delete

urlpatterns = [
    path('', problems_list),
    path('<int:problems_id>/', problem_detail),
    path('<int:problems_id>/comment_add/', comment_add),
    path('comment_delete/<int:comment_id>',comment_delete),
    path('problem_add/',problem_add),
    path('<int:problems_id>/edit/',problem_edit),
    path('<int:problems_id>/delete/',problem_delete)
]