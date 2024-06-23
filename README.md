# Автотесты для сайта hh.ru

[hh.ru](https://hh.ru/)
![img_1.png](img/hh.png)

## Особенности проекта

- Запуск web UI автотестов в Selenoid
- Сборка проекта в Jenkins
- Отчеты Allure Report
- Оповещения о тестовых прогонах в Telegram
- Отчеты с видео, скриншотом, логами, исходной моделью разметки страницы


## Список проверок, реализованных в web UI автотестах
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Выбор города</p> 
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Поиск работы</p> 
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Поиск резюме</p> 
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Поиск компании</p> 
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Проверка выполненых задач</p> 

## Список проверок, реализованных API tests:
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Выбор города</p>
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Поиск работы</p>
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Поиск резюме</p>
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Успешная авторизацияn</p>

## Список проверок, реализованных mobile tests:
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Успешная авторизация</p> 
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Неуспешная авторизация</p>
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Проверка резюме</p>
<p><img width="44" align="center" src="img/active.PNG" alt="checkbox"> Сообщение в тех.поддержку</p>

## Используемый стэк

![img_2.png](img/img_2.png)
<img src="img/browserstack.png" height="48" width="48" />
![img_1.png](img/img_1.png)
![img.png](img/img.png)
![img_2.png](img/img_22.png)
![img_3.png](img/img_353.png)
![img_1.png](img/img_111.png)


## Запуск тестов из терминала
### Для запуска всех автотестов выполнить в cli:
> python -m venv .venv  
> source .venv/bin/activate   
> pip install -r requirements.txt   
> pytest .

### Получение отчета allure:
> allure serve allure-results
> 
> 
## Проект в Jenkins
[Jekins](https://jenkins.autotests.cloud/job/hh_python_project/)


### Запуск автотестов в Jenkins:
1. Открыть [проект](https://jenkins.autotests.cloud/job/hh_python_project/)
2. Build with Parameters ![jek1.png](img/jek1.png)
3. Нажать кпопку Build ![jek2.png](img/jek2.png)


<h2 id="run-tests"><img width="40" align="center" src="img/run-tests.png" alt="run"> Run tests</h2>
<p><b>For web tests:</b></p>
<pre>
    pytest tests/web
</pre>
<p><b>For API tests:</b></p>
<pre>
    pytest tests/api
</pre>
<p><b>For mobile tests on emulator:</b></p>
<pre>
    pytest tests/mobile --context=local_emulator
</pre>
<p><b>For mobile tests on real device:</b></p>
<pre>
    pytest tests/mobile --context=real_local
</pre>
<p><b>For mobile tests on bstack:</b></p>
<pre>
    pytest tests/mobile --context=bstack
</pre>






### [Allure отчет](https://jenkins.autotests.cloud/job/hh_python_project/29/allure/)![allure.png](img/allure.png)

![allure2.png](img/allure2.png)


### [Результат прохождения теста Allure TestOps](https://allure.autotests.cloud/project/4299/dashboards)![allure_tes.png](img/allure_tes.png)


<h2 id="telegram-notification">Оповещения в Telegram <img width="40" align="center" src="img/tt.png" alt="exapmle"></h2>

![img/telegramm.PNG](img/telegramm.PNG)

## [Видео прохождения автотестов](https://selenoid.autotests.cloud/video/93ce3d0fe17922d2d1efc4071cda460d.mp4) ![img_3.png](img/img_3.png)
<img title="Selenoid" src="img/sc.gif"/>

## [Видео прохождение автотестов в мобильной версии](https://app-automate.browserstack.com/sessions/b3d62e0db045e959bb26dd668defc6d081ca2f51/video?token=YzJLVjFKVXNRRTNyQ1g5OEVldk5BdUE5NCtBOHdJSWtqcHQvNzluQk1CamRKRm8yTmNlTm56N2hib0xlc2svS0JYZFVpTFovNzFKTlVnSWRndzNZeHc9PS0teVhzQUhXVzVpUHY2NklYUTI5Sy9UUT09--95eeee272e828880de2260c22359b8ccab0d8203&source=rest_api&diff=1.044777313) ![img/resume.gif](img/resume.gif)




 