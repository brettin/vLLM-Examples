**Table of content:**
- [Managing Model Weight Files](#model_weights)
- [Basics to start a ray cluster for parallel inferencing](#ray_start)
- [Starting the ray cluster and the vllm api_server](#vllm_server_start)
- [Example Inferencing](#example)
- [Pre-installation on a back end polaris node](#pre_install_polaris)
- [Installation](#installation)
- [Tunnels](#tunnels)


<a id="model_weights"></a>
### To manage where model weights are downloaded to
	export HF_DATASETS_CACHE=/rbscratch/brettin/.cache
	export TRANSFORMERS_CACHE=/rbscratch/brettin/.cache

 or

 	import os
  	os.environ['HF_DATASETS_CACHE'] = '/rbscratch/brettin/.cache'
   	os.environ['TRANSFORMERS_CACHE'] = '/rbscratch/homes/brettin/.cache'


<a id="ray_start"></a>
### Basics to start a ray cluster for parallel inferencing
The default port is 6379 and can be modified with the --port option.

	ray start --head
	ray start --address='140.221.84.8:6379'    # the address and port are
 	ray start --address='140.221.84.8:6379'    # this starts a second worker


<a id="vllm_server_start"></a>
### Starting the ray cluster and the vllm api_server.

Start the head node, add another node to this Ray cluster, and start the vllm api server.

	ray start --head --port 6379 --num-cpus 64 --num-gpus 8
	ray start --address='140.221.79.202:6379' --num-cpus 64 --num-gpus 8
 	python -m vllm.entrypoints.api_server --model mistralai/Mistral-7B-v0.1 --tensor-parallel-size 8 --host localhost --port 8000

If you want to start the ray cluster but only use certian GPUs, set CUDA_VISIBLE_DEVICES 

	CUDA_VISIBLE_DEVICES="0,1,2,3" ray start --head --port 6379 --num-cpus 64 --num-gpus 8

To run on a v100 that doesn't support bf16

	python -m vllm.entrypoints.openai.api_server --api-key xxxx --model meta-llama/Meta-Llama-3-8B-Instruct --dtype float16 --tensor-parallel-size 8 --host localhost --port 6379
 
<a id="example"></a>
### Example

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


<a id="pre_install_polaris"></a>
### Pre-installation on a back end polaris node:
	module load conda
	https_proxy=http://proxy.alcf.anl.gov:3128
	http_proxy=http://proxy.alcf.anl.gov:3128
	conda activate /lus/grand/projects/CSC249ADOA01/conda_envs/vLLM


### Installed at -
	/lus/grand/projects/CSC249ADOA01/conda_envs/vLLM
 	/lambda_stor/software/conda_envs/vLLM
  	/rbscratch/brettin/conda_envs


<a href="installation"></a>
### Installation:

	# While this worked previously, it seems not to anymore:
 	# conda create --prefix /lus/grand/projects/CSC249ADOA01/conda_envs/vLLM python=3.11
	conda create --prefix /lus/grand/projects/CSC249ADOA01/conda_envs/vLLM python=3.9
	conda activate /lus/grand/projects/CSC249ADOA01/conda_envs/vLLM
	pip install git+https://github.com/huggingface/transformers.git@main accelerate
	pip install git+https://github.com/vllm-project/vllm.git@main
	pip install jupyter
	pip install ray


	# While this worked previously, it seems not to anymore:
 	# conda create --prefix /rbscratch/brettin/conda_envs/vLLM python=3.11
	conda create --prefix /rbscratch/brettin/conda_envs/vLLM python=3.9
 	conda activate /rbscratch/brettin/conda_envs/vLLM
  	pip install vLLM

	# Installing collected packages: sentencepiece, quantile-python, ninja, mpmath, websockets, uvloop, urllib3, typing-extensions, tqdm, sympy, sniffio, safetensors, rpds-py, regex, pyyaml, python-dotenv, pynvml, psutil, protobuf, packaging, orjson, nvidia-nvtx-cu12, nvidia-nvjitlink-cu12, nvidia-nccl-cu12, nvidia-curand-cu12, nvidia-cufft-cu12, nvidia-cuda-runtime-cu12, nvidia-cuda-nvrtc-cu12, nvidia-cuda-cupti-cu12, nvidia-cublas-cu12, numpy, networkx, msgpack, MarkupSafe, idna, httptools, h11, fsspec, frozenlist, filelock, exceptiongroup, click, charset-normalizer, certifi, attrs, annotated-types, uvicorn, triton, requests, referencing, pydantic-core, nvidia-cusparse-cu12, nvidia-cudnn-cu12, jinja2, anyio, aiosignal, aioprometheus, watchfiles, starlette, pydantic, nvidia-cusolver-cu12, jsonschema-specifications, huggingface-hub, torch, tokenizers, jsonschema, fastapi, xformers, transformers, ray, vLLM

	pip install accelerate

<a id="tunnels"></a>
### Tunneling


### Thruput

1 node, 8 GPUs
tensor_parallel = 8

	n = 100
	Fri 02 Feb 2024 04:38:35 PM CST
	
	real	3m21.177s	
	user	0m0.290s
	sys	0m0.343s

 2 nodes, 16 GPUS
 tensor_parallel = 16

	n = 100
	Sun 04 Feb 2024 01:57:45 PM CST
	
	real	4m30.549s
	user	0m0.272s
	sys	0m0.223s

#### Experiment 1

 
 2 nodes 16 GPUs
 tensor_parallel = 8

 	n = 1
  	Sun 04 Feb 2024 02:19:15 PM CST

	real	0m7.743s
	user	0m0.005s
	sys	0m0.003s

 2 nodes, 16 GPUs
 tensor_parallel = 8
 Note: All jobs ran on the head node GPUs only.

	n = 63
	Sun 04 Feb 2024 02:24:21 PM CST
	
	real	2m7.174s
	user	0m0.047s
	sys	0m0.039s

2 nodes, 16 GPUs
tensor_parallel = 16

	n = 1
	Sun 04 Feb 2024 02:34:24 PM CST
	
	real	0m11.886s
	user	0m0.009s
	sys	0m0.006s

2 nodes, 16 GPUs
tensor_parallel = 16
n = 64

n = 64
Sun 04 Feb 2024 02:39:49 PM CST

real	2m50.721s
user	0m0.125s
sys	0m0.123s




### Ray Log Snippets

	INFO 02-02 07:57:28 llm_engine.py:70] Initializing an LLM engine with config: mo
	del='mistralai/Mistral-7B-v0.1', tokenizer='mistralai/Mistral-7B-v0.1', tokenize
	r_mode=auto, revision=None, tokenizer_revision=None, trust_remote_code=False, dt
	ype=torch.bfloat16, max_seq_len=32768, download_dir=None, load_format=auto, tens
	or_parallel_size=16, quantization=None, enforce_eager=False, seed=0)

	(raylet, ip=140.221.79.201) [2024-02-02 08:12:38,595 E 1113478 1113510] (
	raylet) file_system_monitor.cc:111: /tmp/ray/session_2024-02-02_07-50-38_136817_
	3697590 is over 95% full, available space: 2376220672; capacity: 1888426192896. 
	Object creation will fail if spilling is required. [repeated 2x across clust
	er]


 


