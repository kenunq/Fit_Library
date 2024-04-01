<h1 align="center"><p>Fit Library</p></h1>

<br/>

![Python Version](https://img.shields.io/badge/Python-3.11-blue)
![Django Version](https://img.shields.io/badge/Django-5.0.3-blue)
![DRF Version](https://img.shields.io/badge/DRF-3.15-blue)

---

## Запуск проекта на локальном компьютере

**1. Скачайте проект на локальный компьютер**

```
git clone https://github.com/kenunq/Fit_Library.git
```

**2. Создайте виртуальное окружение**

```
python -m venv venv
```

**3. Активируйте виртуальное окружение**

_macOS_

```
. venv/bin/activate
```

_linux_

```
source venv/bin/activate
```

_windows_

```
venv\Scripts\activate
```

**4. Обновите пакетный установщик pip**

```
python -m pip install --upgrade pip
```

**5. Зайдите в рабочую директорию проекта(все дальнейшие действия будут осуществляется в ней)**

```
cd Fit_Library/
```

**6. Установите зависимости необходимые для запуска проекта**

```
pip install -r requirements.txt
```

**7. Примините миграции**

```
python manage.py migrate
```

**8. Загрузите данные в бд**

```
python manage.py loaddata fixtures/data_dump.json
```

**9.Запустите сервер**

```
python manage.py runserver
```

**10. Откройте проект в браузере по адресу**

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

**user-admin:**

```
username: admin
password: admin
```

**Для остановки сервера нажмите `CTRL+C` или `CMD+C`(для mac)**

---

## Запуск проекта на локальном компьютере через [Docker](https://www.docker.com/get-started/)

**1. Скачайте проект на локальный компьютер**

```
git clone https://github.com/kenunq/Fit_Library.git
```

**2. Зайдите в рабочую директорию проекта(все дальнейшие действия будут осуществляется в ней)**

```
cd Fit_Library/
```

**4. Запустите Docker Desktop на пк.**

**5. Создайте образ и запустите контейнер**

```
docker compose up --build
```

**6. Откройте проект в браузере по адресу**

```
http://127.0.0.1:8000/api/schema/swagger-ui/
```

**user-admin:**

```
username: admin
password: admin
```

**Для остановки контейнера нажмите `CTRL+C` или `CMD+C`(для mac) в консоли**
