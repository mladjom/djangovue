"""
URL configuration for backend project.
"""
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

# Only add language prefix to admin URL pattern, not the whole urlpatterns
urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
)