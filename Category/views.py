from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View
from Category.models import Category
from django.http import JsonResponse
from Questions.models import Question
from Client.models import UserAgents
from django.core.urlresolvers import reverse


class ViewCategories(View):
    def get(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                all_category = Category.objects.all()
                context = {
                    'title': 'الفئات',
                    'all_category': all_category,
                    'logout_user': session_user,
                    'admin_is_manager': request.session.get('is_manager', False),
                    'session_user': session_user.split('_')[0],
                }
                if not all_category.first():
                    context['all_category'] = False
                return render(self.request, 'Dashboard/Category/view_categories.html', context)
        return HttpResponseRedirect(reverse('Dashboard:login'))


class ViewCategory(View):
    def get(self, request, category_id):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                category_oop = Category.objects.filter(pk=category_id)
                if category_oop.first():
                    context = {
                        'title': str(category_oop.first().title),
                        'category_oop': category_oop,
                        'logout_user': session_user,
                        'admin_is_manager': request.session.get('is_manager', False),
                        'session_user': session_user.split('_')[0],
                    }
                    return render(self.request, 'Dashboard/Category/view_category.html', context)
                else:
                    return HttpResponseRedirect(reverse('Dashboard:Category:ViewCategories'))
        return HttpResponseRedirect(reverse('Dashboard:login'))


class QuestionCategory(View):
    def get(self, request, category_id):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                category_oop = Category.objects.filter(pk=category_id).first()
                if category_oop:
                    all_question = Question.objects.filter(category=category_oop)
                    context = {
                        'title': 'بنك الأسئلة',
                        'questions': all_question,
                        'logout_user': session_user,
                        'admin_is_manager': request.session.get('is_manager', False),
                        'session_user': session_user.split('_')[0],
                    }
                    return render(self.request, 'Dashboard/Category/view_question_category.html', context)
                else:
                    return HttpResponseRedirect(reverse('Dashboard:Category:ViewCategories'))
        return HttpResponseRedirect(reverse('Dashboard:login'))


class AddCategory(View):
    def get(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                all_category = Category.objects.all()
                context = {
                    'title': 'أضف فئة جديدة',
                    'all_category': all_category,
                    'logout_user': session_user,
                    'admin_is_manager': request.session.get('is_manager', False),
                    'session_user': session_user.split('_')[0],
                }
                return render(request, 'Dashboard/Category/add_category.html', context)
        return HttpResponseRedirect(reverse('Dashboard:login'))


class AddCategoryAjax(View):
    def post(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                title_category = request.POST.get("title_category")
                category_description = request.POST.get("category_description")
                if title_category != "":
                    category_oop = Category.objects.filter(title=title_category).first()
                    if not category_oop:
                        if len(Category.objects.all()) > 0:
                            last_category = Category.objects.latest('id').id
                        else:
                            last_category = 0
                        id_category = str(chr(last_category + 65)) + "2018"
                        Category(title=title_category, identity=id_category, description=category_description).save()
                        category_oop = Category.objects.filter(title=title_category).first()
                        if category_oop:
                            message = "Done"
                        else:
                            message = "Fail"
                    else:
                        message = "AlreadyExists"
                else:
                    message = "Empty"
                return JsonResponse({'status': message})
        return HttpResponseRedirect(reverse('Dashboard:login'))


class EditCategory(View):
    def post(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                category_id = request.POST.get("id")
                category_title = request.POST.get("title")
                category_description = request.POST.get("description")
                category_oop = Category.objects.filter(pk=category_id)
                if not category_oop.first():
                    message = "NotExists"
                else:
                    category_oop.update(title=category_title, description=category_description)
                    category_oop = Category.objects.filter(pk=category_id).first()
                    if category_oop.title == category_title and category_oop.description == category_description:
                        message = 'Done'
                    else:
                        message = 'Fail'
                return JsonResponse({'status': message})
        return HttpResponseRedirect(reverse('Dashboard:login'))


class RemoveCategory(View):
    def post(self, request):
        if request.session.get('manage', None):
            session_user = request.session.get('manage', None)
            user_agent_oop = UserAgents.objects.filter(user=session_user).latest('id')
            if not user_agent_oop.logout:
                category_id = request.POST.get("id")
                category_oop = Category.objects.filter(pk=category_id)
                if not category_oop.first():
                    message = "NotExists"
                else:
                    category_oop.delete()
                    category_oop = Category.objects.filter(pk=category_id)
                    if not category_oop.first():
                        message = 'Done'
                    else:
                        message = 'Fail'
                return JsonResponse({'status': message})
        return HttpResponseRedirect(reverse('Dashboard:login'))
