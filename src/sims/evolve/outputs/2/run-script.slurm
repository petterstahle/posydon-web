#!/bin/bash
#
#Specify email adress for notification:
#SBATCH --mail-user=petter.stahle@gmail.com
#SBATCH --mail-type=ALL
#SBATCH --account=fragkos
#
#SBATCH --job-name=pop-syn
#SBATCH --output=log_%a.out
#SBATCH --error=log_%a.err
#SBATCH --partition=debug-EL7
#SBATCH --ntasks=1
#SBATCH --mem=4000
#SBATCH --time=00:10:00
#SBATCH --cpus-per-task=1

srun python script.py
