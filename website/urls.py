from django.urls import path

from . import views

urlpatterns = [
    # Web routes
    path("", views.index, name="index"),
    path("projects/<int:page>", views.projects, name="projects"),
    path("projects/<str:query>/<int:page>", views.project_search, name="projects-search"),
    path("resume", views.resume, name="resume"),
    path("blogs/<int:page>", views.blogs, name="blogs"),
    path("blog/<int:id>", views.blog, name="blog"),
    path("blogs/<str:query>/<int:page>", views.blog_search, name="blog-search"),
    path("contact", views.contact, name="contact"),
    path("logout", views.logout_view, name="logout"),
    path("js", views.js, name="js"),
    path("create/project", views.project_form, name="project-form"),
    path("create/blog", views.blog_form, name="blog-form"),

    # API routes
    path("project/<int:id>", views.get_project, name="get-project"),
    path("comments/<int:blog_id>", views.get_comments, name="get-comments"),
    path("comment/<int:id>", views.get_comment, name="get-comment"),
    path("create-comment/<int:blog_id>", views.create_comment, name="create-comment"),
    path("create-reply/<int:comment_id>", views.create_reply, name="create-reply"),
    path("replies/<int:comment_id>", views.get_replies, name="get-replies"),
    path("create-project", views.create_project, name="create-project"),
    path("create-blog", views.create_blog, name="create-blog")
]