def build_matches_table(num_teams):
    # Initialize the list of teams
    teams = list(range(1, num_teams + 1))
    # Initialize the list of rounds
    rounds = []
    # Iterate over each round
    for round_num in range(num_teams - 1):
        # Initialize the list of matches for this round
        matches = []
        # Iterate over each pair of teams
        for i in range(num_teams // 2):
            # Add the match to the list of matches for this round
            matches.append((teams[i], teams[num_teams - 1 - i]))
        # Add the list of matches for this round to the list of rounds
        rounds.append(matches)
        # Rotate the teams for the next round
        teams.insert(1, teams.pop())
    # Return the list of rounds
    return rounds


# Example usage:
print(build_matches_table(4))
