#!/bin/bash

# This is an autogenerated script for Torque PBS

#PBS -S /bin/bash
#PBS -N {{ jobname }}
#PBS -e {{ logdir }}
#PBS -o {{ logdir }}
#PBS -V
#PBS -l vmem={{ memory }}g
#PBS -l mem={{ memory }}g
#PBS -l walltime={{ walltime }}
{{ localhd }}
{{ cores }}
{{ hold_for }}

export TMPDIR={{ tmpdir }}

{{ modules_to_load }}

# change to the working directory
cd {{ working_directory }}

{{ command }}

echo EXIT STATUS $?

echo Job ${PBS_JOBID} -- ${PBS_JOBNAME} Complete!