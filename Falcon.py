from vllm import LLM, SamplingParams
import traceback
traceback.print_exc()
import datetime

def _print(txt="HERE"):
    print("{}\t{}".format(datetime.datetime.now(), txt))
_print("Start.")

import os
if os.environ.get('https_proxy'):
    del os.environ['https_proxy']
if os.environ.get('http_proxy'):
    del os.environ['http_proxy']

#model="tiiuae/falcon-40b"
model="tiiuae/falcon-180B-chat"

_print("Instanciating model {}.".format(model))
llm = LLM(model=model, trust_remote_code=True, tensor_parallel_size=8)  # Name or path of your model

_print("Prompting model.")
output = llm.generate("Hello, my name is")

_print("Printing model output")
print(output)


_print("Done.")

