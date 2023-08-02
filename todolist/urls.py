from django.urls import path
from .views import todolist_view, todolist_add, todolist_detail, todolist_checked, todolist_delete, todolist_edit

urlpatterns = [
    path('',todolist_view),
    path('detail/<int:todolist_id>/',todolist_detail),
    path('add/',todolist_add),
    path('<int:todolist_id>/checked/',todolist_checked),
    path('<int:todolist_id>/edit',todolist_edit),
    path('<int:todolist_id>/delete/',todolist_delete),
]