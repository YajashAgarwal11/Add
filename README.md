# Add
Addition of two numbers in python
Explanation:     
num1 and num2 are two variables storing numbers.
+ is the addition operator.
print() displays the result.

#Print 5 numbers

Explanation:   
i = int(input("Enter a number: "))
This line takes a number as input from the user and stores it as an integer in variable i.
For example, if the user types 3, then i = 3.
while i <= 5:
This is a while loop, which means it will keep running as long as i is less than or equal to 5.
If i is greater than 5, it won't run at all.
print(i)
This prints the current value of i.
i = i + 1
This increases i by 1 every time the loop runs, so the loop eventually stops when i > 5.

#Print i to n

Explanation:    
n = int(input("Enter a number: "))
Takes a number from the user and stores it in variable n.
Example: If user enters 5, then n = 5.
i = 0
Starts a counter variable i from 0.
while i <= n:
The loop continues as long as i is less than or equal to n.
print(i)
Prints the current value of i.
i = i + 1
Increases i by 1 in each loop so the loop moves forward and eventually stops.

#Reverse Print

Explanation:   
i = int(input("Enter a number: "))
Takes a number as input from the user and stores it in variable i.
Example: If user enters 5, then i = 5.
while i >= 0:
The loop runs as long as i is greater than or equal to 0.
It’s a reverse loop, counting down to 0.
print(i)
Displays the current value of i.
i = i - 1
Decreases i by 1 in each loop step to go backwards.

#Sum of numbers from 1 to n

Explanation:  
n = int(input("Enter a number: "))
→ Takes a number n from the user to specify the upper limit.
Example: if user enters 5, we want to find 1 + 2 + 3 + 4 + 5.
i = 1
→ Starting value (i) is 1.
m = 0
→ m will store the sum. Initially it's 0.
while i <= n:
→ Runs the loop until i becomes greater than n.
m = i + m
→ Adds the current number i to the sum m.
i = i + 1
→ Increments i by 1 to move to the next number.
print(m)
→ Prints the updated sum after each step.

#Equilateral or Isosceles or Scalene Triangle

Explanation:  
Checks if all three sides are equal → then it’s an Equilateral Triangle.
If any two sides are equal → it’s an Isosceles Triangle.
If all sides are different → it’s a Scalene Triangle.

#Perimeter and area of a rectangle

Explanation:  
The program asks the user to enter the length and breadth of a rectangle.
It then calculates:
  Perimeter using the formula 2 × (length + breadth)
  Area using the formula length × breadth
Finally, it prints both the perimeter and area of the rectangle.

#Sum of Squares from 1 to n 

Explanation:  
The program starts by taking a number n from the user, which is the range limit.
It then uses a while loop to go from 1 to n, and in each step, it:
Squares the current number (i × i)
Adds that square to a total sum x
This continues until all numbers from 1 to n are squared and added.
Finally, it prints the total sum of squares.
