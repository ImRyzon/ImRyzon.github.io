import json
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

from .models import *


def index(request):
    return render(request, "website/index.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def projects(request, page):
    projects = Project.objects.order_by("title").all()
    paginator = Paginator(projects, 8)

    return render(request, "website/projects.html", {
        "projects" : paginator.get_page(page)
    })


def resume(request):
    return HttpResponseRedirect("static/website/Resume.pdf")


def blogs(request, page):
    blogs = Blog.objects.filter(is_active=True).order_by("-date").all()
    paginator = Paginator(blogs, 5)

    return render(request, "website/blogs.html", {
        "blogs" : paginator.get_page(page)
    })


def blog(request, id):
    blog = Blog.objects.get(pk=id)

    return render(request, "website/blog.html", {
        "blog" : blog
    })


def contact(request):
    return render(request, "website/contact.html")


def get_project(request, id):
    if request.method != "GET":
        return JsonResponse({"error": "Bad request."}, status=400)
    
    project = Project.objects.get(pk=id)

    return JsonResponse(project.serialize(), safe=False)


def project_search(request, query, page):
    projects = Project.objects.filter(title__icontains=query).order_by("title").all()
    paginator = Paginator(projects, 8)

    return render(request, "website/projects.html", {
        "projects" : paginator.get_page(page),
        "query" : query
    })


def blog_search(request, query, page):
    blogs = Blog.objects.filter(title__icontains=query, is_active=True).order_by("-date").all()
    paginator = Paginator(blogs, 5)

    return render(request, "website/blogs.html", {
        "blogs" : paginator.get_page(page),
        "query" : query
    })


def get_comments(request, blog_id):
    if request.method != "GET":
        return JsonResponse({"error": "Bad request."}, status=400)
    
    comments = Blog.objects.get(pk=blog_id).comments.filter(is_active=True, is_reply=False).order_by("-date").all()

    return JsonResponse([comment.serialize() for comment in comments], safe=False)


def get_comment(request, id):
    if request.method != "GET":
        return JsonResponse({"error": "Bad request."}, status=400)
    
    comment = Comment.objects.get(pk=id)

    return JsonResponse(comment.serialize(), safe=False)


@csrf_exempt
def create_comment(request, blog_id):
    if request.method != "POST":
        return JsonResponse({"error": "Bad request."}, status=400)
    
    data = json.loads(request.body)
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    content = data.get("content")
    
    comment = Comment(first_name=first_name, last_name=last_name, content=content)
    comment.save()
    
    Blog.objects.get(pk=blog_id).comments.add(comment)

    return JsonResponse(comment.serialize(), safe=False)


@csrf_exempt
def create_reply(request, comment_id):
    if request.method != "POST":
        return JsonResponse({"error": "Bad request."}, status=400)
    
    data = json.loads(request.body)
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    content = data.get("content")
    
    reply = Comment(first_name=first_name, last_name=last_name, content=content, is_reply=True)
    reply.save()
    
    Comment.objects.get(pk=comment_id).replies.add(reply)

    return JsonResponse(reply.serialize(), safe=False)


def get_replies(request, comment_id):
    if request.method != "GET":
        return JsonResponse({"error": "Bad request."}, status=400)
    
    replies = Comment.objects.get(pk=comment_id).replies.filter(is_active=True, is_reply=True).order_by("-date").all()

    return JsonResponse([reply.serialize() for reply in replies], safe=False)


def js(request):
    return render(request, "website/js.html")
