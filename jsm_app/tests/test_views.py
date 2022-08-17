from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from jsm_app.models import Pedido, Usuario

 
class UsuarioListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Criação de 5 usuários para testes de paginação
        number_of_usuarios = 5

        for usuario_id in range(number_of_usuarios):
            Usuario.objects.create(
                nome=f'Caio {usuario_id}'
            )

    #Função para saber se a url esta no local correto - verifica uma url específica
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/listaclientes')
        self.assertEqual(response.status_code, 200)
     
    #Função para saber se a url esta acessível por nome - gera a url a partir do seu nome
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('listaclientes'))
        self.assertEqual(response.status_code, 200)
    
    #Função para saber se esta usando o template correto
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('listaclientes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listaclientes.html')
        
        
   