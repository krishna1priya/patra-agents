from patra_agent.graph import run_patra_graph

def main():
    question = ("how many models are in the system?")
    result = run_patra_graph(question)
    print(result)

if __name__ == '__main__':
    main()