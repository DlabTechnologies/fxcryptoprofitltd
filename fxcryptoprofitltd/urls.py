
from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse

from . sitemaps import Fxcryptoprofitltd_Static_Sitemap
from django.contrib.sitemaps.views import sitemap


sitemaps =  {
    static : Fxcryptoprofitltd_Static_Sitemap(),
}

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('mt4', views.mt4_page, name='mt4_page'),
    path('mt5', views.mt5_page, name='mt5_page'),
    path('contact', views.contact_page, name='contact_page'),
    path('pro_ecn', views.pro_ecn_page, name='pro_ecn_page'),
    path('raw_ecn', views.raw_ecn_page, name='raw_ecn_page'),
    path('standard_stp', views.standard_stp_page, name='standard_stp_page'),
    path('webtrader', views.webtrader_page, name='webtrader_page'),
    path('who_we_are', views.who_we_are_page, name='who_we_are_page'),
   # path('send_email', views.SendEmail, name='send_email'),

    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('', include('account.urls')),
    path('dlabtech_admin/', admin.site.urls),


   
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)