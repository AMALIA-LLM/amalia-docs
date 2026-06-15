#!/bin/bash
#SBATCH --job-name=run_sphinx
#SBATCH -e logs/%x-%j.err
#SBATCH -o logs/%x-%j.out
#SBATCH --time=0
#SBATCH --cpus-per-task=2
#SBATCH --nodelist=nscluster
#SBATCH -n 1 # Number of tasks

set -e  # Exit immediately if a command exits with a non-zero status

eval "$(conda shell.bash hook)"
source activate /home/r.guerra/.conda/envs/sphinx_env

sphinx-autobuild source /data/r.guerra/amalia-sphinx/build/html --port 8503 --host 0.0.0.0
