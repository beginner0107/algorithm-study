def solution(brown, yellow):
    
    for i in range(1, brown + yellow +1) :
        if (brown + yellow)  % i == 0 :
            width = i
            height = (brown + yellow) // i
            
            if (width - 2) * (height - 2) == yellow :
                if width < height : 
                    width, height = height, width
                
                return [width, height]
    