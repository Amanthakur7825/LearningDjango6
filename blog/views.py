from django.shortcuts import render
from datetime import datetime

def blog_details(request):
    blog =[
        {"title":"django basic" , "is_published":True ,"author":"aman thakur"},
        {"title":"django advance" , "is_published":False ,"author":""},
        {"title":"django rest framework" , "is_published":True ,"author":"aman "}
    ]
    context ={
        "blogs": blog,
        "today": datetime.now(),
        "html_code": "<h1> This is html code </h1>",

    }
    return render(request, "blog/blog_details.html", context)