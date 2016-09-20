import inspect

from django import forms
from django.db import models

from formfactory import _registery


FIELD_CLASSES = [
    getattr(forms.fields, field) for field in dir(forms.fields)
    if inspect.isclass(getattr(forms.fields, field))
]

FIELD_TYPES = tuple(
    (field.__name__, field.__name__) for field in FIELD_CLASSES
    if issubclass(field, forms.fields.Field)
)

ADDITIONAL_VALIDATORS = tuple(
    (validator.__name__, validator.__name__)
    for validator in _registery.get("validators", [])
)

FORM_ACTIONS = tuple(
    (action.__name__, action.__name__)
    for action in _registery.get("actions", [])
)


class FormFactory(forms.Form):
    def __init__(self, *args, **kwargs):
        self.fields = kwargs.pop("fields")
        super(FormFactory, self).__init__(*args, **kwargs)

        for field in self.fields:
            field_type = getattr(forms, field.field_type)
            self.fields[field.slug] = field_type(
                label=field.label,
                initial=field.initial,
                required=field.required,
                disable=field.disable
            )


class Form(models.Model):
    title = models.CharField(
        max_length=256, help_text="A short descriptive title."
    )
    slug = models.SlugField(
        max_length=256, db_index=True, unique=True
    )
    action = models.CharField(
        choices=FORM_ACTIONS, max_length=128
    )

    class Meta:
        ordering = ["title"]

    def __unicode__(self):
        return self.title

    def as_form(self):
        return FormFactory(fields=self.fields.all())


class FieldChoice(models.Model):
    label = models.CharField(max_length=128)
    value = models.CharField(max_length=128)

    class Meta:
        ordering = ["label"]

    def __unicode__(self):
        return "%s:%s" % (self.label, self.value)


class FormField(models.Model):
    title = models.CharField(
        max_length=256,
        help_text="A short descriptive title."
    )
    slug = models.SlugField(
        max_length=256, db_index=True, unique=True
    )
    position = models.PositiveIntegerField(default=0)

    form = models.ForeignKey(Form, related_name="fields")

    field_type = models.CharField(choices=FIELD_TYPES, max_length=128)
    label = models.CharField(max_length=64)
    initial = models.TextField(blank=True, null=True)
    label = models.CharField(max_length=64)
    required = models.BooleanField(default=True)
    disabled = models.BooleanField(default=False)
    choices = models.ManyToManyField(FieldChoice)
    additional_validators = models.CharField(
        choices=ADDITIONAL_VALIDATORS, max_length=128, blank=True, null=True
    )

    class Meta:
        ordering = ["position"]

    def __unicode__(self):
        return self.title
