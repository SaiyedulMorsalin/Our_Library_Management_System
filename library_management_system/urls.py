from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/account/", include("accounts.urls")),
    path("authors/", include("authors.urls")),
    path("books/", include("books.urls")),
    path("", include("core.urls")),
    path("users/", include("users.urls")),
    path("user/borrow/", include("user_borrow_book.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
