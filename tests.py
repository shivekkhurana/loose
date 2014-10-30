#! /usr/bin/python

import unittest
import loose

Loose = loose.Loose


class TestUrlBuilding(unittest.TestCase):

    def setUp(self):
        self.helper = Loose({
            'url': Loose({
                'to': Loose({
                    'events': lambda page=1: (
                        'http://www.someurl.com/model?page=' + str(page)
                    ),
                    'artists': lambda page=1: (
                        'http://www.someurl.com/model?page=' + str(page)
                    )
                })
            })
        })

    def test_default_page(self):
        self.assertEqual(
            self.helper.url.to.artists(), 'http://www.someurl.com/model?page=1')

    def test_specific_page(self):
        self.assertEqual(
            self.helper.url.to.artists(23), 'http://www.someurl.com/model?page=23')


class TestListParams(unittest.TestCase):

    def setUp(self):
        self.numbers_str = Loose({
            'get': lambda int_list=list(): (
                ','.join(int_list)
            )
        })

    def test_default(self):
        self.assertEqual(self.numbers_str.get(), '')

    def test_123(self):
        self.assertEqual(self.numbers_str.get(['1', '2', '3']), '1,2,3')


class TestLooseCallable(unittest.TestCase):

    def setUp(self):
        self.helper = Loose({
            'url': Loose({
                'default': lambda: (
                    'www.google.com'
                ),

                'country': lambda tld: (
                    'www.google.co.' + tld
                )
            }),
            'super_admin': 'yo@yo.com'
        })

    def test_base_url(self):
        self.assertEqual(self.helper.url(), 'www.google.com')

    def test_in_url(self):
        self.assertEqual(self.helper.url.country('in'), 'www.google.co.in')


class TestExceptions(unittest.TestCase):

    def setUp(self):
        self.helper = Loose({
            'url': Loose({
                'default': lambda: (
                    'www.google.com'
                ),

                'country': lambda tld: (
                    'www.google.co.' + tld
                )
            }),
            'super_admin': 'yo@yo.com'
        })

    def test_raise_key_error_if_no_default(self):
        self.assertRaises(KeyError, self.helper)

    def test_raise_key_error_if_method_not_defined(self):
        '''
        - in noDefault case, the default method is called and exception is raised
        - in noUndefinedMethod case, the method does not get called and an attemt to return a pointer is made
          which fails because method doesn't exist
        - if this method is tested in same way as noDefault method, it will return a KeyError because attempt to 
          return a pointer to a lambda function failed, and the exception will not be raised and catched.
        '''
        with self.assertRaises(KeyError):
            self.helper.some_undefined_method()


if __name__ == '__main__':
    unittest.main()
