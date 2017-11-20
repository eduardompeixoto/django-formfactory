import django
from django.forms.widgets import Widget
from django.utils.html import format_html

# TODO Add django 19 and 110 render support
class ParagraphWidget(Widget):
    template_name = "formfactory/forms/widgets/paragraph.html"

    def render(self, *args, **kwargs):

        # Add a basic check for Django 2. No tests yet.
        if django.VERSION[1] >= 11 or django.VERSION[0] > 1:
            return super(ParagraphWidget, self).render(*args, **kwargs)
        else:
            return format_html(self.attrs["paragraph"])
