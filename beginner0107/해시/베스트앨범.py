from collections import defaultdict

def solution(genres, plays):
    answer = []

    # 고유 번호를 저장
    pk = [i for i in range(len(genres) + 1)]

    # 장르별 총 재생 횟수 계산
    genre_play = defaultdict(int)
    for genre, play in zip(genres, plays):
        genre_play[genre] += play

    # 장르별 총 재생 횟수로 정렬
    sorted_genre_play = sorted(genre_play.items(), key=lambda x: x[1], reverse=True)

    # 장르별로 노래를 저장할 리스트 생성
    music_list = defaultdict(list)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        music_list[genre].append((i, play))

    # 장르 내에서 재생 횟수와 고유 번호로 정렬하여 앨범에 수록
    for genre, _ in sorted_genre_play:
        music_list[genre].sort(key=lambda x: (-x[1], x[0]))
        answer.extend([idx for idx, _ in music_list[genre][:2]])

    return answer
