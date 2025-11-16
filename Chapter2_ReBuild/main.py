from chat_assisant_AI import Chater

def start(agent: Chater):
    while True:
        print("input \'b\' to break")
        print("User:")
        input_str = input()
        if input_str == 'b':
            break
        else:
            agent.chat_start(input_str)

if __name__ == '__main__':
    print("What method do u want?\nA catgirl or normal?")
    sign = input()
    agent = Chater(sign)
    start(agent)