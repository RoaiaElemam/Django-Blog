from django.shortcuts import render
from .models import post

# Create your views here.
def post_list(request):
    data = post.objects.all()    #orm-->sql-->db--->list(all posts)
    return render(request ,'post.html',{'posts':data})

def post_DETAIL(request,post_id):
    data = post.objects.get(id=post_id)    #orm-->sql-->db--->list(all posts)
    return render(request ,'post_detail.html',{'post':data})