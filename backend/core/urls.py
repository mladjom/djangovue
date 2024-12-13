'''
URL configuration for backend project.
'''
from django.contrib.sitemaps.views import sitemap
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from blog.sitemaps import CategorySitemap, TagSitemap, ArticleSitemap
from blog.views.article.article_list import ArticleListView
from blog.views.category.category_list import CategoryListView
from blog.views.tag.tag_list import TagListView
from blog.views.article.article_detail import ArticleDetailView
from blog.views.category.category_detail import CategoryDetailView
from blog.views.tag.tag_detail import TagDetailView

sitemaps = {
    'categories': CategorySitemap,
    'tags': TagSitemap,
    'articles': ArticleSitemap,
}

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories-list'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('articles/', ArticleListView.as_view(), name='article-list'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
    path('tags/<slug:slug>/', TagDetailView.as_view(), name='tag-detail'),
    path('articles/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

# Only add language prefix to admin URL pattern, not the whole urlpatterns
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)