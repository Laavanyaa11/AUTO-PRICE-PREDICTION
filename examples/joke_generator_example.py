"""
Example usage of the Joke Generator

Demonstrates various ways to use the JokeGenerator class.
"""

from src.joke_generator import JokeGenerator


def example_1_single_joke():
    """Example 1: Get and print a single random joke."""
    print("\n=== EXAMPLE 1: Single Random Joke ===")
    generator = JokeGenerator()
    generator.get_and_print_joke('official_joke_api')


def example_2_multiple_jokes():
    """Example 2: Get multiple jokes."""
    print("\n=== EXAMPLE 2: Multiple Random Jokes ===")
    generator = JokeGenerator()
    jokes = generator.get_multiple_jokes(count=3, source='official_joke_api')
    generator.print_all_jokes()


def example_3_different_sources():
    """Example 3: Get jokes from different API sources."""
    print("\n=== EXAMPLE 3: Different Joke Sources ===")
    generator = JokeGenerator()
    
    sources = ['official_joke_api', 'dad_jokes', 'programming_jokes']
    
    for source in sources:
        print(f"\nGetting joke from {source}...")
        generator.get_and_print_joke(source)


def example_4_programming_jokes():
    """Example 4: Get programming-specific jokes."""
    print("\n=== EXAMPLE 4: Programming Jokes ===")
    generator = JokeGenerator()
    jokes = generator.get_jokes_by_category('programming', count=5)
    
    if jokes:
        print(f"\nFetched {len(jokes)} programming jokes:\n")
        for i, joke in enumerate(jokes, 1):
            print(f"{i}. {joke.get('setup', '')}")
            print(f"   {joke.get('punchline', '')}\n")


def example_5_error_handling():
    """Example 5: Error handling with invalid source."""
    print("\n=== EXAMPLE 5: Error Handling ===")
    generator = JokeGenerator()
    
    # Try to use invalid source
    print("Trying to fetch from invalid source...")
    result = generator.get_random_joke('invalid_source')
    
    if result is None:
        print("Handled error gracefully!")
    
    # Show available sources
    print("\nAvailable sources:")
    for source in generator.list_available_sources():
        print(f"  ✓ {source}")


def example_6_interactive_menu():
    """Example 6: Interactive joke selector."""
    print("\n=== EXAMPLE 6: Interactive Joke Selector ===")
    generator = JokeGenerator()
    
    sources = generator.list_available_sources()
    
    print("\nAvailable joke sources:")
    for i, source in enumerate(sources, 1):
        print(f"{i}. {source.replace('_', ' ').title()}")
    
    # Simulate user selection (using first source)
    selected_index = 0
    selected_source = sources[selected_index]
    
    print(f"\nFetching from: {selected_source}")
    generator.get_and_print_joke(selected_source)


def main():
    """Run all examples."""
    print("\n" + "#"*70)
    print("#" + " "*68 + "#")
    print("#  RANDOM JOKE GENERATOR - EXAMPLES".ljust(69) + "#")
    print("#" + " "*68 + "#")
    print("#"*70)
    
    examples = [
        example_1_single_joke,
        example_2_multiple_jokes,
        example_3_different_sources,
        example_4_programming_jokes,
        example_5_error_handling,
        example_6_interactive_menu
    ]
    
    for example_func in examples:
        try:
            example_func()
        except Exception as e:
            print(f"\nError running example: {str(e)}")
    
    print("\n" + "#"*70)
    print("#" + " "*68 + "#")
    print("#  All examples completed!".ljust(69) + "#")
    print("#" + " "*68 + "#")
    print("#"*70 + "\n")


if __name__ == "__main__":
    main()
