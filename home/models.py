from django.db import models
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import InlinePanel, FieldPanel, MultiFieldPanel, FieldRowPanel
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page



class HomePage(Page):
    pass

class FormPage(AbstractEmailForm):
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('custom_form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Notification Config"),
    ]

    def get_form_fields(self):
        return self.custom_form_fields.all()

class FormField(AbstractFormField):
    page = ParentalKey('FormPage', related_name='custom_form_fields')

