#!/usr/bin/env ruby
# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <log_entry>"
  exit 1
end

# Extract the log entry
log_entry = ARGV[0]

# Define the regular expression to extract sender, receiver, and flags
pattern = /\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/

# Use the regular expression to find matches
matches = log_entry.match(pattern)

# Display the extracted information if matches are found
puts "#{matches[1]},#{matches[2]},#{matches[3]}" if matches
