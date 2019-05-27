import os
import requests
import re
import sys

from django.utils.translation import ugettext as _
from django.urls import reverse
from django.http import HttpResponse
from django.conf.urls import url
from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.contrib.modeladmin.helpers import AdminURLHelper, ButtonHelper
from wagtail.contrib.modeladmin.views import IndexView

from .models import Employee


class ImportButtonHelper(ButtonHelper):
    import_button_classnames = ['bicolor', 'icon', 'icon-download']

    def import_button(self, classnames_add=None, classnames_exclude=None):
        if classnames_add is None:
            classnames_add = []
        if classnames_exclude is None:
            classnames_exclude = []

        classnames = self.import_button_classnames + classnames_add
        cn = self.finalise_classname(classnames, classnames_exclude)
        text = _('Import {}'.format(self.verbose_name_plural.title()))

        return {
            'url': self.url_helper.get_action_url('import', query_params=self.request.GET),
            'label': text,
            'classname': cn,
            'title': text
        }


class ImportAdminURLHelper(AdminURLHelper):
    non_object_specific_actions = [
        'create', 'choose_parent', 'index', 'import']

    def get_action_url(self, action, *args, **kwargs):
        query_params = kwargs.pop('query_params', None)

        url_name = self.get_action_url_name(action)
        if action in self.non_object_specific_actions:
            url = reverse(url_name)
        else:
            url = reverse(url_name, args=args, kwargs=kwargs)

        return url

    def get_action_url_pattern(self, action):
        if action in self.non_object_specific_actions:
            return self._get_action_url_pattern(action)

        return self._get_object_specific_action_url_pattern(action)


class ImportView(IndexView):
    def import_employees(self):

        try:
            url = 'http://hub.agenciaego.com.ar/api/v2/employees'

            resp = requests.get(url)
            data = resp.json()

            Employee.objects.all().delete()
            
            sort_order = 1
            for item in data.get('employees'):
                employee = Employee(
                    id=item.get('id'),
                    name=item.get('name'),
                    avatar=item.get('avatar'),
                    position=item.get('title'),
                    subposition=item.get('subtitle'),
                    bio=item.get('description'),
                    type=item.get('type_id'),
                    sort_order=sort_order,
                )
                employee.save()
                sort_order += 1


            messages.add_message(self.request, messages.SUCCESS, _(
                'Employees imported correctly'))
            return redirect('employees_employee_modeladmin_index')

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]

            messages.add_message(self.request, messages.ERROR, '{} on {} on line {}'.format(
                'Exception', fname, exc_tb.tb_lineno))
            return redirect('employees_employee_modeladmin_index')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        super().dispatch(request, *args, **kwargs)
        return self.import_employees()


class ImportModelAdminMixin(object):
    button_helper_class = ImportButtonHelper
    url_helper_class = ImportAdminURLHelper

    import_view_class = ImportView

    def get_admin_urls_for_registration(self):
        urls = super().get_admin_urls_for_registration()
        urls += (
            url(
                self.url_helper.get_action_url_pattern('import'),
                self.import_view,
                name=self.url_helper.get_action_url_name('import')
            ),
        )

        return urls

    def import_view(self, request):
        kwargs = {'model_admin': self}
        view_class = self.import_view_class
        return view_class.as_view(**kwargs)(request)


class EmployeeAdmin(ImportModelAdminMixin, ModelAdmin):
    model = Employee
    menu_label = 'Employees'
    menu_icon = 'user'
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ['name', 'real_position']
    search_fields = ('name',)
    ordering = ['sort_order']

    def real_position(self, obj):
        if obj.type == 1:
            return _('Partner')
        elif obj.type == 2:
            return _('Leader')
        else:
            return _('Employee')

    real_position.short_description = _('Position')


modeladmin_register(EmployeeAdmin)
