def team_gen(players, team_size)
    team_num = 1

    players.shuffle.each_slice(team_size) do |team| 
        output(team_num)
        puts team.inspect
        team_num += 1
    end
end

def output(team_num)
    print "Team #" + team_num.to_s + ": "
end

team_gen(["basic","berry","ryan","luke","nish","matt","tj","bullits"], 4)