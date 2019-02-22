#https://stackoverflow.com/questions/2405921/how-can-i-generate-zip-file-without-saving-to-the-disk-with-ruby
require 'rubygems'
require 'zip'

data = "000000000000000000000000000000000000000000000000000000000000000000000" * 1000000


File.open('data.gz', 'w') do |f|
  gz = Zlib::GzipWriter.new(f)
  gz.write data
  gz.close
end
