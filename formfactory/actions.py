from formfactory import _registry
from formfactory.models import FormData, FormDataItem
from formfactory.utils import clean_key


def register(func):
    key = clean_key(func)
    _registry["actions"][key] = func

    def wrapper(*args):
        return func(*args)
    return wrapper


def unregister(func):
    key = clean_key(func)
    if key in _registry["actions"]:
        del _registry["actions"][key]


def get_registered_actions():
    return _registry["actions"]


@register
def store_data(form_instance):
    cleaned_data = form_instance.cleaned_data
    form_data = FormData.objects.create(
        uuid=cleaned_data.pop("uuid"),
        form_id=cleaned_data.pop("form_id"),
    )
    for key, value in cleaned_data.items():
        FormDataItem.objects.create(
            form_data=form_data,
            form_field_id=form_instance.fields[key].field_pk,
            value=value
        )


@register
def send_email(form_instance):
    cleaned_data = form_instance.cleaned_data
    form_data = FormData.objects.create(
        uuid=cleaned_data.pop("uuid"),
        form_id=cleaned_data.pop("form_id"),
    )
    for key, value in cleaned_data.items():
        FormDataItem.objects.create(
            form_data=form_data,
            form_field_id=form_instance.fields[key].field_pk,
            value=value
        )
