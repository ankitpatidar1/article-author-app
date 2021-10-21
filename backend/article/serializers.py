from rest_framework import serializers
from article.models import Article,Author

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField(max_length=500)
    body = serializers.CharField(max_length=500)
    author_id = serializers.IntegerField()

    def create(self,validate_data):
        return Article.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.title = validate_data.get('title',instance.title)
        instance.description = validate_data.get('description',instance.description)
        instance.body = validate_data.get('body',instance.body)
        instance.author_id = validate_data.get('author_id',instance.author_id)
        instance.save()
        return instance

class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    email = serializers.EmailField()

    def create(self,validate_data):
        return Author.objects.create(**validate_data)

    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.email = validate_data.get('email',instance.email)
        instance.save()
        return instance

class ArticleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__' 

class AuthorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__' 