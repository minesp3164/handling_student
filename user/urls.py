from django.urls import path
from .views import login_view, logout_view, signup_view, user_detail

urlpatterns = [
    path('login/', login_view),
    path('logout/',logout_view),
    path('signup/', signup_view),
    path('detail/<str:username>',user_detail),

]