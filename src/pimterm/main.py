import argparse
from openai import OpenAI


client = OpenAI()

def handle_command(args):

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "hatGPT you are a bot that gives back specific Linux commands required to complete the task mentioned. Please provide only the command itself, without any additional explanation. If the solution requires installing software, include only the necessary command to install it, with minimal additional text. your given text will be displayed on a linux terminal so give your awnsers as plain text"},
        {"role": "user", "content": args.command}
        ] 
    )

    print(completion.choices[0].message.content)
          
def handle_question(args):
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Chatgpt, you will be asked questions by a client that recieves your response in the linux terminal, therefore make your awnsers short and plaintext. dont add ethical warnings or redundant information. awnser the question in the languagtge it is being asked."},
        {"role": "user", "content": args.question}
        ] 
    )
    print(completion.choices[0].message.content)

def main():
    parser = argparse.ArgumentParser(description="pimterm Command Line Interface")
    subparsers = parser.add_subparsers(help='commands')

    # Command subparser
    command_parser = subparsers.add_parser('command', aliases=['c'], help='Send a command to the program')
    command_parser.add_argument('command', type=str, help='Command to execute')
    command_parser.set_defaults(func=handle_command)

    # Question subparser
    question_parser = subparsers.add_parser('question', aliases=['q'], help='Ask a question')
    question_parser.add_argument('question', type=str, help='Question to ask')
    question_parser.set_defaults(func=handle_question)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
