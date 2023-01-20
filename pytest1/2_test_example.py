def test_equal():
  result = 1 + 2
  assert result == 3

def test_notequal():
  result = 1 + 2
  assert result != 100

def test_string1():
  result = "Hello" + "World"
  assert result == "HelloWorld"

def test_string2():
  string = "HelloWorld"
  assert string.startswith('H')

def test_string3():
  string = "HelloWorld"
  assert "oWo" in string
