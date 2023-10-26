# Пульт охраны банка

Пульт охраны - это сайт, которой можно подключить к удаленной базе данных с визитами 
и карточками пропуска сотрудников банка.

### Как установить

Для запуска блога у вас уже должен быть установлен Python 3.10.12

- Скачайте код
- Установите зависимости командой `pip install -r requirements.txt`
- Запустите сервер командой `python3 manage.py runserver`

После этого переходите по ссылке [127.0.0.1:8000](http://127.0.0.1:8000), вы увидите главную страницу.

## Переменные окружения

Часть настроек проекта берётся из переменных окружения. Чтобы их определить, создайте файл `.env` рядом с `manage.py` и запишите туда данные в таком формате: `ПЕРЕМЕННАЯ=значение`.

**Для запуска проекта эти настройки не требуются**, значения уже проставлены по умолчанию.
- ALLOWED_HOSTS - список разрешенных сайтов, по умолчанию, 'localhost'. [https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts](https://docs.djangoproject.com/en/3.1/ref/settings/#allowed-hosts)
- DEBUG — дебаг-режим, по умолчанию, `False`. Поставьте `True`, чтобы увидеть отладочную информацию в случае ошибки.
  
**Доступны следующие переменные:**
- `SECRET_KEY` — секретный ключ проекта. [https://docs.djangoproject.com/en/3.1/ref/settings/#secret-key](https://docs.djangoproject.com/en/3.1/ref/settings/#secret-key)
- `DB_HOST` — адрес базы данных. [https://docs.djangoproject.com/en/3.1/ref/settings/#host](https://docs.djangoproject.com/en/3.1/ref/settings/#host)
- `DB_PORT` — порт для подключения к базе данных.[https://docs.djangoproject.com/en/3.1/ref/settings/#port](https://docs.djangoproject.com/en/3.1/ref/settings/#port)
- `DB_NAME` — название базы данных. [https://docs.djangoproject.com/en/3.1/ref/settings/#name](https://docs.djangoproject.com/en/3.1/ref/settings/#name)
- `DB_USER` — логин для доступа к базе данных. [https://docs.djangoproject.com/en/3.1/ref/settings/#user](https://docs.djangoproject.com/en/3.1/ref/settings/#user)
- `DB_PASSWORD` — пароль для доступа к базе данных. [https://docs.djangoproject.com/en/3.1/ref/settings/#password](https://docs.djangoproject.com/en/3.1/ref/settings/#password)




## Страницы сайта
### Активные карты допуска  

Отображает информацию об общем количестве активных пропусков и список сотрудников с активными 
пропусками.
* Имя и фамилия сотрудника
* Код пропуска
* Время регистрации 
 
![Активные пропуски](https://github.com/univernik77/SecurityConsole/assets/146747152/30748a05-531f-40f4-a007-d6155c1a9270)



### Список пользователей в хранилище  

Отображает информацию о сотрудниках, в данный момент находящихся в хранилище:  
* Общее количество сотрудников в хранилище
* Имя и фамилия сотрудника
* Время входа в хранилище
* Время нахождения в хранилище
* Флаг `True`, если раньше за сотрудником была замечена подозрительная активность, в виде
пребывания в хранилище на срок больше 1 часа. Флаг `False`, если такой активности не было. 

![Хранилище](https://github.com/univernik77/SecurityConsole/assets/146747152/193aebe9-ada6-4539-afd4-6ebf52030e2f)


### Личная карточка сотрудника   

Отображает информацию о времени и длительность посещения хранилища отдельным сотрудником.
* Имя и фамилия сотрудника
* Время входа в хранилище
* Время нахождения в хранилище
* Флаг `True`, если время пребывания в хранилище больше 1 часа. Флаг `False`, если меньше.  

![Личная карточка](https://github.com/univernik77/SecurityConsole/assets/146747152/1d2ba9b0-7f79-48e9-a986-d0a309fa4eb4)



### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
