## Installation

The backbone of this tool is the Abstract Syntax Tree (AST). The AST will be generated using the f-ast tool: [fAST: Flattening Abstract Syntax Trees for Efficiency, ICSE 2019](https://oro.open.ac.uk/59268/1/main.pdf). The tool supports any ANTLR4 grammar of over 170 different types of programming languages. 

Some benefits of using the f-ast:

- f-ast leverages [protobuf](https://github.com/protocolbuffers/protobuf) to store the AST and make the parsing much faster than the other tools.
- f-ast is built based on [srcml](https://www.srcml.org/) and [srcSlice](https://github.com/srcML/srcSlice). That is, it can incorporate the slicing information of the program, such as [the use-def chain](https://en.wikipedia.org/wiki/Use-define_chain) (taken from srcSlice) into the AST. The use-def chain is a critical information to generate the graph representation of the AST.

A runnable docker image of the tool can be pulled by using this command:

```bash
  $ docker pull yijun/fast:latest
```

## Example usages:

The example files can be found in [this](https://github.com/bdqnghi/fAST-instruction/tree/master/sample_files)

To generate an protobuffer representation of the AST.

```bash
  $ cd sample_files
  $ docker run -v $(pwd):/e -it yijun/fast -p Bubblesort.java Bubblesort.pb
```

To generate an flatbuffer representation of the AST.

```bash
  $ cd sample_files
  $ docker run -v $(pwd):/e -it yijun/fast -S -G Bubblesort.java Bubblesort.fbs
```

While the protobuf representation is more convenient when traversing and modifying the AST, the flatbuffer representation is much faster in parsing time.

To generate an Graph representation of from the fbs representation:

```bash
  $  docker run -v $(pwd):/e --entrypoint ggnn -it yijun/fast Bubblesort.fbs dummy.txt Bubblesort.txt
```
Ignore the dummy.txt, it's a redundant output (we intended to use it for other purpose)
The Bubblesort.txt is a graph representation with the format: source_id, source_node_type edge_type sink_id, sink_node_type.
For example, the edge:
```
22,3 1 21,4
```
means that the node with id 22 connects to the node with id 21 via the edge type 1. Also, the node with id 22 has the type of 3, the node with id 21 has the type of 4.

For the list of node types, see [this](https://github.com/bdqnghi/fAST-instruction/blob/master/types/srcml_node_types.tsv).

For the list of edge types, see [this](https://github.com/bdqnghi/fAST-instruction/blob/master/types/edge_types.tsv).
