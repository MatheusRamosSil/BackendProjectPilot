from django.urls import path
from . import views_news_api


urlpatterns = [
    path('', views_news_api.ApiNewsViews.get_all_news),
    path('country/<slug:country>/', views_news_api.ApiNewsViews.get_news_category_or_country),
    path('category/<slug:category>/', views_news_api.ApiNewsViews.get_news_category_or_country),
    path('search/editors/<slug:country>/<slug:category>/<slug:language>',views_news_api.ApiNewsViews.search_news_editors, name='search_news_editors'),
    path('search/<slug:q>/',views_news_api.ApiNewsViews.search_news, name='search_news'),
]


