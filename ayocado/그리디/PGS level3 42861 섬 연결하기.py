def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    bridge = set([costs[0][0]])
    answer = 0

    while len(bridge) != n:
        for cost in costs:
            if cost[0] in bridge and cost[1] in bridge:
                continue
            if cost[0] in bridge or cost[1] in bridge:
                bridge.update([cost[0], cost[1]])
                answer += cost[2]
                break
    return answer