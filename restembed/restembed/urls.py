
from django.conf.urls import url
from django.contrib import admin
from coreapp.views import save_embed
from coreapp.views import video_all

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', save_embed),
    url(r'^new/$', video_all, name="view-all"),
]
