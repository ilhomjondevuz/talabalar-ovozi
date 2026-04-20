from django.db import models


class Feedback(models.Model):
    student_name = models.CharField(max_length=100)
    opinion = models.TextField()
    rating = models.IntegerField(choices=[(1,'Yomon'),(2,'O‘rtacha'),(3,'Yaxshi'),(4,'Zo‘r'),(5,'A’lo')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name
