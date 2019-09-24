---
layout: post
title: More on Graph Inspection
tags: ["tensorflow","tutorial"]
mathjax: false
---

In [Tensorflow: The Confusing Parts (1)](https://jacobbuckman.com/post/2018-06-25-tensorflow-the-confusing-parts-1/), I described the abstractions underlying Tensorflow at a high level in an intuitive manner. In this follow-up post, I dig more deeply, and examine how these abstractions are actually implemented. Understanding these implementation details isn't necessarily essential to writing and using Tensorflow, but it allows us to inspect and debug computational graphs.

## Inspecting Graphs

The computational graph is not just a nebulous, immaterial abstraction; it is a computational object that exists, and can be inspected. Complicated graphs are difficult to debug if we are representing them entirely in our heads, but inspecting and debugging the actual graph object makes thigs much easier.

To access the graph object, use `tf.get_default_graph()`, which returns a pointer to the global default graph object:

###### Code:
```python
import tensorflow as tf
g = tf.get_default_graph()
print g
```
###### Output:
```python
<tensorflow.python.framework.ops.Graph object at 0x1144ffd90>
```

This object has the potential to tell us everything we need to know about the computational graph we have constructed. But only if we know how to use it! First, let's take a step back and dive a bit deeper into something I glossed over in the first part: the difference between edges and nodes.

The mathematical definition of a graph includes both edges and nodes. A Tensorflow graph is no exception: it has `tf.Operation` objects (nodes) and `tf.Tensor` objects (edges). An operation results in a single tensor (edge) as an output, so it's fine to conflate the two in most cases; that's what I did in TFTCP1. But in terms of the actual Python objects that make up the graph, they are programmatically distinct.

When we create a new node, there are actually three things happening under the hood:

1. We gather up all the `tf.Tensor` objects corresponding to the incoming edges for our new node
2. We create a new node, which is a `tf.Operation` object
3. We create one or more new outgoing edges, which are `tf.Tensor` objects, and return pointers to them

There are three primary ways that we can inspect the graph to understand how these pieces fit together:

1. **List All Nodes:** `tf.Graph.get_operations()` returns all operations in the graph
2. **Inspecting Nodes:** `tf.Operation.inputs` and `tf.Operation.outputs` each return a list of `tf.Tensor` objects, which correspond to the incoming edges and outgoing edges, respectively
3. **Inspecting Edges:** `tf.Tensor.op` returns a single `tf.Operation` for which this tensor is the output, and `tf.Tensor.consumers()` returns a list of all `tf.Operations` for which this tensor is used as an input.

Here's an example of these in action:

###### Code
```python
import tensorflow as tf
a = tf.constant(2, name='a')
b = tf.constant(3, name='b')
c = a + b

print "Our tf.Tensor objects:"
print a
print b
print c
print

a_op = a.op
b_op = b.op
c_op = c.op

print "Our tf.Operation objects, printed in compressed form:"
print a_op.__repr__()
print b_op.__repr__()
print c_op.__repr__()
print

print "The default behavior of printing a tf.Operation object is to pretty-print:"
print c_op

print "Inspect consumers for each tensor:"
print a.consumers()
print b.consumers()
print c.consumers()
print

print "Inspect input tensors for each op:"
# it's in a weird format, tensorflow.python.framework.ops._InputList, so we need to convert to list() to inspect
print list(a_op.inputs)
print list(b_op.inputs)
print list(c_op.inputs)
print

print "Inspect input tensors for each op:"
print a_op.outputs
print b_op.outputs
print c_op.outputs
print

print "The list of all nodes (tf.Operations) in the graph:"
g = tf.get_default_graph()
ops_list = g.get_operations()
print ops_list
print

print "The list of all edges (tf.Tensors) in the graph, by way of list comprehension:"
tensors_list = [tensor for op in ops_list for tensor in op.outputs]
print tensors_list
print

print "Note that these are the same pointers we can find by referring to our various graph elements directly:"
print ops_list[0] == a_op, tensors_list[0] == a
```
###### Output
```python
Our tf.Tensor objects:
Tensor("a:0", shape=(), dtype=int32)
Tensor("b:0", shape=(), dtype=int32)
Tensor("add:0", shape=(), dtype=int32)

Our tf.Operation objects, printed in compressed form:
<tf.Operation 'a' type=Const>
<tf.Operation 'b' type=Const>
<tf.Operation 'add' type=Add>

The default behavior of printing a tf.Operation object is to pretty-print:
name: "add"
op: "Add"
input: "a"
input: "b"
attr {
  key: "T"
  value {
    type: DT_INT32
  }
}

Inspect consumers for each tensor:
[<tf.Operation 'add' type=Add>]
[<tf.Operation 'add' type=Add>]
[]

Inspect input tensors for each op:
[]
[]
[<tf.Tensor 'a:0' shape=() dtype=int32>, <tf.Tensor 'b:0' shape=() dtype=int32>]

Inspect input tensors for each op:
[<tf.Tensor 'a:0' shape=() dtype=int32>]
[<tf.Tensor 'b:0' shape=() dtype=int32>]
[<tf.Tensor 'add:0' shape=() dtype=int32>]

The list of all nodes (tf.Operations) in the graph:
[<tf.Operation 'a' type=Const>, <tf.Operation 'b' type=Const>, <tf.Operation 'add' type=Add>]

The list of all edges (tf.Tensors) in the graph, by way of list comprehension:
[<tf.Tensor 'a:0' shape=() dtype=int32>, <tf.Tensor 'b:0' shape=() dtype=int32>, <tf.Tensor 'add:0' shape=() dtype=int32>]

Note that these are the same pointers we can find by referring to our various graph elements directly:
True True
```

There are a couple of funky things that we have to do to make everything nice to look at, but once you get used to them, inspecting the graph becomes second nature.

Of course, no discussion of graphs would be complete without taking a look at `tf.Variable` objects too:

###### Code
```python
import tensorflow as tf
a = tf.constant(2, name='a')
b = tf.get_variable('b', [], dtype=tf.int32)
c = a + b

g = tf.get_default_graph()
ops_list = g.get_operations()
print

print "tf.Variable objects are really a bundle of four operations (and their corresponding tensors):"
print b
print ops_list
print

print "Two of these are accessed via their tf.Operations,",
print "the core", b.op.__repr__(), "and the initializer", b.initializer.__repr__()
print "The other two are accessed via their tf.Tensors,",
print "the initial-value", b.initial_value, "and the current-value", b.value()
print

print "A tf.Variable core-op takes no inputs, and outputs a tensor of type *_ref:"
print b.op.__repr__()
print list(b.op.inputs), b.op.outputs
print

print "A tf.Variable current-value is the output of a \"/read\" operation, which converts from *_ref to a tensor with a concrete data-type."
print "Other ops use the concrete node as their input:"
print b.value()
print b.value().op.__repr__()
print list(c.op.inputs)
```
###### Output
```python
tf.Variable objects are really a bundle of four operations (and their corresponding tensors):
<tf.Variable 'b:0' shape=() dtype=int32_ref>
[<tf.Operation 'a' type=Const>, <tf.Operation 'b/Initializer/zeros' type=Const>, <tf.Operation 'b' type=VariableV2>, <tf.Operation 'b/Assign' type=Assign>, <tf.Operation 'b/read' type=Identity>, <tf.Operation 'add' type=Add>]

Two of these are accessed via their tf.Operations, the core <tf.Operation 'b' type=VariableV2> and the initializer <tf.Operation 'b/Assign' type=Assign>
The other two are accessed via their tf.Tensors, the initial-value Tensor("b/Initializer/zeros:0", shape=(), dtype=int32) and the current-value Tensor("b/read:0", shape=(), dtype=int32)

A tf.Variable core-op takes no inputs, and outputs a tensor of type *_ref:
<tf.Operation 'b' type=VariableV2>
[] [<tf.Tensor 'b:0' shape=() dtype=int32_ref>]

A tf.Variable current-value is the output of a "/read" operation, which converts from *_ref to a tensor with a concrete data-type.
Other ops use the concrete node as their input:
Tensor("b/read:0", shape=(), dtype=int32)
<tf.Operation 'b/read' type=Identity>
[<tf.Tensor 'a:0' shape=() dtype=int32>, <tf.Tensor 'b/read:0' shape=() dtype=int32>]
```

So a `tf.Variable` adds (at least) four ops, but most of the details can be happily abstracted away by the `tf.Variable` interface. In general, you can just assume that a `tf.Variable` will be the thing you want it to be in any given circumstance. For example, if you want to assign a value to a variable, it will resolve to the core-op; if you want to use the variable in a computation, it will resolve to the current-value-op; etc.

Take some time to play around with inspecting simple Tensorflow graphs in a Colab or interpreter - it will pay off in time saved debugging later!
