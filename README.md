# mypypack

This is a repo for practicing package management in python.

## Tutorial.

1. Install [poetry](https://python-poetry.org/docs/).
2. Make folder `mypypack`: `mkdir mypypack`.
3. Make folder `mypack`: `mkdir mypack`.
4. Let Poetry initialize the package: `poetry new mypack`.
5. Move into your package folder: `cd mypack`.
6. Notice the directories it created and the files it put inside the directories.
7. Edit the `mypack.toml` file it created as you like.
8. Let poetry create venv using your .toml file (created inside mypack by poetry): `poetry shell`.
9. Add `greetings.py` (from this repo) to your local `mypack folder`.
10. Play inside poetry python shell:  `python`
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

