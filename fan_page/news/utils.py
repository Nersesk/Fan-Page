
from .models import *

category = Category.objects.all()
menu = [{'name': 'News','name_url':'Home'},
       {'name': 'Shop','name_url':'shop'},
        {'name': 'About us','name_url':'about'},
       ]



class DataMixin:
    paginate_by = 4
    def get_user_context(self,**kwargs):
        context = kwargs
        context['category'] = category
        context['menu'] = menu
        return context
