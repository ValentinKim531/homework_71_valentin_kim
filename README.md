## 1. 🌍 Пароли и логины для входа и тестирования приложения

<table>
    <tr>
        <th>Вход для:</th>
        <th>Логин</th>
        <th>Пароль</th>
    </tr>
    <tr>
        <td>администратора(admin)</td>
        <td>vvkim@mail.ru</td>
        <td>1234</td>
    </tr>
    <tr>
        <td>пользователя</td>
        <td>jane@mail.ru</td>
        <td>1234</td>
    </tr>
</table>

---

 # 🧑‍💻 API для проекта "Инстаграм". 

 ## 📃 CRUD для публикаций
---

 **Для аутентификации пользователя необходимо:**

 *  запустить приложение путем набора следующей команды в терминале `./manage.py runserver`
 *  в приложении `POSTMAN` 
  <a href="https://www.postman.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354202/postman-icon.svg" alt="postman" width="20" height="20"/> </a> , используя метод `POST`, указать следущий путь, на примере пользователя с *id=1*: 
  
```python
    http://127.0.0.1:8000/api/login/
```

*  добавить в `Body > raw` словарик данных пользователя `(логин и пароль)`: 

```python
{  
    "username": "vvkim@mail.ru",  
    "password": "1234"  
}
```

* нажать кнопку `Send`

* из результата запроса скопировать значение ключа `token` и вставить его в 
`Headers`: в поле `Key` добавить `Authorization`, в поле `Value` вставить сам `token` в следующем виде: `Token <скопированный ключ>`


## 📝 Post list
 **Для просмотра `постов` необходимо:**
* в приложении `POSTMAN` 
  <a href="https://www.postman.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354202/postman-icon.svg" alt="postman" width="20" height="20"/> </a> , используя метод `GET`, указать следущий путь: 
  
```python
    http://127.0.0.1:8000/api/posts
```

и нажать кнопку `Send`

## 📝 Post detail

**Для детального просмотра `поста` необходимо:**

 * в приложении `POSTMAN` <a href="https://www.postman.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354202/postman-icon.svg" alt="postman" width="20" height="20"/> </a>, используя метод `GET`, указать следущий путь, на примере `поста` с *id=6*: 

```python
    http://127.0.0.1:8000/api/posts/6
```
 * нажать кнопку `Send`

***Результат запроса будет отражен в следующем виде:***

```python
    {
    "id": 6,
    "description": "no words...",
    "image": "http://127.0.0.1:8000/uploads/posts/ocean.jpeg",
    "author": 1,
    "created_at": "2023-03-28T10:06:44.904000Z",
    "updated_at": "2023-04-25T07:41:18.383645Z"
}
```

---
## 📝 Post update

**Для редактирования `поста` необходимо:**

 *  в приложении `POSTMAN` <a href="https://www.postman.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354202/postman-icon.svg" alt="postman" width="20" height="20"/> </a>, используя метод `PUT`, указать следущий путь, на примере `поста` с *id=6*:
  
```python 
    http://127.0.0.1:8000/api/posts/6/
```

 *  добавить в `Body > raw` словарик данного `поста` с желаемыми изменениями для обновления, например: 

```python
    {  
    "description": "no words new update",
    "author": 1
} 
```

 * нажать кнопку `Send`
  
***Результат запроса будет отражен в следующем виде:***

```python
    {
    "id": 6,
    "description": "no words new update",
    "image": "http://127.0.0.1:8000/uploads/posts/ocean.jpeg",
    "author": 1,
    "created_at": "2023-03-28T10:06:44.904000Z",
    "updated_at": "2023-04-25T08:09:38.965355Z"
}
```

## 📝 Post create

**Для добавления нового `поста` необходимо:**

 * в приложении `POSTMAN` <a href="https://www.postman.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354202/postman-icon.svg" alt="postman" width="20" height="20"/> </a>, используя метод `POST`, указать следущий путь: 

```python
    http://127.0.0.1:8000/api/posts/
```

*  добавить в `Body > raw` словарик данного `поста` с желаемыми изменениями для обновления, например: 

```python
{  
    "description": "new post",
    "author": 1
}  
```

 * нажать кнопку `Send`

 ***Результат запроса будет отражен в следующем виде:***

```python
    {
    "id": 9,
    "description": "new post",
    "image": null,
    "author": 1,
    "created_at": "2023-04-25T08:24:54.352098Z",
    "updated_at": "2023-04-25T08:24:54.352131Z"
}
```


---
## 📫 Post delete

**Для удаления `поста` необходимо:**

 *  в приложении `POSTMAN` <a href="https://www.postman.com/" target="_blank" rel="noreferrer"> <img src="https://www.svgrepo.com/show/354202/postman-icon.svg" alt="postman" width="20" height="20"/> </a>, используя метод `DELETE`, указать следущий путь, на примере задачи с *id=6*: 
  
```python
    http://127.0.0.1:8000/api/posts/6/
```

 * нажать кнопку `Send`



















