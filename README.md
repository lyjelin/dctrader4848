# dctrader4848

# Python Virtual Environment `venv`

> 참고: [Python virtualenv && requirement.txt 사용법](https://blog.ugonfor.kr/138)

1. virtualenv

```shell
$ pip install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```

2. venv에서 사용하는 파이썬 버전을 설정하고 싶으면:

```shell
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

```shell
# requirement.txt를 생성할 때
(venv) $ pip freeze > requirements.txt

# requirement.txt가 주어졌을 때
(venv) $ pip install -r requirements.txt
```

# Django Setup

1. venv 가상환경이 설치되었다는 assumption하에 진행!

```shell
mkdir myProject
cd myProject
virtualenv venv
source venv/bin/activate	// 가상환경 실행

pip3 install django
django-admin startproject backend .	// backend 폴더, manage.py 생성

python3 manage.py startapp testapp
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

```shell
python3 manage.py migrate
python3 manage.py createsuperuser	// 관리자 계정 생성
python3 manage.py runserver
```

4. `python3 manage.py runserver` 명령어 입력해서 서버 호스팅 시작!

http://127.0.0.1:8000/ 에 접속 시 아래 화면이 뜨면 성공

<img src="/backend/asset/image/server-initial-launch.png" alt="isolated" width="200"/>
