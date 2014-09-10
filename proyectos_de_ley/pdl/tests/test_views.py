import json
import os
import re
import unittest

from bs4 import BeautifulSoup

from django.test import Client
from django.test import TestCase

from pdl import views
from pdl.models import Proyecto


class SimpleTest(TestCase):
    def setUp(self):
        this_folder = os.path.abspath(os.path.dirname(__file__))
        dummy_db_json = os.path.join(this_folder, 'dummy_db.json')
        self.dummy_items = json.loads(open(dummy_db_json, 'r').read())
        self.maxDiff = None

    def test_index(self):
        c = Client()
        response = c.get('/')
        soup = BeautifulSoup(response.content)
        result = soup.find_all('h1')[0].get_text()
        self.assertEqual('Proyectos de Ley', result)

    def test_get_last_items(self):
        for i in self.dummy_items:
            b = Proyecto(**i)
            b.save()

        expected = '03774'
        item = views.get_last_items()[0]
        result = re.search("<b>([0-9]{5})/[0-9]{4}-CR</b>", item).groups()[0]
        self.assertEqual(expected, result)

    def test_prettify_item1(self):
        this_folder = os.path.abspath(os.path.dirname(__file__))
        prettified_file = os.path.join(this_folder, 'prettified_03774.txt')
        with open(prettified_file, "r") as f:
            prettified_item = f.read()
        item = self.dummy_items[0]

        # save it to test database
        b = Proyecto(**item)
        b.save()
        # now get it as QuerySet object
        item = Proyecto.objects.get(codigo='03774')
        result = views.prettify_item(item)
        self.assertEqual(prettified_item, result)

    def test_prettify_item2(self):
        """Test when no pdf_url and no expediente are Blank in object."""
        this_folder = os.path.abspath(os.path.dirname(__file__))
        prettified_file = os.path.join(this_folder, 'prettified_03774_2.txt')
        with open(prettified_file, "r") as f:
            prettified_item = f.read()
        item = self.dummy_items[0]
        item['pdf_url'] = ''
        item['expediente'] = ''
        item['seguimiento_page'] = ''

        # save it to test database
        b = Proyecto(**item)
        b.save()
        # now get it as QuerySet object
        item = Proyecto.objects.get(codigo='03774')
        result = views.prettify_item(item)
        self.assertEqual(prettified_item, result)

    def test_hiperlink_congre(self):
        expected = "<a href='/congresista/dammert_ego_aguirre/' title='ver " \
                   "todos sus proyectos'>Dammert Ego Aguirre, Manuel " \
                   "Enrique Ernesto</a>;\n" \
                   "<a href='/congresista/lescano_ancieta_yonhy/' " \
                   "title='ver todos sus proyectos'>Lescano Ancieta, " \
                   "Yonhy</a>"
        congresistas = "Dammert Ego Aguirre, Manuel Enrique Ernesto; " \
                       "Lescano Ancieta, Yonhy"
        result = views.hiperlink_congre(congresistas)
        self.assertEqual(expected, result)

    def test_convert_name_to_slug(self):
        name = 'Eguren Neuenschwander, Juan Carlos'
        expected = 'eguren_neuenschwander_juan/'
        result = views.convert_name_to_slug(name)
        self.assertEqual(expected, result)