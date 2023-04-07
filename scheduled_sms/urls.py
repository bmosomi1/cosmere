
from django.urls import path
from scheduled_sms import views

app_name = "scheduled_sms"

urlpatterns = [
    path("", views.schedule_sms, name="schedule_sms"),
    path("dashboard", views.schedule_sms_dashboard, name="schedule_sms_dashboard"),
    path("sample/merged", views.scheduled_sample_merged, name="sample_merged"),
    path("list/scheduled/sms", views.list_scheduled_sms, name="list_scheduled_sms"),
    path("list/scheduled/per/month", views.list_scheduled_per_month, name="list_scheduled_per_month"),
    path("schedule/per/month", views.schedule_per_month, name="schedule_per_month"),
    path("edit/schedule/per/month/<int:id>", views.edit_schedule_per_month, name="edit_schedule_per_month"),
    path("deactivate/scheduled/per/month/<int:id>", views.deactivate_scheduled_per_month, name="deactivate_scheduled_per_month"),

    # simple
    path('simple/sms', views.simple_sms, name="simple_sms"),
    path('simple/sms/preview', views.simple_sms_preview, name='simple_sms_preview'),
    path('simple/send', views.send, name='simple_send'),

    # excel
    path('schedule/excel', views.schedule_excel, name="schedule_excel"),
    path('schedule/excel/merged', views.schedule_excel_merged, name="schedule_excel_merged"),
    path('schedule/excel/confirm', views.schedule_excel_confirm, name="schedule_excel_confirm"),

    # path('list/scheduled/messages', views.list_scheduled_messages, name="list_scheduled_messages"),
    path('list/scheduled/per/code', views.list_scheduled_per_track_code, name="list_scheduled_per_track_code"),
    path('list/scheduled/per/code', views.list_scheduled_per_track_code, name="list_scheduled_per_track_code"),
    path('disable/scheduled/per/code/<str:track_code>', views.disable_scheduled_per_track_code, name="disable_scheduled_per_track_code"),
    path('detail/scheduled/per/track_code/<str:track_code>', views.detail_scheduled_per_track_code, name="detail_scheduled_per_track_code"),
]