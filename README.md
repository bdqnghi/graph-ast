## Graph-Ast

Generate graph representation of the source code based on the paper: [Learning to Represent Program with Graph](https://arxiv.org/abs/1711.00740)

### Installation

The backbone of this tool is the Abstract Syntax Tree (AST). The AST will be generated using the f-ast tool: [fAST: Flattening Abstract Syntax Trees
for Efficiency](https://oro.open.ac.uk/59268/1/main.pdf).

First, pull the docker image of the f-ast tool:

```bash
  $ docker pull yijun/fast:latest
```
