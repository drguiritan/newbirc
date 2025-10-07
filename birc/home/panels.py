from django.template.loader import render_to_string
from wagtail.admin.panels import Panel
from django.utils.safestring import mark_safe

class ReadOnlyTablePanel(Panel):
    """
    A custom panel for displaying read-only tabular data in Wagtail admin.
    """
    
    def __init__(self, rows_field, columns_field, heading="Table Data", **kwargs):
        super().__init__(**kwargs)
        self.rows_field = rows_field
        self.columns_field = columns_field
        self.heading = heading
    
    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update(
            rows_field=self.rows_field,
            columns_field=self.columns_field,
            heading=self.heading,
        )
        return kwargs
    
    class BoundPanel(Panel.BoundPanel):
        template_name = "admin/panels/readonly_table_panel.html"
        
        def get_context_data(self, parent_context=None):
            context = super().get_context_data(parent_context)
            
            # Get the instance (page)
            instance = self.instance
            
            # Get columns from the instance
            columns = getattr(instance, self.panel.columns_field, None) or []
            
            # Get rows from the related model
            rows_queryset = getattr(instance, self.panel.rows_field, None)
            rows = []
            
            if rows_queryset and hasattr(rows_queryset, 'all'):
                for row in rows_queryset.all():
                    rows.append(row.cells or [])
            
            context.update({
                'heading': self.panel.heading,
                'columns': columns,
                'rows': rows,
                'has_data': bool(columns and rows),
            })
            
            return context
        

class PageIDPanel(Panel):
    """
    Custom read-only panel to display the Page ID in Wagtail admin.
    Works in content_panels or promote_panels.
    """
    def __init__(self, heading="Page ID", **kwargs):
        super().__init__(**kwargs)
        self.heading = heading

    class BoundPanel(Panel.BoundPanel):
        def render_html(self, parent_context=None):
            instance = self.instance
            page_id = getattr(instance, "id", "Not saved yet")
            
            html = f"""
            <div class="field">                
                <div>
                   <h2> {page_id}</h2>
                </div>
            </div>
            """
            
            return mark_safe(html)


