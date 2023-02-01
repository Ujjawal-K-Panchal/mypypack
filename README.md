# mypypack

This is a repo for practicing package management in python.
Clone this repo. Then don't work in this repo. Go outside this repo (1 level) and follow Tutorial.

## 1. Tutorial.

1. Install [poetry](https://python-poetry.org/docs/).
2. Make folder `Mypypack`: `mkdir Mypypack`.
3. Make folder `mypack`: `mkdir Mypypack/mypack`.
4. cd into Mypack: `cd Mypypack`/
5. Let Poetry initialize the package: `poetry new mypack`.
6. Move into your package folder: `cd mypack`.
7. Notice the directories it created and the files it put inside the directories.
8. Edit the `mypack.toml` file it created as you like.
9. Let poetry create venv using your .toml file (created inside mypack by poetry): `poetry shell`.
10. Add `greetings.py` (from this repo) to your local `mypack folder`.
11. Play inside poetry python shell: `python`
```python
	>>> from mypack import greetings
	>>> greetings.sayHi()
	'Hi!'
	>>> greetings.sayHello()
	'Hello!'
	>>> import mypack #demonstrate an error that we later solve.
	>>> mypack.greetings.sayHi() #will give an error.
	AttributeError: module 'mypack' has no attribute 'greetings'
```
11. Go inside `./mypack/__init__.py` and add the following line to top: `from . import greetings`.
12. Now see the error vanish:
```python
	>>> import mypack
	>>> mypack.greetings.sayHi()
	'Hi!'
```

### 1.1. Testing.

1. We require pytest for this: `pip install pytest`.
2. Make folder `tests` as follows: `mkdir Mypypack/mypack/tests`.
3. Now you are free to write unit tests as required. For now, just copy the `Mypypack/mypack/tests/test_greetings.py` file from `this repo` and put it in the `Mypypack/mypack/tests/` folder which you just created.
4. Now cd into `Mypypack` and run `pytest mypack`. Note you can just also type `pytest` or `pytest mypack/tests/`. Or the full path: `pytest mypack/tests/test_greetings.py`. You can even get out of this repo. In this case, `pytest` will find all test files and do unit tests one by one.
5. Do a verbose unit test: `pytest -v mypack`.

 
