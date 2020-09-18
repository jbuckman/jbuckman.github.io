---
layout: post
title: Neural Tangent Kernel&#58; Answers & Questions
tags: ["deep learning", "ntk", "tutorial"]
published: false
mathjax: true
invisible: true
---

This is a brief tutorial on the *neural tangent kernel* (NTK), which is one of the most popular recent approaches to understanding neural networks. Rather than walk through the derivation of NTK itself, this post focuses on how NTK fits into the broader conceptual space.

Some backstory: a few months ago, I decided to take a look at the NTK literature and try to understand what is going on. This quest yielded many fruitful insights, but also left me with some open questions. The goal of this post is twofold: to provide a resource for people who wish to better understand NTK, and to get the opinions of experts on addressing my concerns.

### What is NTK?
The Neural Tangent Kernel is, at its core, a linear approximation to a neural network. Linear models are powerful and simple to understand, but rely very strongly on having a good feature space. We first go through some of the basic math of linear models, highlighting their limitations. We make the connection to kernel methods, which are simply one particular way of implementing linear models; they find the exact same solutions and, thus, suffer from the same limitations. Finally, we use these ideas to make a connection to NTK, and understand some of its properties.

### Linear Models
We first provide a simple and general definition of linear methods.

We have a space of inputs $x\in\chi$ and a target function $y:\chi\to\mathbb{R}$ (for simplicity we'll just assume the targets are real) and we'll have $k$ feature functions $f_k:\chi\to\mathbb{R}$. For ease of notation we can stack these real valued functions into $f(x) \in \mathbb{R}^k$. A *linear model*, parameterized by $\theta$, outputs a linear combination of these basis functions/vectors: $f(x)^T \theta = f_1(x) \theta_1 + ... +f_k(x) \theta_k$ for $\theta \in R^k$.

*Important note:* Some readers may be used to thinking about linearity in terms of a ``natural feature space'', e.g., linearity wrt the pixels of an image. In this post, we keep things a bit more abstract: there is no notion of a natural feature space. This means that it is not important whether $f_k$ is itself linear, or whether it is some more complicated nonlinear feature function. In fact, since $\chi$ need not even be a vector space, the question of whether $f_k$ is linear is not even meaningful in general. The only important thing is that the overall output is linear wrt $f_k$ and $\theta$.

A train set $X$ is a sample of points in $\chi$. $F_k = f_k(X)$ denotes a column vector of $f_k(x)$ evaluated for every $x\in X$, and the matrix $F = [F_1, ..., F_k]$ represents the basis of a vector space of possible outputs of our linear model $f_\theta$ in the support of $X$. Similarly, the vector $Y=y(X)$, i.e., the target function evaluated at every point in the train set. We'll just study least-squares regression, which finds a $\theta$ that minimizes $L_\theta = ||F\theta - Y||^2_2$ and outputs the linear model $f_\theta$.

Since linear models are so simple, it's very easy to study their failure modes. They can fail to find the true target $y$ for two reasons. The first is if $y$ is not representable as a linear combination of the features $f$, i.e., $y$ does not live in the span of $f$. Thus, in order to be sure that we will find a good solution for some unknown task, we need a large and representative set of feature functions.

The second reason is when there is not enough training data to narrow down the true solution. We know from linear algebra that there might be a whole hyperplane of least squares solutions, that is, a whole set of $\theta$s that all minimize the error $||F\theta - Y||^2_2$.  As a general rule, if there are more features, more data will be required to narrow down the solution; thus, this failure mode is mitigated when the set of feature functions is *small*, causing a fundamental tension.

This second failure mode can also be mitigated through regularization. When there is a hyperplane of solutions, the algorithm still must pick one of them. Minimizing a regularized objective $||F\theta - Y||^2_2 + \lambda Reg(\theta)$ in the limit of $\lambda\to0$ can be interpreted as selecting the $\theta$ in the hyperplane with lowest $Reg(\theta)$, if $Reg$ is convex. One common approach is to pick the minimum-norm $\theta$, which is, in fact, the same as the implicit regularization provided by gradient descent if the initialization parameters are $0$. But this formulation is general, and so we could have more fancy regularizations. For example, defining $\theta^*$ such that $f(x)^T\theta^*=y(x)$ for all $x$ (and assuming such a $\theta^*$ exists), we could have $Reg(\theta) = || \theta - \theta^*||_2^2$, a regularizer that would always result in the correct function being selected, regardless of training data. This is, of course, of no practical value, but it serves to highlight an important point: optimal behaviour can always be achieved by a linear model if it has enought capacity and perfect regularization. (A more realistic regularizer to achieve optimal behaviour of linear models might be if we knew $y$ was sampled from a known distribution, and we constructed a Bayes-optimal regularizer.)

To summarize, getting linear models to work well must involve both 
1. Finding a basis that can express the correct solution. 
2. Finding a basis which does not include bad solutions, or a regularizer which avoids such bad solutions.

If these conditions are met, a humble linear model can get optimal behaviour for any set of tasks. 

Unfortunately, these conditions are rarely met. In practice, we always run into problems; either the feature functions have a span that does not include the target function, or the span contains so many functions that we can always find a "bad function" that fits $(X,Y)$ without finding the goal function $y$. And, in practice, we generally do not know enough about the domain to construct a tractable regularizer.


### Weight vs. Kernel Implementations of Linear Regression
The closed-form solution of the parameters of the least-squares linear regression problem is $\theta = (F^TF)^{-1}F^T Y$. (The "hyperplane of solutions" mentioned earlier comes from the fact that if the feature correlation matrix $F^TF$ is not invertible, we will have a whole hyperplane of pseudo-inverse matrices that will result in valid solutions. From now on, assume $(F^TF)^{-1}$ refers to any such matrix.) This means that, on any point $x \in \chi$, we will output $f(x)^T\theta = f(x)^T(F^TF)^{-1}F^TY$.

The kernel perspective simply notices that a linear model only depends on dot products between features, not the features themselves. Concretely, the previous equation can be rewritten as $f(x)^T\theta = f(x)^T(F^TF)^{-1}F^TY = \sum_{x' \in X} \langle f(x), f(x') \rangle_F y(x')$, where $\langle a,b \rangle_F = a^T (F^TF)^{-1} b$ is a dot product.

Thus, by using the kernel trick, it's never necessary to explicitly compute the features of a point. This allows the usage of infinite dimensional feature functions! In practice, if the number of features is much larger than the number of points in the train set $X$, using the kernel trick will be computationally advantageous. (But on the flipside, for very large datasets the kernel trick will become intractable, due to the cubic cost of computing the matrix inverse needed for the dot product $\langle \cdot,\cdot \rangle_F$. Learning the parameter $\theta$ with an optimization algorithm is more practical for large datasets.)

We reemphasise that kernel methods *are linear methods*, as per our definition. Thus, all the issues we discussed in the previous section apply to all kernel methods. This also includes more complex algorithms like SVMs, which are linear methods using the maximum margin loss instead of the $\ell_2$. And, of course, they also apply to any linearized approximations of neural networks, kernel or otherwise. Let's examine this last idea in detail.

### Linearization of Neural Networks
Consider a neural network $g_\xi$, randomly initialized with some parameters $\xi\in\mathbb{R}^k$.[^0] For some input $x$, we will sometimes write $g_\xi(x)$ as $g(\xi, x)$ in order to emphasize the dependence on the parameters $\xi$.

The Taylor approximation tells us that $g(\xi, x)$ is approximately linear locally with respect to $\xi$.

$$g(\xi, x) \approx g(\xi_0, x) + (\nabla_\xi g(\xi, x)\vert_{\xi=\xi_0})^T (\xi - \xi_0)$$

We can use the Taylor expansion to construct a linearized approximation of $g_\xi$. Define a feature function $f^{g}_{\xi_0}(x)=\nabla_{\xi} g(\xi, x) \vert_{\xi=\xi_0}$, which computes the vector of gradients of the outputs of the neural network with respect to parameters at their random initialization. We have that $g(\xi, x) \approx c(x) + f^{g}_{\xi_0}(x)^T \theta$. Since $c(x) = g(\xi_0, x)$ is a constant function, independent of the parameters, it isn't relevant in any way for our analysis.

It is intuitive that $f^{g}_{\xi_0}$ provides the features for the linear model approximating the function $g_{\xi}$; after all, a basic property of linear models is that the gradients w.r.t. the parameters are the features. Thus, on a train set $X$ we can use the linear model $f^{g}_{\xi_0}(X)^T\theta$, with parameters $\theta\in\mathbb{R}^k$, to minimize $||f^{g}_{\xi_0}(X)^T\theta - Y||^2_2$. Note that since $|\theta| = |\xi|$, this linear model will have the same number of features as $g$ has parameters.

### On NTK

So what is NTK? It's the Taylor approximation of a neural network at the infinite-width limit (with a specific initialization technique). In this regime, using the kernel trick is indispensible because the features/gradients are infinite-dimensional.

Some find NTK interesting because the Taylor linearization of infinite-width networks is *exact*, not approximate. However, infinite-width neural networks are themselves approximations to finite-width neural networks. So, both the Taylor linearization and the NTK linearization are approximations to the dynamics of finite-width neural networks; they simply differ in where the approximation step happens.

Our discussion up to this point has laid the groundwork for our questions about NTK.

Firstly, since NTK is a kernel method, and kernel methods are linear methods, there are some natural questions one should ask about NTK. Specifically, the questions one should ask about any linear method: (1) Does the feature space contain all the target functions we might want? (2) Does the feature space contain any bad solutions? If so, does the (implicit GD) regularization avoid such solutions? If it is not the case that NTK's implicit feature space has these desirable properties, it seems like it is a poor model for finite-width deep neural networks, which are interesting precisely *because* they are able to find good solutions in spite of the enormous size of their function class.

Secondly, how does NTK's performance compare against the canonical linearization of a standard NN, which we derived from the Taylor expansion in the previous section? The Taylor expansion algorithm is much easier to understand and implement, and won't suffer from the cubic cost of kernel methods, so it seems like that linearization should be at least compared, if not preferred. Since it is cheaper, it could be used to compare the performance of NN linearizations against standard NNs on complex datasets like ImageNet.

I've not been able to find the answers to these questions in any of the existing NTK literature. We hope that the community can help us out here! These questions seem essential to motivate further study of NTK, since one possible outcome is that the answer to the first question is "no and no", and to the second question is "both linearizations perform about the same, and perform worse than regular NNs". If this is true, then it's not clear why one should study NTK at all.

[^0]: This argument applies for any continuous parameterized function.