from django.shortcuts import render, HttpResponseRedirect
from .models import *
from django.http import JsonResponse
from django.views.generic import View
from ipware.ip import get_real_ip
from django.utils import timezone
from django.contrib.auth.views import logout
from django.core.urlresolvers import reverse
from Category.models import Category
import re, datetime
from django.db.models import Q
from django.template import loader
from django.core.mail import send_mail
from django.utils.crypto import get_random_string
from Event.models import Event
from Video.models import Video


class ViewUsers(View):
    def get(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                all_client = Client.objects.all()
                all_category = Category.objects.all()
                context = {
                    'title': 'عرض المستخدمين',
                    'all_client': all_client,
                    'logout_user': session_user,
                    'admin_is_manager': request.session.get('is_manager', False),
                    'session_user': session_user.split('_')[0],
                    'all_category': all_category,
                }
                return render(request, 'Dashboard/Users/view_users.html', context)
        return HttpResponseRedirect(reverse('Dashboard:login'))


class AddUser(View):
    def get(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                context = {
                    'title': 'أضف مستخدم جديد',
                    'logout_user': session_user,
                    'admin_is_manager': request.session.get('is_manager', False),
                    'session_user': session_user.split('_')[0],
                }
                return render(request, 'Dashboard/Users/add_user.html', context)
        return HttpResponseRedirect(reverse('Dashboard:login'))


class RemoveUser(View):
    def post(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                user_id = request.POST.get("id_user_model", False)
                if user_id:
                    client_oop = Client.objects.filter(pk=user_id)
                    if not client_oop.first():
                        message = "NotExists"
                    else:
                        client_oop.delete()
                        client_oop = Client.objects.filter(pk=user_id)
                        if not client_oop.first():
                            message = 'Done'
                        else:
                            message = 'Fail'
                else:
                    message = "Empty"
                return JsonResponse({'status': message})
            logout(request)
        return HttpResponseRedirect(reverse('Dashboard:login'))


class EditUser(View):
    def post(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                user_id = request.POST.get("id_user_model", False)
                if user_id:
                    client_oop = Client.objects.filter(pk=user_id)
                    if not client_oop.first():
                        return JsonResponse({'status': "NotExists"})
                    else:
                        name1 = request.POST.get("name1_user_model", False)
                        name2 = request.POST.get("name2_user_model", False)
                        name3 = request.POST.get("name3_user_model", False)
                        name4 = request.POST.get("name4_user_model", False)
                        email = request.POST.get("email_user_model", False)
                        password = request.POST.get("password_user_model", False)
                        gender = request.POST.get("gender_user_model", False)
                        category = request.POST.get("category_user_model", False)
                        phone = request.POST.get("mobile_user_model", False)
                        identity = request.POST.get("identity_user_model", False)
                        is_active = request.POST.get("is_active_user_model", False)
                        inputs = [name1, name2, name3, name4, email, password, is_active, category, phone, identity]
                        if check_input_is_empty(inputs):
                            return JsonResponse({'msg': 'isEmpty'})
                        else:
                            if not verify_password(password):
                                return JsonResponse({'msg': 'PasswordContextError'})
                            if not verify_email(email):
                                return JsonResponse({'msg': 'EmailContextError'})
                            if gender != "1" and gender != "2":
                                return JsonResponse({'msg': 'GenderContextError'})
                            if is_active != "1" and is_active != "2":
                                return JsonResponse({'msg': 'ActiveContextError'})
                            if not phone.isnumeric() or len(phone) != 10:
                                return JsonResponse({'msg': 'PhoneContextError'})
                            if not identity.isnumeric() or len(identity) != 9:
                                return JsonResponse({'msg': 'IdentityContextError'})
                            if not check_input_is_alpha([name1, name2, name2, name4]):
                                return JsonResponse({'msg': 'NameContextError'})
                            category_oop = Category.objects.filter(identity=category).first()
                            if not category_oop:
                                return JsonResponse({'msg': 'CategoryContextError'})
                            if is_active == "1":
                                active = True
                            else:
                                active = False
                            client_oop.update(email=email, password=password, category=category_oop, first_name=name1,
                                              father_name=name2, grand_name=name3, last_name=name4, gender=gender,
                                              mobile=phone, identity=identity, is_active=active)
                            check_oop = Client.objects.filter(pk=user_id, category=category_oop, email=email,
                                                              password=password, first_name=name1, father_name=name2,
                                                              grand_name=name3, last_name=name4, gender=gender,
                                                              mobile=phone, identity=identity, is_active=active).first()
                            if check_oop:
                                return JsonResponse({'msg': 'Done'})
                            else:
                                return JsonResponse({'msg': 'Fail'})
                else:
                    return JsonResponse({'status': "isEmpty"})
            logout(request)
        return HttpResponseRedirect(reverse('Dashboard:login'))


class MainPage(View):
    def get(self, request):
        videos = Video.objects.all()
        context = {
            'title': 'الصفحة الرئيسية',
            'videos': videos
        }
        if request.session.get('client', False):
            session_user = request.session.get('client', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                client_oop = Client.objects.filter(username=session_user).first()
                context['client'] = client_oop
                context['type_session'] = 'Client'
                context['session_user'] = session_user
                context['logout_user'] = session_user
            else:
                logout(request)
        elif request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                context['type_session'] = 'Manager'
                context['session_user'] = session_user.split('_')[0]
                context['logout_user'] = session_user
                context['admin_is_manager'] = request.session.get('is_manager', None)
            else:
                logout(request)
        return render(request, 'main_page.html', context)


class LoginClient(View):
    def get(self, request):
        if request.session.get('manage', None):
            return HttpResponseRedirect(reverse('MainPage'))
        if request.session.get('client', None):
            session_user = request.session.get('client', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                return HttpResponseRedirect(reverse('Client:ProfileClient', args={session_user}))
        context = {"title": "تسجيل الدخول"}
        return render(request, 'Client/login.html', context)


class RegisterClient(View):
    def get(self, request):
        if not request.session.get('manage', False) and not request.session.get('client', False):
            category_all = Category.objects.filter(~Q(identity='default'))
            context = {
                "title": "الالتحاق بالمسابقة",
                "category_all": category_all,
            }
            return render(request, 'Client/register.html', context)
        return HttpResponseRedirect(reverse('MainPage'))


class LogoutClient(View):
    def get(self, request, session_user):
        UserAgents.objects.filter(user=session_user, logout=False).update(logout=True, end_session=timezone.now())
        logout(request)
        return HttpResponseRedirect(reverse('MainPage'))


class CheckLoginClient(View):
    def post(self, request):
        email = request.POST.get('email', False)
        password = request.POST.get('password', False)
        list_of_input = [email, password]
        if not check_input_is_empty(list_of_input):
            client_oop = Client.objects.filter(email=email).first()
            if client_oop:
                if client_oop.password == password:
                    message = 'Done'
                    request.session.set_expiry(7200)
                    request.session['client'] = client_oop.username
                else:
                    message = 'ContextError'
            else:
                message = 'ContextError'
        else:
            message = 'Empty'
        context = {'msg': message}
        if message == "ContextError":
            LoginAttempts(ip=str(get_real_ip(request)), name=email, password=password,
                          browser_family=request.user_agent.browser.family,
                          browser_version=request.user_agent.browser.version_string,
                          os_family=request.user_agent.os.family,
                          os_version=request.user_agent.os.version_string,
                          device_family=request.user_agent.device.family).save()
        elif message == "Done":
            user_agents = UserAgents.objects.filter(user=email, logout=False)
            client_oop = Client.objects.filter(email=email).first()
            if user_agents.first():
                user_agents = user_agents.latest('id')
                UserAgents.objects.filter(pk=user_agents.id).update(logout=True, end_session=timezone.now())
            UserAgents(ip=str(get_real_ip(request)), user=client_oop.username,
                       browser_family=request.user_agent.browser.family,
                       browser_version=request.user_agent.browser.version_string,
                       os_family=request.user_agent.os.family,
                       os_version=request.user_agent.os.version_string,
                       device_family=request.user_agent.device.family).save()
            context['url'] = reverse('Client:ProfileClient', args={client_oop.username})
        return JsonResponse(context)


class ProfileClient(View):
    def get(self, request, profile_client):
        if request.session.get('client', None):
            session_user = request.session.get('client', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                client_oop = Client.objects.filter(username=profile_client).first()
                if client_oop:
                    if client_oop.username == session_user:
                        all_event = Event.objects.filter(category=client_oop.category)
                        context = {
                            "title": "الصفحة الشخصية",
                            'client': client_oop,
                            'session_user': session_user,
                            'events': all_event
                        }
                        return render(request, 'Client/profile.html', context)
                    else:
                        return HttpResponseRedirect(reverse('Client:ProfileClient', args={session_user}))
        return HttpResponseRedirect(reverse('Client:LoginClient'))


class SettingsClient(View):
    def get(self, request, profile_client):
        if request.session.get('client', None):
            session_user = request.session.get('client', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                client_oop = Client.objects.filter(username=profile_client).first()
                if client_oop:
                    if client_oop.username == session_user:
                        category_all = Category.objects.all()
                        context = {
                            "title": "الإعدادات",
                            'client': client_oop,
                            'session_user': session_user,
                            "category_all": category_all,
                        }
                        return render(request, 'Client/settings.html', context)
                    else:
                        return HttpResponseRedirect(reverse('Client:ProfileClient', args={session_user}))
            else:
                logout(request)
        return HttpResponseRedirect(reverse('Client:LoginClient'))


class CheckVerifyCode(View):
    def post(self, request):
        if request.session.get('client', None):
            session_user = request.session.get('client', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                client_oop = Client.objects.filter(username=session_user)
                if client_oop.first():
                    code = request.POST.get("code")
                    if check_input_is_empty([code]):
                        message = "empty"
                    else:
                        verify_email_oop = VerifyEmail.objects.filter(client=client_oop.first()).first()
                        if verify_email_oop.random_number == code:
                            client_oop.update(is_active=True)
                            message = "Done"
                        else:
                            message = "Fail"
                    return JsonResponse({'msg': message})
            else:
                logout(request)
        else:
            return JsonResponse({'msg': 'FailLogin'})
        return


# Settings
class SaveSettings(View):
    def post(self, request):
        if request.session.get('client', None):
            session_user = request.session.get('client', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                client_oop = Client.objects.filter(username=session_user)
                if client_oop.first() and client_oop.first().is_active:
                    name1 = request.POST.get("name1", False)
                    name2 = request.POST.get("name2", False)
                    name3 = request.POST.get("name3", False)
                    name4 = request.POST.get("name4", False)
                    gender = request.POST.get("gender", False)
                    category = request.POST.get("category", False)
                    phone = request.POST.get("phone", False)
                    identity = request.POST.get("id_client", False)
                    list_of_input = [name1, name2, name3, name4, category, phone, identity]
                    if check_input_is_empty(list_of_input):
                        return JsonResponse({'msg': 'isEmpty'})
                    else:
                        if gender != "1" and gender != "2":
                            return JsonResponse({'msg': 'GenderContextError'})
                        if not phone.isnumeric() or len(phone) != 10:
                            return JsonResponse({'msg': 'PhoneContextError'})
                        if not identity.isnumeric() or len(identity) != 9:
                            return JsonResponse({'msg': 'IdentityContextError'})
                        if not check_input_is_alpha([name1, name2, name2, name4]):
                            return JsonResponse({'msg': 'NameContextError'})
                        category_oop = Category.objects.filter(identity=category).first()
                        if not category_oop:
                            return JsonResponse({'msg': 'CategoryContextError'})
                        client_oop.update(category=category_oop, first_name=name1, father_name=name2, grand_name=name3,
                                          last_name=name4, gender=gender, mobile=phone, identity=identity)
                        check_oop = Client.objects.filter(username=session_user, category=category_oop,
                                                          first_name=name1, father_name=name2, grand_name=name3,
                                                          last_name=name4, gender=gender, mobile=phone,
                                                          identity=identity).first()
                        if check_oop:
                            return JsonResponse({'msg': 'Done'})
                        else:
                            return JsonResponse({'msg': 'Fail'})
                else:
                    return JsonResponse({'msg': 'NotActive'})
            else:
                logout(request)
                return JsonResponse({'msg': 'FailLogin'})
        else:
            return JsonResponse({'msg': 'FailLogin'})


class ChangePassword(View):
    def post(self, request):
        if request.session.get('client', None):
            session_user = request.session.get('client', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                client_oop = Client.objects.filter(username=session_user)
                if client_oop.first() and client_oop.first().is_active:
                    password = request.POST.get("password", False)
                    new_password = request.POST.get("new_password", False)
                    re_password = request.POST.get("re_password", False)
                    list_of_input = [password, new_password, re_password]
                    if check_input_is_empty(list_of_input):
                        message = 'isEmpty'
                    else:
                        if client_oop.first().password == password:
                            if new_password == re_password:
                                if password != new_password:
                                    if verify_password(new_password):
                                        client_oop.update(password=new_password)
                                        new_client_oop = Client.objects.filter(password=new_password).first()
                                        if new_client_oop.password == new_password:
                                            status_password = send_code("password", new_client_oop,
                                                                        new_client_oop.first_name,
                                                                        new_client_oop.last_name, "")
                                            if status_password:
                                                message = 'Done'
                                                logout(request)
                                            else:
                                                message = 'try_again'
                                        else:
                                            message = 'Fail'
                                    else:
                                        message = "PasswordContextError"
                                else:
                                    message = "NoAnyChange"
                            else:
                                message = 'isNotMatch'
                        else:
                            message = "inCorrectPassword"
                    return JsonResponse({'msg': message})
                else:
                    message = "NotActive"
            else:
                message = 'FailLogin'
                logout(request)
        else:
            return JsonResponse({'msg': 'FailLogin'})
        return JsonResponse({'msg': message})


class ChangeEmail(View):
    def post(self, request):
        if request.session.get('client', None):
            session_user = request.session.get('client', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                client_oop = Client.objects.filter(username=session_user)
                if client_oop.first() and client_oop.first().is_active:
                    email = request.POST.get("email", False)
                    new_email = request.POST.get("new_email", False)
                    list_of_input = [email, new_email]
                    if check_input_is_empty(list_of_input):
                        message = 'isEmpty'
                    else:
                        if client_oop.first().email == email:
                            if email != new_email:
                                if verify_email(new_email):
                                    new_oop = Client.objects.filter(email=new_email).first()
                                    if not new_oop:
                                        client_oop.update(email=new_email)
                                        new_client_oop = Client.objects.filter(email=new_email).first()
                                        if new_client_oop:
                                            status_notification = send_code("notification", email,
                                                                            client_oop.first().first_name,
                                                                            client_oop.first().last_name,
                                                                            new_email)
                                            if status_notification:
                                                status_random = send_code("random", new_client_oop,
                                                                          new_client_oop.first_name,
                                                                          new_client_oop.last_name, "")
                                                if status_random:
                                                    message = 'Done'
                                                    Client.objects.filter(email=new_email).update(is_active=False)
                                                else:
                                                    message = 'try_again'
                                            else:
                                                message = 'try_again'
                                        else:
                                            message = 'Fail'
                                    else:
                                        message = 'isExist'
                                else:
                                    message = "EmailContextError"
                            else:
                                message = "NoAnyChange"
                        else:
                            message = "inCorrectEmail"
                else:
                    message = "NotActive"
            else:
                message = 'FailLogin'
                logout(request)
        else:
            return JsonResponse({'msg': 'FailLogin'})
        return JsonResponse({'msg': message})


# Users


class VerifyPassword(View):
    def post(self, request):
        if not request.session.get('manage', False) and not request.session.get('client', False):
            email = request.POST.get("email_form", False)
            password = request.POST.get("password_form", False)
            re_password = request.POST.get("re_password_form", False)
            list_of_input = [email, password, re_password]
            if check_input_is_empty(list_of_input):
                return JsonResponse({'msg': 'isEmpty'})
            client_oop = Client.objects.filter(email=email)
            if client_oop.first():
                message = 'isExist'
            else:
                if verify_email(email):
                    if str(password) == str(re_password):
                        if verify_password(password):
                            return JsonResponse({'msg': 'isDone', 'valid_email': email, 'valid_password': password})
                        else:
                            message = "PasswordContextError"
                    else:
                        message = 'isNotMatch'
                else:
                    message = "EmailContextError"
        else:
            message = "isContextError"
        return JsonResponse({'msg': message})


class CreateAccount(View):
    def post(self, request):
        if not request.session.get('manage', False) and not request.session.get('client', False):
            email = request.POST.get("valid_email", False)
            password = request.POST.get("valid_password", False)
            name1 = request.POST.get("name1", False)
            name2 = request.POST.get("name2", False)
            name3 = request.POST.get("name3", False)
            name4 = request.POST.get("name4", False)
            gender = request.POST.get("gender", False)
            category = request.POST.get("category", False)
            phone = request.POST.get("phone", False)
            identity = request.POST.get("identity", False)
            list_of_input = [email, password, name1, name2, name3, name4, category, phone, identity]
            if check_input_is_empty(list_of_input):
                return JsonResponse({'msg': 'isEmpty'})
            if gender != "1" and gender != "2":
                return JsonResponse({'msg': 'GenderContextError'})
            client_oop = Client.objects.filter(email=email)
            if client_oop.first():
                return JsonResponse({'msg': 'isExist'})
            if not verify_email(email):
                return JsonResponse({'msg': 'EmailContextError'})
            if not verify_password(password):
                return JsonResponse({'msg': 'PasswordContextError'})
            if not phone.isnumeric() or len(phone) != 10:
                return JsonResponse({'msg': 'PhoneContextError'})
            if not identity.isnumeric() or len(identity) != 9:
                return JsonResponse({'msg': 'IdentityContextError'})
            if not check_input_is_alpha([name1, name2, name2, name4]):
                return JsonResponse({'msg': 'NameContextError'})
            if category == 'default':
                if not Category.objects.filter(identity=category).first():
                    Category(title='الفئة الافتراضية', identity=category).save()
            category_oop = Category.objects.filter(identity=category).first()
            if not category_oop:
                return JsonResponse({'msg': 'CategoryContextError'})
            all_client = Client.objects.all()
            if all_client.first():
                last_id = all_client.latest('id').id
                client_old = Client.objects.filter(pk=last_id).first()
                new_id = client_old.username[5:]
                chart = client_old.username[0]
                client_num = client_old.username[5:]
                if client_num == "99999":
                    ascii_code = ord(chart)
                    new_id = 0
                    if 65 <= ascii_code < 90 or 97 <= ascii_code < 122:
                        chart = chr(ascii_code + 1)
                    else:
                        chart = "a"
            else:
                new_id = 0
                chart = "A"
            year = str(datetime.date.today().year)
            generate = chart + year
            generate += "{:0>5s}".format(str(int(new_id) + 1))
            while True:
                if Client.objects.filter(username=generate).first():
                    id_last_user = generate[5:]
                    if id_last_user != "99999":
                        generate = generate[:5] + "{:0>5s}".format(str(int(id_last_user) + 1))
                    else:
                        year_last_user = str(int(generate[1:5]) + 1)
                        chart_last_user = generate[:1]
                        generate = chart_last_user + year_last_user + id_last_user
                else:
                    break
            Client(email=email, password=password, category=category_oop, first_name=name1,
                   father_name=name2, grand_name=name3, last_name=name4, gender=gender,
                   mobile=phone, identity=identity, username=generate).save()
            client_oop = Client.objects.filter(email=email).first()
            if client_oop:
                request_status = send_code("random", client_oop, name1, name4, '')
                if request_status:
                    return JsonResponse({'msg': 'isDone', 'url': reverse('Client:LoginClient')})
                else:
                    client_oop = Client.objects.filter(email=email).first()
                    if client_oop:
                        client_oop.delete()
                    message = 'try_again'
            else:
                message = 'isFail'
        else:
            message = "FailLogin"
        return JsonResponse({'msg': message})


def send_code(status, client_oop, first_name, last_name, new_email):
    try:
        if status == 'random':
            get_random = get_random_string(length=6, allowed_chars='1234567890')
            verify_email_oop = VerifyEmail.objects.filter(client=client_oop)
            if not verify_email_oop.first():
                VerifyEmail(client=client_oop).save()
                verify_email_oop = VerifyEmail.objects.filter(client=client_oop)
            verify_email_oop.update(random_number=get_random)
            context = {
                'username': str(first_name) + " " + str(last_name),
                'random': get_random,
                'email': client_oop.email,
            }
            html_message = loader.render_to_string("Message/verify_email.html", context)
            title = "التحقق من صحة البريد الإلكتروني"
            send_mail(title, '', '', [client_oop.email], fail_silently=False, html_message=html_message)
        elif status == "notification":
            context = {
                'username': str(first_name) + " " + str(last_name),
                'email': client_oop,
                'new_email': new_email
            }
            html_message = loader.render_to_string("Message/change_email.html", context)
            title = "إشعار بتغيير البريد الإلكتروني"
            send_mail(title, '', '', [client_oop], fail_silently=False, html_message=html_message)
        elif status == "password":
            context = {
                'username': str(first_name) + " " + str(last_name),
                'email': client_oop.email,
            }
            html_message = loader.render_to_string("Message/change_password.html", context)
            title = 'إشعار بتغيير كلمة المرور'
            send_mail(title, '', '', [client_oop.email], fail_silently=False, html_message=html_message)
        return True
    except:
        return False


def verify_email(email):
    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
    return re.match(regex, email) is not None


def verify_password(password):
    flag = 0
    if len(password) >= 8:
        flag += 1
    if re.search("(?=(?:[^a-zA-Z\u0627-\u064a]*[a-zA-Z\u0627-\u064a]){2})", password):
        flag += 1
    if re.search('[ !@#$%^&*()_+\-=\[\]{}:\\|,.\/?0-9]', password):
        flag += 1
    return flag == 3


def check_input_is_empty(list_of_input):
    """
    :param list_of_input: list
    :return: True if any input is empty
    """
    for index in list_of_input:
        if index:
            index = str(index).strip()
            if not index:
                return True
        else:
            return True
    return False


def check_input_is_alpha(list_of_input):
    """
    :param list_of_input: list
    :return: True if all input is alpha
    """
    for index in list_of_input:
        index = str(index).strip()
        if index.count(" ") > 0:
            index = index.replace(" ", "space")
        if not index.isalpha():
            return False
    return True
