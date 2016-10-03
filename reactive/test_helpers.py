import shutil
import tempfile
import unittest

import helpers


class ConfigTest(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tempdir)

    def test_write_sysctl_existing(self):
        temp_sysctl_file = self.tempdir + "/sysctl_new"
        helpers.write_sysctl('one', temp_sysctl_file)
        with open(temp_sysctl_file) as f:
            self.assertEqual(f.readline(), "one\n")
        self.assertTrue(True)

    def test_write_sysctl_new(self):
        temp_sysctl_file = self.tempdir + "/sysctl_new"
        helpers.write_sysctl(' one ; two = val w space\t;', temp_sysctl_file)
        with open(temp_sysctl_file) as f:
            self.assertEqual(f.read(), "one\ntwo = val w space\n\n")
        self.assertTrue(True)
