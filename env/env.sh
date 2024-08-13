export HF_DATASETS_CACHE=/rbscratch/vllm/.cache
export TRANSFORMERS_CACHE=/rbscratch/vllm/.cache  # depricated
export HF_HOME=/rbscratch/vllm/.cache

export PATH=${PATH}:/home/brettin/anaconda3/bin
conda activate /rbscratch/brettin/conda_envs/vLLM
