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
