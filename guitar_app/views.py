import requests
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from bs4 import BeautifulSoup

tab_url = "http://www.guitartabs.cc/"


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_string = self.request.GET.get('search_string')
        scraped_content = requests.get("http://www.guitartabs.cc/search.php?tabtype=any&band=&song={}".format(search_string)).content
        clean_data = BeautifulSoup(scraped_content).find(class_="tabslist")
        for link in clean_data.find_all('a'):
            link["href"] = reverse('tab_view', kwargs={'url': link["href"]})
        context["scraped_content"] = clean_data.prettify()
        return context


class TabView(TemplateView):
    template_name = 'tab.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_url = tab_url + context["url"]
        tabs = requests.get(new_url).content
        clean_tab = BeautifulSoup(tabs).find_all('pre')
        context["tabs"] = [tab.prettify() for tab in clean_tab]
        return context
