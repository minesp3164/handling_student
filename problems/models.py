from django.db import models


class Difficulty(models.Model):
    difficult = models.CharField(max_length=100)

    def __str__(self):
        return self.difficult


class Answer(models.Model):
    content = models.TextField()
    correct = models.BooleanField(default=False)

    def __str__(self):
        return self.content


class Problems(models.Model):
    user = models.ForeignKey(
        "user.User",
        verbose_name="작성자",
        on_delete=models.CASCADE
                )
    difficulty = models.ForeignKey(Difficulty, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Comment(models.Model):
    user = models.ForeignKey(
        "user.User",
        verbose_name="작성자",
        on_delete=models.CASCADE
                )
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.problem.title}에 대한 댓글'