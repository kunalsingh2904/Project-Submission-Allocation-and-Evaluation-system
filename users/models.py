from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from PIL import Image

current_year = settings.CURRENT_YEAR

user_types = (
    ('student', 'student'),
    ('teacher', "teacher"),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default_pic.jpg', upload_to='image/')
    types = models.CharField(default='student', choices= user_types, max_length=20)
    join_year = models.CharField(max_length=10, default=current_year)

    def __str__(self):
        return self.user.username + " " + self.types + " " + self.join_year
    
    class Meta:
        ordering = ['-join_year']

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height >300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



