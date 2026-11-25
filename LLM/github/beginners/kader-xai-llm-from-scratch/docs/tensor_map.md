# Tensor Map — every shape in the model

Keep this table next to you while working the chapters. `B` = batch, `T` = context length,
`C` = embedding dim, `H` = number of heads, `vocab` = vocabulary size.

| Step | Tensor | Shape | Chapter |
|---|---|---|---|
| Input token ids | `ids` | `(B, T)` | 01 |
| Token embedding | `tok_emb` | `(B, T, C)` | 02 |
| Position embedding | `pos_emb` | `(T, C)` → broadcast | 03 |
| Combined embedding | `x = tok+pos` | `(B, T, C)` | 04 |
| LayerNorm | `ln(x)` | `(B, T, C)` (unchanged) | 05 |
| Q / K / V (per head) | `q, k, v` | `(B, T, C/H)` | 06 |
| Attention scores | `q @ kᵀ` | `(B, T, T)` | 06 |
| Attention weights | `softmax(masked)` | `(B, T, T)` | 06 |
| Head output | `weights @ v` | `(B, T, C/H)` | 06 |
| Multi-head (concat + proj) | `mha(x)` | `(B, T, C)` | 07 |
| FeedForward | `ff(x)` | `(B, T, C)` (4C hidden) | 08 |
| Transformer block | `block(x)` | `(B, T, C)` (unchanged) | 09 |
| Final LayerNorm | `ln_f(x)` | `(B, T, C)` | 10 |
| LM head | `head(x)` | `(B, T, vocab)` | 10 |
| Loss | `cross_entropy` | scalar | 10 |
| Sampled next token | `multinomial` | `(B, 1)` | 13 |

## The two equations that matter

**Causal self-attention (one head):**
```
attention(Q, K, V) = softmax( (Q·Kᵀ / √d_k)  +  causal_mask ) · V
```

**The transformer block (Pre-LN residual):**
```
x = x + MultiHeadAttention( LayerNorm(x) )
x = x + FeedForward(        LayerNorm(x) )
```

Everything else is plumbing around these two.
