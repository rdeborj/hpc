#!/usr/bin/env python3

from grid.Sge import Sge

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
	"command": "ls -la"}

hpc.create_cluster_shell_script(
	output = output,
	template_filename = test_template,
	context = context)


# blah = hpc.render_template(template_filename = test_template, context = context)
hpc.submit_job(jobid="1234")
