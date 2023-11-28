# Regular Expressions in Ruby

Regular expressions (regex) are powerful tools for pattern matching and text manipulation. In Ruby, you can use the built-in `Regexp` class to work with regular expressions. Here's a brief guide on using regular expressions in Ruby:

## 1. Matching a Specific String

```ruby
pattern = /hello/
text = "Hello, world! This is a greeting."
match = text.match(pattern)
puts match[0]  # Outputs: "hello"
```

## 2. Matching Multiple Alternatives

```ruby
pattern = /(apple|orange|banana)/
text = "I like oranges and bananas, but not apples."
matches = text.scan(pattern)
puts matches  # Outputs: ["orange", "banana"]
```

## 3. Matching Digits

```ruby
pattern = /\d+/  # Matches one or more digits
text = "There are 123 apples in the basket."
match = text.match(pattern)
puts match[0]  # Outputs: "123"
```

## 4. Matching Word Boundaries

```ruby
pattern = /\bword\b/
text = "This is a word. Not a keyword or password."
match = text.match(pattern)
puts match[0]  # Outputs: "word"
```

## 5. Matching Email Addresses

```ruby
pattern = /\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b/
text = "Contact me at user@example.com for more information."
match = text.match(pattern)
puts match[0]  # Outputs: "user@example.com"
```

## 6. Matching Dates

```ruby
pattern = /\d{4}-\d{2}-\d{2}/
text = "The meeting is scheduled for 2023-12-01."
match = text.match(pattern)
puts match[0]  # Outputs: "2023-12-01"
```

## 7. Replacing Text

```ruby
pattern = /apple/
text = "I have an apple, and she has an apple too."
replaced_text = text.gsub(pattern, "orange")
puts replaced_text  # Outputs: "I have an orange, and she has an orange too."
```

## 8. Checking for a Match

```ruby
pattern = /pattern/
text = "This text contains the pattern."
if text.match?(pattern)
  puts "Pattern found!"
else
  puts "Pattern not found."
end
```

## 9. Matching URLs

```ruby
pattern = %r{https?://\S+}
text = "Visit my website at https://www.example.com."
match = text.match(pattern)
puts match[0]  # Outputs: "https://www.example.com"
```

These are basic examples, and you can create more complex patterns based on your specific requirements. Refer to the [Ruby Regexp documentation](https://ruby-doc.org/core-3.0.2/Regexp.html) for more details on regular expressions in Ruby.
```

This `README.md` file provides a quick reference with simple examples for each topic. Feel free to customize it further based on your needs.
