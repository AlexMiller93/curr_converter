from .utils import get_quotes
from django.db import models

# Create your models here.


class Converter(models.Model):
    """

    """
    from_curr = models.CharField(max_length=5, help_text="Input currency")
    to_curr = models.CharField(max_length=5, help_text="Output currency")
    value = models.SmallIntegerField(help_text="Quantity to be converted")
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"From {self.from_curr} to {self.to_curr} \
        in quantity {self.value} {self.from_curr} in {self.timestamp}"

    def convert_value(self):
        """

        :return:
        """

        # Getting the quote
        rate = get_quotes(self.from_curr, self.to_curr)

        # Returning the quantity
        quantity = round(rate * self.value, 2)
        return quantity

