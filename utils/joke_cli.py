"""
Command-line interface for Joke Generator

Provides an interactive CLI tool to fetch and display jokes.
"""

import sys
import argparse
from src.joke_generator import JokeGenerator


class JokeCLI:
    """Command-line interface for joke generator."""
    
    def __init__(self):
        self.generator = JokeGenerator()
    
    def run_interactive(self):
        """Run interactive mode."""
        print("\n🎭 Random Joke Generator - Interactive Mode 🎭\n")
        print("Commands:")
        print("  'joke' or 'j'  - Get a random joke")
        print("  'list' or 'l'  - List available sources")
        print("  'source'       - Change joke source")
        print("  'help' or 'h'  - Show this help")
        print("  'exit' or 'q'  - Exit program\n")
        
        current_source = 'official_joke_api'
        
        while True:
            try:
                command = input("Enter command: ").strip().lower()
                
                if command in ['joke', 'j']:
                    self.generator.get_and_print_joke(current_source)
                
                elif command in ['list', 'l']:
                    sources = self.generator.list_available_sources()
                    print("\nAvailable sources:")
                    for i, source in enumerate(sources, 1):
                        status = "(current)" if source == current_source else ""
                        print(f"  {i}. {source.replace('_', ' ').title()} {status}")
                    print()
                
                elif command == 'source':
                    sources = self.generator.list_available_sources()
                    print("\nAvailable sources:")
                    for i, source in enumerate(sources, 1):
                        print(f"  {i}. {source.replace('_', ' ').title()}")
                    
                    choice = input("\nSelect source (number): ").strip()
                    try:
                        index = int(choice) - 1
                        if 0 <= index < len(sources):
                            current_source = sources[index]
                            print(f"\nSource changed to: {current_source}\n")
                        else:
                            print("Invalid selection!\n")
                    except ValueError:
                        print("Invalid input!\n")
                
                elif command in ['help', 'h']:
                    print("\nCommands:")
                    print("  'joke' or 'j'  - Get a random joke")
                    print("  'list' or 'l'  - List available sources")
                    print("  'source'       - Change joke source")
                    print("  'help' or 'h'  - Show this help")
                    print("  'exit' or 'q'  - Exit program\n")
                
                elif command in ['exit', 'q']:
                    print("\n👋 Thanks for using Joke Generator! Goodbye!\n")
                    break
                
                else:
                    print("Unknown command. Type 'help' for available commands.\n")
            
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted. Goodbye!\n")
                break
            except Exception as e:
                print(f"Error: {str(e)}\n")
    
    def run_single_joke(self, source='official_joke_api'):
        """Fetch and display a single joke."""
        self.generator.get_and_print_joke(source)
    
    def run_multiple_jokes(self, count=5, source='official_joke_api'):
        """Fetch and display multiple jokes."""
        jokes = self.generator.get_multiple_jokes(count, source)
        self.generator.print_all_jokes(jokes, source)
    
    def run_category_jokes(self, category='programming', count=5):
        """Fetch jokes by category."""
        jokes = self.generator.get_jokes_by_category(category, count)
        if jokes:
            print(f"\n=== {count} {category.upper()} JOKES ===")
            for i, joke in enumerate(jokes, 1):
                print(f"\n{i}. {joke.get('setup', '')}")
                print(f"   {joke.get('punchline', '')}")
            print()


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Random Joke Generator - Fetch jokes from various APIs',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''Examples:
  python joke_cli.py                    # Interactive mode
  python joke_cli.py -j                 # Get single joke
  python joke_cli.py -m 5 -s dad_jokes # Get 5 dad jokes
  python joke_cli.py -c programming -n 3  # Get 3 programming jokes
        '''
    )
    
    parser.add_argument('-i', '--interactive', action='store_true',
                        help='Run in interactive mode')
    parser.add_argument('-j', '--joke', action='store_true',
                        help='Get a single random joke')
    parser.add_argument('-m', '--multiple', type=int, metavar='COUNT',
                        help='Get multiple random jokes')
    parser.add_argument('-s', '--source', default='official_joke_api',
                        help='Joke source (default: official_joke_api)')
    parser.add_argument('-c', '--category', metavar='CATEGORY',
                        help='Get jokes from category (e.g., programming)')
    parser.add_argument('-n', '--number', type=int, default=5,
                        help='Number of category jokes to fetch (default: 5)')
    
    args = parser.parse_args()
    cli = JokeCLI()
    
    # If no arguments provided, run interactive mode
    if len(sys.argv) == 1:
        cli.run_interactive()
    
    elif args.interactive:
        cli.run_interactive()
    
    elif args.joke:
        cli.run_single_joke(args.source)
    
    elif args.multiple:
        cli.run_multiple_jokes(args.multiple, args.source)
    
    elif args.category:
        cli.run_category_jokes(args.category, args.number)


if __name__ == '__main__':
    main()
