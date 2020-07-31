from django.db import models


class Question(models.Model):
    question_text = models.CharField('Текст вопроса', max_length=200)
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    choice_text = models.CharField('Вариант ответа', max_length=200)
    votes = models.IntegerField('Голоса', default=0)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'
