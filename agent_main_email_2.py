from graphs.email_agent import email_agent_graph
from example_emails import EMAILS

def main():
    message_1 = {"messages": [("human", EMAILS[2])]}
    for chunk in email_agent_graph.stream(message_1, stream_mode="values"):
        chunk["messages"][-1].pretty_print()

if __name__ == "__main__":
    main()