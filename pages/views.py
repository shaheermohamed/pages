from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/Home.html'
class Contactpageview(TemplateView):
    template_name = 'pages/about.html'
