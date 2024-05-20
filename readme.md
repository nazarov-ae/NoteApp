# NoteApp
## _Application for working with your notes_

## Features

- Create your own account
- Adding notes
- Editing notes
- Deleting notes
- Searching notes

## Tech

The application works with a SQLite database

## Screenshotes

[![Screenshot-1.jpg](https://i.postimg.cc/qvg3Q4ZK/Screenshot-1.jpg)](https://postimg.cc/FY5zH5vF)
[![Screenshot-2.jpg](https://i.postimg.cc/FRXk9cFb/Screenshot-2.jpg)](https://postimg.cc/sBKgmMh1)
[![Screenshot-3.jpg](https://i.postimg.cc/xTpkXBT1/Screenshot-3.jpg)](https://postimg.cc/crY1j9np)
[![Screenshot-4.jpg](https://i.postimg.cc/tTb70jD2/Screenshot-4.jpg)](https://postimg.cc/CZvwD93q)
[![Screenshot-5.jpg](https://i.postimg.cc/sxXjyDW9/Screenshot-5.jpg)](https://postimg.cc/5YhdSJn6)


## QT
* на практике QT не использовал, поэтому рекомендации даю больше общего плана
* здесь используется подход MVVM, постарайся ему следовать
* если юзаешь QT, обязательно изучи сигналы и слоты 

## Рекомендации
* прочитать PEP в части рекомендаций к оформлению кода, нейминга и форматирования текта
  еще лучше установить либу prospector, прогнать через нее код и пройтись сообщениям
* в readme должны быть описаны шаги как запустить проект у себя локально
* изучить и использовать пакетный менеджер, начать с pip
* добавить файл с зависимостями requirements.txt (к предыдущему пункту)
* добавить обработку ошибок на всех уровнях, ошибки должны
  * логироваться в файл 
  * выводится пользователю в понятном для него виде
* изучить юнит-тестирование и покрыть код тестами (unittest/pytest) 

## MVVM
В концепции архитектуры Model-View-ViewModel (MVVM)
* Model
  содержит бизнес-логику и данные.
  Модель должна быть независима от интерфейса пользователя и не содержать 
  логику представления или управления состоянием пользовательского интерфейса.
* View отвечает за отображение данных пользователю и взаимодействие с
  пользователем, но не должно содержать логику обработки данных.
  Все взаимодействия передаются в ViewModel.
* ViewModel служит посредником между Model и View. ViewModel обращается к
  модели за данными, обрабатывает их (например, преобразует для отображения) и
  обновляет View. ViewModel не должна знать о конкретных элементах View, чтобы
  обеспечить возможность их легкой замены или изменения без влияния на модель
  или ViewModel.
Попробуй изменить код, так чтобы он соответствовал этому концепту.
