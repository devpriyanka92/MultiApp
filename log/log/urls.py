from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from .import views as root_views
from django.conf.urls.static import static
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(), name='login'),
    path('index/',root_views.index),
    path('logout/', root_views.logout, name='logout'),
    path('chat/',root_views.chat,name='chat'),
]