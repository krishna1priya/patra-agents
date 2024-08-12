from patra_agent.graph import run_patra_graph

def main():
    question = ("I'm planning to deploy a convolutional neural network model in a new location similar to the griffy-lake "
                "edgedevice. Which model would you recommend for best deployment accuracy and power consumption values? "
                "Tell me about all the options and explain me why?")
    result = run_patra_graph(question)
    print(result)

if __name__ == '__main__':
    main()