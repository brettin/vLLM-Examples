# proxy settings
export HTTP_PROXY="http://proxy.alcf.anl.gov:3128"
export HTTPS_PROXY="http://proxy.alcf.anl.gov:3128"
export http_proxy="http://proxy.alcf.anl.gov:3128"
export https_proxy="http://proxy.alcf.anl.gov:3128"
export ftp_proxy="http://proxy.alcf.anl.gov:3128"
export no_proxy="admin,polaris-adminvm-01,localhost,*.cm.polaris.alcf.anl.gov,polaris-*,*.polaris.alcf.anl.gov,*.alcf.anl.gov"

module load conda
#module load cudatoolkit-standalone/12.0.0
conda activate /lus/grand/projects/CSC249ADOA01/conda_envs/vLLM

export HF_DATASETS_CACHE=/lus/grand/projects/CSC249ADOA01/brettin/.cache/
export TRANSFORMERS_CACHE=/lus/grand/projects/CSC249ADOA01/brettin/.cache/
export HF_HOME=/lus/grand/projects/CSC249ADOA01/brettin/.cache
