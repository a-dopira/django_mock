from unittest import TestCase

from django.urls import reverse

from notes.models import Note


class NoteViewTestCase(TestCase):
    def setUp(self):
        self.note = Note.objects.create(title="Тестова нотатка", text="Це тестова нотатка")

    def test_note_update_view(self):
        update_url = reverse('note_edition', args=[self.note.pk])
        response = self.client.get(update_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_edition.html')
        self.assertContains(response, 'Редагування нотатки')
        self.assertContains(response, 'Оновлення нотатки')
        self.assertContains(response, 'Зберегти зміни')

    def test_note_create_view(self):
        create_url = reverse('note_create')
        response = self.client.get(create_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/note_edition.html')
        self.assertContains(response, 'Створення нотатки')
        self.assertContains(response, 'Створення нотатки')
        self.assertContains(response, 'Створити')


    def tearDown(self):
        self.note.delete()