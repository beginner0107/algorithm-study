def solution(m, musicinfos):
    class Music:
        def __init__(self, title, playtime):
            self.title = title # 정렬하게 위해 필요 (음악 제목)
            self.playtime = playtime # 음악 재생 시간

    def convert_sharp(sheet): # 음을 한 글자로 치환
        return sheet.replace("C#", "c").replace("D#", "d") \
            .replace("F#", "f").replace("G#", "g") \
            .replace("A#", "a")

    def to_minutes(time): # 시간을 분으로 변환한 뒤 반환
        hour, minute = map(int, time.split(":"))
        return hour * 60 + minute

    def generate_played_sheet(sheet, playtime): # 연주함
        played = ""
        len_sheet = len(sheet)
        for i in range(playtime):
            played += sheet[i % len_sheet]
        return played

    target = convert_sharp(m) # O(n)
    matched_musics = []
    for musicinfo in musicinfos: # O(n)
        start, end, title, sheet = musicinfo.split(",")
        playtime = to_minutes(end) - to_minutes(start) # O(1)
        played = generate_played_sheet(convert_sharp(sheet), playtime) # O(n) * O(n)
        if target in played: # 만약 조건에 일치하는 음악이 연주한 음악에 존재한다면
            matched_musics.append(Music(title, playtime)) # music 객체에 넣어줌

    if not matched_musics: # 만약 일치하는 음악이 존재하지 않다면 (None) 반환
        return "(None)"
    matched_musics.sort(key=lambda x: x.playtime, reverse=True) # 연주 시간으로 내림차순 정렬
    return matched_musics[0].title # 제목을 반환