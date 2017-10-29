import unittest

from grid.Sge import Sge
import pprint
import filecmp
import os

hpc = Sge()
test_template = "sge.bash"
output = "testoutput.sh"
context = {
    "jobname": "Job1234",
    "logdir": "log",
    "memory": 8,
    "type": "n",
    "sync": "n",
    "queue": "short",
    "command": "ls -la",
    "submit": False,
    "queue": "all.q"
    }

hpc_output = hpc.create_cluster_shell_script(
    output = output,
    template_filename = test_template,
    context = context)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(hpc_output)

class testSgeMethods(unittest.TestCase):
    def testScript(self):
        expected_test_sge_output = "tests/test_Sge_expected.sh"
        self.assertTrue(filecmp.cmp(output, expected_test_sge_output))

    def get_jobid_from_submission_test(self, sge_output):
        sge_output_string = "echo 'Your job 8123354 (\"Job1234\") has been submitted"
        expected_test_sge_jobid = "8123354"
        self.assertTrue(
            hpc.get_jobid_from_submission_output_string(sge_output=sge_output_string) == expected_test_sge_jobid
            )

