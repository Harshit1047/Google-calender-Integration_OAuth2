from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from django.http import JsonResponse, HttpResponseRedirect
from django.views import View
from django.conf import settings

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'


class GoogleCalendarInitView(View):
    def get(self, request):
        flow = InstalledAppFlow.from_client_secrets_file(
            settings.GOOGLE_CLIENT_SECRET_FILE, SCOPES)
        auth_url, _ = flow.authorization_url(prompt='consent')

        return HttpResponseRedirect(auth_url)


class GoogleCalendarRedirectView(View):
    def get(self, request):
        code = request.GET.get('code')
        flow = InstalledAppFlow.from_client_secrets_file(
            settings.GOOGLE_CLIENT_SECRET_FILE, SCOPES)
        flow.fetch_token(code=code)

        credentials = flow.credentials
        service = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

        try:
            events = service.events().list(calendarId='primary').execute()
            return JsonResponse(events)
        except HttpError as error:
            return JsonResponse({'error': str(error)})


def home(request):
    return JsonResponse({'message': 'Welcome to the home page!'})

def calendar_init(request):
    return JsonResponse({'message': 'Calendar initialization logic goes here'})

def calendar_redirect(request):
    return JsonResponse({'message': 'Calendar redirect logic goes here'})
