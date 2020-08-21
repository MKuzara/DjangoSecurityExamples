from django.db import models

# Create your models here.
class ExampleUser(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=25)

    def compare_password(self, password):
        if password == self.password:
            return True
        return False