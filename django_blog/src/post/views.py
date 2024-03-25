from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render
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
    # context_object_name='posts'

# def posts(request):
#     #  return HttpResponse('<h1>All posts:</h1>')
#     posts=Post.objects.all()
#     data={
#         'title': 'All posts',
#         'message': 'Hello',
#         'posts': posts,
#     }

    # return render(request, 'post/posts.html', context=data)


# def post_detail(request, post_id):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         raise Http404("Пост не существует")
#     context = {
#         'post': post,
#         'message': 'Детально ознакомьтесь с постом',
#     }
#     return render(request, 'post/post_detail.html', context)

class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    # context_object_name='p'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["from"]=PostFrom()
    #     return context
        


def post_archive(request, year):
    if int(year) > 2024 or int(year) < 1995:
        # return HttpResponseNotFound('Ошибка 404: Страница не найдена')
        return redirect('post_detail', 1)
    return HttpResponse(f'archive for:{year}')

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


class CreatePostView(CreateView):
    model = Post
    template_name = 'post/create.html'
    fields=['title', 'user', 'status']

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('posts')
    # template_name = 'post/post_confirm_delete.html'


def page_404(request, exception):
    return HttpResponseNotFound('<h3>Page not found:^(</h3>)')

def template_test(request):
    # return render(request, 'template_test.html')
    return TemplateResponse(request, 'template_test.html')