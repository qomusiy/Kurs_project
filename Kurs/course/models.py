from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    teacher_id = models.TextField()
    description = models.TextField()
    stars = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    made_date = models.DateField()
    language = models.CharField(max_length=20)
    image = models.ImageField(upload_to='course_img', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.title}, {self.teacher_id}, {self.created}"
