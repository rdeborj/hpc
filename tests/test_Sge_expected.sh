#!/bin/bash

# This is an auto-generated script for Sun Grid Engine Submission

#$ -S /bin/bash
#$ -cwd
#$ -N Job1234
#$ -e log
#$ -o log
#$ -r yes
#$ -l h_vmem=8g
#$ -b n
#$ -sync n
#$ -q <: $queue :>



ls -la

echo EXIT STATUS $?

echo Job ${JOB_ID} -- ${JOB_NAME} Complete!