# 🎭 Random Joke Generator

A Python-based random joke generator that fetches jokes from multiple external APIs. Get a laugh anytime with just a few lines of code!

## ✨ Features

- **Multiple API Sources**: Access jokes from various external APIs
  - Official Joke API
  - JokeAPI
  - icanhazdadjoke.com
  - Programming Jokes

- **Easy to Use**: Simple and intuitive API
- **Interactive CLI**: Command-line interface for interactive joke fetching
- **Batch Fetching**: Get multiple jokes at once
- **Category Support**: Fetch jokes by category (e.g., programming)
- **Error Handling**: Graceful error handling for network issues
- **Caching**: Built-in caching for recently fetched jokes

## 📦 Installation

### Requirements
- Python 3.6+
- `requests` library

### Setup

```bash
# Install dependencies
pip install requests

# Or use requirements.txt
pip install -r requirements.txt
```

## 🚀 Quick Start

### Basic Usage

```python
from src.joke_generator import JokeGenerator

# Create generator instance
generator = JokeGenerator()

# Get and print a random joke
generator.get_and_print_joke('official_joke_api')
```

### Available API Sources

```python
# List all available sources
sources = generator.list_available_sources()
print(sources)
# Output: ['official_joke_api', 'joke_ninja', 'dad_jokes', 'programming_jokes']
```

### Get Multiple Jokes

```python
# Fetch multiple jokes
jokes = generator.get_multiple_jokes(count=5, source='official_joke_api')

# Print all jokes
generator.print_all_jokes()
```

### Get Category-Specific Jokes

```python
# Get programming jokes
jokes = generator.get_jokes_by_category('programming', count=3)
```

### Different API Sources

```python
# Official Joke API - General jokes
generator.get_and_print_joke('official_joke_api')

# Dad Jokes
generator.get_and_print_joke('dad_jokes')

# JokeAPI - Various categories
generator.get_and_print_joke('joke_ninja')

# Programming Jokes
generator.get_and_print_joke('programming_jokes')
```

## 📚 API Reference

### JokeGenerator Class

#### `__init__(timeout=5)`
Initialize the JokeGenerator.

**Parameters:**
- `timeout` (int): Request timeout in seconds (default: 5)

#### `get_random_joke(source='official_joke_api')`
Fetch a random joke from a specific API.

**Parameters:**
- `source` (str): API source to fetch from

**Returns:**
- Dictionary with joke data or None if request fails

#### `get_and_print_joke(source='official_joke_api')`
Fetch and print a random joke.

**Parameters:**
- `source` (str): API source to fetch from

**Returns:**
- Boolean indicating success

#### `get_multiple_jokes(count=5, source='official_joke_api')`
Fetch multiple random jokes.

**Parameters:**
- `count` (int): Number of jokes to fetch
- `source` (str): API source to fetch from

**Returns:**
- List of joke dictionaries

#### `get_jokes_by_category(category='programming', count=3)`
Fetch jokes by category.

**Parameters:**
- `category` (str): Category of jokes
- `count` (int): Number of jokes to fetch

**Returns:**
- List of jokes in specified category

#### `format_joke(joke_data, source='official_joke_api')`
Format joke data based on API source format.

**Parameters:**
- `joke_data` (dict): Dictionary containing joke data
- `source` (str): API source for formatting

**Returns:**
- Formatted joke string or None

#### `list_available_sources()`
List all available joke API sources.

**Returns:**
- List of available API source names

## 💻 CLI Usage

### Interactive Mode

```bash
python utils/joke_cli.py
```

Then use commands:
- `joke` or `j` - Get a random joke
- `list` or `l` - List available sources
- `source` - Change joke source
- `help` or `h` - Show help
- `exit` or `q` - Exit program

### Single Joke

```bash
python utils/joke_cli.py -j
```

### Multiple Jokes

```bash
python utils/joke_cli.py -m 5 -s official_joke_api
```

### Category Jokes

```bash
python utils/joke_cli.py -c programming -n 3
```

### All CLI Options

```bash
python utils/joke_cli.py -h
```

## 🧪 Examples

Run all examples:

```bash
python examples/joke_generator_example.py
```

Individual examples:

```python
# Example 1: Single joke
from examples.joke_generator_example import example_1_single_joke
example_1_single_joke()

# Example 2: Multiple jokes
from examples.joke_generator_example import example_2_multiple_jokes
example_2_multiple_jokes()

# Example 3: Different sources
from examples.joke_generator_example import example_3_different_sources
example_3_different_sources()

# Example 4: Programming jokes
from examples.joke_generator_example import example_4_programming_jokes
example_4_programming_jokes()

# Example 5: Error handling
from examples.joke_generator_example import example_5_error_handling
example_5_error_handling()

# Example 6: Interactive menu
from examples.joke_generator_example import example_6_interactive_menu
example_6_interactive_menu()
```

## 📊 Supported API Sources

### 1. Official Joke API
- **URL**: https://official-joke-api.appspot.com
- **Format**: Setup/Punchline
- **Categories**: General, Programming, Knock-knock

### 2. JokeAPI
- **URL**: https://v2.jokeapi.dev
- **Format**: Single or Setup/Delivery
- **Categories**: Multiple categories available

### 3. icanhazdadjoke
- **URL**: https://icanhazdadjoke.com
- **Format**: Single joke
- **Style**: Dad jokes

### 4. Programming Jokes
- **Source**: Official Joke API (Programming category)
- **Format**: Setup/Punchline
- **Focus**: Programming-related humor

## ⚙️ Configuration

### Timeout Settings

```python
# Create generator with custom timeout
generator = JokeGenerator(timeout=10)
```

### Error Handling

The generator handles various error scenarios:
- Network timeouts
- Connection errors
- HTTP errors
- Invalid API responses
- JSON parsing errors

## 🎯 Use Cases

1. **Daily Dose of Humor**: Add jokes to your daily routine
2. **Web Applications**: Integrate jokes into web apps or dashboards
3. **Slack/Discord Bots**: Power joke commands in chat
4. **Training Data**: Use jokes for NLP/ML training
5. **Testing**: Generate random content for testing

## 🔒 Privacy & Terms

- All API services are public and free to use
- Respect API rate limits
- Check individual API terms of service
- No personal data is collected

## 🐛 Troubleshooting

### Connection Issues

```python
# Check if API is reachable
generator = JokeGenerator(timeout=10)  # Increase timeout
result = generator.get_random_joke()
if result is None:
    print("API unreachable. Check your internet connection.")
```

### No Jokes Returned

```python
# Try different source
sources = generator.list_available_sources()
for source in sources:
    result = generator.get_random_joke(source)
    if result:
        print(f"Success with {source}")
        break
```

## 📝 File Structure

```
AUTO-PRICE-PREDICTION/
├── src/
│   └── joke_generator.py          # Main generator class
├── utils/
│   └── joke_cli.py                # CLI interface
├── examples/
│   └── joke_generator_example.py  # Example usage
└── JOKE_GENERATOR_README.md       # This file
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report issues
- Suggest new features
- Add new API sources
- Improve documentation

## 📄 License

MIT License - See LICENSE file for details

## 🎉 Enjoy!

Happy joking! If you found this useful, don't forget to ⭐ the repository!

---

**For more information**: Check out the main README.md or visit the repository.
