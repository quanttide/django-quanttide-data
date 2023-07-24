from django.test import SimpleTestCase, override_settings
from django.apps import apps


@override_settings(INSTALLED_APPS=['django_package.apps.DjangoPackageConfig'])
class AppConfigTestCase(SimpleTestCase):
    def test_install_app(self):
        self.assertTrue(apps.is_installed('django_package'))
        app_config = apps.get_app_config('django_package')
        self.assertEqual('django_package', app_config.name)
