import unittest
import json
from time import time

from mock import mock, mock_open, patch
from lib.behaviors import compute

class BehaviorRepositoryTests(unittest.TestCase):
  def test_config_good_values(self):
    com = compute.Compute("")
    config = com.get_configuration("[1000,2000]")
    self.assertEqual(config[compute.MIN_KEY], 1000)
    self.assertEqual(config[compute.MAX_KEY], 2000)

  def test_config_bad_json(self):
    com = compute.Compute("")
    config = com.get_configuration("1000,2000]")
    self.assertEqual(config, None)

  def test_config_one_value(self):
    com = compute.Compute("")
    config = com.get_configuration("[1000]")
    self.assertEqual(config, None)

  def test_config_non_integer_value(self):
    com = compute.Compute("")
    config = com.get_configuration("[1000, 'test']")
    self.assertEqual(config, None)

  def test_config_bad_range(self):
    com = compute.Compute("")
    config = com.get_configuration("[1000, 500]")
    self.assertEqual(config, None)

  def test_config_no_values(self):
    com = compute.Compute("")
    config = com.get_configuration("[]")
    self.assertEqual(config, None)

  def test_config_three_values(self):
    com = compute.Compute("")
    config = com.get_configuration("[1000,2000,5,50]")
    self.assertEqual(config[compute.MIN_KEY], 1000)
    self.assertEqual(config[compute.MAX_KEY], 2000)

  def test_sample_returns_same_value_for_seed(self):
    com = compute.Compute("")
    val = com.sample(1, 100, 200)
    self.assertEqual(val, 155)

  def test_sample_returns_value_in_range(self):
    com = compute.Compute("")
    val = com.sample(time(), 100, 200)
    self.assertGreaterEqual(val, 100)
    self.assertLessEqual(val, 200)

if __name__ == '__main__':
    unittest.main()            