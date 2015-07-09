import unittest
from main import MainHandler

class TestSuite(unittest.TestCase):
  def test(self):
    handler = MainHandler()
    score = handler.testGet()
    self.failIf(score != 1)

def main():
  unittest.main()

if __name__ == "__main__":
  main()
