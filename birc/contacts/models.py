# contacts/models.py
from django.db import models
from django.shortcuts import render
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, FieldRowPanel
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractFormSubmission



class FormField(AbstractFormField):
    """Form field for ContactPage - allows creating fields in Wagtail admin"""
    page = ParentalKey(
        'ContactPage',
        on_delete=models.CASCADE,
        related_name='form_fields',
    )


class ContactPage(AbstractEmailForm):
    """
    Contact form page with built-in spam protection using honeypot technique.
    Compatible with Wagtail 7.x
    """
    
    # Page fields
    intro = RichTextField(
        blank=True,
        help_text="Introduction text that appears above the form"
    )
    thank_you_text = RichTextField(
        blank=True,
        help_text="Text displayed on the thank you page after submission"
    )

    subpage_types = []
    
    # Content panels for Wagtail admin
    content_panels = Page.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro'),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], heading="Email Settings"),
    ]
    
    def serve(self, request, *args, **kwargs):
        """
        Override serve to add honeypot spam protection.
        Wagtail 7 compatible implementation.
        """
        if request.method == 'POST':
            form = self.get_form(
                request.POST,
                request.FILES,
                page=self,
                user=request.user
            )
            
            if form.is_valid():
                # SPAM PROTECTION: Check honeypot field
                if request.POST.get('website', '').strip():
                    # Silently show success page without saving
                    return self.render_landing_page(
                        request,
                        form,
                        None
                    )
                
                form_submission = self.process_form_submission(form)
                
                if self.to_address:
                    self.send_mail(form)
                
                return self.render_landing_page(
                    request,
                    form,
                    form_submission
                )
        else:
            form = self.get_form(page=self, user=request.user)
        
        # Render normal form page
        context = self.get_context(request)
        context['form'] = form
        return render(request, self.get_template(request), context)
    
class ContactFormSubmission(AbstractFormSubmission):
    """Store submissions for ContactPage separately."""
    page = models.ForeignKey('ContactPage', on_delete=models.CASCADE, related_name='custom_submissions')
