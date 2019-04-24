from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View
from Exam.models import Exam, SettingsExam
from Category.models import Category
from Client.models import UserAgents
from django.http import JsonResponse
from datetime import datetime
from django.core.urlresolvers import reverse


class ViewExams(View):
    def get(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                all_exam = SettingsExam.objects.all()
                all_category = Category.objects.all()
                context = {
                    'title': 'الاختبارات',
                    'all_Exam': all_exam,
                    'all_category': all_category,
                    'logout_user': session_user,
                    'admin_is_manager': request.session.get('is_manager', False),
                    'session_user': session_user.split('_')[0],
                }
                return render(request, 'Dashboard/SettingsExam/view_exam.html', context)
        return HttpResponseRedirect(reverse('Dashboard:login'))


class AddExam(View):
    def get(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                all_exam = SettingsExam.objects.all()
                all_category = Category.objects.all()
                context = {
                    'title': 'أضف اختبار جديد',
                    'all_Exam': all_exam,
                    'all_category': all_category,
                    'logout_user': session_user,
                    'admin_is_manager': request.session.get('is_manager', False),
                    'session_user': session_user.split('_')[0],
                }
                return render(request, 'Dashboard/SettingsExam/add_exam.html', context)
        return HttpResponseRedirect(reverse('Dashboard:login'))
