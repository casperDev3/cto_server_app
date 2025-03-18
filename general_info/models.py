from django.db import models

class GeneralInformation(models.Model):
    site_name = models.CharField(max_length=255, verbose_name="Название сайта")
    email = models.EmailField(verbose_name="Email для контактов")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    address = models.TextField(verbose_name="Адрес")
    about = models.TextField(verbose_name="О сайте", blank=True, null=True)

    def __str__(self):
        return{
        "Name site:":self.site_name,
        "Email:":self.email,
        "Phone:":self.phone,
        "Address:":self.address,
        "About:":self.about,
        }
