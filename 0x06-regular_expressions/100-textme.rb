#!/usr/bin/env ruby
# script whose output is [Sender][Receiver][Flags]
out=ARGV[0].match(/\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/)
se=out[1]
re=out[2]
flags=out[3]
puts "#{se},#{re},#{flags}"
