from wagtail import hooks
from django.utils.html import format_html
from django.templatetags.static import static

from django.db import transaction
import json

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
    

@hooks.register('after_edit_page')
def import_species_data_after_edit(request, page):
    """Import species data after page is edited."""
    from .models import SpeciesDataTable, SpeciesDataRow
    
    if isinstance(page, SpeciesDataTable):
        print(f"DEBUG HOOK: after_edit_page called for {page}")
        
        # Check if files were uploaded
        columns_file = request.FILES.get('columns_file')
        rows_file = request.FILES.get('rows_file')
        
        print(f"DEBUG HOOK: columns_file={columns_file}, rows_file={rows_file}")
        
        if columns_file and rows_file:
            print(f"DEBUG HOOK: Processing files...")
            
            # Read columns
            columns_file.seek(0)
            columns_data = json.loads(columns_file.read())
            page.columns = columns_data
            
            # Read rows
            rows_file.seek(0)
            rows_data = json.loads(rows_file.read())
            
            print(f"DEBUG HOOK: Got {len(columns_data)} columns and {len(rows_data)} rows")
            
            with transaction.atomic():
                # Save columns
                page.save(update_fields=['columns'])
                print(f"DEBUG HOOK: Saved columns")
                
                # Delete old rows
                deleted = page.rows.all().delete()
                print(f"DEBUG HOOK: Deleted {deleted[0]} old rows")
                
                # Create new rows
                rows_to_create = [
                    SpeciesDataRow(page=page, cells=row_cells)
                    for row_cells in rows_data
                ]
                
                SpeciesDataRow.objects.bulk_create(rows_to_create)
                print(f"DEBUG HOOK: Created {len(rows_to_create)} new rows")
                
                # Verify
                final_count = page.rows.count()
                print(f"DEBUG HOOK: Final row count: {final_count}")


@hooks.register('after_create_page')
def import_species_data_after_create(request, page):
    """Import species data after page is created."""
    from .models import SpeciesDataTable, SpeciesDataRow
    
    if isinstance(page, SpeciesDataTable):
        print(f"DEBUG HOOK: after_create_page called for {page}")
        
        # Check if files were uploaded
        columns_file = request.FILES.get('columns_file')
        rows_file = request.FILES.get('rows_file')
        
        print(f"DEBUG HOOK: columns_file={columns_file}, rows_file={rows_file}")
        
        if columns_file and rows_file:
            print(f"DEBUG HOOK: Processing files...")
            
            # Read columns
            columns_file.seek(0)
            columns_data = json.loads(columns_file.read())
            page.columns = columns_data
            
            # Read rows
            rows_file.seek(0)
            rows_data = json.loads(rows_file.read())
            
            print(f"DEBUG HOOK: Got {len(columns_data)} columns and {len(rows_data)} rows")
            
            with transaction.atomic():
                # Save columns
                page.save(update_fields=['columns'])
                print(f"DEBUG HOOK: Saved columns")
                
                # Create new rows
                rows_to_create = [
                    SpeciesDataRow(page=page, cells=row_cells)
                    for row_cells in rows_data
                ]
                
                SpeciesDataRow.objects.bulk_create(rows_to_create)
                print(f"DEBUG HOOK: Created {len(rows_to_create)} new rows")
                
                # Verify
                final_count = page.rows.count()
                print(f"DEBUG HOOK: Final row count: {final_count}")    