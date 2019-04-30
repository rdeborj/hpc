"""
The Sge module provides methods and attributes for jobs to be submitted
to a SGE compatible high performance compute cluster.
"""
import os
import sys
from subprocess import call
from jinja2 import Environment, FileSystemLoader

class Sge(object):
    """
    NAME
        Sge -- A SGE class for parallel job submission

    SYNOPSIS
        hpc = Sge()

    DESCRIPTION
        The Sun Grid Engine (SGE) can be used to run parallel jobs across numerous nodes and
        cores across a network.  The Sge module provides APIs and wrappers for handling
        routine tasks that are typically performed on the command line.
    """
    def __init__(self):
        """
        This is the standard object initialization method that is automatically
        executed when the class is called.  The initialization method sets up
        the path and template environment for use with the jinja2 library.

        NOTE:
            Do not call this method directly.

        USAGE:
            from grid.Sge import Sge
            hpc = Sge()

        ARGUMENTS:
            none

        RETURNS:
            none
        """
        self.template_path = os.path.dirname(os.path.abspath(__file__))
        self.template_environment = Environment(
            autoescape=False,
            loader=FileSystemLoader(os.path.join(self.template_path, 'templates')),
            trim_blocks=False)


    def render_template(self, template_filename, context):
        """
        This method takes the key-value pairs from the context dictionary and populates
        the variables in the Jinja2 formatted template.

        USAGE:
            <object>.render_template(
                template_filename='template.bash',
                context={"jobname":"Job1234"})

        ARGUMENTS:
            * template_filename: name of the template BASH shell file to use (required)

            * context: a dictionary containing attributes and their values for use
                with SGE (required)

        RETURNS:
            Returns a string block containing fully executable BASH script that
            can be submitted to SGE.
        """
        return self.template_environment.get_template(template_filename).render(context)


    def create_cluster_shell_script(self, output, template_filename, context):
        """
        A method for creating and submitting a SGE compatible shell script to a high
        performance compute cluster using the Sun Grid Engine.

        USAGE:
            <object>.create_cluster_shell_script(
                output='output.sh',
                template_filename='file.sh',
                context={"submit": True}

        ARGUMENTS:
            * output: filename for the output shell script (required)

            * template_filename: name of the template BASH shell file to use (required)

            * context: a dictionary containing attributes and their values for use
                with SGE (required)

        RETURNS:
            Returns a dictionary containing attributes including: output
            """
        with open(output, 'w') as output_filehandle:
            shell_script = self.render_template(template_filename, context)
            output_filehandle.write(shell_script)
        if context['submit']:
            self.submit_job(script=output)

        return {"output":output}


    def submit_job(self, script):
        """
        A method for submitting a job to a SGE based high performance compute
        cluster.

        USAGE
            obj.submit_job(script="file.sh")

        ARGUMENTS
            * script: name of the script to submit to SGE

        RETURNS
            Returns a dictionary containing attributes including: jobid
        """
        command = " ".join(["qsub", script])
        print("Command is: ", command)

        try:
            return_code = call(command, shell=True)
            if return_code != 0:
                print("Job submission terminated by signal",
                      -return_code,
                      file=sys.stderr)
            else:
                print("Job submission returned", return_code, file=sys.stderr)
        except OSError as job_error:
            print("Execution failed:", job_error, file=sys.stderr)

    def create_hold_job_string(self, jobs):
        """
        Create the hold_jid string used in job dependencies for SGE.

        USAGE:
            <object>.create_hold_jid_string(list_of_jobs)

        ARGUMENTS:
            * list_of_jobs: a list of jobs to convert to a string formmatted
              for the hold_jid parameter in SGE

        RETURNS:
            Retuns a string containing a comma-separated list of dependent jobs
        """
        return ",".join(jobs)

    def get_jobid_from_submission(self, sge_output, sge_output_jobid_index=2):
        """
        When a job is submitted to SGE, the returned output to STDOUT includes
        the job ID.  This can be used to generate a dependency list of for
        inventory purposes when tracking jobs.

        USAGE:
            <object>.get_jobid_from_submission(sge_output)

        ARGUMENTS:
            * sge_output: output string from SGE when job is submitted
                  (rquired)
            * sge_output_jobid_index: SGE job ID 0-based array location
                  from SGE submission output (default: 2)

        RETURNS:
            Returns a dictionary containing the extracted job ID from the
            input string: {'jobid':<jobid>}
        """
        return sge_output.split()[sge_output_jobid_index]
