from django.test import TestCase
from jsm_app.models import Usuario, Categoria


class UsuarioModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Usuario.objects.create(nome='Lismar', email='lico@gmail.com')

    def test_nome_label(self):
        usuario = Usuario.objects.get(id=1)
        field_label = usuario._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')

    def test_email_label(self):
        usuario = Usuario.objects.get(id=1)
        field_label = usuario._meta.get_field('email').verbose_name
        self.assertEquals(field_label, 'email')

    def test_nome_max_length(self):
        usuario = Usuario.objects.get(id=1)
        max_length = usuario._meta.get_field('nome').max_length
        self.assertEquals(max_length, 100)

class CategoriaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Categoria.objects.create(nome='Construção')

    def test_nome_label(self):
        categoria = Categoria.objects.get(id=1)
        field_label = categoria._meta.get_field('nome').verbose_name
        self.assertEquals(field_label, 'nome')

    def test_nome_max_length(self):
        categoria = Categoria.objects.get(id=1)
        max_length = categoria._meta.get_field('nome').max_length
        self.assertEquals(max_length, 100)  
        
