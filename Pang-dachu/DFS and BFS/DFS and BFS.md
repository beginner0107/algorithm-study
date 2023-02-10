# DFS와 BFS     

## DFS와 BFS는 어떤 상황에서 사용할까?

1) 그래프의 모든 정점을 방문하는 문제   
> DFS, BFS 큰 상관 없음.

2) 경로의 특징을 저장하는 문제      
> DFS : 각 정점에 숫자가 적혀있으며 start - end 경로에 같은 숫자가 있으면 안되는 문제, 각각의 경로마다 그 특징을 저장해두어야 하는 문제     

3) 최단거리를 구하는 문제   
> BFS : 미로찾기, 최단거리  
> DFS : 처음 발견하는 경우의 수가 최단 거리가 아닌 경우가 있을 수 있음.     

4) 그래프가 큰 경우     
> DFS 가 좋은 편이라고 함   

5) 그래프가 크지 않은 경우, 탐색 거리가 크지 않은 경우  
> BFS가 좋은 편이라고 함    


## 예제     
* [백준 1260 - DFS와 BFS](https://www.acmicpc.net/problem/1260)        
* [프로그래머스 - 게임 맵 최단거리](https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3)




## ref 

* [duckracoon Tistory](https://duckracoon.tistory.com/entry/DFS%EC%99%80-BFS-%EA%B0%81%EA%B0%81-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94-%EA%B2%BD%EC%9A%B0)

* [Stackoverflow](https://stackoverflow.com/questions/3332947/what-are-the-practical-factors-to-consider-when-choosing-between-depth-first-sea)
