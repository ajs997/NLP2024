#!/bin/bash -l                         

# --- Resource related ---             
#SBATCH --ntasks=1
#SBATCH -A grad-nlp-cs6501
#SBATCH -t 1:00:00 # Minute:Second
#SBATCH -p gpu # Partation type
#SBATCH --gres=gpu:2 # Request one GPU
#SBATCH --mem-per-cpu=4GB # CPU memory

# Load the modules
module load anaconda cuda cudnn

# Activate the virtual Python environment
conda activate test
export HF_HOME="/huggingface/hub"
export HF_DATASETS_CACHE="/huggingface/datasets"

# Run the test code
# python check_cuda.py
python demo.py
# python demo.py --task train