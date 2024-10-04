from patra_agent.graph import run_patra_graph
from patra_agent.util import llm

def main():
    question = ("What is the architecture of edge device?")
    result = run_patra_graph(question)
    # messages = [    (     
    #    "system",        
    #                  "You are a helpful assistant that translates English to French. Translate the user sentence.",   
    #                    ),    ("human", "man?"),]
    # ai_msg = llm.invoke(messages)
    # print(ai_msg.content)

if __name__ == '__main__':
    main()