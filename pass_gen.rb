# constants 
PASS_LEN = 16.freeze
ASCII_START = 33.freeze
ASCII_END = 126.freeze

# efficiently generates a random password of only printable chars
# by using ascii with a psuedo-random number generator
def generate(password, rng)
    PASS_LEN.times do 
        password << rng.rand(ASCII_START..ASCII_END).chr
    end

    password.split("").shuffle!.join
end

puts generate("", Random.new)