from http.client import HTTPResponse
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser


from .models import Article
from .serializers import ArticleSerializer

@csrf_exempt
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        seralizer = ArticleSerializer(articles, many=True)
        return JsonResponse(seralizer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        seralizer = ArticleSerializer(data=data)
        if seralizer.is_valid():
            seralizer.save()
            return JsonResponse(seralizer.data, status=201)
        return JsonResponse(seralizer.errors, status=400)

@csrf_exempt
def article_details(request, pk):
    try:
        article = Article.objects.get(pk=pk)

    except Article.DoesNotExist:
        return HTTPResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        seralizer = ArticleSerializer(article,data=data)
        if seralizer.is_valid():
            seralizer.save()
            return JsonResponse(seralizer.data, status=201)
        return JsonResponse(seralizer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)
