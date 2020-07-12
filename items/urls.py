from django.urls import path
from . import views

app_name='items'
urlpatterns = [
    path('',views.input_orders,name='inputorders'),
    path('checksales/',views.view_sales,name='viewsales'),
    path('io/',views.io,name='io'),
    path('idate/',views.idate,name="idate"),
    path('getpdf/',views.getpdf,name="pdfPage")

]
