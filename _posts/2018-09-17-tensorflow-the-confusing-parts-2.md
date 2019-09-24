---
layout: post
title: Tensorflow: The Confusing Parts (2)
tags: ["tensorflow","tutorial", "tftcp"]
mathjax: true
---

*This post is the second of a series; click [here](https://jacobbuckman.com/post/tensorflow-the-confusing-parts-1/) for the previous post, or [here](https://jacobbuckman.com/categories/tftcp/) for a list of all posts in this series.*

## Naming and Scoping

### Naming Variables and Tensors

As we discussed in Part 1, every time you call `tf.get_variable()`, you need to assign the variable a new, unique name. Actually, it goes deeper than that: every tensor in the graph gets a unique name too. The name can be accessed explicitly with the `.name` property of tensors, operations, and variables. For the vast majority of cases, the name will be created automatically for you; for example, a constant node will have the name `Const`, and as you create more of them, they will become `Const_1`, `Const_2`, etc.[^0] You can also explicitly set the name of a node via the `name=` property, and the enumerative suffix will still be added automatically:

###### Code:
```python
import tensorflow as tf
a = tf.constant(0.)
b = tf.constant(1.)
c = tf.constant(2., name="cool_const")
d = tf.constant(3., name="cool_const")
print a.name, b.name, c.name, d.name
```
###### Output
```python
Const:0 Const_1:0 cool_const:0 cool_const_1:0
```

Explicitly naming nodes is nonessential, but can be very useful when debugging. Oftentimes, when your Tensorflow code crashes, the error trace will refer to a specific operation. If you have many operations of the same type, it can be tough to figure out which one is problematic. By explicitly naming each of your nodes, you can get much more informative error traces, and identify the issue more quickly.

### Using Scopes

As your graph gets more complex, it becomes difficult to name everything by hand. Tensorflow provides the `tf.variable_scope` object, which makes it easier to organize your graphs by subdividing them into smaller chunks. By simply wrapping a segment of your graph creation code in a `with tf.variable_scope(scope_name):` statement, all nodes created will have their names automatically prefixed with the `scope_name` string. Additionally, these scopes stack; creating a scope within another will simply chain the prefixes together, delimited by a forward-slash.

###### Code:
```python
import tensorflow as tf
a = tf.constant(0.)
b = tf.constant(1.)
with tf.variable_scope("first_scope"):
  c = a + b
  d = tf.constant(2., name="cool_const")
  coef1 = tf.get_variable("coef", [], initializer=tf.constant_initializer(2.))
  with tf.variable_scope("second_scope"):
    e = coef1 * d
    coef2 = tf.get_variable("coef", [], initializer=tf.constant_initializer(3.))
    f = tf.constant(1.)
    g = coef2 * f
    
print a.name, b.name
print c.name, d.name
print e.name, f.name, g.name
print coef1.name
print coef2.name

```
###### Output
```python
Const:0 Const_1:0
first_scope/add:0 first_scope/cool_const:0
first_scope/second_scope/mul:0 first_scope/second_scope/Const:0 first_scope/second_scope/mul_1:0
first_scope/coef:0
first_scope/second_scope/coef:0
```

Notice that we were able to create two variables with the same name - `coef` - without any issues! This is because the scoping transformed the names into `first_scope/coef:0` and `first_scope/second_scope/coef:0`, which are distinct.

## Saving and Loading

At its core, a trained neural network consists of two essential components:

+ The *weights* of the network, which have been learned to optimize for some task
+ The *network graph*, which specifies how to actually use the weights to get results

Tensorflow separates these two components, but it's clear that they need to be very tightly paired.
Weights are useless without a graph structure describing how to use them, and a graph with random weights is no good either.
In fact, even something as small as swapping two weight matrices is likely to totally break your model.
This often leads to frustration among beginner Tensorflow users; using a pre-trained model as a component of a neural network is a great way to speed up training, but can break things in a myriad of ways.

### Saving A Model

When working with only a single model, Tensorflow's built-in tools for saving and loading are straightforward to use: simply create a `tf.train.Saver()`.
Similarly to the `tf.train.Optimizer` family, a `tf.train.Saver` is not itself a node, but instead a higher-level class that performs useful functions on top of pre-existing graphs.
And, as you may have anticipated, the 'useful function' of a `tf.train.Saver` is saving and loading the model.
Let's see it in action!

###### Code:
```python
import tensorflow as tf
a = tf.get_variable('a', [])
b = tf.get_variable('b', [])
init = tf.global_variables_initializer()

saver = tf.train.Saver()
sess = tf.Session()
sess.run(init)
saver.save(sess, './tftcp.model')
```
###### Output
Four new files:
```python
checkpoint
tftcp.model.data-00000-of-00001
tftcp.model.index
tftcp.model.meta
```

There's a lot of stuff to break down here.

First of all: Why does it output *four* files, when we only saved one model?
The information needed to recreate the model is divided among them.
If you want to copy or back up a model, make sure you bring all three of the files (the three prefixed by your filename).
Here's a quick description of each:

+ `tftcp.model.data-00000-of-00001` contains the weights of your model (the first bullet point from above). It's most likely the largest file here.
+ `tftcp.model.meta` is the network structure of your model (the second bullet point from above). It contains all the information needed to re-create your graph.
+ `tftcp.model.index` is an indexing structure linking the first two things. It says "where in the data file do I find the parameters corresponding to this node?"
+ `checkpoint` is not actually needed to reconstruct your model, but if you save multiple versions of your model throughout a training run, it keeps track of everything.

Secondly, why did I go through all the trouble of creating a `tf.Session` and `tf.global_variables_initializer` for this example?

Well, if we're going to save a model, we need to have something to save.
Recall that computations live in the graph, but values live in the session.
The `tf.train.Saver` can access the structure of the network through a global pointer to the graph.
But when we go to save the *values of the variables* (i.e. the weights of the network), we need to access a `tf.Session` to see what those values are; that's why `sess` is passed in as the first argument of the `save` function.
Additionally, attempting to save uninitialized variables will throw an error, because attempting to access the value of an uninitialized variable always throws an error.
So, we needed both a session and an initializer (or equivalent, e.g. `tf.assign`).

### Loading A Model

Now that we've saved our model, let's load it back in.
The first step is to recreate the variables: we want variables with all the same names, shapes, and dtypes as we had when we saved it.
The second step is to create a `tf.train.Saver` just as before, and call the `restore` function.

###### Code:
```python
import tensorflow as tf
a = tf.get_variable('a', [])
b = tf.get_variable('b', [])

saver = tf.train.Saver()
sess = tf.Session()
saver.restore(sess, './tftcp.model')
sess.run([a,b])
```
###### Output
```python
[1.3106428, 0.6413864]
```

Note that we didn't need to initialize `a` or `b` before running them!
This is because the `restore` operation moves the values from our files into the session's variables.
Since the session no longer contains any null-valued variables, initialization is no longer needed.
(This can backfire if we aren't careful: running an init *after* a restore will override the loaded values with randomly-initialized ones.)

### Choosing Your Variables

When a `tf.train.Saver` is initialized, it looks at the current graph and gets the list of variables; this is permanently stored as the list of variables that that saver "cares about".
We can inspect it with the `._var_list` property:

###### Code:
```python
import tensorflow as tf
a = tf.get_variable('a', [])
b = tf.get_variable('b', [])
saver = tf.train.Saver()
c = tf.get_variable('c', [])
print saver._var_list
```
###### Output
```python
[<tf.Variable 'a:0' shape=() dtype=float32_ref>, <tf.Variable 'b:0' shape=() dtype=float32_ref>]
```

Since `c` wasn't around at the time of our saver's creation, it does not get to be a part of the fun.
So in general, make sure that you already have all your variables created before creating a saver.

Of course, there are also some specific circumstances where you may actually want to only save a subset of your variables!
`tf.train.Saver` lets you pass the `var_list` when you create it to specify which subset of available variables you want it to keep track of.

###### Code:
```python
import tensorflow as tf
a = tf.get_variable('a', [])
b = tf.get_variable('b', [])
c = tf.get_variable('c', [])
saver = tf.train.Saver(var_list=[a,b])
print saver._var_list
```
###### Output
```python
[<tf.Variable 'a:0' shape=() dtype=float32_ref>, <tf.Variable 'b:0' shape=() dtype=float32_ref>]
```

### Loading Modified Models

The examples above cover the 'perfect sphere in frictionless vacuum' scenario of model-loading.
As long as you are saving and loading your own models, using your own code, without changing things in between, saving and loading is a breeze.
But in many cases, things are not so clean.
And in those cases, we need to get a little fancier.

Let's take a look at a couple of scenarios to illustrate the issues.
First, something that works without a problem.
What if we want to save a whole model, but we only want to load part of it?
(In the following code example, I run the two scripts in order.)

###### Code:
```python
import tensorflow as tf
a = tf.get_variable('a', [])
b = tf.get_variable('b', [])
init = tf.global_variables_initializer()
saver = tf.train.Saver()
sess = tf.Session()
sess.run(init)
saver.save(sess, './tftcp.model')
```
```python
import tensorflow as tf
a = tf.get_variable('a', [])
init = tf.global_variables_initializer()
saver = tf.train.Saver()
sess = tf.Session()
sess.run(init)
saver.restore(sess, './tftcp.model')
sess.run(a)
```
###### Output
```python
1.1700551
```

Good, easy enough!
And yet, a failure case emerges when we have the reverse scenario: we want to load one model as a component of a larger model.

###### Code:
```python
import tensorflow as tf
a = tf.get_variable('a', [])
init = tf.global_variables_initializer()
saver = tf.train.Saver()
sess = tf.Session()
sess.run(init)
saver.save(sess, './tftcp.model')
```
```python
import tensorflow as tf
a = tf.get_variable('a', [])
d = tf.get_variable('d', [])
init = tf.global_variables_initializer()
saver = tf.train.Saver()
sess = tf.Session()
sess.run(init)
saver.restore(sess, './tftcp.model')
```
###### Output
```python
Key d not found in checkpoint
         [[{{node save/RestoreV2}} = RestoreV2[dtypes=[DT_FLOAT, DT_FLOAT, DT_FLOAT], _device="/job:localhost/replica:0/task:0/device:CPU:0"](_arg_save/Const_0_0, save/RestoreV2/tensor_names, save/RestoreV2/shape_and_slices)]]
```

We just wanted to load `a`, while ignoring the new variable `d`. And yet, we got an error, complaining that `d` was not present in the checkpoint!

A third scenario is where you want to load one model's parameters into a *different* model's computation graph.
This throws an error too, for obvious reasons: Tensorflow cannot possibly know where to put all those parameters you just loaded.
Luckily, there's a way to give it a hint.

Remember `var_list` from one section-header ago?
Well, it turns out to be a bit of a misnomer.
A better name might be "var_list_or_dictionary_mapping_names_to_vars", but that's a mouthful, so I can sort of see why they stuck with the first bit.

Saving models is one of the key reasons that Tensorflow mandates globally-unique variable names.
In a saved-model-file, each saved variable's name is associated with its shape and value.
Loading it into a new computational graph is as easy as mapping the original-names of the variables you want to load to variables in your current model.
Here's an example:

###### Code:
```python
import tensorflow as tf
a = tf.get_variable('a', [])
init = tf.global_variables_initializer()
saver = tf.train.Saver()
sess = tf.Session()
sess.run(init)
saver.save(sess, './tftcp.model')
```
```python
import tensorflow as tf
d = tf.get_variable('d', [])
init = tf.global_variables_initializer()
saver = tf.train.Saver(var_list={'a': d})
sess = tf.Session()
sess.run(init)
saver.restore(sess, './tftcp.model')
sess.run(d)
```
###### Output
```python
-0.9303965
```

This is the key mechanism by which you can combine models that do not have the exact same computational graph.
For example, perhaps you got a pre-trained language model off of the internet, and want to re-use the word embeddings.
Or, perhaps you changed the parameterization of your model in between training runs, and you want this new version to pick up where the old one left off; you don't want to have to re-train the whole thing from scratch.
In both of these cases, you would simply need to hand-make a dictionary mapping from the old variable names to the new variables.

A word of caution: it's very important to know *exactly* how the parameters you are loading are meant to be used.
If possible, you should use the exact code the original authors used to build their model, to ensure that that component of your computational graph is identical to how it looked during training.
If you need to re-implement, keep in mind that basically any change, no matter how minor, is likely to severely damage the performance of your pre-trained net.
Always benchmark your reimplementation against the original!

#### Inspecting Models

If the model you want to load came from the internet - or from yourself, >2 months ago - there's a good chance you won't *know* how the original variables were named.
To inspect saved models, use [these tools](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/framework/python/framework/checkpoint_utils.py), which come from the official Tensorflow repository.
For example:

###### Code:
```python
import tensorflow as tf
a = tf.get_variable('a', [])
b = tf.get_variable('b', [10,20])
c = tf.get_variable('c', [])
init = tf.global_variables_initializer()
saver = tf.train.Saver()
sess = tf.Session()
sess.run(init)
saver.save(sess, './tftcp.model')
print tf.contrib.framework.list_variables('./tftcp.model')
```
###### Output
```python
[('a', []), ('b', [10, 20]), ('c', [])]
```

With a little effort and a lot of head-scratching, it's usually possible to use these tools (in conjunction with the original codebase) to find the names of the variables you want.

## Conclusion

Hopefully this post helped clear up the basics behind saving and loading Tensorflow models.
There are a few other advanced tricks, like automatic checkpointing and saving/restoring meta-graphs, that I may touch on in a future post; but in my experience, those use-cases are rare, especially for beginners.
As always, please let me know in the comments or via email if I got anything wrong, or there is anything important I missed.
Thanks for reading!

[^0]: There will also be a suffix `:output_num` added to the tensor names. For now, that's always `:0`, since we are only using operations with a single output. See [this StackOverflow question for more info](https://stackoverflow.com/questions/40925652/in-tensorflow-whats-the-meaning-of-0-in-a-variables-name). Thanks Su Tang for pointing this out!
