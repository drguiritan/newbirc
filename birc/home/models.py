
# from wagtail.admin.panels import FieldPanel


# from wagtail.images.models import Image
# from wagtail.admin.panels import FieldPanel, ImageChooserPanel
# from wagtail.models import BaseSetting, register_setting


from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField

from wagtail.admin.panels import FieldPanel,MultiFieldPanel,PageChooserPanel,InlinePanel
from wagtail.images.models import Image
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting
from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

#The Master Page
class HomePage(Page):
    class Meta:
        verbose_name = "BIRC CONTENT MENU"



# URE Master Page
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
        verbose_name = "Creating pages for URE only"


# URE Child Page
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


#site wide Master Page
class SiteWidePage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="preferred size 190x214"
    )
    short_description = RichTextField(blank=True)
    content = RichTextField(blank=True)  # main content for the page

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("short_description"),
        FieldPanel("content"),
    ]

    subpage_types = ['SiteWideArticlePage']  # No child pages allowed, or list allowed page types

    class Meta:
        verbose_name = "Creating pages for other purpose"

#site wide Child Pages
class SiteWideArticlePage(Page):
    cover_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    short_description = RichTextField(blank=True)
    content = RichTextField(blank=True)
    extra_field = RichTextField(blank=True)  # e.g., Author, Category, Date

    content_panels = Page.content_panels + [
        FieldPanel("cover_image"),
        FieldPanel("short_description"),
        FieldPanel("content"),
        FieldPanel("extra_field"),
    ]

    parent_page_types = ["SiteWidePage"]  # can only be added under SiteWidePage
    subpage_types = []  # cannot have child pages

    class Meta:
        verbose_name = "Site-wide Article Page"




# Partner model linked to SiteConfiguration
class Partner(models.Model):
    site_config = ParentalKey(   #the parental
        'home.SiteConfiguration', # Link to the settings model
        on_delete=models.CASCADE,
        related_name='partners'
    )
    title = models.CharField(max_length=255, blank=True)
    page = models.ForeignKey(Page, null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    logo = models.ForeignKey(Image, null=True, blank=True, on_delete=models.SET_NULL, related_name='+')

    panels = [
        FieldPanel("title"),
        PageChooserPanel("page"),
        FieldPanel("logo"),
    ]

    def __str__(self):
        return self.title or "Partner"
 
    

@register_setting
class SiteConfiguration(ClusterableModel,BaseSiteSetting):

    site_name = models.CharField(max_length=255, default="FSUU BIRC")
    phone_number = models.CharField(max_length=50, default="+91 123 654 7898")
    address = models.TextField(default="San. Francisco St. Butuan City, Philippines")
    email = models.EmailField(default="biodiversity@urios.edu.ph")

    site_description = RichTextField(
        blank=True,
        verbose_name="About the site",
        default="",
        features=['bold', 'italic', 'link', 'image', 'h2', 'h3', 'ol', 'ul'],  # Enable images
    )

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("site_name"),
                FieldPanel("phone_number"),
                FieldPanel("address"),
                FieldPanel("email"),
                FieldPanel("site_description"),
            
            ],
            heading="Site wide configuration"
        ),
         InlinePanel("partners", label="BIRC Partner"), # Works because of ParentalKey
    ]

    class Meta:
        verbose_name = "Site Configuration"