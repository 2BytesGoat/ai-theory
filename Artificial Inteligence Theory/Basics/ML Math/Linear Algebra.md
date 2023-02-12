# Components

## Vectors
Are 1-Dimensional arrays of numbers, arranged in order.

```python
x = [22, 0, -1, 42, 5] # this is a vector
print(x[0]) # this is the first element of the vector
>> 22
```

## Matrices 
Are 2-Dimensional arrays of numbers. Imagine stacking several vectors on top of each other.

```python
x = [[1, 2, 3,  4,  5,  6],
	 [7, 8, 9, 10, 11, 12]] # this is a matrix
print(x[1][1]) # if we print the element from row 1, column 1
>> 8 # we see it's the 8th element of the matrix
```

>[!tip] Did you know that
> **Black and white images** are actually 2D matrices with values ranging from 0-255. Each value of the image is a pixel, and the number of pixels is given by the width times height of the image.

## Tensors 
Are n-Dimensional arrays of numbers. Imagine a vector is a toothpick, and that you can stack them both on top of each other and side-wise. I struggle to imagine tensors of a dimension higher than 3D, and the best way to wrap my head around them is with a real-world example.

```python
x = [[[0, 1], [2, 3]],
	 [[4, 5], [6, 7]]] # this is a 3D tensor
print(x[0][1][1]) # if we print the element at row 0, column 1 and depth 1
>> 3 # we see we get element number 3
```

>[!tip] Did you know that
> **Color images** are actually 3D matrices (or tensors) with values ranging from 0-255. You get a colored image by stacking Red, Green and Blue images on top of each other ([see example](https://upload.wikimedia.org/wikipedia/commons/5/56/RGB_channels_separation.png)). The dimensions are image height, image width and color channel.

## Identity matrix


# Operations

## Tier 1 - Operations

Addition can be done on arrays of the same shape, or between an array and a vector which share a dimension. Matrices and vectors also support addition, subtraction, multiplication and division with scalars.

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

## Tier 2 - Operations

## Transpose

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

## Element-wise product (Hadmard product)

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

## Dot product

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

### Distributivity 
Matrix multiplication is distributive.
`x * (y + z) = x * y + x * z`

### Associativity
Matrix multiplication is associative.
`x * (y * z) = (x * y) * z`

### Commutativity
Matrix multiplication is ***not*** commutative, however the dot product between two vectors is.
`np.dot(x.T, y) == np.dot(y.T, x) `

