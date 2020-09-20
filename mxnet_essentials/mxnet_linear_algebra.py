# -*- coding: utf-8 -*-
# !pip install mxnet gluoncv
import mxnet as mx

##########################
# Instantiate two scalars
##########################
x = mx.nd.array([3.0]) 
y = mx.nd.array([2.0])

##########################
# Add them
##########################
print('x + y = ', x + y)

##########################
# Multiply them
##########################
print('x * y = ', x * y)

##########################
# Divide x by y
##########################
print('x / y = ', x / y)

##########################
# Raise x to the power y. 
##########################
print('x ** y = ', mx.nd.power(x,y))

mx.nd.array([9]).asscalar()

# Vectors
u = mx.nd.arange(4)
print('u = ', u)

print(u[3])

a = 2
x = mx.nd.array([1,2,3])
y = mx.nd.array([10,20,30])
print(a * x)
print(a * x + y)

# Matrices.

A = mx.nd.zeros((5,4))
A

x = mx.nd.arange(20)
A = x.reshape((5, 4))
A

print('A[2, 3] = ', A[2, 3])

print('row 2', A[2, :])
print('column 3', A[:, 3])

A.T

# Tensors
X = mx.nd.arange(24).reshape((2, 3, 4))
print('X.shape =', X.shape)
print('X =', X)

u = mx.nd.array([1, 2, 4, 8])
v = mx.nd.ones_like(u) * 2
print('v =', v)
print('u + v', u + v)
print('u - v', u - v)
print('u * v', u * v)
print('u / v', u / v)

B = mx.nd.ones_like(A) * 3
print('B =', B)
print('A + B =', A + B)
print('A * B =', A * B)

# Random
signal = mx.nd.random.randn(1000, 1)
print(signal.shape)

# Statistics
print(mx.nd.sum(signal))
print(mx.nd.mean(signal))

print(mx.nd.mean(signal))
print(mx.nd.sum(signal) / signal.size)

# Matrix Multiplication
A = mx.nd.ones(shape=(3, 4))
B = mx.nd.ones(shape=(4, 5))
mx.nd.dot(A, B)

# l2 norm
mx.nd.norm(signal)
# formula: mx.nd.sqrt(mx.nd.sum(signal ** 2))

# l1 norm
mx.nd.sum(mx.nd.abs(signal))

