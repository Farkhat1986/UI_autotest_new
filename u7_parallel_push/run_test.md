## Параллельный запуск тестов

### Для параллельного запуска используется библиотека pytest-xdist

* ### Для установки данной библиотеки применяется следующая команда:
```commandline
pip install pytest-xdist
```

### Основные команды для запуска тестов, которые прописываются в терминале:

* ### Запуск локально Chrome
```commandline
pytest -n 2 --browser=chrome
```

* ### Запуск локально Firefox
```commandline
pytest -n 2 --browser=firefox
```

* ### Запуск через Selenium Grid
```commandline
pytest -n 4 --browser=chrome --remote
```

* ### Запустим одновременно Chrome и Firefox
```commandline
pytest -n 4 --browser=chrome --remote
pytest -n 4 --browser=firefox --remote

или 

pytest -n 4 --browser=chrome
pytest -n 4 --browser=firefox
```