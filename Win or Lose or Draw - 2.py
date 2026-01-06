def compare(team_a_points, team_b_points):
    if team_a_points > team_b_points:
        result = "Win"
        
    elif team_a_points == team_b_points:
        result = "Draw"
    else:
        result = "Lose"
    return result
    

team_a_points = int(input())
team_b_points = int(input())

compare_result = compare(team_a_points, team_b_points)

print(compare_result)