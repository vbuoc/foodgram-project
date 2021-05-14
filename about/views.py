from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'flatpages/default.html'


class AboutTechView(TemplateView):
    template_name = 'flatpages/default.html'