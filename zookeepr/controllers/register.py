from zookeepr.lib.base import *

class RegisterController(BaseController):
    def index(self):
        errors, defaults = {}, m.request_args
        if defaults:
            form_result, errors = model.UserInfoSchema().validate(defaults)
            if not errors:
                model.UserInfo(**form_result) # database insert
                return m.subexec('thankyou.myt')
        m.subexec('myform.myt', defaults=defaults, errors=errors)

    def new(self, name):
        m.write("huzzah you are called %s and you registered lol" % name)
