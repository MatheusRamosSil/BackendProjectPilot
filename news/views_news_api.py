from django.views import View
from newsapi import NewsApiClient
from django.conf import settings
from django.http import JsonResponse

class ApiNewsViews(View):
    '''
          def get_top_headlines(request,country):
        result = NewsApiClient(api_key=settings.API_NEWS_KEY).get_top_headlines(q=None, qintitle=None, sources=None, language=None,country=country, category=None, page_size=None, page=None)
        return JsonResponse(result)
    '''
    def get_all_news(request):
        result = NewsApiClient(api_key=settings.API_NEWS_KEY).get_top_headlines()
        return JsonResponse(result)

    def get_news_category_or_country(request,category = None,country = None):
        result = NewsApiClient(api_key=settings.API_NEWS_KEY).get_top_headlines(q=None, qintitle=None, sources=None, language=None,country=country, category=category, page_size=None, page=None)
        return JsonResponse(result)

    def search_news_editors(request,country= None,category = None,language = None):
        result = NewsApiClient(api_key= settings.API_NEWS_KEY).get_sources(country,category,language)
        return JsonResponse(result)

    def search_news(request,
            q=None,
            qintitle=None,
            sources=None,
            domains=None,
            exclude_domains=None,
            from_param=None,
            to=None,
            language=None,
            sort_by=None,
            page=None,
            page_size=None):
        result = NewsApiClient(api_key=settings.API_NEWS_KEY).get_everything(q,qintitle,sources,
                                                                            domains,exclude_domains,from_param,to,
                                                                            language,sort_by,page,page_size)
        return JsonResponse(result)
