from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from main.views import index, item_detail, home_view


urlpatterns = [
    path('', home_view, name='home'),
    path('item/<int:item_id>/', item_detail, name='item_detail'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
