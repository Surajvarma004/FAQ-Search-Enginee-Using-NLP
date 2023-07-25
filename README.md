# Question Similarty

# step 1
create environment using python=3.7
> conda create --name faq python=3.7

# Step 2 (Activate ENv)
> conda activate faq

# Step 3 (Install Dependencies)
> pip install -r requirements.txt

# Step 4 Run python file
> python app.py


# Step 5 Check using API 
this project is used to find similar question

# API CALL

## Request
http://192.168.3.124:8091/find_question
## DATA
{
    "ques":"how to apply masters in us",
    "conf":0.10
}
## Responce
> {
    "similar_questions": [
        "How can I get entry in MIT?",
        "What's the procedure for an Indian student to get admitted into a MS program in the US?",
        "What are the colleges that I can apply for MS in CS in US based on my profile?",
        "How can I transfer to manipal university?",
        "What are the best institutes for MS in USA?",
        "What should be the timeline for applying to a us university for undergraduate (I am in 11 standard)?"
    ]
}
