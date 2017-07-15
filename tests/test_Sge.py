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
    "submit": False}

hpc_output = hpc.create_cluster_shell_script(
    output = output,
    template_filename = test_template,
    context = context)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(hpc_output)


filecmp.cmp(output, "tests/test_Sge_expected.sh")
print(os.getcwd())

class testSgeMethods(unittest.TestCase):
    def testScript(self):
        self.assertTrue(filecmp.cmp(output, "tests/test_Sge_expected.sh"))
