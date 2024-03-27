from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.template.response import TemplateResponse
from post.models import Post
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy


class PostList(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'post/posts.html'
    context_object_name='posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name='post'


class CreatePostView(CreateView):
    model = Post
    template_name = 'post/create.html'
    fields=['title', 'user', 'status']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')

class AboutView(TemplateView):
    template_name= 'post/about.html'
    context_object_name='about'

       

@csrf_exempt
def get_post_handler(request):
    if request.method=='POST':
        return HttpResponse('POST request')
    is_actual = request.GET.get('is_actual')
    user = request.GET.get('user')
    
    posts = Post.objects.filter(is_actual= bool(is_actual), user__username=user)
    response = {
        'post': list(posts)
    }
    return JsonResponse(response)






def template_test(request):
    # return render(request, 'template_test.html')
    return TemplateResponse(request, 'template_test.html')


#DRF views
