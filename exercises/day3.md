### Functions exercises
1. Write a function that takes a number as a parameter and prints its square.
1. Write another function that takes a number as a parameter and returns the square. 
1. Are the results of the two functions above different? Which of the two functions can be used to compute x<sup>2</sup> + y<sup>2</sup> ?
1. Write a function that takes any number of strings and an integer `n` as parameters.
`n` should be an optional parameter. Return the list of strings longer than `n`. 
By default, it should return a list containing all words.

    E.g. 
    * `f('hello', 'hi', 'bye', n=2)` -> `['hello', 'bye']`
    * `f('hello', 'hi')` -> `['hello', 'hi']`
    * `f()` -> `[]`
    * `f(n=10)` -> `[]`
1. Write a function that builds html tags. Apply html escaping for html special chars. 
The function will receive 2 parameters – tag type and tag content and will return the generated html as a string. 
    
    E.g.: `f('b', 'Ham&Eggs')` returns `"<b>Ham&amp;Eggs</b>"`
    
    HTML char escaping:
    * `<` becomes `&lt`;
    * `>` becomes `&gt`;
    * `"` becomes `&quot`;
    * `&` becomes `&amp`;

### Modules and packages exercises
1. Create a Python package with a module in it where you place one of the functions defined above.
1. Create a Python module where you import and call the functions defined above 
(the one from the package and the remaining ones from `<functions_exercises_module>`).

### Comprehensions exercises
1. Create a dict `{"a": 97, "b": 98, ... }` using comprehension. Use `ord` built-in to obtain ASCII code.
Keys range from "a" to "e". 
    ```python
    >>> import string
    >>> string.ascii_lowercase
    'abcdefghijklmnopqrstuvwxyz'
    >>> ord('a')
    97
    ```
1. Using the dictionary generated above, create another one where you swap keys and values. 
1. Filter the above dictionary to contain only even keys. 
1. Can you obtain dictionary from ex. 3 from the given string (`"abcde"`) in a single dict comprehension? 


### Generators exercises
1. Create a generator function that receives a parameter `max_nr` and yields a random number between `1` and `max_nr`, indefinitely. 
    ```python
    >>> import random
    >>> random.randint(1, 10)  # returns a random integer between 1 and 10
    1
    >>> random.randint(1, 10)
    10
    >>> random.randint(1, 10)
    6
    ```
1. Write a generator function that yields unique elements from an iterable received as parameter.

### Aggregations functions exercises
1. Write a function `filter_short_words(word_list, n)` that returns the words in `word_list` shorter than `n`. Use `filter` built-in function.
1. Given a list of tuples `(product, price_eur)`, build the list of `(product, price_ron)`, knowing that the exchange rate is `4.75`. Use `map` built-in function.
    ```python
    def f(tup):
        return (tup[0], tup[1]*4.75)
    ```
1. Write a function that receives any number of strings and returns the list of unique strings ordered by number of appearances (most frequent → least frequent). 
Use `sorted` built-in function.
    
    E.g. `f('hello', 'there', 'hello', 'hi', 'hi', 'hello')` -> `['hello', 'hi', 'there']`
