# nginx-locations

### Полезное

- [Downloading files with curl ](http://www.compciv.org/recipes/cli/downloading-with-curl/)
- [unzip](https://askubuntu.com/questions/86849/how-to-unzip-a-zip-file-from-the-terminal)
- [nginx: alias](http://nginx.org/en/docs/http/ngx_http_core_module.html#alias)
- [nginx location 404 not found](https://stackoverflow.com/questions/41099318/nginx-location-404-not-found)

### Задание

1. Настройте `server` блок, который слушает 8080 порт.
2. Установите `server_name` равным значению `example.com`.
3. Добавьте `location` блок для пути `/`, который обслуживает файл [index.html](https://stepik.org/media/attachments/lesson/686238/index.html). Файл должен быть неизмененным - если будете копировать-вставлять текст из файле, то возможно может добавиться лишний символ.
4. Добавьте `location` блок для пути `/images`, который обслуживает файлы из архива [cats.zip](https://stepik.org/media/attachments/lesson/686238/cats.zip)
5. Добавьте `location` блок для пути `/gifs`, который обслуживает файлы из архива [gifs.zip](https://stepik.org/media/attachments/lesson/686238/gifs.zip)
6. Добавьте `location` блок для пути `/secret_word`, который возвращает строку `jusan-nginx-locations` со статусом `201`.

Чтобы проверить запрос на созданный `server` блок, запустите команду.

```bash
curl -H "Host: example.com" http://localhost:8080/
```

---

### Ответ
root@DESKTOP-8CKU5JA:/etc/nginx# curl -H "Host: example.com" http://localhost:8080/
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cats Page</title>
</head>

<body>
    <p>
    <h1>Cat with Flower</h1>
    <img src="/images/flower.png" alt="flower">
    </p>

    <p>
    <h1>Cat with Glasses</h1>
    <img src="/images/glasses.png" alt="glasses">
    </p>

    <p>
    <h1>Gray Cat</h1>
    <img src="/images/gray-animal.jpeg" alt="gray-animal">
    </p>

    <p>
    <h1>Cats mafia</h1>
    <img src="/images/mafia.png" alt="mafia">
    </p>

    <p>
    <h1>Sleepy Cat</h1>
    <img src="/images/sleep.png" alt="sleep">
    </p>
</body>

</html>root@DESKTOP-8CKU5JA:/etc/nginx# curl -H "Host: example.com" http://localhost:8080/images/
<html>
<head><title>Index of /images/</title></head>
<body>
<h1>Index of /images/</h1><hr><pre><a href="../">../</a>
<a href="__MACOSX/">__MACOSX/</a>                                          24-Oct-2024 12:39                   -
<a href="cats.zip">cats.zip</a>                                           24-Oct-2024 12:39            20746072
<a href="flower.png">flower.png</a>                                         25-Mar-2022 10:14             6173737
<a href="glasses.png">glasses.png</a>                                        25-Mar-2022 10:13             4996355
<a href="gray-animal.jpeg">gray-animal.jpeg</a>                                   25-Mar-2022 10:13              458964
<a href="mafia.png">mafia.png</a>                                          25-Mar-2022 10:15             3772725
<a href="sleep.png">sleep.png</a>                                          25-Mar-2022 10:15             5347316
</pre><hr></body>
</html>
root@DESKTOP-8CKU5JA:/etc/nginx# curl -H "Host: example.com" http://localhost:8080/gifs/
<html>
<head><title>Index of /gifs/</title></head>
<body>
<h1>Index of /gifs/</h1><hr><pre><a href="../">../</a>
<a href="dancing.gif">dancing.gif</a>                                        21-Oct-2024 09:56              253794
<a href="gifs.zip">gifs.zip</a>                                           21-Oct-2024 09:56             4334529
<a href="jam.gif">jam.gif</a>                                            21-Oct-2024 09:56              471720
<a href="sad.gif">sad.gif</a>                                            21-Oct-2024 09:56             3605836
</pre><hr></body>
</html>
root@DESKTOP-8CKU5JA:/etc/nginx# curl -H "Host: example.com" http://localhost:8080/secret_word
jusan-nginx-locationsroot@DESKTOP-8CKU5JA:/etc/nginx#
tail -fn4 /var/log/nginx/access.log
127.0.0.1 - - [24/Oct/2024:17:47:18 +0500] "GET / HTTP/1.1" 200 729 "-" "curl/7.81.0" "-"
127.0.0.1 - - [24/Oct/2024:17:47:21 +0500] "GET /images/ HTTP/1.1" 200 968 "-" "curl/7.81.0" "-"
127.0.0.1 - - [24/Oct/2024:17:47:23 +0500] "GET /gifs/ HTTP/1.1" 200 610 "-" "curl/7.81.0" "-"
127.0.0.1 - - [24/Oct/2024:17:47:28 +0500] "GET /secret_word HTTP/1.1" 201 21 "-" "curl/7.81.0" "-"


