from patra_agent.graph import run_patra_graph

def main():
    # few_shot_prompt = (
    #     "If one model can be accessed by three users, then 6 users can access 2 models and If there are 4 models available,  12 users who can use all models. Based on this, what is the max number of users who can access all the models?"
    # )
    # question = ("One model can be used by three users. Based on this, What is the max number of users who can access all the models?")
    question = ("Name the datasheet?")
    result = run_patra_graph(question)
    print(result)

if __name__ == '__main__':
    main()