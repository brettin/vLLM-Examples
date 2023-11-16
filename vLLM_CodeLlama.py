from vllm import LLM, SamplingParams
import traceback
traceback.print_exc()

import torch

import os
os.environ['HF_DATASETS_CACHE']  = '/gpustor/brettin/.cache'
os.environ['TRANSFORMERS_CACHE'] = '/gpustor/brettin/.cache'

for i in range(torch.cuda.device_count()):
   print(torch.cuda.get_device_properties(i).name)

#llm = LLM(model="codellama/CodeLlama-34b-Instruct-hf", tensor_parallel_size=2, swap_space=1 )
# llm = LLM(model="codellama/CodeLlama-34b-Instruct-hf", tensor_parallel_size=2)
llm = LLM(model="codellama/CodeLlama-7b-Instruct-hf")
traceback.print_exc()


PROMPT = '''def remove_non_ascii(s: str) -> str:
    """ <FILL_ME>
    return result
'''
traceback.print_exc()

# import time
# for n in range(10):
sampling_params = SamplingParams(temperature=0.8, top_p=0.95)
filling = llm.generate(PROMPT, sampling_params)
print(filling)
for output in [filling]:
    print(output[0].prompt)
    print(output[0].outputs)

traceback.print_exc()
# time.sleep(2)


