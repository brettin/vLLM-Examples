# to manage where model weights are downloaded to
export HF_DATASETS_CACHE=/rbscratch/brettin/.cache
export TRANSFORMERS_CACHE=/rbscratch/brettin/.cache
conda activate /rbscratch/brettin/conda_envs/vLLM


from vllm import LLM
from vllm import SamplingParams

llm=LLM(model='openlm-research/open_llama_13b')
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)

prompts = ["What is an R&D 100 award"]
outputs = llm.generate(prompts, sampling_params)

for output in outputs:
	prompt = output.prompt
	generated_text = output.outputs[0].text
	print (generated_text)




Installation:

Installed at -
/lus/grand/projects/CSC249ADOA01/conda_envs/vLLM

conda create --prefix /lus/grand/projects/CSC249ADOA01/conda_envs/vLLM python=3.11


