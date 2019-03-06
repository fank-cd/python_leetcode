# coding:utf-8

# 有趣的电影

# 某城市开了一家新的电影院，吸引了很多人过来看电影。该电影院特别注意用户体验，专门有个
# LED显示板做电影推荐，上面公布着影评和相关电影描述。
#
# 作为该电影院的信息部主管，您需要编写一个
# SQL查询，找出所有影片描述为非boring(不无聊)的并且id为奇数的影片，结果请按等级rating排列。
#
#
#
# 例如，下表
# cinema:
#
# +---------+-----------+--------------+-----------+
# | id | movie | description | rating |
# +---------+-----------+--------------+-----------+
# | 1 | War | great 3D | 8.9 |
# | 2 | Science | fiction | 8.5 |
# | 3 | irish | boring | 6.2 |
# | 4 | Ice song | Fantacy | 8.6 |
# | 5 | House card | Interesting | 9.1 |
# +---------+-----------+--------------+-----------+
#
# 对于上面的例子，则正确的输出是为：
#
# +---------+-----------+--------------+-----------+
# | id | movie | description | rating |
# +---------+-----------+--------------+-----------+
# | 5 | House card | Interesting | 9.1 |
# | 1 | War | great 3D | 8.9 |
# +---------+-----------+--------------+-----------+
#


# SQL
# 重点是order by 还有逆序排序的时候是DESC
"""
SELECT * FROM cinema WHERE description != "boring" AND
mod(id,2)=1 ORDER BY rating DESC;
"""