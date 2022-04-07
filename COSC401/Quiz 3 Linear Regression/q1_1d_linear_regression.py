def dot(xVec, yVec):
    return sum([x * y for x, y in zip(xVec, yVec)])

def linear_regression_2d(data):
    """
    Calculate the slope and intercept of a linear regression line
    of the form y = mx + c.

    Calculate using
    m = (n x.y - ∑x ∑y) / (n x.x - (∑x)^2)

    c = (∑y - m∑x) / n

    """
    n = len(data)
    x = [x for x, y in data]
    y = [y for x, y in data]
    x_sum = sum(x)
    y_sum = sum(y)
    x_squared_sum = sum([x**2 for x in x])
    xy_sum = sum([x * y for x, y in data])
    m = (n * xy_sum - x_sum * y_sum) / (n * x_squared_sum - x_sum**2)
    c = (y_sum - m * x_sum) / n
    return m, c

def linear_regression_1d(data):
    n = len(data)
    x = [x for x, y in data]
    x2 = [x for x, y in data]
    y = [y for x, y in data]
    xy=dot(x,y)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum([x**2 for x in x])
    # m = (n x.y - ∑x ∑y) / (n x.x - (∑x)2)
    m=((n*dot(x,y))-sum_x*sum_y)/((n*dot(x,x2))-sum([x**2 for x in x]))
    # c = (∑y - m∑x)/n
    c=(sum(y)-m*sum(x))/n
    return m,c




data = [(1, 4), (2, 7), (3, 10)]
m, c = linear_regression_1d(data)
print(m, c)
print(4 * m + c)

