:point_right::point_left: cpp

### General Relativity Sim


-  [ x ] Lorentz Transformation
-  [ ] Minkowski Spacetime
-  [ ] Schwartzchild metric g matrix
-  [ ] Tensor Arithmetic
-  [ ] Reimannian Manifolds


Soources:
https://bjlkeng.github.io/posts/manifolds/

#### Manifolds

___Motivation : Manifolds are important because they allow multi-dimensional structures to be expressed and understood in terms of the relatively well-understood properties of Eucledian Space.___


___*Manifolds are geometrical objects that, when looked upon infinitesimally small (differentiated), locally resemble Eucledian Geometry with _k_ less dimensions. A 3D Manifold entails a 4D object that locally resembles a 3D Eucledian Object*___


1D Example: A 1 dimensional line can be bent into a circle, thus entering the second dimension. When looking at the surface of the circle infinitesimally small, it locally resembles a one-dimensional line segment.

2D Example : The simplest example is a sphere. When looked upon, the surface of the sphere locally resembles a two-dimensional Eucledian plane. 



Formal Definition of Topological Manifolds:

An n-dimensional topological manifold M is a tolopogical *Hausdorff space* with a countable base which is locally *homeomorphic* to R^n. This means that for every point __p__ in __M__, there is an open neighbourhood __U__ of __p__ and a homeomorphism ___phi : U -> V___ which maps the set __U__ onto the open set __V__ which is a subset of __R^n__. Aditionally:
* The mapping ___phi : U -> V___ is called a __chart__ or __coordinate system__.
* The set ___U___ is the __domain__ or __local coordinate neighbourhood__ of the chart.
* The image of the point __p__ in ___U___, denoted by ___phi(p) in R^N___, is called the __coordinates__ or __local coordinates__ of __p__ in the chart.
* A set of charts ___{ phi_alpha | alpha in N }___, with domains __U_alpha__ is called the __atlas__ of M, if the union of all elemets in __U_aphpa__ where __alpha is in N__ = __M__.

 

> (guess) Homeomorphic : Two objects that, from a topological point of view, are identical, but geometrically change chape


```
A topological space X is Hausdorff if for any x,y in X with x!=y there exists open sets 
U (containing x) and V (containing y) such that U intersecting V = NULL.

        [ 
          Topological Space : is a set X together with a collection of open subsets T that 
          satisfies the four conditions:
            * It contains the empty set NULL
            * X is in T
            * The intersection of a finite number of sets in T is also in T
            * The union of an arbitrary number of sets in T is also in T  
        ]
```

#### Domains
The manifold __X__ has domains or local coordinate neighourhoods. As an example, we will take two domains, U_alpha and U_beta. They both have an individual shape in R^n space and intersect, but they don't cover the entirety of the manifold space.

> If the manifold has enough domains that it covers it's whole area exactly, it is called an __Atlas__.


#### Chart
Each local point on the manifold has a mapping into a lower dimensional Eucledian space through the homography ___phi___, also called the __chart__ or __coordinate system__.

if we do map one of the manifold points __p__ into Eucledian, that point will be called the __coordinate__ or __local coordinate__ of __p__. 

#### Mappings
Manifolds are based on mapping. You can map the manifold into local coordinates (Eucledian), or you can do multiple mapings between the parameter of a curve to the location on the manifold and then to local coordinates.

The ___transition map___ is the mapping between the intersecting parts of U_alpha and U_beta :            
  phi_{alpha, beta} = phi_beta o phi_alpha^-1  AND      
  NULL_{beta, alpha} = phi_alpha o phi_beta^-1 WHERE      
  phi_alpha( U_alpha intersection U_beta ) OR      
  phi_beta ( U_alpha intersection U_beta )      
```
The 'o' symbol above refers to a function composition:     
   h = f o g = f(g(x))
```

Depending on the differentiability of these transition functions, they might transform the manifold into an ___differentiable manifold___ denoted by C^k, where k is the number it is continuously differentiable. The most important variation is the one where it is infinitely differentiable, creating what is often called ___Smooth Manifolds___. 

Such manifolds allow the use of calculus on it's surface


```

Example : A 1D Manifold with Multiple Charts

Our 1D manifold is a unit circle or r = 1. If we use polar coordinates, we can refer to it as r, theta.

A simple mapping like phi(r, theta) will not work because theta is a multi-valued, so we need to restrict the domain. We will also need more than one chart mapping because a chart can only work on an open set, we can't use [0, 2PI).

We can create four charts that have the form M -> R:
```
![The four charts](https://i.imgur.com/zlt1QGS.png)

```
There is overlap between the charts where each one has an open set.

The four charts together form the atlas for M, because their domains span the entirety of the manifold.


This is one of many possible variations for the charts. You can also split the manifold using standard Eucledian coordinates and a stereographic projection. You take either the south or the north pole, than choose any other point on the manifold and project onto the x axis. The two options do not map onto the same point in R^1.

Using the north pole, for any given point    p = (x, y)   on the circle, we can find the interesct with the X-axis using triangles:
```
![Mapping based on the North Pole](https://i.imgur.com/SfRMTmh.png)

```
Similarely, we can do the same thing from the south pole for any point  q :
```
![Mapping based on the South Pole](https://i.imgur.com/kNiTiLH.png)

```
Together, they make up the atlas for M. Since the charts are 1-1, and knowing that x^2 + y^2 = 1 we can find the inverse:
```
![Calculating the Inverse homography](https://i.imgur.com/gvmdNRA.png)


```
With these, we can find the transition map phi_{alpha, beta}:
```