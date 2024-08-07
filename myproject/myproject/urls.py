from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('predict', views.pred, name='pred'),
    path('finder', views.find, name='finder'),
]