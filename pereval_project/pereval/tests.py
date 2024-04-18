from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .serializers import PassSerializer
from .models import *


class PassTestCase(APITestCase):

    def setUp(self):
        # Объект перевал 1
        self.pass_1 = Pass.objects.create(
            tourist=Users.objects.create(
                email='Ivanov@mail.ru',
                last_name='Иванов',
                first_name='Петр',
                otc='Васильевич',
                phone='89999999999'
            ),
            beauty_title='beauty_title',
            title='title',
            other_titles='other_title',
            connect='connect',
            coord=Coords.objects.create(
                latitude=22.222,
                longtitude=11.111,
                height=1000.0
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )

        # Изображение для объекта перевал 1
        self.image_1 = Images.objects.create(
            title='Title_1',
            image='https://images.app.goo.gl/eT3kx7tigk33vNQG8',
            rel_pass=self.pass_1
        )

        # Объект перевал 2
        self.pass_2 = Pass.objects.create(
            tourist=Users.objects.create(
                email='Petrov@mail.ru',
                last_name='Петров',
                first_name='Иван',
                otc='Васильевич',
                phone='89999998877'
            ),
            beauty_title='beauty_title2',
            title='title2',
            other_titles='other_title2',
            connect='connect2',
            coord=Coords.objects.create(
                latitude=11.222,
                longtitude=22.111,
                height=2000.0
            ),
            level=Level.objects.create(
                winter='1A',
                summer='1A',
                autumn='1A',
                spring='1A'
            )
        )

        # Изображение для объекта перевал 2
        self.image_2 = Images.objects.create(
            title='Title_2',
            image='https://images.app.goo.gl/8JQJ8qgxTuFYCcRG7',
            rel_pass=self.pass_2
        )

    def test_pereval_list(self):
        """Тест endpoint /Pereval/ - список всех объектов модели Pass"""

        response = self.client.get(reverse('pass-list'))
        serializer_data = PassSerializer([self.pass_1, self.pass_2], many=True).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_pereval_detail(self):
        """Тест endpoint /Pereval - объект модели Pass по его id"""

        response = self.client.get(reverse('pass-detail', kwargs={'pk': self.pass_1.id}))
        serializer_data = PassSerializer(self.pass_1).data

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer_data, response.data)

    def test_pereval_user_email(self):
        """Тест endpoint /Pereval/user__email=<email> - объекты модели Pass отфильтрованные по email пользователя"""

        email = self.pass_1.user.email
        url = f'/Pereval/?user__email={email}'

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
