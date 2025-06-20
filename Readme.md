## Variables and Data_Types

## Data_Types: 

| 🔢 No. | Type Category     | Type Name                   | Example                | Description                        |
| ------ | ----------------- | --------------------------- | ---------------------- | ---------------------------------- |
| 1️⃣    | Numeric           | `int`                       | `x = 10`               | Integer numbers                    |
| 2️⃣    | Numeric           | `float`                     | `x = 3.14`             | Decimal numbers                    |
| 3️⃣    | Numeric           | `complex`                   | `x = 3 + 4j`           | Complex numbers (real + imaginary) |
| 4️⃣    | Text              | `str`                       | `x = "hello"`          | String of characters               |
| 5️⃣    | Boolean           | `bool`                      | `x = True`             | Logical values: True or False      |
| 6️⃣    | None Type         | `NoneType`                  | `x = None`             | Represents null / empty value      |
| 7️⃣    | Sequence          | `list`                      | `[1, 2, 3]`            | Ordered, changeable collection     |
| 8️⃣    | Sequence          | `tuple`                     | `(1, 2, 3)`            | Ordered, unchangeable collection   |
| 9️⃣    | Sequence          | `range`                     | `range(5)`             | Sequence of numbers                |
| 🔟     | Set               | `set`                       | `{1, 2, 3}`            | Unordered, no duplicate values     |
| 1️⃣1️⃣ | Set               | `frozenset`                 | `frozenset({1, 2, 3})` | Immutable set                      |
| 1️⃣2️⃣ | Mapping           | `dict`                      | `{"a": 1}`             | Key-value pairs                    |
| 1️⃣3️⃣ | Binary            | `bytes`                     | `b'hello'`             | Immutable binary data              |
| 1️⃣4️⃣ | Binary            | `bytearray`                 | `bytearray([65, 66])`  | Mutable binary data                |
| 1️⃣5️⃣ | Binary            | `memoryview`                | `memoryview(b'hello')` | Memory view object                 |
| 1️⃣6️⃣ | Functional        | `function`                  | `def fun(): pass`      | User-defined or built-in functions |
| 1️⃣7️⃣ | Callable/Advanced | `lambda`, `class`, `object` | `lambda x: x*2`        | Functional or object types         |


## Variables 

| 🔢 No. | Category                  | Example                         | Description                             |
| ------ | ------------------------- | ------------------------------- | --------------------------------------- |
| 1️⃣    | **Standard Variable**     | `x = 10`                        | A normal variable                       |
| 2️⃣    | **Multiple Assignment**   | `a, b = 5, 6`                   | Assign multiple values at once          |
| 3️⃣    | **Same Value Assignment** | `x = y = z = 100`               | Assign same value to multiple variables |
| 4️⃣    | **Swapping Variables**    | `a, b = b, a`                   | Swap values in one line                 |
| 5️⃣    | **Dynamic Typing**        | `a = 5 → a = "hello"`           | Type can change at runtime              |
| 6️⃣    | **Type Hinting**          | `x: int = 5`                    | Optional: Suggests expected type        |
| 7️⃣    | **Constant (Convention)** | `PI = 3.14`                     | Treated as constant (all caps)          |
| 8️⃣    | **Local Variable**        | Defined in function             | Exists only inside that function        |
| 9️⃣    | **Global Variable**       | `global x` used inside func     | Defined outside function, used inside   |
| 🔟     | **Nonlocal Variable**     | `nonlocal x` inside nested func | Used in nested functions                |
| 1️⃣1️⃣ | **Class Variable**        | `self.count = 0`                | Shared across all instances of a class  |
| 1️⃣2️⃣ | **Instance Variable**     | Defined as `self.name`          | Unique to each object of a class        |
| 1️⃣3️⃣ | **Temporary Variable**    | `for i in range(5)`             | Exists during loop or operation         |
| 1️⃣4️⃣ | **Del Variable**          | `del x`                         | Deletes variable from memory            |
| 1️⃣5️⃣ | **Function as Variable**  | `f = lambda x: x*2`             | Assign function to a variable           |


## Checking Data_Types

| 🔢 No. | Method                         | Syntax / Example                    | Use Case / Description                              |
| ------ | ------------------------------ | ----------------------------------- | --------------------------------------------------- |
| 1️⃣    | `type()`                       | `type(a)`                           | Most basic and official way to find the type        |
| 2️⃣    | `isinstance()`                 | `isinstance(a, int)`                | Check if variable is of a specific type             |
| 3️⃣    | `__class__`                    | `a.__class__`                       | Returns the class object of the variable            |
| 4️⃣    | `__class__.__name__`           | `a.__class__.__name__`              | Gives the type name as a clean string               |
| 5️⃣    | `type(a).__name__`             | `type(a).__name__`                  | Clean string format of the variable’s type          |
| 6️⃣    | `match type(a):`               | Python 3.10+ only                   | Pattern matching based on data type                 |
| 7️⃣    | `callable()`                   | `callable(obj)`                     | Checks if a variable is a function or callable      |
| 8️⃣    | `eval() + type()`              | `type(eval("5+5"))`                 | Check type of a string expression at runtime        |
| 9️⃣    | `vars()`                       | `vars(obj)`                         | Shows internal attributes of a class object         |
| 🔟     | `dir()`                        | `dir(a)`                            | Lists all methods and properties of an object       |
| 1️⃣1️⃣ | `get_type_hints()`             | `get_type_hints(func)`              | Extracts type annotations from functions or classes |
| 1️⃣2️⃣ | `inspect.getclasstree()`       | `inspect.getclasstree([type(a)])`   | Displays class hierarchy for inspection             |
| 1️⃣3️⃣ | `types.FunctionType` etc.      | `isinstance(f, types.FunctionType)` | For checking specific function/lambda types         |
| 1️⃣4️⃣ | `globals()['a']` / `locals()`  | `globals()['a']`                    | Access and inspect variables dynamically at runtime |
| 1️⃣5️⃣ | `__annotations__`              | `func.__annotations__`              | Access type hints directly from function/class      |
| 1️⃣6️⃣ | `json.dumps()` with try/except | `json.dumps(a)`                     | Check if a variable is JSON serializable            |
| 1️⃣7️⃣ | `__dir__()`                    | `a.__dir__()`                       | Same as `dir()`, but as a method                    |
| 1️⃣8️⃣ | `__repr__()` or `str()`        | `a.__repr__()`                      | Shows how the object is represented as a string     |
| 1️⃣9️⃣ | `a.__class__ is int`           | `if a.__class__ is int:`            | Identity-based comparison for type                  |
| 2️⃣0️⃣ | `f"{a} is {type(a)}"`          | Formatted string using `f""`        | Smart display with value and type                   |


## Conditional statement

| 🔢 No. | 🔸 Concept Name                  | 🔍 Description                                                                 | 🧪 Example / Syntax                               |
| ------ | -------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------- |
| 1      | `if` Statement                   | Basic condition check.                                                         | `if age > 18:`                                    |
| 2      | `if...else` Statement            | Two-way decision: True → A, False → B                                          | `if n % 2 == 0: print("Even") else: print("Odd")` |
| 3      | `if...elif...else`               | Multiple conditions.                                                           | `if marks > 90: ... elif > 70: ... else: ...`     |
| 4      | `and`, `or`, `not` (Logical)     | Combine multiple conditions in `if`.                                           | `if age > 18 and has_id:`                         |
| 5      | Chained Comparisons              | Clean syntax for range conditions.                                             | `if 10 < x < 100:`                                |
| 6      | Membership: `in`, `not in`       | Check if a value exists in a sequence.                                         | `if item in ['pen', 'book']:`                     |
| 7      | Ternary Operator                 | One-line short if-else.                                                        | `status = "Pass" if marks >= 33 else "Fail"`      |
| 8      | Nested `if`                      | `if` inside another `if`.                                                      | `if age > 18: if gender == "M": ...`              |
| 9      | Boolean Flag Conditions          | Use variables like `is_ready`, `logged_in`.                                    | `if not logged_in:`                               |
| 10     | Dictionary as Switch             | Use `dict.get()` as alternative to `if-elif` chain.                            | `{"add": a + b, "sub": a - b}.get(op, "Invalid")` |
| 11     | `match-case` (Python 3.10+)      | Real `switch-case` style logic.                                                | `match var: case 1: ... case 2: ... case _: ...`  |
| 12     | `assert` as Condition            | Raise error if condition fails (used in testing).                              | `assert age >= 18, "Underage"`                    |
| 13     | Conditions in `loops`, `try`     | Use `if` inside `for`, `while`, `try` for control flow.                        | `for i in range(5): if i == 3: break`             |
| 14     | Short-circuiting with `and`/`or` | Conditions that execute only if needed (`and` skips second if first is False). | `x > 0 and print("x is positive")`                |
