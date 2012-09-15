import unit_helper
import unittest
import re

from httperf import Httperf

class HttperfTestCase(unittest.TestCase):

    def testInitHttperfWithDefaults(self):
        global httperf0
        httperf0 = Httperf()
        assert httperf0, "Httperf did not instantiate"

    def testInitWithDefaultPathSet(self):
        self.assertEqual(httperf0.path, "httperf")


    def testInitHttperfWithPath(self):
        global httperf1
        httperf1 = Httperf(path=unit_helper.httperf_path)
        assert httperf1, "Httperf did not instantiate with "+httperf_path

    def testInitWithPathSetsPath(self):
        self.assertEqual(httperf1.path, unit_helper.httperf_path)

    def testInitWithArgsCreatesArg(self):
        httperf = Httperf(server="localhost")
        self.assertEqual(httperf.params["server"], "localhost")

    def testInitWithBadArg(self):
        with self.assertRaises(Exception):
            httperf = Httperf(bad="localhost")

    def testUpdateOptionAlreadyCreated(self):
        httperf = Httperf(server="localhost")
        httperf.update_option("server", "newhost")
        self.assertEqual(httperf.params["server"], "newhost")

    def testUpdateOptionNotYetCreated(self):
        httperf = Httperf()
        httperf.update_option("server", "newhost")
        self.assertEqual(httperf.params["server"], "newhost")

    def testRun(self):
        httperf = Httperf()
        global res_string
        res_string = httperf.run()
        self.assertNotEqual(res_string, None)

    def testRunResultsNotEmpty(self):
        self.assertNotEqual(res_string, "")

    def testRunResultsContainsHttperfResults(self):
        m = re.search('httperf --client=0/1 --server=localhost' , res_string)
        self.assertNotEqual(m, None)


if __name__ == "__main__":
    unittest.main()

