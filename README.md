# Age-Detector
Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old.
Time Complexity: The time complexity of this program is O(1) because the execution time of this program does not depend on the input size. 

Auxiliary Space: The program uses a constant amount of auxiliary space, regardless of the input size.  The auxiliary space used by this program is O(1).

This approach has the advantage of being able to handle cases where the birth date is in the future or the current date is not a valid date (e.g. February 29 in a non-leap year). It also allows you to easily calculate the age in other units, such as months or days, by simply accessing the corresponding attribute of the relativedelta object (e.g. age.months or age.days).

