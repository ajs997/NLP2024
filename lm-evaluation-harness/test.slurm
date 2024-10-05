#!/bin/bash -l                         

# --- Resource related ---             
#SBATCH --ntasks=1
#SBATCH -A uvailp
#SBATCH -t 1:00:00 # Minute:Second
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

#lm_eval --model hf \
    #--model_args pretrained=meta-llama/Llama-2-7b-hf \
    #--tasks arithmetic,asdiv \
    #--device cuda:0 \
    #--batch_size 8
lm_eval --model hf \
    --model_args pretrained=meta-llama/Llama-2-7b-hf,peft=/scratch/zwz3wu/NLP2024/llm-tuning-main/ckp_sst_llama_lora_32_dev_0927 \
    --tasks mmlusr,mmlu \
    --device cuda:0 \
    --batch_size 8

