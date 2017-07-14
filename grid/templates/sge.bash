#!/bin/bash

# This is an auto-generated script for Sun Grid Engine Submission

#$ -S /bin/bash
#$ -cwd
#$ -N {{ jobname }}
#$ -e {{ logdir }}
#$ -o {{ logdir }}
#$ -r yes
#$ -l h_vmem={{ memory }}g
#$ -b {{ type }}
#$ -sync {{ sync }}
#$ -q <: $queue :>

{{ hold_for }}

{{ command }}

echo EXIT STATUS $?

echo Job ${JOB_ID} -- ${JOB_NAME} Complete!