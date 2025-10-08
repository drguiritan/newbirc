# contacts/wagtail_hooks.py
from wagtail import hooks
from wagtail.admin.menu import MenuItem
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


@hooks.register('construct_main_menu')
def hide_default_forms_menu_item(request, menu_items):
    """
    Removes the built-in 'Forms' menu from Wagtail admin sidebar.
    """
    menu_items[:] = [item for item in menu_items if item.name != 'forms']

    
@hooks.register('register_admin_menu_item')
def register_form_submissions_menu_item():
    """Adds a 'Form Submissions' link to the Wagtail admin sidebar."""
    return MenuItem(
        _('Contact Messages'),
        reverse('wagtailforms:index'),
        icon_name='mail',
        order=700,
    )

