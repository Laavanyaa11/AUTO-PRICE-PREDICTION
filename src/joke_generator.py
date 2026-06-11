"""
Random Joke Generator using External APIs

This module provides functions to fetch and display random jokes
from various external joke APIs.
"""

import requests
import json
from typing import Dict, Optional, List
import time


class JokeGenerator:
    """Generate random jokes from external APIs."""
    
    # Available joke APIs
    JOKE_APIS = {
        'official_joke_api': 'https://official-joke-api.appspot.com/random_joke',
        'joke_ninja': 'https://v2.jokeapi.dev/joke/Any',
        'dad_jokes': 'https://icanhazdadjoke.com/',
        'programming_jokes': 'https://official-joke-api.appspot.com/jokes/programming/random'
    }
    
    def __init__(self, timeout: int = 5):
        """
        Initialize JokeGenerator.
        
        Parameters:
        - timeout: Request timeout in seconds (default: 5)
        """
        self.timeout = timeout
        self.last_joke = None
        self.jokes_cache = []
    
    def get_random_joke(self, source: str = 'official_joke_api') -> Optional[Dict]:
        """
        Fetch a random joke from a specific API.
        
        Parameters:
        - source: API source ('official_joke_api', 'joke_ninja', 'dad_jokes', 'programming_jokes')
        
        Returns:
        - Dictionary with joke data or None if request fails
        """
        if source not in self.JOKE_APIS:
            print(f"Error: Unknown source '{source}'. Available sources: {list(self.JOKE_APIS.keys())}")
            return None
        
        url = self.JOKE_APIS[source]
        headers = {
            'User-Agent': 'JokeGenerator/1.0 (Python)'
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            
            joke_data = response.json()
            self.last_joke = joke_data
            
            return joke_data
        
        except requests.exceptions.Timeout:
            print(f"Error: Request to {source} timed out.")
            return None
        except requests.exceptions.ConnectionError:
            print(f"Error: Failed to connect to {source}.")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"Error: HTTP error occurred - {e}")
            return None
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON response from {source}.")
            return None
        except Exception as e:
            print(f"Error: Unexpected error - {str(e)}")
            return None
    
    def format_joke(self, joke_data: Dict, source: str = 'official_joke_api') -> Optional[str]:
        """
        Format joke data based on API source format.
        
        Parameters:
        - joke_data: Dictionary containing joke data
        - source: API source to determine format
        
        Returns:
        - Formatted joke string or None
        """
        if not joke_data:
            return None
        
        try:
            if source == 'official_joke_api':
                setup = joke_data.get('setup', '')
                punchline = joke_data.get('punchline', '')
                return f"{setup}\n{punchline}"
            
            elif source == 'joke_ninja':
                if joke_data.get('type') == 'single':
                    return joke_data.get('joke', '')
                else:
                    setup = joke_data.get('setup', '')
                    delivery = joke_data.get('delivery', '')
                    return f"{setup}\n{delivery}"
            
            elif source == 'dad_jokes':
                return joke_data.get('joke', '')
            
            elif source == 'programming_jokes':
                setup = joke_data.get('setup', '')
                punchline = joke_data.get('punchline', '')
                return f"{setup}\n{punchline}"
            
            else:
                return str(joke_data)
        
        except Exception as e:
            print(f"Error formatting joke: {str(e)}")
            return None
    
    def get_and_print_joke(self, source: str = 'official_joke_api') -> bool:
        """
        Fetch and print a random joke in one call.
        
        Parameters:
        - source: API source to fetch from
        
        Returns:
        - True if successful, False otherwise
        """
        joke_data = self.get_random_joke(source)
        
        if joke_data:
            formatted_joke = self.format_joke(joke_data, source)
            if formatted_joke:
                print("\n" + "="*60)
                print(f"🎭 JOKE FROM {source.upper().replace('_', ' ')}")
                print("="*60)
                print(formatted_joke)
                print("="*60 + "\n")
                return True
        
        return False
    
    def get_multiple_jokes(self, count: int = 5, source: str = 'official_joke_api') -> List[Dict]:
        """
        Fetch multiple random jokes.
        
        Parameters:
        - count: Number of jokes to fetch
        - source: API source to fetch from
        
        Returns:
        - List of joke dictionaries
        """
        jokes = []
        
        for i in range(count):
            print(f"Fetching joke {i+1}/{count}...")
            joke_data = self.get_random_joke(source)
            
            if joke_data:
                jokes.append(joke_data)
                time.sleep(0.5)  # Be respectful to the API
            else:
                print(f"Failed to fetch joke {i+1}")
        
        self.jokes_cache = jokes
        print(f"\nSuccessfully fetched {len(jokes)} jokes!")
        return jokes
    
    def print_all_jokes(self, jokes: Optional[List[Dict]] = None, source: str = 'official_joke_api'):
        """
        Print all jokes from a list.
        
        Parameters:
        - jokes: List of joke dictionaries (uses cache if None)
        - source: API source for formatting
        """
        if jokes is None:
            jokes = self.jokes_cache
        
        if not jokes:
            print("No jokes to display.")
            return
        
        print("\n" + "#"*60)
        print(f"# COLLECTION: {len(jokes)} Jokes from {source.upper().replace('_', ' ')}")
        print("#"*60 + "\n")
        
        for i, joke_data in enumerate(jokes, 1):
            formatted_joke = self.format_joke(joke_data, source)
            if formatted_joke:
                print(f"Joke #{i}:")
                print("-" * 60)
                print(formatted_joke)
                print("-" * 60 + "\n")
    
    def get_jokes_by_category(self, category: str = 'programming', count: int = 3) -> List[Dict]:
        """
        Fetch jokes by category (if source supports it).
        
        Parameters:
        - category: Category of jokes
        - count: Number of jokes to fetch
        
        Returns:
        - List of jokes in specified category
        """
        url = f"https://official-joke-api.appspot.com/jokes/{category}/random/{count}"
        headers = {'User-Agent': 'JokeGenerator/1.0 (Python)'}
        
        try:
            response = requests.get(url, headers=headers, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching {category} jokes: {str(e)}")
            return []
    
    def list_available_sources(self) -> List[str]:
        """List all available joke API sources."""
        return list(self.JOKE_APIS.keys())
    
    def get_last_joke(self) -> Optional[str]:
        """Get the last fetched joke formatted."""
        if self.last_joke:
            # Try to determine source from last fetch
            return self.format_joke(self.last_joke, 'official_joke_api')
        return None


def main():
    """Main function to demonstrate joke generator functionality."""
    print("\n🎭 Welcome to Random Joke Generator! 🎭\n")
    
    generator = JokeGenerator()
    
    # Display available sources
    print("Available joke sources:")
    for source in generator.list_available_sources():
        print(f"  - {source}")
    print()
    
    # Example 1: Get a random joke
    print("\n[Example 1] Fetching a random joke...")
    generator.get_and_print_joke('official_joke_api')
    
    # Example 2: Get a dad joke
    print("[Example 2] Fetching a dad joke...")
    generator.get_and_print_joke('dad_jokes')
    
    # Example 3: Get multiple programming jokes
    print("[Example 3] Fetching multiple programming jokes...")
    jokes = generator.get_jokes_by_category('programming', count=3)
    generator.print_all_jokes(jokes, 'programming_jokes')
    
    # Example 4: Get jokes from different source
    print("[Example 4] Fetching a joke from JokeAPI...")
    generator.get_and_print_joke('joke_ninja')


if __name__ == "__main__":
    main()
