# Documentation

## GPT Language Model Implementation

A complete implementation of the GPT Language Model is available in this module. The model is based on the implementation of GPT-2 from OpenAI and huggingface/transformers.

### Classes

#### LayerNorm
`LayerNorm(ndim: int, bias: bool) -> None:` 
This class creates a LayerNorm module but with an optional bias. Pytorch does not support bias = False simply.

##### Methods
- `forward(input: Tensor) -> Tensor:` Performs the layer normalization on the input tensor.

#### CausalSelfAttention
`CausalSelfAttention(config: object) -> None:` 
This class creates a CausalSelfAttention module using a given config object.

##### Methods
- `forward(x: Tensor) -> Tensor:` Performs the causal self attention operation on the input tensor x.

#### MLP
`MLP(config: object) -> None:` 
This class creates an MLP (Multilayered Perceptron) module using the given config object.

##### Methods
- `forward(x: Tensor) -> Tensor:`: Performs the MLP operation on the input tensor x.

#### Block
`Block(config: object) -> None:` 
This class creates a Block module using the provided config object.

##### Methods
- `forward(x: Tensor) -> Tensor:`: Performs the operations of the Block on the input tensor x.

#### GPTConfig
This is a dataclass that holds the configuration options for the GPT model.

#### GPT
`GPT(config: object) -> None:`  
This class creates a GPT model using the provided config object.

##### Methods
- `get_num_params(non_embedding: bool = True) -> int:`: Returns the number of parameters in the model. If non_embedding = True (default), then the count does not include position embeddings.

- `_init_weights(module: object) -> None:`: Initializes the weights of the given module.

- `forward(idx: Tensor, targets: Optional[Tensor]) -> Tuple[Tensor, Optional[float]]:`: Performs the forward pass of the model on the indices provided in idx. If targets are provided, also calculates loss.

- `crop_block_size(block_size: int) -> None:`: Adjusts the block size of the model if necessary.

- `from_pretrained(model_type: str, override_args: Optional[dict] = None) -> object:`: Returns a GPT model with weights pretrained on a given model_type.

- `configure_optimizers(weight_decay: float, learning_rate: float, betas: tuple, device_type: str) -> object:`: Configures and returns an AdamW optimizer for the model.

- `estimate_mfu(fwdbwd_per_iter: int, dt: float) -> float:`: Estimates the model's flops utilization (MFU) in units of A100 bfloat16 peak FLOPS.

- `generate(idx: Tensor, max_new_tokens: int, temperature: float = 1.0, top_k: Optional[int] = None) -> Tensor:`: Generates and completes a sequence of indices (provided in idx) max_new_tokens times. The final sequence is returned.