from django.shortcuts import render , redirect
from .models import post
from .form import postform


# Create your views here.
def post_list(request):
    data = post.objects.all()    #orm-->sql-->db--->list(all posts)
    return render(request ,'post.html',{'posts':data})

def post_DETAIL(request,post_id):
    data = post.objects.get(id=post_id)    #orm-->sql-->db--->list(all posts)
    return render(request ,'post_detail.html',{'post':data})

#add post
def add_post(request):
    if request.method=='POST':
        form=postform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form=postform()
    form=postform()
    return render(request ,'new.html',{'form':form}) 

#EDIT post
def edit_post(request,post_id):
    data = post.objects.get(id=post_id) 
    if request.method=='POST':
        form=postform(request.POST,request.FILES,instance=data)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.author=request.user
            myform.save()
            return redirect('/blog/')
    else:
        form=postform(instance=data)
    form=postform()
    return render(request ,'edit.html',{'form':form})

#delete post
def delete_post(request,post_id):
    data = post.objects.get(id=post_id)    #orm-->sql-->db--->list(all posts)
    data.delete()
    return redirect('/blog/')
