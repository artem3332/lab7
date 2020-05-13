# Лабораторная работа №7. Задача Коши.
<br>Выполнил студент группы 425</br>
<br>Романов Артём</br>
## Вариант № 18:
Решить методом Хойна задачу Коши
<br>![Image alt](https://github.com/artem3332/lab7/blob/master/raw/1.png)</br>
<br>![Image alt](https://github.com/artem3332/lab7/blob/master/raw/2.png)</br>
с заданной относительной точностью 0,01.
Требуется построение графиков решения y(x),y'(x), а также фазовых траекторий.
Дополнительно: <br></br>
Найти точное решение и сопоставить его с полученным приближенным решением.
Найти с помощью встроенных функций решение и сопоставить его с исходным приближенным решением.
## Теоретическая часть:
Метод Хойна является частным случаем методов Рунге-Кутты второго порядка
![Image alt](https://github.com/artem3332/lab7/blob/master/raw/3.png)
![Image alt](https://github.com/artem3332/lab7/blob/master/raw/4.png)<br></br>
![Image alt](https://github.com/artem3332/lab7/blob/master/raw/5.png)
## Практическая часть:
Программа состоит из 5 функций . В функции U выражено y'' , в функции V произвел замену z=y' , 
в функции Houna_Y_ реализуется метод Хойна для y , в функции Houna_Z_ реализуется метод Хойна для z=y'.
В функции main само решение задачи Коши. 
## Результаты:
В результате работы программы для функции ![Image alt](https://github.com/artem3332/lab7/blob/master/raw/1.png) <br></br>
Мы получили данные графики:
![Image alt](https://github.com/artem3332/lab7/blob/master/raw/res.png)

