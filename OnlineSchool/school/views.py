from django.http import HttpResponse, JsonResponse
from .models import Product, User, Tutorial, UserTutorial
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.db.models import Sum


# Create your views here.
@require_GET
def get_statistic_by_all_products(request):
    """
    Получение статистики по всем продуктам.

    Обрабатывает GET-запросы и возвращает статистику по всем продуктам на платформе.

    Возвращает Json со Общим числом простмотров всех уроков,
    общим временем просмотра всех уроков,
    общим количеством студентов и
    процентом конверсии пользователей,
    для каждого продукта на платформе

    :return: Объект JsonResponse.
    """
    result = {}
    products = Product.objects.all()
    for product in products:
        # users = UserTutorial.objects.filter(tutorial__products__id=product.id)
        watches = UserTutorial.objects.filter(watch_status=True, tutorial__products__id=product.id)
        total_sum = UserTutorial.objects.filter(watch_time__gt=0, tutorial__products__id=product.id).aggregate(Sum('watch_time'))
        result[product.name] = {
            "Total watches": watches.count(),
            "Total watch time": total_sum['watch_time__sum'],
            "Total students": product.users.count(),
            "Conversion": str(int(product.users.count()/User.objects.count()*100)) + " %",
        }
    print(products)

    return JsonResponse(result, status=200)


@csrf_exempt
@require_POST
def user_get_tutorials_by_specific_product(request):
    """
    Получение статистики по конкретному продукту пользователем.

    Обрабатывает POST-запросы и возвращает статистику по продукту.

    Принимает в теле запроса параметры user_id и product_id

    Возвращает Json со временем просмотра,
    статусом просмотра и
    датой последнего просмотра,
    для каждого урока в продукте

    :param user_id: ID пользователя.
    :param product_id: ID продукта.
    :return: Объект JsonResponse.
    """
    user_id = request.POST.get("user_id")
    product_id = request.POST.get("product_id")

    if not(user_id and product_id):
        return HttpResponse(status=400)

    product = Product.objects.get(id=product_id)
    user_tutorials = UserTutorial.objects.filter(user__id=user_id, tutorial__products__id=product_id)
    result = {product.name: []}

    for user_tutorial in user_tutorials:
        if product in user_tutorial.tutorial.products.all():
            result[product.name].append({
                user_tutorial.tutorial.name: [
                    user_tutorial.watch_time,
                    user_tutorial.watch_status,
                    user_tutorial.last_watch,
                ]
            })

    return JsonResponse(result, status=200)

@csrf_exempt
@require_POST
def user_get_tutorials_by_products(request):
    """
    Получение статистики по продуктам пользователя.

    Обрабатывает POST-запросы и возвращает статистику по  всем продуктам пользователя.

    Принимает в теле запроса параметр user_id

    Возвращает Json со временем просмотра и
    статусом просмотра
    для каждого урока в каждом продукте пользователя

    :param user_id: ID пользователя.
    :return: Объект JsonResponse.
    """
    user_id = request.POST.get("user_id")

    if not user_id:
        return HttpResponse(status=400)

    result = {}
    products = Product.objects.filter(users__id=user_id)
    user_tutorials = UserTutorial.objects.filter(user__id=user_id)

    for product in products:
        result[product.name] = []
        for user_tutorial in user_tutorials:
            if product in user_tutorial.tutorial.products.all():
                result[product.name].append({user_tutorial.tutorial.name: [user_tutorial.watch_time, user_tutorial.watch_status]})

    return JsonResponse(result, status=200)


@csrf_exempt
@require_POST
def create_user(request):
    """
    Создание пользоваателя

    Обрабатывает POST-запросы и добавляет в базу данных запись о пользователе.

    Принимает в теле запроса параметр user_name

    Возвращает HttpResponse со статусом 201

    :param user_name: Имя пользователя.
    :return: Объект HttpResponse.
    """
    user_name = request.POST.get("user_name")

    if not user_name:
        return HttpResponse(status=400)

    User.objects.create(name=user_name)
    return HttpResponse(status=201)


@csrf_exempt
@require_POST
def create_product(request):
    """
    Создание продукта

    Обрабатывает POST-запросы и добавляет в базу данных запись о продукте.

    Принимает в теле запроса параметры user_id и product_name

    Возвращает HttpResponse со статусом 201

    :param user_id: ID пользователя.
    :param product_name: Название продукта.
    :return: Объект HttpResponse.
    """
    user_id = request.POST.get("user_id")
    product_name = request.POST.get("product_name")

    if not(user_id and product_name):
        return HttpResponse(status=400)

    Product.objects.create(name=product_name, owner=User.objects.get(pk=user_id))
    return HttpResponse(status=201)


@csrf_exempt
@require_POST
def create_tutorial(request):
    """
    Создание урока

    Обрабатывает POST-запросы и добавляет в базу данных запись об уроке.

    Принимает в теле запроса параметры products_id, tutorial_name, video_url, video_length

    Возвращает HttpResponse со статусом 201

    :param products_id: ID продуктов в состав которых входит урок.
    :param tutorial_name: Название урока.
    :param video_url: URL видо урока.
    :param video_length: Длинна видео урока в секундах.
    :return: Объект HttpResponse.
    """
    products_id = request.POST.get("products_id")
    tutorial_name = request.POST.get("tutorial_name")
    video_url = request.POST.get("video_url")
    video_length = request.POST.get("video_length")

    if not(products_id and tutorial_name and video_url and video_length):
        return HttpResponse(status=400)

    products_id_set = products_id.split()

    products = Product.objects.filter(id__in=products_id_set)

    tut = Tutorial(name=tutorial_name, video_url=video_url, video_length=video_length)
    tut.save()
    tut.products.set(products)
    tut.save()
    return HttpResponse(status=201)


@csrf_exempt
@require_POST
def user_get_product(request):
    """
    Получение пользователем урока

    Обрабатывает POST-запросы и добавляет в базу данных записи о принадлежности продукта и уроков в нем пользвателю.

    Принимает в теле запроса параметры user_id и product_id

    Возвращает HttpResponse со статусом 201

    :param user_id: ID пользователя приобретающего продукт.
    :param product_id: ID приобретаемого продукта.
    :return: Объект HttpResponse.
    """
    user_id = request.POST.get("user_id")
    product_id = request.POST.get("product_id")

    if not(user_id and product_id):
        return HttpResponse(status=400)

    product = Product.objects.get(id=product_id)
    user = User.objects.get(id=user_id)
    tutorials = Tutorial.objects.filter(products__id=product_id)

    for tutorial in tutorials:
        if not UserTutorial.objects.filter(user=user, tutorial=tutorial).exists():
            UserTutorial.objects.create(user=user, tutorial=tutorial)

    product.users.add(user)

    return HttpResponse(status=201)


@csrf_exempt
@require_POST
def user_watch_tutorial(request):
    """
    Просмотр пользователем урока

    Обрабатывает POST-запросы и добавляет в базу данных записи о статистике просмотра пользователем урока.

    Принимает в теле запроса параметры user_id, tutorial_id и watch_time

    Возвращает HttpResponse со статусом 201

    :param user_id: ID пользователя смотрящего урок.
    :param tutorial_id: ID просматриваемого урока.
    :param watch_time: Время которое пользователь просмотривал урок.
    :return: Объект HttpResponse.
    """
    user_id = request.POST.get("user_id")
    tutorial_id = request.POST.get("tutorial_id")
    watch_time = request.POST.get("watch_time")

    if not(user_id and tutorial_id and watch_time):
        return HttpResponse(status=400)

    watch_time = int(watch_time)

    user_tutorial = UserTutorial.objects.get(user__id=user_id, tutorial__id=tutorial_id)
    user_tutorial.watch_time = watch_time if watch_time > user_tutorial.watch_time else user_tutorial.watch_time
    user_tutorial.watch_status = True if watch_time >= 0.8 * user_tutorial.tutorial.video_length else False
    user_tutorial.save()

    return HttpResponse(status=201)
