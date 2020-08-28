from django.apps import AppConfig
from django.utils.module_loading import autodiscover_modules

class AppsConfig(AppConfig):
    name = 'apps.start_app'
    # print(AppConfig.ready.__doc__)
    # print(AppConfig.ready.__dict__)
    # print(AppConfig.ready.__class__)
    # print(AppConfig.ready.__module__)
    def ready(self):
        print('进入ready方法')
        # autodiscover_modules({'register_to' :'a.py'})