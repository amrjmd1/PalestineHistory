from django.shortcuts import render, HttpResponseRedirect
from Client.models import *
from django.http import JsonResponse
from django.views.generic import View
from ipware.ip import get_real_ip
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse
from django.utils import timezone


class HomePage(View):
    def get(self, request):
        if request.session.get('manage', False):
            session_user = request.session.get('manage', False)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if user_agent_oop.logout:
                logout(request)
                return HttpResponseRedirect(reverse('Dashboard:login'))
            context = {
                'title': 'الرئيسية',
                'logout_user': session_user,
                'admin_is_manager': request.session.get('is_manager', False),
                'session_user': session_user.split('_')[0],
            }
            return render(request, 'Dashboard/index.html', context)
        else:
            return HttpResponseRedirect(reverse('MainPage'))


class LoginDashboard(View):
    def get(self, request):
        if request.session.get('client', None):
            return HttpResponseRedirect(reverse('MainPage'))
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                return HttpResponseRedirect(reverse('Dashboard:HomePage'))
            else:
                logout(request)
                return HttpResponseRedirect(reverse('MainPage'))
        context = {"title": "تسجيل الدخول"}
        return render(request, 'Dashboard/login.html', context)


class LogoutDashboard(View):
    def get(self, request, session_user):
        UserAgents.objects.filter(user=session_user, logout=False).update(logout=True, end_session=timezone.now())
        logout(request)
        return HttpResponseRedirect(reverse('MainPage'))


class CheckLoginDashboard(View):
    def post(self, request):
        username = request.POST.get('username').strip()
        password = request.POST.get('password')
        if username != "" and password != "":
            if username.find('@') != -1:
                username_list = username.split("@")
                name = username_list[0]
                domain = username_list[1]
                if domain.lower() == 'django':
                    if not Manager.objects.filter(username=name).first():
                        message = 'ContextError'
                    else:
                        check_user = Manager.objects.filter(username=name).first()
                        if check_user.password == password:
                            message = 'Done'
                            request.session.set_expiry(7200)
                            request.session['manage'] = username.replace('@', '_')
                            request.session['is_manager'] = check_user.is_manager
                        else:
                            message = 'ContextError'
                else:
                    message = 'ContextError'
            else:
                message = 'ContextError'
        else:
            message = 'Empty'

        context = {'msg': message}
        if message == "ContextError":
            LoginAttempts(ip=str(get_real_ip(request)), name=username, password=password,
                          browser_family=request.user_agent.browser.family,
                          browser_version=request.user_agent.browser.version_string,
                          os_family=request.user_agent.os.family,
                          os_version=request.user_agent.os.version_string,
                          device_family=request.user_agent.device.family, manage=True).save()
        elif message == "Done":
            username = username.replace('@', '_')
            user_agents = UserAgents.objects.filter(user=username, logout=False)
            if user_agents.first():
                user_agents = user_agents.latest('id')
                UserAgents.objects.filter(pk=user_agents.id).update(logout=True, end_session=timezone.now())
            UserAgents(ip=str(get_real_ip(request)), user=username,
                       browser_family=request.user_agent.browser.family,
                       browser_version=request.user_agent.browser.version_string,
                       os_family=request.user_agent.os.family,
                       os_version=request.user_agent.os.version_string,
                       device_family=request.user_agent.device.family).save()
            context['url'] = reverse('Dashboard:HomePage')
        return JsonResponse(context)
