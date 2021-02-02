from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class Fxcryptoprofitltd_Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = 'yearly'

    def items(self):
        return ['home_page','mt4_page','mt5_page', 'contact_page','pro_ecn_page','raw_ecn_page','standard_stp_page']

    def location(self, item):
        return reverse(item)




