from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from .models import FAQ

class FAQModelTestCase(TestCase):
    def setUp(self):
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a high-level Python web framework."
        )

    def test_get_translated_question_fallback(self):
        # Assuming translation returns a non-empty string
        translated = self.faq.get_translated_question("hi")
        self.assertTrue(isinstance(translated, str))
        self.assertNotEqual(translated, "")

class FAQAPITestCase(TestCase):
    def setUp(self):
        FAQ.objects.create(
            question="What is Python?",
            answer="Python is a programming language."
        )

    def test_api_list_faqs_default_language(self):
        url = reverse("faq-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("data", data)
        self.assertTrue(len(data["data"]) > 0)

    def test_api_list_faqs_with_language_param(self):
        url = reverse("faq-list")
        response = self.client.get(url + "?lang=bn")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # Each FAQ in the API response should include a 'translated_question'
        self.assertIn("translated_question", data["data"][0])
