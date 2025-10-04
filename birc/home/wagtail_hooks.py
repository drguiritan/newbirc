from wagtail import hooks
from django.utils.html import format_html
from django.templatetags.static import static


# Add custom CSS
@hooks.register("insert_global_admin_css")
def global_admin_css():
    return format_html(
        '<link rel="stylesheet" href="{}">', static("css/admin_custom.css")
    )

@hooks.register("construct_help_menu")
def remove_help_menu(request, menu_items):
    # Clear out all help menu items
    menu_items.clear()

@hooks.register("construct_reports_menu")
def remove_reports_menu(request, menu_items):
    # Clear out all reports menu items
    menu_items.clear()



@hooks.register("construct_settings_menu")
def remove_redirects_from_settings_menu(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != "redirects"]


@hooks.register("construct_page_action_menu")
def disable_root_actions(menu_items, request, context):
    page = context.get("page")
    if page and page.is_root():
        # Remove all root actions (Add, Edit, Delete, etc.)
        menu_items.clear()

@hooks.register("get_available_page_types")
def restrict_root_add_page_types(parent_page, request):
    # The "Root" page has id=1 and is the invisible container above your homepage
    if parent_page.is_root():
        return []  # No page types allowed at Root    