from django.db import models

# Create your models here.


class ToDoList(models.Model):
    content = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.content)
    #
    # class Meta:
    #     verbose_name_plural = 'Searches'
