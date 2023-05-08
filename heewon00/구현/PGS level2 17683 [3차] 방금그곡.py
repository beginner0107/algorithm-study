import math
def solution(m, musicinfos):
    answer = ''
    playtime = 0
    
    def rep(melody):
        return melody.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
    
    for music in musicinfos:
        start,end,title,melody=music.split(',')
        
        start=list(map(int,start.split(":")))
        end=list(map(int,end.split(":")))
        play=(end[0]*60+end[1]) - (start[0]*60+start[1])
        
        melody=rep(melody)
        
        q,r=divmod(play, len(melody)) 
        melody=melody*q+melody[:r]
        
        find_melody=rep(m)
        
        if find_melody in melody:    
            if answer!='':
                if playtime<play:
                    playtime=play
                    answer=title
            else:
                answer=title
                playtime=play
                
    if answer=='':
        return "(None)"
    
    return answer
