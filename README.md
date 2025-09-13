# EN

# Brainduck
An improved version of Brainf#ck, created in Python. Only built-in libraries. Write like a real programmer (no)

•   / - Adds a memory cell with the value 0.
•   > - Moves the memory pointer forward (to the next cell).
•   < - Moves the memory pointer backward (to the previous cell).
•   + - Increments the value in the current memory cell by 1.
•   - - Decrements the value in the current memory cell by 1.
•   ^ - Deletes all memory (clears the memory array).
•   % - Sets the current memory cell to 0 (zeroes out the sector).
•   # - Prints the entire memory array to the console.
•   . - Prints the value of the current memory cell to the console (with a newline).
•   , - Prints the value of the current memory cell to the console (without a newline).
•   ? - Imports a file (using the value in the current memory cell as the filename) and executes it immediately (experimental).
•   ~ - Waits (sleeps) for a specified number of seconds (the value in the current memory cell determines the duration).
•   : - Prints the character corresponding to the ASCII code stored in the current memory cell (with a newline).
•   ; - Prints the character corresponding to the ASCII code stored in the current memory cell (without a newline).
•   | - Appends a space to the console output (without a newline).
•   @text / ['execution before loop', 'code', number of repetitions(as a number)]@ - Assigns a value to the current memory cell, either as plain text or as a cycle array.
•   $ - Executes the code stored in the current memory cell.

The interpreter also supports newlines in the code and ignores any text outside of the recognized commands.

#RU

# Брейндак
Улучшенная версия Brainf#ck, созданная на Python. Только встроенные библиотеки. Пишите как настоящий программист (нет)

/ - добавляет ячейку памяти как 0
> - переход вперед
< - переход назад
+ - плюсует на 1 в текущий сектор
- - минусует на 1 в текущий сектор
^ - удаление всей памяти
% - нулируем сектор
# - выводит память
. - выводит сектор(с новой строки)
, - выводит сектор(не с новой строки)
? - импортирует файл(с помощью значения сектора) и сразу выполняет(экспериментально)
~ - ждет определенное колво секунд(значение сектора)
: - выводит значение сектора как букву(с новой строки)
 - выводит значение сектора как букву(не с новой строки)
| - прибавляет пробел к строке консоли(не с новой строки)
@текст / ['выполнение перед циклом', 'код', колво повторении(как число]@ - задает сектору значение как текст или как массив цикла
$ - выполняет код из значения сектора

поддерживает новые строки и игнорирует текст вне кода
