from wagtail.admin.panels import FieldPanel


class FileUploadPanel(FieldPanel):
    """
    Custom panel for file upload fields that only exist in the form.
    """
    def __init__(self, field_name, **kwargs):
        # Don't require the field to exist on the model
        super().__init__(field_name, **kwargs)
    
    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        return kwargs
    
    class BoundPanel(FieldPanel.BoundPanel):
        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            # The field comes from the form, not the model
            self.form_field_name = self.panel.field_name