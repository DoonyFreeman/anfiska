from django.test import TestCase
from django.urls import reverse

from .models import IceCream


class IceCreamModelTests(TestCase):
    def test_str(self):
        item = IceCream(title="Тестовое", price=10.0)
        self.assertEqual(str(item), "Тестовое")


class IceCreamViewTests(TestCase):
    def setUp(self):
        self.obj = IceCream.objects.create(
            title="А",
            description="Описание",
            price=5.50,
            is_available=True,
        )

    def test_list_view(self):
        url = reverse('ice_cream:ice_cream_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.obj.title)

    def test_empty_catalog_message(self):
        # clear the table and request again
        IceCream.objects.all().delete()
        response = self.client.get(reverse('ice_cream:ice_cream_list'))
        self.assertEqual(response.status_code, 200)
        # fallback notice should be shown and at least one demo title
        self.assertContains(response, 'демонстрационные позиции')
        self.assertContains(response, 'Классический пломбир')

    def test_fallback_detail(self):
        IceCream.objects.all().delete()
        # use id from _default_catalog
        response = self.client.get(reverse('ice_cream:ice_cream_detail', args=[0]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Классический пломбир')

    def test_detail_view(self):
        url = reverse('ice_cream:ice_cream_detail', args=[self.obj.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.obj.description)
