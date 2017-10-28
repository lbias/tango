from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.staticfiles import finders


class GeneralTests(TestCase):
    def test_serving_static_files(self):
        # If using static media properly result is not NONE once it finds rango.jpg
        result = finders.find('images/rango.jpg')
        self.assertIsNotNone(result)


class IndexPageTests(TestCase): 
    def test_index_using_template(self):
        # Check the template used to render index page
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'rango/index.html')

    def test_rango_picture_displayed(self):
        # Check if is there an image called 'rango.jpg' on the index page
        response = self.client.get(reverse('index'))
        self.assertIn(b'img src="/static/images/rango.jpg', response.content)
    
    def test_index_has_title(self):
        # Check to make sure that the title tag has been used
        response = self.client.get(reverse('index'))
        self.assertIn(b'<title>', response.content)
        self.assertIn(b'</title>', response.content)


class AboutPageTests(TestCase):    
    def test_about_contain_image(self):
        # Check if is there an image on the about page
        response = self.client.get(reverse('about'))
        self.assertIn(b'img src="/media/', response.content)

    def test_about_using_template(self):
        # Check the template used to render index page
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'rango/about.html')        
        
        
class ModelTests(TestCase):
    def setUp(self):
        try:
            from populate_rango import populate
            populate()
        except ImportError:
            print('The module populate_rango does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')
                
    def get_category(self, name):
        
        from rango.models import Category
        try:                  
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:    
            cat = None
        return cat
        
    def test_python_cat_added(self):
        cat = self.get_category('Python')  
        self.assertIsNotNone(cat)
         
    def test_python_cat_with_views(self):
        cat = self.get_category('Python')
        self.assertEquals(cat.views, 128)
        
    def test_python_cat_with_likes(self):
        cat = self.get_category('Python')
        self.assertEquals(cat.likes, 64)
        

class View1Tests(TestCase):
    def test_about_using_template(self):
        # Check the template used to render index page
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'rango/about.html')


class View2Tests(TestCase):
    def setUp(self):
        try:
            from populate_rango import populate
            populate()
        except ImportError:
            print('The module populate_rango does not exist')
        except NameError:
            print('The function populate() does not exist or is not correct')
        except:
            print('Something went wrong in the populate() function :-(')

    def get_category(self, name):
        from rango.models import Category
        try:
            cat = Category.objects.get(name=name)
        except Category.DoesNotExist:
            cat = None
        return cat

    def test_python_cat_added(self):
        cat = self.get_category('Python')
        self.assertIsNotNone(cat)

    def test_python_cat_with_views(self):
        cat = self.get_category('Python')
        self.assertEquals(cat.views, 128)

    def test_python_cat_with_likes(self):
        cat = self.get_category('Python')
        self.assertEquals(cat.likes, 64)
