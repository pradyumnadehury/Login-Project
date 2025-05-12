from django.shortcuts import render

# Create your views here.
def book_details(request):
  data3={"math":{"book1":"Math Magicy","book2":"I love Math"},
         "science":{"book1":"looking Around:Class 5","book2":"Science Class 5"}}
  return render(request,"bookdetails.html",{"data3":data3})
def members(request):
  return render(request,"index.html")
