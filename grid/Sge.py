import os
import sys
from jinja2 import Environment, FileSystemLoader
import subprocess

class Sge:
	def __init__(self):
		"""
		NAME
		    __init__ -- object initialization method, automatically called when defining an object

		SYNOPSIS
		    from grid.Sge import Sge
		    hpc = Sge()

		DESCRIPTION
		    The initialization method sets up the path and template environment
		    for use with the jinja2 library.
		"""
		self.PATH = os.path.dirname(os.path.abspath(__file__))
		self.TEMPLATE_ENVIRONMENT = Environment(
			autoescape = False,
			loader = FileSystemLoader(os.path.join(self.PATH, 'templates')),
			trim_blocks = False)


	def render_template(self, template_filename, context):
		"""
		NAME
		    obj.render_template(template_filename, context) -- Render a Jinja2 template with values from context

		SYNOPSIS
		    obj.render_template(template_filename = 'template.bash', context = {"jobname": "Job1234"})

		DESCRIPTION
		    This method takes the key-value pairs from the context dictionary and populates
		    the variables in the Jinja2 formatted template.
		"""
		return(self.TEMPLATE_ENVIRONMENT.get_template(template_filename).render(context))


	def create_cluster_shell_script(self, output, template_filename, context):
		"""
		NAME

		SYNOPSIS

		DESCRIPTION
		"""
		with open(output, 'w') as f:
			shell_script = render_template(template_filename, context)
			f.write(output)


	def submit_job(self, jobid):
		"""
		NAME

		SYNOPSIS

		DESCRIPTION
		"""
		print(" ".join(["Submitting job", jobid]))
