% Prolog provides 'is' to evaluate mathematical expressions

% X is 2 + 2. = X = 4

%CAN DO
% sqrt, sin, cos, tan, asin, acos, atan, atan2, sinh, cosh, tanh,
% asinh, acosh, atanh, log, log10, exp, pi, e

% You can use parenthese

% X is 3 + (2 * 10). =  X = 23
% You can also make comparisons

% 50 > 30. = yes

% (3*10) >= (50/2). = yes

% \+ (3 = 10). = yes (How to check for not equal)

% 5+4 =:= 4+5. = yes (Check for equality between expressions)

% 5+4 =\= 4+5. = yes (Check for non-equality between expressions)

% 5 > 10 ; 10 < 100. (Checks if 1 OR the other is true)


% X is mod(7,2). = X = 1 (Modulus)


double_digit(X,Y) :- Y is X*2.
% double_digit(4,Y). = Y = 8

% Take the 1st argument, multiply it times 2 and return it as the

% 2nd argument


% Get random value between 0 and 10

% random(0,10,X).


% Get all values between 0 and 10

% between(0,10,X).


% Add 1 and assign it to X

% succ(2,X).


% Get absolute value of -8

% X is abs(-8).


% Get largest value

% X is max(10,5).


% Get smallest value

% X is min(10,5).