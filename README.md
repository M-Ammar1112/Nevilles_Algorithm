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

### Importance:
nevilles's algorithm has immense importance than other polynomial interpolation methods that is this algorithm is numerically stable that is it uses the given data directly and there is no requirement to represent the polynomial in the basis of 1,t,... . Although, it is fast and dynamic and it has the simple structure and easy to update.

## Mathematical Explanation:
If we consider a polynomial P(X) having 'n' number of nodes so the formula is as follows

$$P_{a,...,b}(x)=(\frac{x-x_{j}}{x_{i}-x_{j}})P_{a,...,j-1,j+1,...b}(x) + (\frac{x_{i}-x}{x_{i}-x{j}})P_{a,..i-1,i+1,..,b}(x)$$
So, by using the formula recursively we can generate an array of polynomials

$$P_{0}(x)$$
$$P_{1}(x)P_{0,1}(x)$$
$$P_{2}(x)P_{1,2}(x)P_{0,1,2}(x)$$
$$.$$
$$.$$
$$.$$
$$P_{n}(x)P_{n-1,n}(x)....P_{0,...,n}$$

So, we can display the polynomial array as matrix form

$$S_{ij}(x)$$
where i and j are the position of element in the matrix

$$S_{00}(x)$$
$$S_{10}(x)S_{11}(x)$$
$$S_{20}(x)S_{21}(x)S_{22}(x)$$
$$.$$
$$.$$
$$.$$
So, for all j=0 P(x) is constant and equals to f(x) and all values oj j>0 the general recursive formula is as given which is also used in the code. So, if there is (n+1) data points given:

$$(x_{0},y_{0}),(x_{1},y_{1}),(x_{2},y_{2}),....,(x_{n},y_{n})$$
for an underlying function f and given number of x for which we would like to estimate of f(x). We are interested in computing degree n polynomial given:

$$P_{0,1,...n}(x)$$
The general recursive formula for this is as follow

$$$$

$$P_{i-j,i-j+1,..,i}(x)=\frac{(x-x_{i-j})P_{i-j+1,..,i}(x)+(x-x_{i})P_{i-j,...,i-1}(x)}{x_{i}-x_{i-j}}$$

## About the code:
In this code we define a function called neville which has three arguments. These three arguments is used in the code and given when the function is called. In this functon we use the formula of neville's interpolation algorithm which is made recursive by the loops used in this code. Moreover,we import three libraries numpy,scipy and matplotlib. These libraries are used in making the plot of the given data and expressing the coordinate of the interpolating algorithm.

## Code:
### Importing libraries:
#### Numpy library:
The numpy library is used here to get the result of interpolation directly from it so we can compare it with the estimate given by neville's algorithm and can judge the accuracy of the algorithm at the certain point.
#### The scipy library:
The function make_interp_spline is called from the scipy library to make the nodes to form the smooth curve ehen nodes are greater than three. We take the list x and y as an argument in the function that we import and assign it to X_Y_Spline method. Furthermore,we use numpy linspace function and set the curve smoothness to 500 and assign it to X_ and we put X_ as an argument in X_Y_Spline method and assign it to y.
#### The matplotlib library:
The pyplot and style functions are imported from this library. pyplot is used to plot the nodes on the graph style function is used here to set the style of the grid to 'ggplot'. we use a third argument 'r*' and 'g*' which represents the input nodes to be red and interpolating point a to be green coordinate. To implement the plotting we use if-else loop to set the control flow. If the input nodes are lesser than four so the plot is without converting it to curve else when the nodes are greater than four so it first converts it to the curve using scipy implementation and than plot it on the grid using matplotlib.

### Definition of function:
At first we define a function neville which have three arguments that is xlist,ylist and a. xlist is the input list of x and it is the list of size n, ylist is the input list of y which is corresponding to x in a sequece which is of the size n and 'a' is the arbitrary value of 'x' for which the value of polynomial to be estimated.
### Setting up variables:
we set two variables inside the neville function which is n and p. n is the len(xlist) in which the length of xlist input is assigned to n and p uses n and generate a list od zero's whose length is of size n. The example is as follows in which we take xlist as a hardcoded list which have five elements and a print function to print p:

xlist=[1,2,3,4,5]\n
n = len(xlist)\n
p = n*[0]\n
print(p)
