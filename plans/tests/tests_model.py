from django.test import TestCase
from plans.models import Plan
from plans.models import Tier

class PlanAttributeTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.plan_data = {
            "name":"Plano de bronze",
            "description": "Tem direito a 1 mês de academia",
            "tier": "Bronze",
            "price": 79,
            "is_active": True
        }

        cls.plan_obj = Plan.objects.create(**cls.plan_data)

    def test_user_max_length(self):
        expected_max_length = 255
        received_max_length = Plan._meta.get_field("name").max_length
        msg = f'Verifique se a propriedade `max_length` do atributo name foi definida como {expected_max_length}'
        self.assertEqual(expected_max_length,received_max_length,msg)

    def test_description_max_length(self):
        expected_max_length = 255
        received_max_length = Plan._meta.get_field("description").max_length
        msg = f'Verifique se a propriedade `max_length` do atributo description foi definida como {expected_max_length}'
        self.assertEqual(expected_max_length,received_max_length,msg)
    
    def test_tier_type_choices(self):
        expected_choices = Tier.choices
        received_type_choices = Plan._meta.get_field("tier").choices
        msg = f'Verifique se a propriedade `choices` do atributo tier foi definida como {expected_choices}'
        self.assertEqual(expected_choices,received_type_choices,msg)

    def test_if_is_active_is_default_equal_false(self):
        expected_default = False
        received_default = Plan._meta.get_field("is_active").default
        msg = f'Verifique se a propriedade `default` do atributo is_active foi definida como {expected_default}'
        self.assertEqual(expected_default,received_default,msg)