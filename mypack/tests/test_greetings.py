from mypack import __version__
from mypack import greetings

def test_version():
	assert __version__ == "1.0.0"

def test_greetings():
	assert greetings.sayHi() == "Hi!", f"{greetings.sayHi} broken!"
	assert greetings.sayHello() == "Hello!", f"{greetings.sayHello} broken!"