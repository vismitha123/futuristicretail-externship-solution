from django.shortcuts import render



# Rendering the home page html
def home(request):
    return render(request,'home.html')
#Rendering the page to input items and generating bill
def input_orders(request):
    return render(request,'inputorders.html')
#Rendering a page to view daily sales
def view_sales(request):
    return render(request,'viewsales.html')
##Rendering a page to check covid spread
def check_spread(request):
    return render(request,'checkspread.html')
