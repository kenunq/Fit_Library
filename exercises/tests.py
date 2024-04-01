from rest_framework.test import APITestCase

from exercises.models import Exercise


class ExerciseTest(APITestCase):
    @classmethod
    def setUp(cls):
        cls.user1_username = "user1"
        cls.user1_password = "qaz123WSX."
        cls.user1_email = "test@test.ru"

        cls.exercise1_data = {
            "name": "Подтягивания",
            "description": "Упражнение на мышцы спины и рук, выполняемое подтягиванием тела вверх\
            до касания или приближения подбородка к перекладине.",
            "type_exercise": "Силовые",
            "difficulty": "Средний",
            "duration": "5 минут",
            "repeats": "3 подхода по 5 повторений",
        }

        cls.exercise2_data = {
            "name": "Отжимания",
            "description": "Упражнение на мышцы груди, рук и плеч, выполняемое отталкиванием тела\
            от пола до полного выпрямления рук.",
            "type_exercise": "Силовые",
            "difficulty": "Для начинающих",
            "duration": "5 минут",
            "repeats": "3 подхода по 10 повторений",
        }

        cls.exercise1 = Exercise.objects.create(
            name="Приседания",
            description="Приседания - это упражнение для развития силы и гибкости в нижней части тела. Оно включает\
            глубокое сгибание коленей и опускание бедер к пятам, сохраняя спину прямой.",
            type_exercise="Силовые",
            difficulty="Для начинающих",
            duration="5 минут",
            repeats="3 подхода по 20 раз",
        )

    def test_get_exercise(self):
        response = self.client.get("/api/v1/exercises/")

        self.assertEqual(response.status_code, 401)  # Пользователь не авторизован

        response = self.client.post(
            "/auth/users/",
            data={"email": self.user1_email, "username": self.user1_username, "password": self.user1_password},
        )

        self.assertEqual(response.status_code, 201)  # Регистрация прошла успешно

        response = self.client.post(
            "/auth/jwt/create/", data={"username": self.user1_username, "password": self.user1_password}
        )

        self.assertEqual(response.status_code, 200)  # Аутентификация прошла успешно

        token = response.data["access"]

        response = self.client.get("/api/v1/exercises/", headers={"Authorization": f"JWT {token}"})

        self.assertEqual(response.status_code, 200)  # Авторизованный пользователь получил данные

        response = self.client.get("/api/v1/exercises/1/", headers={"Authorization": f"JWT {token}"})

        self.assertEqual(response.status_code, 200)

    def test_post_exercise(self):
        response = self.client.post("/api/v1/exercises/", data=self.exercise2_data)

        self.assertEqual(response.status_code, 401)  # Пользователь не авторизован

        response = self.client.post(
            "/auth/users/",
            data={"email": self.user1_email, "username": self.user1_username, "password": self.user1_password},
        )

        self.assertEqual(response.status_code, 201)  # Регистрация прошла успешно

        response = self.client.post(
            "/auth/jwt/create/", data={"username": self.user1_username, "password": self.user1_password}
        )

        self.assertEqual(response.status_code, 200)  # Аутентификация прошла успешно

        token = response.data["access"]

        response = self.client.post(
            "/api/v1/exercises/", data=self.exercise2_data, headers={"Authorization": f"JWT {token}"}
        )

        self.assertEqual(response.status_code, 201)

    def test_put_exercise(self):
        response = self.client.put("/api/v1/exercises/1/", data=self.exercise1_data)

        self.assertEqual(response.status_code, 401)

        response = self.client.post(
            "/auth/users/",
            data={"email": self.user1_email, "username": self.user1_username, "password": self.user1_password},
        )

        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/auth/jwt/create/", data={"username": self.user1_username, "password": self.user1_password}
        )

        self.assertEqual(response.status_code, 200)

        token = response.data["access"]

        response = self.client.put(
            "/api/v1/exercises/1/", data=self.exercise1_data, headers={"Authorization": f"JWT {token}"}
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.data["name"], self.exercise1_data["name"])  # Данные изменены

    def test_delete_exercise(self):
        response = self.client.delete("/api/v1/exercises/1/")

        self.assertEqual(response.status_code, 401)

        response = self.client.post(
            "/auth/users/",
            data={"email": self.user1_email, "username": self.user1_username, "password": self.user1_password},
        )

        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/auth/jwt/create/", data={"username": self.user1_username, "password": self.user1_password}
        )

        self.assertEqual(response.status_code, 200)

        token = response.data["access"]

        response = self.client.get("/api/v1/exercises/1/", headers={"Authorization": f"JWT {token}"})

        response = self.client.delete("/api/v1/exercises/1/", headers={"Authorization": f"JWT {token}"})

        self.assertEqual(response.status_code, 204)

        response = self.client.get("/api/v1/exercises/1/", headers={"Authorization": f"JWT {token}"})

        self.assertFalse(response.data.get("name"))  # Данные были удалены

    def test_filter_exercises(self):
        response = self.client.post(
            "/auth/users/",
            data={"email": self.user1_email, "username": self.user1_username, "password": self.user1_password},
        )

        self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/auth/jwt/create/", data={"username": self.user1_username, "password": self.user1_password}
        )

        self.assertEqual(response.status_code, 200)

        token = response.data["access"]

        response = self.client.post(
            "/api/v1/exercises/", data=self.exercise1_data, headers={"Authorization": f"JWT {token}"}
        )

        self.assertEqual(response.status_code, 201)  # Данные созданны

        response = self.client.get("/api/v1/exercises/", headers={"Authorization": f"JWT {token}"})

        self.assertEqual(len(response.data["result"]), 2)  # Без фильтрации мы получаем 2 объекта

        response = self.client.get("/api/v1/exercises/?difficulty=Средний", headers={"Authorization": f"JWT {token}"})

        self.assertEqual(len(response.data["result"]), 1)  # С фильтрацией мы получаем 1 объект

        self.assertNotIn("Для начинающих", response.data)  # Данных с уровнем сложности "Для начинающих" нету
