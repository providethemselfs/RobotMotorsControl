## Проект RobotMotorsControl

### Общее описание проекта RobotMotorsControl

Цель проекта - сделать ПО, управляющее летающим роботом. Пока данный репозиторий - лишь заготовка, но кто знает, чем все это кончится.  
В настоящий момент реализован простейший алгоритм вычисления перемещения робота вдоль **географической широты** по прямой с заданной **постоянной** скоростью.

### Описание работы с Git
Мною были произведены следующие работы:
* Создан репозиторий **RobotMotorsControl** на платформе [GitHub](https://github.com/providethemselfs/RobotMotorsControl)
* Склонирован на рабочую машину командой _git clone https://github.com/providethemselfs/RobotMotorsControl.git_
* Добавлены файлы _motors_control.py_ и _README.md_
* Сохранены изменения в ветке **master** при помощи команд: 
  * _git add ._
  * _git commit -m "Загружены исходние коды управления моторами робота"_ 
  * _git push origin master_
* Создана новая ветка **feature_new_velocity** посредством команды _git checkout -b feature_new_velocity_
* Улучшена плавность изменения местоположения: дискретизация по времени изменилась с 1 секунды на 0.5 секунд
* Сохранены изменения в репозитории с помощью команд:
  * _git add ._
  * _git commit -m "Повышена плавность работы"_ 
  * _git push origin feature_new_velocity_
* На платформе [GitHub](https://github.com/providethemselfs/RobotMotorsControl) нажал кнопку _Compare & pull request
* Выбрал ветку _feature_new_velocity_ для сравнения, добавил описание запроса на слияние
* Провел ревью, высказал замечания
* Внес изменения и запулил заново
* Создал новый запрос на слияние с веткой master и подтвердил его