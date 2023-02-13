Algebra can be a bit daunting at first, especially to folks that haven't trained their math muscle in a long time. However, there are a platitude of math libraries that do the heavy lifting for us. Our task is to understand which formulas to use, and why they behave like they do.

My recommendation for this chapter, is to shuffle around the notions and not worry too much about fully grasping them from one shot. This information will make a lot more sense once you find an application for it, so just look around, make yourself familiar with the terms for later on.

![](media/linear_algebra/introduction.jpeg | 420)
Goat Writing Math Formulas on a Blackboard (image generated with [Stable Diffusion](https://en.wikipedia.org/wiki/Stable_Diffusion))

# 1. Components

## 1.1. Vectors
Are 1-Dimensional arrays of numbers, arranged in order.

```python
x = [22, 0, -1, 42, 5] # this is a vector
print(x[0]) # this is the first element of the vector
>> 22
```

## 1.2. Matrices 
Are 2-Dimensional arrays of numbers. Imagine stacking several vectors on top of each other.

```python
x = [[1, 2, 3,  4,  5,  6],
	 [7, 8, 9, 10, 11, 12]] # this is a matrix
print(x[1][1]) # if we print the element from row 1, column 1
>> 8 # we see it's the 8th element of the matrix
```

>[!tip] Did you know that
> **Black and white images** are actually 2D matrices with values ranging from 0-255. Each value of the image is a pixel, and the number of pixels is given by the width times height of the image.

## 1.3. Tensors 
Are n-Dimensional arrays of numbers. Imagine a vector is a toothpick, and that you can stack them both on top of each other and side-wise. I struggle to imagine tensors of a dimension higher than 3D, and the best way to wrap my head around them is with a real-world example.

```python
x = [[[0, 1], [2, 3]],
	 [[4, 5], [6, 7]]] # this is a 3D tensor
print(x[0][1][1]) # if we print the element at row 0, column 1 and depth 1
>> 3 # we see we get element number 3
```

>[!tip] Did you know that
> **Color images** are actually 3D matrices (or tensors) with values ranging from 0-255. You get a colored image by stacking Red, Green and Blue images on top of each other ([see example](https://upload.wikimedia.org/wikipedia/commons/5/56/RGB_channels_separation.png)). The dimensions are image height, image width and color channel.

## 1.4. The Identity Matrix

It is a type of 2D matrix, in which all elements are zero, except the ones of the main diagonal.

```python
identity = [
			[1, 0, 0],
			[0, 1, 0],
			[0, 0, 1]
		   ]
```

# 2. Operations

## 2.1. Tier 1 Operations

Matrices and vectors also support addition, subtraction, multiplication and division with scalars. Addition can be done on arrays of the same shape, or between an array and a vector which share a dimension. 

```python
import numpy as np

x = np.array([[1, 2, 3],
			  [4, 5, 6]])
y = np.array([[1, 2, 3],
			  [4, 5, 6]])
z = np.array([1, 2, 3])	# a vector is a 1D array

# adding a scaler
print(x + 1)
>> array([[2, 3, 4],
		  [5, 6, 7]])

# multiple operations
print(x * 2 + 1)
>> array([[ 3,  5,  7], 
	  	  [ 9, 11, 13]])

# adding two arrays
print(x + y)
>> array([[ 2,  4,  6], 
	  	  [ 8, 10, 12]])

# adding an array and a vector
print(x + z)
>> array([[ 2, 4, 6], 
	  	  [ 5, 7, 9]])
```

## 2.2. Tier 2 Operations

### 2.2.1. Transpose

> "The transpose of a matrix is the mirror image of the matrix across a diagonal line, called the main diagonal." - **Deep Leaning** by *Ian Goodfellow et al.*

```python
import numpy as np

x = np.array([[1, 2, 3],
			  [4, 5, 6]])
x_transposed = x.T
print(x_transposed)
>> array([[1, 4],
		  [2, 5],
	      [3, 6]])
```

There are a few terms that you'll encounter when people start multiplying matrices and vectors, and you'll need to know the difference, or it's going to get messy.

### 2.2.2. Element-wise Product (Hadmard product)

The element-wise product is used in classical computer vision to create filters (blur, edge-detection).

```python
import numpy as np

x = np.array([[1, 2, 3],
			  [4, 5, 6]])
y = np.array([[1, 2, 3],
			  [4, 5, 6]])
print(x * y)
>> array([[ 1,  4,  9],
          [16, 25, 36]])
          
''' this is the same as doing
rez[0][0] = x[0][0] * y[0][0]
rez[1][1] = x[1][0] * y[1][1]
...
'''
```

### 2.2.3. Dot Product

The dot product is used in Deep Learning models in order to parallelize computations, rather than having to use less efficient methods such as for loops. You'll see more about that in the Deep Learning chapter.

```python
import numpy as np

x = np.array([[1, 2, 3],
			  [4, 5, 6]])
z = np.array([[1, 2],
			  [3, 4],
			  [5, 6]])
print(np.dot(x, z))
>> array([[22, 28],
          [49, 64]])
          
''' this is the same as doing
rez[0][0] = x[0][0] * z[0][0] + x[0][1] * z[1][0] + x[0][2] * z[2][0]
rez[0][1] = x[0][0] * z[0][1] + x[0][1] * z[1][1] + x[0][2] * z[2][1]
...
'''
```
 
> [!warning] Be careful
> Consider three arrays
> - `x.shape()` is (2, 3), 
> - `y.shape()` is (2, 3) and 
> - `y.shape()` is (3, 2) respectively. 
> 
> You can do **element-wise product** only if the dimensions are the same (between x and y).
> 
> You can do **dot product** only if the shared dimension is closest between the two arrays (between x and z).

Some of us may not have heard this words since one of our past lives. However, it's important to know they exist, so we know what to look them up later.

### 2.3.4. Bonus - Product Properties

#### Distributivity 
Matrix multiplication is distributive.
`x * (y + z) = x * y + x * z`

#### Associativity
Matrix multiplication is associative.
`x * (y * z) = (x * y) * z`

#### Commutativity
Matrix multiplication is ***not*** commutative, however the dot product between two vectors is.
`np.dot(x.T, y) == np.dot(y.T, x) `

## 2.3. Tier 3 Operations

### 2.3.1. Matrix inverse 

The matrix inverse of X is the matrix which has the following property ... $$X^{-1} \odot X = I_n$$... where the symbol I represents the identity matrix.

```python
import numpy as np
from numpy.linalg import inv

x = np.array([[1, 2], [3, 4]])
x_inverse = inv(x)

print(x_inverse)
>>[[-2.   1. ]
   [ 1.5 -0.5]]
```

### 2.3.2. Norms

Norms are used to calculate the length of a vector in Euclidean space, and for the formula for those that are not light-hearted: $$||x||_p = (\sum|x_i|^p)^{1/p}$$
```python
import numpy as np
from numpy.linalg import norm

x = np.array([1, 2, 3, 4])
# by default numpy sets p to be 2
# this is also called the L2 norm
x_norm = norm(x) 

print(x_norm)
>> 5.477

# it returns the same value 
# no matter the sape of the array
y = np.array([[1, 2], [3, 4]])
y_norm = norm(y)

print(y_norm)
>> 5.477
```

The most commonly used norms are L1 and L2 norm. We may choose to use one in favor of the other, depending on the values within the array. If the values are closer to 0, we will choose the L1 norm.

>[!tip] Did you know that
> Another wacky name for the L2 norm is the Frobenius norm.

# References
1. **Introduction to linear algebra** - [Khan Academy](https://www.khanacademy.org/math/linear-algebra)