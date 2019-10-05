# Graph-Ast

Generate graph representation of the source code based on the paper: [Learning to Represent Program with Graph, ICLR 2018](https://arxiv.org/abs/1711.00740)

## Installation

The backbone of this tool is the Abstract Syntax Tree (AST). The AST will be generated using the f-ast tool: [fAST: Flattening Abstract Syntax Trees for Efficiency, ICSE 2019](https://oro.open.ac.uk/59268/1/main.pdf). The tool supports any ANTLR4 grammar of over 170 different types of programming languages.

First, pull the docker image of the f-ast tool:

```bash
  $ docker pull yijun/fast:latest
```
This tool leverages [protobuf](https://github.com/protocolbuffers/protobuf) to store the AST and make the parsing much faster than the other tools.

#### Some example usages:

To generate an AST representation of a file.

```bash
  $ "docker run -v $(pwd):/e -it yijun/fast -p Test.java Test.pb
```

The Test.pb file is the AST representation under the protobuf format. For example on how to read and traverse the tree, see this link.

Since the goal of this tool is to generate the graph representation of the source code, the next step is to run:

```python
  $  python3 generate_graph Test.pb Test.txt
```

The Test.txt is a graph representation with the format: source_id, source_node_type edge_type sink_id, sink_node_type.
For example, the edge:
```
22,3 1 21,4
```
means that the node with id 22 connect to node with id 21 via the edge with id 1. Also the node with id 22 has the type of 3, the node with id 21 has the type of 4.

For the list of edge types, see this link.
F
