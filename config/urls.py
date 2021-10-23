from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls.conf import include

from config.views import Index
from radio.views import AudioList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name="index"),
    path('posters/', include('perfomances.urls'), name='poster_list'),
    path('radio/', AudioList.as_view(), name="radio"),
    path('api/cart/', include('cart.urls'))
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) if settings.DEBUG else urlpatterns
