
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from article.models import Article, Author
from article.serializers import ArticleSerializer , AuthorSerializer ,\
 ArticleModelSerializer, AuthorModelSerializer

class ArticleViewset(ModelViewSet):
    serializer_class = ArticleModelSerializer
    queryset = Article.objects.all()

class AuthorViewset(ModelViewSet):
    serializer_class = AuthorModelSerializer
    queryset = Author.objects.all()

class ArticleView(APIView):
    
    def get(self, request):
        articles = Article.objects.all()
        serialize_data = ArticleSerializer(articles, many=True)
        return Response({"articles": serialize_data.data})
    
    def post(self, request):
        article = request.data.get('article',None)
        response_data = {}
        if article :
            _serialize =  ArticleSerializer(data=article)
            try:
                if _serialize.is_valid(raise_exception=True):
                    _instance = _serialize.save()
                    response_data.update({"status":200,"message":" successfully %s article created" % _instance.title})
            except Exception as ex:
                response_data.update({"status":503,"message":" Something wrong with Post function \n %s" % ex})
        else:
            response_data.update({"status":400,"message":" article content not available in request"})            
        return Response(response_data)

    def put(self,request,pk):
        try:
            saved_article = Article.objects.get(pk=pk)
            article = request.data.get('article',None)
            response_data = {}
            if article :
                
                _serialize =  ArticleSerializer(instance=saved_article, data=article)

                if _serialize.is_valid(raise_exception=True):
                    _instance = _serialize.save()
                    response_data.update({"status":200,"message":" successfully %s article updated" % _instance.title})
            
            else:
                response_data.update({"status":400,"message":" article content not available in request"})
        
        except Exception as ex:
                response_data.update({"status":503,"message":" Something wrong with Put function \n %s" % ex})            
        return Response(response_data)

    def delete(self,request,pk):
        article = Article.objects.get(pk=pk)
        article.delete()
        return Response({"status":200,"message":" successfully %s article deleted" % article.title})


class AuthorView(APIView):

    def get(self,request):
        authors = Author.objects.all()
        serialized = AuthorSerializer(authors,many=True)
        return Response({"authors":serialized.data})
    
    def post(self,request):
        _response = {}
        try:
            author = request.data.get('author',None)
            if author:
                serialized = AuthorSerializer(data=author)
                if serialized.is_valid(raise_exception=True):
                    instance = serialized.save()
                    _response.update({"status":200,"message":" successfully %s author created" % instance.name})
            else:
                _response.update({"status":400,"message":" author content not available in request"})
        except Exception as ex:
            _response.update({"status":503,"message":" Something wrong with Post function \n %s" % ex})
                    
        return Response(_response)


    
    def put(self,request,pk):
        saved_author = Author.objects.get(pk=pk)
        try:
            author = request.data.get('author',None)
            _response = {}
            if author:
                serialized = AuthorSerializer(instance=saved_author,data=author)
                if serialized.is_valid(raise_exception=True):
                    _serialized = serialized.save()
                    _response.update({"status":200,"message":"successfully %s author updated" % _serialized.name})
            else:
                _response.update({"status":400,"message":" author content not available in request"})
        except Exception as ex:
            _response.update({"status":503,"message":" Something wrong with Post function \n %s" % ex})
                    
        return Response(_response)

        
    
    def delete(self,request,pk):
        author = Author.objects.get(id=pk)
        author.delete()
        return Response({"status":200,"message":" successfully delete %s author" % author.name})
        

