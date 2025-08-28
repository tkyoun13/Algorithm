import sys

input = sys.stdin.readline

N = int(input())
total_recommendations = int(input())

if total_recommendations > 0:
    recommend_list = list(map(int, input().split()))
else:
    recommend_list = []

photo_frames = []

for t, student_id in enumerate(recommend_list):
    
    is_in_frame = False
    for frame in photo_frames:
        if frame['id'] == student_id:
            frame['count'] += 1
            is_in_frame = True
            break
            
    if is_in_frame:
        continue
    
    if len(photo_frames) >= N:
        photo_frames.sort(key=lambda x: (x['count'], x['time']))
        photo_frames.pop(0)
    
    photo_frames.append({
        'id': student_id,
        'count': 1,
        'time': t
    })

final_candidates = [frame['id'] for frame in photo_frames]
final_candidates.sort()

print(*final_candidates)