# Run using
#   ruby script.rb
# Require Ruby >= 2.0.x

def oval(input_file, output_file)
  output = []
  IO.readlines(input_file).each_with_index do |row, index|
    next if index == 0 || index % 2 == 1
    map = {}
    # I use an hash because has faster lookup for
    # keys and can do delete in O(1)
    row.split(" ").each do |num|
      map[num].nil? ? map[num] = 1 : map.delete(num)
    end
    output << "Case ##{index/2}: #{map.keys.first}"
  end
  IO.write(output_file, "#{output.join("\n")}\n")
end

oval("oval-quiz-sm.in", "oval-quiz-sm.out")
oval("oval-quiz-lg.in", "oval-quiz-lg.out")
