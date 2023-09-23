# IMPLEMENTATION_OF_NEVILLE'S_ALGORITHM_IN_PYTHON

## Abstract
This report is concerned with the implementation of neville's algorithm in python. neville's algorithm is the recursive algorithm that provides the numerical solution for polynomial interpolations. So, in this report we make the function of neville's algorithm to find the estimate of polynomial on arbitrary value of x.

<h2>Introduction:</h2>
<h3>Nevilles's Algorithm:</h3>
<body>It is appropriate to discuss about neville's algorithm in detail before going into the explanation of code. Neville's algorithm is a recurrence relation used for polynomial interpolation. When there is a N degree polynomial p(x) so it have N+1 data points from which it goes through (x,y) which is the abscissa and ordinate of an underlying function f(x). So, we have to estimate p(x) on any value of x by following method.
so if we take the polynomial</body> 

$$P_{i,j}$$ 
<body>which is the degree of N=j-i and passes through the points</body>


$$(x_{k},y_{k})$$
<body>where k=i,i+1,....,j
So, the polynomial recurrence relation which it should testify is as follows:</body>

$$P_{i,i}(x)=Y_{i}$$
<body>when i is greater than 0 and lesser than N</body>

$$P_{i,j}(x)=\frac{(x_{j}-x)P_{i,j-1}(x)+(x-x_{i})P_{i+1,j}(x)}{x_{j}-x{i}}$$
<body>when i is greater than 0 and j is greater than i and lesser than N
