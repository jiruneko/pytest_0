from logging import debug

from django.urls import clear_script_prefix


class TestCase:
  @classmethod
  def setup_class(cls):
    print("setup_class")

  @classmethod
  def teardown_class(cls):
    print("teardown_class")

  def test_test1(self):
    print("test1")

  def test_test2(self):
    print("test2")
