"""
You are keeping score for a baseball game with the strange rules. 
The game consists of several rounds, where the scores of past rounds 
may affect future rounds' scores.

At the beginning of the game, you start with an empty record. 
You are given a list of strings 'ops' where 'ops[i]' is the 'ith' operation 
you must apply to the record and is one of the following.

    1. An integer 'x' - Record a new score of 'x'.
    2. '+' -  Record a new score that is the sum of the previous two scores. 
        It is guaranteed there will always be two previous scores.
    3.  "D" - Record a new score that is double the previous score. 
        It is guaranteed there will always be a previous score.
    4. "C" - Invalidate the previous score, removing it from the recordd. 
        It is guaranteed there will always be a previous sore.

Return a sum of all the socres on the record.

Example 1: 
Input: 'ops' = ["5", "2", "C", "D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30

Example 2:
Input 'ops' = ["5", "-2", "4", "C", "D", "9", "+", "+"]
Output: 
Explanation:
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + (-2) + (-4) + 9 + 5 + 14 = 27
"""

def cal_points(ops):
    record = [] # Declare an empty record
    for op in ops:
        try:
            opToInt = int(op); # Convert the operation to an integer
            record.append(opToInt)
        except ValueError: # ValueError is trigger if the op is not convertible to int
            last_index = record.__len__() - 1
            if op == "+":
                # Since it is guaranted there will always be two previous scores
                last_score = record[last_index]
                second_to_last_score = record[last_index - 1]
                record.append(last_score + second_to_last_score)
            elif op == "D":    
                # Since it is guaranteed there will always be a previous cores
                double_prev_score = 2 * record[last_index]
                record.append(double_prev_score)
            elif op == "C":
                # Since it is guaranteed there will always be a previous cores
                record.pop()
    total = 0
    for score in record:
        total += score
    return total        

# TEST EXAMPE 1
output_1 = cal_points(["5", "2", "C", "D","+"])
print(output_1) # 30

# TEST EXAMPLE 2
output_2 = cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"])
print(output_2) # 27