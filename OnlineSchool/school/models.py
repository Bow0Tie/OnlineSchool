from django.db import models


# Create your models here.
class User(models.Model):
    """
    Модель User.

    Эта модель хранит информацию о пользователях.

    :param name: Имя пользователя.
    """
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Модель Product.

    Эта модель хранит информацию о продуктах.

    :param name: Имя продукта.
    :param owner: Пользователь владеющий продуктом.
    :param users: Пользователи купившие продукт.
    """
    name = models.CharField(max_length=30)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    users = models.ManyToManyField(User, related_name="buyers", blank=True)

    def __str__(self):
        return self.name


class Tutorial(models.Model):
    """
    Модель Tutorial.

    Эта модель хранит информацию об уроках.

    :param name: Имя урока.
    :param video_url: URL видео урока.
    :param video_length: Длинна видео урока в секундах.
    :param products: Продукты в которых содержится этот урок.
    :param users: Пользователи имеющие доступ к уроку.
    """
    name = models.CharField(max_length=30)
    video_url = models.URLField()
    video_length = models.IntegerField()
    products = models.ManyToManyField(Product)
    users = models.ManyToManyField(User, through="UserTutorial")

    def __str__(self):
        return self.name


class UserTutorial(models.Model):
    """
    Модель UserTutorial.

    Эта модель хранит статистику пользователя по уроку.

    :param user: Пользователь урока.
    :param tutorial: Урок к которому относится статистика.
    :param watch_time: Время простмотра урока пользователем.
    :param watch_status: Статус просмотра урока.
    :param last_watch: Дата и время последнего просмотра пользователем урока.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE)
    watch_time = models.IntegerField(default=0)
    watch_status = models.BooleanField(default=False)
    last_watch = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self):
        return f"{self.user}, {self.tutorial}"
