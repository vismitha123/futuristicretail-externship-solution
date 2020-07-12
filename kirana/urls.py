from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),

    path('items/',include('items.urls')),
    path('checkspread/',views.check_spread,name='checkspread'),


]
urlpatterns+= staticfiles_urlpatterns()
