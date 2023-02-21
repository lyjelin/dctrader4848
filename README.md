# dctrader4848

# Python Virtual Environment `venv`

> 참고: [Python virtualenv && requirement.txt 사용법](https://blog.ugonfor.kr/138)

1. virtualenv

```s
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

2. venv에서 사용하는 파이썬 버전을 설정하고 싶으면:

```s
# python 2
$ python -m virtualenv venv
$ virtualenv venv --python=python
$ virtualenv venv --python=python2.7

# python 3
$ python3 -m virtualenv venv
$ virtualenv venv --python=python3
$ virtualenv venv --python=python3.5
```

3. requirement.txt

```s
# requirement.txt를 생성할 때
(venv) $ pip freeze > requirements.txt

# requirement.txt가 주어졌을 때
(venv) $ pip install -r requirements.txt
```

# Django Setup

1. venv 가상환경이 설치되었다는 assumption하에 진행!

```s
$ mkdir myProject
$ cd myProject
$ virtualenv venv
$ source venv/bin/activate	// 가상환경 실행

$ pip3 install django
$ django-admin startproject backend .	// backend 폴더, manage.py 생성

$ python3 manage.py startapp testapp
```

2. `backend/settings.py`

```python
INSTALLED_APPS = [
    ...,
    'testapp',
]

# 새로 생성한 app 추가
```

3. 아래 command 콘솔에 입력

```s
$ python3 manage.py migrate
$ python3 manage.py createsuperuser	// 관리자 계정 생성
$ python3 manage.py runserver
```

4. `python3 manage.py runserver` 명령어 입력해서 서버 호스팅 시작!

http://127.0.0.1:8000/ 에 접속 시 아래 화면이 뜨면 성공

<img src="/backend/asset/image/server-initial-launch.png" alt="isolated" width="200"/>

# REST API

HTTP method로 CRUD를 표현하는데, 여기서는:

- `POST`: 데이터 등록 및 전송
- `GET`: 데이터 조회
- `DELETE`: 데이터 삭제

### Serializer, APIView로 CRUD 구현

> 참고: [리액트와 장고(DRF) 연동하기- (2) serializer, APIView로 CRUD 구현](https://breathtaking-life.tistory.com/136)

1. Models 생성

```python
# 예제
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
```

2. Models 생성했다면 migration으로 DB에 적용시켜줌: `makemigrations`, `migrate`

```s
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

3. `admin` 등록

```python
from django.contrib import admin
from .models import Review

admin.site.register(Article)
```

그리고 `createsuperuser`를 통해 admin 계정 생성

```s
$ python3 manage.py createsuperuser
```

4. Serializer

`serializer`는 DRF가 제공하는 class인데, DB instance를 json데이터로 생성해준다!
main_app에 `serializers.py`를 생성하고 models와 fields 작성해줌

```python
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'updated_at')
```

5. `views.py` class 선언

> `Article` 전체 목록을 보여주는 `ArticleList`와 `Article`의 세부사항을 보여주는 `ArticleDetail`을 작성
> `CRUD` 기능은 APIView로 구현 (이 외에도 ViewSet, Mixins 등이 있음)

### 먼저, 데이터를 처리하기 위해 밑 항목들을 import해줌

```python
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from .serializers import ArticleSerializer
from .models import Article
```

### `ArticleList` 작성 (GET, POST)

```python
class ArticleList(APIView): #목록 작성
    def get(self, request):
        articles = Articles.objects.all()
        serializer = ArticleSerializer(articles, many=True) # 여러 객체 serialize하려면 many=True
        return Response(serializer.data)

    def post(self, request): # 새 글 작성시
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(): # 유효성 검사
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### `ArticleDetail` 작성 (GET, PUT, DELETE)

```python
class ArticleDetail(APIView):
    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None): # Article Detail
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None): # Article 수정
        review = self.get_object(pk)
        serializer = ArticleSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def delete(self, request, pk, format=None): # Article 삭제
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

6. `urls` 작성

### `backend` 폴더 안에 있는 `urls.py`에 다음과 같이 추가

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls'))
]
```

### `main_app` 폴더 내부에 `urls.py`를 생성하고 다음과 같이 추가한다

```python
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArticleList, ArticleDetail

urlpatterns = [
    path('article/', ArticleList.as_view()),
    path('article/<int:pk>/', ArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
```

7. 실행; 웹서버 동작!!

```s
$ python manage.py runserver
```

그냥 `127.0.0.1:8000/article/`로 들어가면 `Page Not Found`가 뜬다
=> `urls.py`에서 메인 경로 등록 안해놔서 생기는 것

`127.0.0.1:8000/article/` 로 들어가면 ArticleList는 두 가지 형태로 나타난다.
첫 번째 박스는 Article를 보여주는 GET
두 번째 박스는 Article를 등록할 수 있는 POST로 구현되어 있다.

### Data `GET`, `POST`

Content에서 json을 전달하면 데이터가 추가되고(POST), 확인할 수 있다(GET)

# React (ft. Frontend)

1. 리액트 폴더 생성

```s
# At root dir
$ npm create react-app frontend
```

2. `frontend/package.json`에서 `proxy` 설정해주기

> React에서 proxy를 설정함으로써 개발은 3000 port에서 실행, 서비스는 8000 port에서 실행하도록 한다. React에서 백엔드 서버로 API 요청 시 호출 할 때 발생 할 수 있는 CORS 관련 오류를 방지하기 위하여 Proxy를 설정해 준다. 8000 port에서 api를 받아올 수 있도록 설정하는 것이다

3. CORS 관련 세팅하기

> `CORS(Cross-Origin Resource Sharing)`는 클라이언트와 서버의 포트가 다른 상태에서 클라이언트 측에서 서버 측으로 무언가를 요청했을 때 브라우저가 보안상의 이유로 요청을 차단하는 문제다. React의 3000 port에서 Django의 8000 port로 요청했을 때 보안상의 이유로 차단되기 때문에 이를 해결해 줘야 한다
