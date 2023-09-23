# IMPLEMENTATION_OF_NEVILLE'S_ALGORITHM_IN_PYTHON

## Abstract
This report is concerned with the implementation of neville's algorithm in python. neville's algorithm is the recursive algorithm that provides the numerical solution for polynomial interpolations. So, in this report we make the function of neville's algorithm to find the estimate of polynomial on arbitrary value of x.

## Introduction:
### Nevilles's Algorithm:
It is appropriate to discuss about neville's algorithm in detail before going into the explanation of code. Neville's algorithm is a recurrence relation used for polynomial interpolation. When there is a N degree polynomial p(x) so it have N+1 data points from which it goes through (x,y) which is the abscissa and ordinate of an underlying function f(x). So, we have to estimate p(x) on any value of x by following method.
so if we take the polynomial

$$P_{i,j}$$ 
which is the degree of N=j-i and passes through the points


$$(x_{k},y_{k})$$
where k=i,i+1,....,j
So, the polynomial recurrence relation which it should testify is as follows:

$$P_{i,i}(x)=Y_{i}$$
when i is greater than 0 and lesser than N

$$P_{i,j}(x)=\frac{(x_{j}-x)P_{i,j-1}(x)+(x-x_{i})P_{i+1,j}(x)}{x_{j}-x{i}}$$
when i is greater than 0 and j is greater than i and lesser than N

### Description:
Neville's Algorithm which is derived by eric harold neville in 1934 is based on the newton method for the polynomial interpolation which also involves recursion. In 1966, Lyness and Moler exhibited how to process the Maclaurin series of the last adding polynomial, which brings about mathematical approximations for the subsidiaries of the capability at the beginning. They did this by involving undetermined coefficients for the polynomials in Neville's calculation. The selection of points for evaluation is unrestricted in any capacity, despite the way that "this cycle needs more operations than are expected in limited difference approach." They likewise show how their methodology might be utilized to take care of direct issues.
