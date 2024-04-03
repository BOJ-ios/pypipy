# pypipy

## Contained functions

1. adder

```python
def addAll(*args):
    return sum(args)
```

2. multiplier

```python
def mulAll(*args):
    result = 1
    for i in range(len(args)):
        result *= args[i]
    return result
```

3. a-b

```python
def aMinusB(a, b):
    return a - b
```

4. info

```python
def info():
    print("나만의 패키지")
```
