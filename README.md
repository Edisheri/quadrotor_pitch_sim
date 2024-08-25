# Симуляция Динамики Тангажа Квадрокоптера

## Описание проекта

Этот проект представляет собой программную симуляцию динамики квадрокоптера вдоль оси тангажа с использованием PID-контроллера. Симуляция моделирует эволюцию углового положения, скорости и ускорения квадрокоптера с учетом различных параметров, предоставляя графическое отображение результатов.

## Основные возможности

- **Моделирование вращательной динамики**: Рассчитывает динамику квадрокоптера в канале тангажа.
- **PID-контроллер**: Управляет угловым положением с высокой точностью.
- **Визуализация данных**: Генерация графиков углового положения, скорости и ускорения.

## Установка

1. **Клонирование репозитория**:
    ```bash
    git clone https://github.com/Edisheri/quadrotor_pitch_sim.git
    cd quadrotor_pitch_sim
    ```
2. **Создание виртуального окружения и установка зависимостей**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Использование

1. **Запуск симуляции**:
    ```bash
    python main.py
    ```
2. **Просмотр результатов**: После завершения симуляции откроются графики изменения углового положения, скорости и ускорения квадрокоптера.

## Структура проекта

- `main.py`: Основной скрипт для запуска симуляции.
- `quadrotor.py`: Модуль для моделирования динамики квадрокоптера.
- `pid_controller.py`: Реализация PID-контроллера.
- `visualization.py`: Модуль для построения графиков.

## Конфигурация

Файл `config.yaml` содержит следующие параметры:
- `I`: Момент инерции квадрокоптера.
- `torque_coefficient`: Коэффициент тяги двигателя.
- `setpoint`: Целевое угловое положение.
- `initial_conditions`: Начальные условия (угол и угловая скорость).
- `t_span`: Временной интервал симуляции.
- `t_eval`: Временные точки для расчета.

## Лицензия

Этот проект распространяется под лицензией MIT. См. файл `LICENSE` для получения дополнительной информации.
