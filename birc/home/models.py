
# from wagtail.admin.panels import FieldPanel


# from wagtail.images.models import Image
# from wagtail.admin.panels import FieldPanel, ImageChooserPanel
# from wagtail.models import BaseSetting, register_setting


from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField

from wagtail.admin.panels import FieldPanel,MultiFieldPanel,PageChooserPanel
from wagtail.images.models import Image
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting

class HomePage(Page):
    class Meta:
        verbose_name = "BIRC CONTENT MENU"



# Master Page
class StudentResearchPage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    short_description = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("short_description"),
    ]

    subpage_types = ["ResearchArticlePage"]

    class Meta:
        verbose_name = "Creating content page for URE"


# Child Page
class ResearchArticlePage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    short_description = RichTextField(blank=True)
    content = RichTextField(blank=True)
    extra_field = RichTextField(blank=True)  # e.g. Adviser, Year, Category

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("short_description"),
        FieldPanel("content"),
        FieldPanel("extra_field"),
    ]

    parent_page_types = ["StudentResearchPage"]
    subpage_types = []




@register_setting
class SiteConfiguration(BaseSiteSetting):

    site_name = models.CharField(max_length=255, default="FSUU BIRC")
    phone_number = models.CharField(max_length=50, default="+91 123 654 7898")
    address = models.TextField(default="San. Francisco St. Butuan City, Philippines")
    email = models.EmailField(default="biodiversity@urios.edu.ph")

    partner1_title = models.CharField(max_length=255, blank=True)
    partner1_page = models.ForeignKey(
            Page,
            null=True,
            blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
        )
    partner1_logo = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    partner2_title = models.CharField(max_length=255, blank=True)
    partner2_page = models.ForeignKey(
                    Page,
                    null=True,
                    blank=True,
                    on_delete=models.SET_NULL,
                    related_name='+'
                )
    partner2_logo = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("site_name"),
                FieldPanel("phone_number"),
                FieldPanel("address"),
                FieldPanel("email"),
                FieldPanel("partner1_title"),
                PageChooserPanel("partner1_page"),
                FieldPanel("partner1_logo"),  # Use FieldPanel for images in Wagtail 7
                FieldPanel("partner2_title"),
                PageChooserPanel("partner2_page"),
                FieldPanel("partner2_logo"),  # Use FieldPanel for images in Wagtail 7
            ],
            heading="Site wide configuration"
        ),
    ]

    class Meta:
        verbose_name = "Site Configuration"