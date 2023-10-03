#!/usr/bin/env ruby
# regex matching patten in the beginning and end of a string
puts ARGV[0].scan(/\Ah.{1}n\z/).join
