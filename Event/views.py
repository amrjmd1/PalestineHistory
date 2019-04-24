from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View
from Event.models import Event
from Category.models import Category
from django.http import JsonResponse
from Client.models import UserAgents
from django.core.urlresolvers import reverse
from django.utils import timezone
import datetime


class ViewAddEvent(View):
    def get(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                all_category = Category.objects.all()
                context = {
                    'title': 'إضافة حدث',
                    'all_category': all_category,
                    'logout_user': session_user,
                    'admin_is_manager': request.session.get('is_manager', False),
                    'session_user': session_user.split('_')[0],
                }
                return render(request, 'Dashboard/Event/addEvent.html', context)


class ViewEvent(View):
    def get(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                all_event = Event.objects.all()
                all_category = Category.objects.all()
                context = {
                    'title': 'الأحداث',
                    'all_event': all_event,
                    'all_category': all_category,
                    'logout_user': session_user,
                    'admin_is_manager': request.session.get('is_manager', False),
                    'session_user': session_user.split('_')[0],
                }
                return render(request, 'Dashboard/Event/view_event.html', context)
        return HttpResponseRedirect(reverse('Dashboard:login'))


class AddEvent(View):
    def post(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                title_event = request.POST.get("title_event")
                start_date = request.POST.get("start_date")
                end_date = request.POST.get("end_date")
                description = request.POST.get("description")
                category_identity = request.POST.get("category_identity")
                if title_event != "" and start_date != "" and end_date != "" and category_identity != "":
                    if category_identity == "0":
                        category_oop = Category.objects.all()
                    else:
                        category_oop = Category.objects.filter(identity=category_identity)
                        if not category_oop.first():
                            return JsonResponse({'status': 'NotFoundCategory'})
                    event_oop = Event.objects.filter(title=title_event).first()
                    if not event_oop:
                        for category in category_oop:
                            all_event = Event.objects.all()
                            if all_event.first():
                                last_event = Event.objects.latest('id').id
                            else:
                                last_event = 0
                            year = str(datetime.date.today().year)
                            chart = str(chr((last_event % 26) + 65))
                            id_event = chart + year
                            if Event.objects.filter(identity=id_event).first():
                                id_event = id_event.lower()
                            start_date = timezone.make_aware(datetime.datetime.strptime(start_date, "%m/%d/%Y"))
                            end_date = timezone.make_aware(datetime.datetime.strptime(end_date, "%m/%d/%Y"))
                            Event(title=title_event, start_date=start_date, end_date=end_date, description=description,
                                  identity=id_event, category=category).save()
                        event_oop = Event.objects.filter(title=title_event).first()
                        if event_oop:
                            message = "Done"
                        else:
                            message = "Fail"
                    else:
                        message = "AlreadyExists"
                else:
                    message = "Empty"
                return JsonResponse({'status': message})
        return HttpResponseRedirect(reverse('Dashboard:login'))


class EditEvent(View):
    def post(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                event_id = request.POST.get("id")
                event_title = request.POST.get("title")
                event_oop = Event.objects.filter(pk=event_id)
                if not event_oop.first():
                    message = "NotExists"
                else:
                    event_oop.update(title=event_title)
                    event_oop = Event.objects.filter(pk=event_id).first()
                    if event_oop.title == event_title:
                        message = 'Done'
                    else:
                        message = 'Fail'
                return JsonResponse({'status': message})
        return HttpResponseRedirect(reverse('Dashboard:login'))


class RemoveEvent(View):
    def post(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                event_id = request.POST.get("id")
                event_oop = Event.objects.filter(pk=event_id)
                if not event_oop.first():
                    message = "NotExists"
                else:
                    event_oop.delete()
                    event_oop = Event.objects.filter(pk=event_id)
                    if not event_oop.first():
                        message = 'Done'
                    else:
                        message = 'Fail'
                return JsonResponse({'status': message})
        return HttpResponseRedirect(reverse('Dashboard:login'))
