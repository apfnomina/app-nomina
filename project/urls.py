from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from main import views
from welcome.views import index, health

urlpatterns = [
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', index),
    url(r'^health$', health),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^explorer/', include('explorer.urls')),
    url(r'^api-rest/rangoispt/(?P<fec_fin>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/(?P<monto>\d+\.\d+)/$',
    views.RangoIsptViewSet.as_view(), name='my_rest_view'),
    url(r'^api-rest/ispt/(?P<fec_fin>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/(?P<monto>\d+\.\d+)/$',
    views.CalculoIsptViewSet.as_view(), name='my_rest_view'),
    url(r'^api-rest/sueldonivel/(?P<fec_fin>((19|20)\d\d)-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01]))/(?P<nivel>[G-Pg-p0-9]{1,4})/$',
    views.SueldoPorNivelViewSet.as_view(), name='my_rest_view'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
