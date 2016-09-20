from django import forms
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.test.client import Client

from formfactory import actions, models, validators


def load_fixtures(kls):
    kls.form_data = {
        "title": "Form 1",
        "slug": "form-1"
    }
    kls.form = models.Form.objects.create(**kls.form_data)

    for count, field_type in enumerate(models.FIELD_TYPES):
        setattr(kls, "formfield_data_%s" % count, {
            "title": "Form Field %s" % count,
            "slug": "form-field-%s" % count,
            "position": count,
            "form": kls.form,
            "field_type": field_type,
            "label": "Form Field %s" % count,
        })
        setattr(kls, "formfield_%s" % count, models.FormField.objects.create(
            **getattr(kls, "formfield_data_%s" % count)
        ))


class TestValidatorIncomplete(validators.BaseValidator):
    pass


class TestActionIncomplete(actions.BaseAction):
    pass


class TestValidator(validators.BaseValidator):
    validation_message = "%(value) is not divible by 2"

    def condition(self, value):
        return not value % 2


class TestAction(actions.BaseAction):
    def run(self, form_data):
        return True


class ValidatorTestCase(TestCase):
    def setUp(self):
        self.validator = TestValidator()
        self.incomplete_validator = TestValidatorIncomplete()

    def test_registry(self):
        validators.register(self.validator)

        # ensure the class is registered as expected
        self.assertIn(self.validator, validators.get_registered_validators())

    def test_unregistry(self):
        validators.register(self.validator)

        # ensure the class is registered as expected
        self.assertIn(self.validator, validators.get_registered_validators())

        validators.unregister(self.validator)

        # ensure the class is unregistered as expected
        self.assertNotIn(
            self.validator, validators.get_registered_validators()
        )

    def test_validation(self):

        # ensure an excpetion is raised if the validation class is not complete
        self.assertRaises(
            NotImplementedError, self.incomplete_validator.validate, None
        )

        # ensure that the validate method returns correctly
        self.assertTrue(self.validator.validate(4))


class ActionTestCase(TestCase):
    def setUp(self):
        self.action = TestAction()
        self.incomplete_action = TestActionIncomplete()

    def test_registry(self):
        actions.register(self.action)

        # ensure the class is registered as expected
        self.assertIn(self.action, actions.get_registered_actions())

    def test_unregistry(self):
        actions.register(self.action)

        # ensure the class is registered as expected
        self.assertIn(self.action, actions.get_registered_actions())

        actions.unregister(self.action)

        # ensure the class is unregistered as expected
        self.assertNotIn(self.action, actions.get_registered_actions())

    def test_action(self):

        # ensure an excpetion is raised if the validation class is not complete
        self.assertRaises(
            NotImplementedError, self.incomplete_action.run, None
        )

        # ensure that the run method returns correctly
        self.assertTrue(self.action.run({}))


class ModelTestCase(TestCase):
    def setUp(self):
        load_fixtures(self)

    def test_field_constant(self):

        # ensure the field types are populated
        self.assertIn(("DateTimeField", "DateTimeField"), models.FIELD_TYPES)
        self.assertIn(("BooleanField", "BooleanField"), models.FIELD_TYPES)
        self.assertIn(("CharField", "CharField"), models.FIELD_TYPES)

    def test_form(self):

        # ensure the form model has been saved correctly
        for key, value in self.form_data.items():
            self.assertEqual(getattr(self.form, key), value)

        # ensure all form fields were saved
        self.assertEqual(self.form.fields.count(), len(models.FIELD_TYPES))

        # ensure the form object is returned
        self.assertIsInstance(self.form.as_form(), forms.Form)

    def test_formfield(self):

        # ensure the form model has been saved correctly
        for count in range(len(models.FIELD_TYPES)):
            formfield_data = getattr(self, "formfield_data_%s" % count)
            for key, value in formfield_data.items():
                formfield = getattr(self, "formfield_%s" % count)
                self.assertEqual(getattr(formfield, key), value)


class AdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.editor = get_user_model().objects.create(
            username="editor",
            email="editor@test.com",
            is_superuser=True,
            is_staff=True
        )
        self.editor.set_password("password")
        self.editor.save()
        self.client.login(username="editor", password="password")

    def test_admin(self):
        response = self.client.get("/admin/")
        self.assertEqual(response.status_code, 200)

        response = self.client.get("/admin/formfactory/")
        self.assertEqual(response.status_code, 200)

    def test_admin_form(self):
        response = self.client.get("/admin/formfactory/form/add/")
        self.assertEqual(response.status_code, 200)

    def test_admin_fieldoption(self):
        response = self.client.get("/admin/formfactory/fieldchoice/add/")
        self.assertEqual(response.status_code, 200)


class ViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        load_fixtures(self)

    def test_detail(self):
        pass

    def test_list(self):
        pass

    def tearDown(self):
        pass
