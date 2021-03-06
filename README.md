# Саплин Алексей Б05-821
**Задача 2**: Дано регулярное выражение и натуральные числа
`k` и `l`, такие , что `0 <= l < k`. Вывести минимальное `n`, равное `l` по модулю `k`, такое, что язык содержит слова длины `n`

## Алгоритм решения
Будем постепенно обрабатывать наше регулярное выражение в обратной
польской записи, используя стэк. Будем в стэке поддерживать наши состояния.

**Что есть состояние?** Состояние - класс `State`, описанный в `main.py`.
Он хранит словарь, где ключ - остаток по модулю `k`, а значение - минимальная длина слова, длина которого равна значению
ключа по модулю `k`.

**Как мы пересчитываем состояния?** Рассмотрим, как мы это делаем при любой операции
1. **Буква** - дает нам состояние `{1: 1}`
2. **1** - дает нам состояние `{0: 0}`
3. **+** - в качестве нового значения для каждого остатка берем минимальное значение из состояний для этого остатка
4. **.** - для каждого остатка из первого состояния перебираем остаток из второго состояния и пытаемся обновить ответ в
новом состоянии
(сложить остатки по модулю и сложить длины)
5. **∗** - сведем обработку звезды Клини к решению задачи о рюкзаке, заметим, что у нас есть не больше `k` элементов: 
вес предмета - его остаток от деления на `k`, стоимость - длина слова, которая отвечает за этот остаток.
Решаем задачу о рюкзаке и обновляем ответы

Так как мы всегда рассматриваем слова минимальной длины для каждого остатка, и мы рассматриваем все такие слова, то в
финальном состоянии (`final_state` у `Parser`) у нас будут минимальные длины слов для каждого остатка(или `INF` если
слов, с длиной равной `x` по модулю `k` в языке нет). Алгортим корректен

**Сложность алгоритма** - `O(nk^2)`, где `n` - длина регулярного выражения, `k` - из условия. Так как сложность обработки
символа, если он равен **∗** - `O(k^2)`.

## Запуск решения и тестов
### Тесты
Для тестов требуется фреймворк `pytest`. Его можно установить с помощью `pip install pytest` или же выполнить в корне
проекта `pip install -r requirements.txt`.

Запускаются тесты командой `pytest tests.py`

### Решение
Достаточно выполнить `python3 main.py`. Требуемая версия: `Python 3.5+`
