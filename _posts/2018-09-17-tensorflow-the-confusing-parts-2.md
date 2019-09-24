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
