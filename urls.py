from django.urls import path
from calendar_integration.views import home, GoogleCalendarInitView, GoogleCalendarRedirectView

urlpatterns = [
    path('', home, name='home'),
    path('rest/v1/calendar/init/', GoogleCalendarInitView.as_view(), name='calendar-init'),
    path('rest/v1/calendar/redirect/', GoogleCalendarRedirectView.as_view(), name='calendar-redirect'),
]
