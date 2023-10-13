# from functools import partial
# from collections import namedtuple
# from typing import Optional, Tuple, Union

# import torch
# from torch.nn import Module, ModuleList
# from torch import nn, einsum
# import torch.nn.functional as F

# from beartype import beartype

# from einops import rearrange, repeat, reduce, pack, unpack

# from colt5_attention import topk as maybe_differentiable_topk

# import torch.distributed as dist

# import snntorch as snn
# from snntorch import spikeplot as splt
# from snntorch import spikegen

# class SpikeExpert(Module):
#     def __init__(
#         self,
#         dim,
#         hidden_mult = 4,
#         mult_bias = True,
#         prenorm = False
#     ):
#         super().__init__()
#         dim_hidden = int(dim * hidden_mult * 2 / 3)
#         # Temporal Dynamics
#         self.num_steps = 25
#         beta = 0.95
        
#         # Initialize layers
#         self.fc1 = nn.Linear(dim, dim_hidden)
#         self.lif1 = snn.Leaky(beta=beta)
#         self.fc2 = nn.Linear(dim_hidden, dim)
#         self.lif2 = snn.Leaky(beta=beta)

#     def forward(self, x):
        
#         # Initialize hidden states at t=0
#         mem1 = self.lif1.init_leaky()
#         mem2 = self.lif2.init_leaky()

#         # Record the final layer
#         spk2_rec = []
#         mem2_rec = []

#         for step in range(self.num_steps):
#             cur1 = self.fc1(x)
#             spk1, mem1 = self.lif1(cur1, mem1)
#             cur2 = self.fc2(spk1)
#             spk2, mem2 = self.lif2(cur2, mem2)
#             spk2_rec.append(spk2)
#             mem2_rec.append(mem2)

#         return torch.stack(mem2_rec, dim=0)