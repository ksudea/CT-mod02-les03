# Task 1

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

attended_submitted = "Alice" in submitted and "Alice" in attended
if(attended_submitted):
    print(attended_submitted, "Alice attended class and submitted assignment")
else: 
    print(attended_submitted, "Alice did not both attend class and submit assignment")