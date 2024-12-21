import asyncio
from colorama import init, Fore, Style
from chat import chat

# Initialize colorama for Windows color support
init()

async def main():
    print(f"{Fore.CYAN}Welcome to Simple Chat! Type 'exit' to quit.{Style.RESET_ALL}")
    
    while True:
        # Get user input
        user_input = input(f"\n{Fore.GREEN}You:{Style.RESET_ALL} ")
        
        # Check for exit command
        if user_input.lower() == 'exit':
            break
        
        try:
            # Get and display AI response
            response = await chat(user_input)
            if response:
                print(f"\n{Fore.BLUE}Assistant:{Style.RESET_ALL} {response}")
        except Exception as error:
            print(f"{Fore.RED}Error: {str(error)}{Style.RESET_ALL}")

if __name__ == "__main__":
    asyncio.run(main())