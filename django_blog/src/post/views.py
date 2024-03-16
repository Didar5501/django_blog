from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.template.response import TemplateResponse
from post.models import Post

# def index(request):
#     print(request)
#     print(request.scheme)
#     print(request.path)
#     print(request.encoding)
#     return HttpResponse ('<h1>Hello World!</h1>')

# def about(request):
#     print('http://127.0.0.1:8000'+request.get_full_path())
#     return HttpResponse ('<a href="#"> About page!</a>') 

# def contacts(request):
#     return HttpResponse ('<h2>Contacts page</h2>') 

# def ggg(request):
#     return HttpResponse ('<h2> GGG page</h2>') 

# def arсhive(request):
#     return HttpResponse ('Arсhive page') 

# def arсhive_2 (request):
#     return HttpResponse ('Arсhive page_2')

# def group (request):
#     print(request.path)
#     group_number=request.path
#     return HttpResponse (f'group #{group_number[12:-1]}')
      


# def home(request):
#     return HttpResponse('<h1>HOME</h1>')

def posts(request):
    #  return HttpResponse('<h1>All posts:</h1>')
    posts=Post.objects.all()
    data={
        'title': 'All posts',
        'message': 'Hello',
        'posts': posts,
    }

    return render(request, 'post.html', context=data)


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404("Пост не существует")
    context = {
        'post': post,
        'message': 'Детально ознакомьтесь с постом',
    }
    return render(request, 'post_detail.html', context)

def post_archive(request, year):
    if int(year)> 2024 or int(year)<1995:
        raise Http404
    return HttpResponse(f'archive for:{year}')

def get_post_handler(request):
    if request.POST:
        return HttpResponse('POST request')
    return HttpResponse('GET request')

def page_404(request, exception):
    return HttpResponseNotFound('<h3>Page not found:^(</h3>)')

def template_test(request):
    # return render(request, 'template_test.html')
    return TemplateResponse(request, 'template_test.html')