from openai import OpenAI
import os

def gptTwiTeacher():
    api_key = os.environ.get("GPT_KEY")
    client = OpenAI(api_key=api_key) 
    
    
    prompt = f"""You are a friendly, patient, and knowledgeable Twi language teacher. You help learners understand and speak Twi confidently. Always use simple explanations and examples.
            For every question or lesson: Explain the concept in English and Give the Twi version. Optionally ask a follow-up question or give a short practice exercise.
            If the learner makes a mistake, kindly correct it and explain why. Start with a greeting and ask what the student wants to talk about.""" 

    # Using the GPT-4 model to analyse the answer
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are a TWI teacher. You help learners understand and speak TWI confidently. Always use simple explanations and examples."
            },
            {
                "role": "user",
                "content": f"Question or respons in TWI or English."
            },
            {
                "role": "assistant",
                "content" : prompt
            }
        ],
        temperature=0.7,
        max_tokens=300,
        top_p=1
    )

    return response

if __name__ == "__main__":
    response = gptTwiTeacher()
    print(response.choices[0].message.content)