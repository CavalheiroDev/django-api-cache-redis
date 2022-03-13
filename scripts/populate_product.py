from faker import Faker
from django.db import transaction
from product.models import Product


def run():
    fake = Faker(locale="pt_BR")
    for i in range(1, 1500):
        with transaction.atomic():
            try:
                uuid = fake.uuid4()
                name = fake.company()
                description = fake.paragraph(nb_sentences=5)
                price = 800

                Product.objects.create(id=uuid, name=name, description=description, price=price)
            except Exception as e:
                print("error: ", e)
