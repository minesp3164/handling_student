from django.urls import path
from .views import problems_list, problems_detail
urlpatterns = [
    path('', problems_list),
    path('<int:problems_id>/', problems_detail)
]