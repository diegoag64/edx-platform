"""
Commerce URLs
"""


from django.conf import settings
from django.conf.urls import include

from . import views
from django.urls import path, re_path

COURSE_URLS = ([
    path('', views.CourseListView.as_view(), name='list'),
    re_path(fr'^{settings.COURSE_ID_PATTERN}/$', views.CourseRetrieveUpdateView.as_view(), name='retrieve_update'),
], 'courses')

ORDER_URLS = ([
    path('<slug:number>/', views.OrderView.as_view(), name='detail'),
], 'orders')

app_name = 'v1'
urlpatterns = [
    path('courses/', include(COURSE_URLS)),
    path('orders/', include(ORDER_URLS)),
]
