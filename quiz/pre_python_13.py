"""
13. 리스트 메서드 중 하나를 이용하여 아래의 리스트에 '지구'라는 요소를 삽입하시오.

planet =['태양','수성','금성','화성','목성','토성','천왕성','해왕성']

결과 :
planet =['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']


예시
<입력>
print(planet)

<출력>
['태양', '수성', '금성', '지구', '화성', '목성', '토성', '천왕성', '해왕성']
"""

planet = ['태양', '수성', '금성', '화성', '목성', '토성', '천왕성', '해왕성']
planet.insert(3, '지구')

print(planet)
