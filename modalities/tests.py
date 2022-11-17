from rest_framework.test import APITestCase
from modalities.models import Modality
from teachers.models import Teacher
from users.models import User


class One_To_Many_Tests(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:

        cls.user_data_1 = {
            "username": "User1Test",
            "first_name": "User1",
            "last_name": "Test",
            "phone": "123456789",
            "birthdate": "1998-04-12",
            "is_active": True,
            "password": "12345",
            "email": "test1@email.com",
        }

        cls.user_data_2 = {
            "username": "User2Test",
            "first_name": "User2",
            "last_name": "Test",
            "phone": "123456789",
            "birthdate": "1998-04-12",
            "is_active": True,
            "password": "12345",
            "email": "test2@email.com",
        }

        cls.modalites = [Modality(name=f"modalidate {num}") for num in range(1, 11)]

        cls.user_1 = User.objects.create_user(**cls.user_data_1)
        cls.user_2 = User.objects.create_user(**cls.user_data_2)

        cls.teacher_1 = Teacher.objects.create(user=cls.user_1)
        cls.teacher_2 = Teacher.objects.create(user=cls.user_2)

    def test_relatioship_one_to_many(self):

        for modality in self.modalites:
            modality.teacher = self.teacher_1
            modality.save()

        self.assertEqual(len(self.modalites), self.teacher_1.modalities.count())

        for modalite in self.modalites:
            self.assertIs(modalite.teacher, self.teacher_1)

    def test_if_modality_cannot_be_ministred_more_than_one_teacher(self):

        for modality in self.modalites:
            modality.teacher = self.teacher_1
            modality.save()

        for modality in self.modalites:
            modality.teacher = self.teacher_2
            modality.save()

        for modality in self.modalites:
            self.assertIn(modality, self.teacher_2.modalities.all())
            self.assertNotIn(modality, self.teacher_1.modalities.all())
