from django.urls import path
from .views import problems_list, problems_detail, comment_add, comment_delete

urlpatterns = [
    path('', problems_list),
    path('<int:problems_id>/', problems_detail),
    path('<int:problems_id>/comment_add/', comment_add),
    path('comment_delete/<int:comment_id>',comment_delete)

]