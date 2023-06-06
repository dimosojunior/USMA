from . import views
from django.urls import path
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
    TokenRefreshView,
    
)

urlpatterns = [
	path('signin/', views.signin, name="signin"),
	path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name='logout'),

    path('user_create_view/', views.user_create_view.as_view(), name="user_create_view"),

    
    # path('UserView/', views.UserView.as_view(), name="UserView"),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
]