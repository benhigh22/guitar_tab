
from django.conf.urls import url
from django.contrib import admin
from guitar_app.views import IndexView, TabView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<url>.+)', TabView.as_view(), name='tab_view')
]
