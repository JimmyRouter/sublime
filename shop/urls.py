from django.conf.urls.static import static
from django.urls import path
from shop.views import *

from sublime_app.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path("", MainPage.as_view(), name='home'),
    path("products/<slug:tag>/", ProductPage.as_view(), name="products"),
    path("products/about/", ProductPage.as_view(), name="about"),
    path("products/privacy/", ProductPage.as_view(), name="privacy"),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)

# handler404 = exeption404

