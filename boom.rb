require "zlib"
include Zlib

data = "000000000000000000000000000000000000000000000000000000000000000000000" * 1000000

compressed_data = Deflate.deflate(data)

puts(data.length)
puts(compressed_data.length)

File::new( "new.zip","rw")
