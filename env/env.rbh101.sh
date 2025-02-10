export HF_DATASETS_CACHE=/rbscratch/brettin/.cache
export TRANSFORMERS_CACHE=/rbscratch/brettin/.cache  # depricated
export HF_HOME=/rbscratch/brettin/.cache

export PATH=${PATH}:/home/brettin/anaconda3/bin
conda activate vllm-0.6.6-post1

# export OMP_NUM_THREADS=192
# When setting:
# --kv-cache-dtype fp8
# export VLLM_ATTENTION_BACKEND=FLASHINFER
