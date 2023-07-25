# your code starts here:
questions_file = open("Python-Complete-Course\July-25-2023\Quiz System\questions.txt",'r')
questions = [question.strip() for question in questions_file.readlines()]
questions_file.close()

total_score = 0
for question in questions:
    question_ans = question.split("=")
    user_answer = input(f"{question_ans[0]}=")
    if user_answer == question_ans[1]:
        total_score+=1

result_file = open("Python-Complete-Course\July-25-2023\Quiz System\\result.txt",'w')
result_file.write(f"Your final score is {total_score}/{len(questions)}.")

result_file.close()