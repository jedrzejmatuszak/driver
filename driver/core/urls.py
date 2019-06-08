from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from core.views import *


urlpatterns = [
    path('hint/', HintList.as_view(), name='hint-list'),
    path('hint/<int:pk>/', HintDetail.as_view(), name='hint-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
