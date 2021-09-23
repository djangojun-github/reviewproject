from django.urls import path
from .views import signupview, loginview, listview, detailview, CreateClass, evaluationview
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change_done', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('list/', listview, name='list'),
    path('detail/<int:pk>', detailview, name='detail'),
    path('create/', CreateClass.as_view(), name='create'),
    path('evaluation/<int:pk>', evaluationview, name='evaluation'),
]