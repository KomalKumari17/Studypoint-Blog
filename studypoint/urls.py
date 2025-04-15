from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from cms.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", homePage, name="homePage"),
    path('filter/<int:topic_id>', filter, name="filter"),
    path("search/", search, name="search"),
    path("login/", loginView, name="login"),
    path("logout/", logoutFilter, name="logout"),
    path("register/", register, name="register"),
    path("view/<int:tutorial_id>", view, name="view"),
    path("view/<int:content_id>/comment/create", saveComment, name="saveComment"),
    path("single-view/<int:content_id>", singleView, name="singleView"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)