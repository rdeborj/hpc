#!/usr/bin/env python3

from grid.Sge import Sge

hpc = Sge()
test_template = "sge.bash"
context = {
	"jobname": "Job1234",
	"logdir": "log",
	"memory": 8,
	"type": "n",
	"sync": "n",
	"queue": "short",
	"command": "ls -la"}
blah = hpc.render_template(template_filename = test_template, context = context)
print(blah)
hpc.submit_job(jobid="1234")
