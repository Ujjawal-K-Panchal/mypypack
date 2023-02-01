# mypypack

This is a repo for practicing package management in python.
Clone this repo. Then don't work in this repo. Go outside this repo (1 level) and follow Tutorial.

This is a quick, partial summary of [JCharisTech's much lengthier and in-depth tutorial](https://www.youtube.com/watch?v=ueuLe4PipiI).

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

## 2. Testing.

1. We require pytest for this: `pip install pytest`.
2. Make folder `tests` as follows: `mkdir Mypypack/mypack/tests`.
3. Now you are free to write unit tests as required. For now, just copy the `Mypypack/mypack/tests/test_greetings.py` file from `this repo` and put it in the `Mypypack/mypack/tests/` folder which you just created.
4. Now cd into `Mypypack` and run:
```python
	pytest mypack #no specification of ut folder. Find and run.
	pytest mypack/tests/ #a ut folder. Find and run.
	pytest mypack/tests/test_greetings.py #single ut file run.
```
5. Do a verbose unit test: `pytest -v mypack`.

## 3. Quality Assessment.

Note: Since we are making a package, we want the code to be of acceptable complexity and quality. Since this code will be rapidly called, reference, read and maintained. Therefore, the following steps are useful for the same.

1. cd into `Mypypack/` folder you created (Ignore if already here).
2. Type: `pip install radon`.
3. See what radon has to offer: `radon`.
3. Compute [cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity#:~:text=Cyclomatic%20complexity%20is%20a%20software,McCabe%2C%20Sr.) of your code: `radon cc mypack`. Output looks as follows:

```
Mypack/mypack/greetings.py
    F 9:0 sayHiTo - A
    F 15:0 sayHelloTo - A
    F 1:0 sayHi - A
    F 5:0 sayHello - A
Mypack/tests/test_greetings.py
    F 7:0 test_greetings - A
    F 4:0 test_version - A
```
4. You will see each file listed with its assessed quality. For eg. consider line : `F 9:0 sayHiTo - A` The startig char `F` is a function, `9:0` is the line. `sayHiTo` is the function name. `A` is received grade. `A` is good. `D` or `E` need work.
5. This was `radon cc` option. There are others available. Check `radon` to find out.
6. Maintanibility index `radon mi` is of particular interest, since we are making a package.


## 4. Used/Unused Dependency Management.

We want our project to be efficient and not install unrequired libraries. Also to remove any unused code.`vulture` provides an excellent solution to this.

1. cd into your folder root: `cd Mypypack` (Ignore if already here).
2. install vulture: `pip install vulture`.
3. type in: `vulture mypack`.

```
mypack/mypack/greetings.py:1: unused import 'math' (90% confidence)
mypack/mypack/greetings.py:11: unused function 'sayHiTo' (60% confidence)
mypack/mypack/greetings.py:17: unused function 'sayHelloTo' (60% confidence)
```
Note: confidence interval since it cannot know with 100% surity if something is somehow used or not. Thisindeterminacy is possible through some `hacky` programming practices.


## 5. Code Formatting.

We want our package to have easy to read, standard formatted code. You can have `black` cleanup your files and format them to the standard `PEP8` compliant code.


1. cd into your folder root: `cd Mypypack` (Ignore if already here).
2. `pip install black`.
3. Copy your `greetings.py` code to another window in your editor without saving it. This is so we can notice how `black` changed our code.
4. run: `black mypack/mypack/greetings.py`
5. If you want to experience how it changes, change around your `greetings.py` with bad formatting and do step 4 again. This will help you appreciate what `black` did.

## 6. TOML file changes.

Note how poetry created a TOML file. Now lets add a few things to it.

1. In `[tool.poetry]` section, below authors line add `readme = "README.md"`.
2. In same section, below readme, add `homepage = "<project homepage link>"`.
3. Similarly add `repository = "<package repo link>"`.
4. Add license: `license = "MIT"`.
5. Add keywords: `keywords = ["package-managment", "packaging", "<your name>"]`.

You can look at the toml format, poetry tool, and choose to add additional files if you choose.

## 7. Final Checks & Building.

Now lets check our package using `poetry` to make sure everything works.

1. cd into your package: `cd Mypypack/mypack`.
2. Run: `poetry check`. If everything works, it should say `All set!`. Otherwise it will point an error.
3. Finally, we build our package using `poetry`: `poetry build`. This will build a `.whl` file and a `.tar.gz` file. These will be pushed to PyPi.
