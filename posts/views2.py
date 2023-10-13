from django.views import generic
from .models import post
 
class postlist(generic.ListView):
     model=post

     #context---> post_list
     #template---> post_list.html

class Postdetail(generic.DetailView):
     model=post