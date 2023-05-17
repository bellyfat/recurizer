# recurizer
LLM-based recursive summary tool

### Problem
1. Embeddings for code kinda suck. Unlike, text where it is easy to gather specific context from 1-5 specific samples, 
code's "context" can be spread around multiple files and one flag can drastically change the program's effect.
If this flag is not returned as context from the vector db retrieval, we're out of luck.
2. Completions/Chat are limited by the context window (4k for `gpt-3.5`, 8k/32k for `gpt-4`). Luckily,
many codebases do not exceed this limit and tools exist for this (see [`GrePT`](https://github.com/jackbarry24/GrePT)).
But, codebases that do exceed this context window limit tend to exceed it by a light, making chat based
q and a tools useless. 

### Proposal

A system that recursively summarizes each file/folder in a directory storing each summary in a `.summary` file.
Clever prompting will be used to preserve the important context program/function I/O, allowing us to
keep track of the 'bigger picture' but also being able to query at the lower-level. 

Why this will work, the script will simply generate these `.summary` files in each directory, this will also mean 
that you can use the program from a higher directory without having to regenerate all of the summaries. 
It will simply see that a `.summary` file already exists in certain subdirectories, and avoid generating
new summaries for those. 


