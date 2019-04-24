from django.conf.urls import url
from Client.views import *

app_name = 'Client'

urlpatterns = [
    url(r'^profile/(?P<profile_client>[\w-]+)/$', ProfileClient.as_view(), name='ProfileClient'),
    url(r'^login$', LoginClient.as_view(), name='LoginClient'),
    url(r'^register', RegisterClient.as_view(), name='RegisterClient'),
    url(r'^logout_user/(?P<session_user>[\w-]+)/$', LogoutClient.as_view(), name='logoutClient'),
    url(r'^authentication/$', CheckLoginClient.as_view(), name='Login_Form_Ajax'),
    url(r'^settings/(?P<profile_client>[\w-]+)/$', SettingsClient.as_view(), name='SettingsClient'),
    url(r'^check_verify_code/$', CheckVerifyCode.as_view(), name='Check_Verify_Code_Ajax'),
    url(r'^save_settings/$', SaveSettings.as_view(), name='Save_Settings_Ajax'),
    url(r'^change_password/$', ChangePassword.as_view(), name='Change_Password_Ajax'),
    url(r'^change_email/$', ChangeEmail.as_view(), name='Change_Email_Ajax'),
    url(r'^verify_password/$', VerifyPassword.as_view(), name='VerifyPasswordAjax'),
    url(r'^create_account/$', CreateAccount.as_view(), name='CreateAccountAjax'),
]
