#!/bin/bash -l                         

# --- Resource related ---             
#SBATCH --ntasks=1
#SBATCH -A uvailp
#SBATCH -t 30:00:00 # Minute:Second
#SBATCH -p gpu # Partation type
#SBATCH --gres=gpu:2 # Request one GPU
#SBATCH --mem-per-cpu=32GB # CPU memory

# Load the modules
module load anaconda cuda cudnn

# Activate the virtual Python environment
conda activate test
export HF_HOME="/scratch/zwz3wu/huggingface/hub"
export HF_DATASETS_CACHE="/scratch/zwz3wu/huggingface/datasets"

# Run the test code
# python check_cuda.py
# python demo.py
python demo.py --task train


# --model_args pretrained=EleutherAI/gpt-j-6b,parallelize=True,load_in_4bit=True,peft=nomic-ai/gpt4all-j-lora