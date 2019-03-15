# coding:utf-8
# 给定一个salary表，如下所示，有m = 男性和 f = 女性的值 。
# 交换所有的f和m值（例如，将所有 f值更改为 m，反之亦然）。
# 要求使用一个更新（Update）语句，并且没有中间临时表。
#
# 请注意，你必须编写一个Update语句，不要编写任何Select语句。
#
#
#
# 例如:
#
# | id | name | sex | salary |
# | ---- | ------ | ----- | -------- |
# | 1 | A | m | 2500 |
# | 2 | B | f | 1500 |
# | 3 | C | m | 5500 |
# | 4 | D | f | 500 |
#
# 运行你所编写的更新语句之后，将会得到以下表:
#
# | id | name | sex | salary |
# | ---- | ------ | ----- | -------- |
# | 1 | A | f | 2500 |
# | 2 | B | m | 1500 |
# | 3 | C | f | 5500 |
# | 4 | D | m | 500 |
#


"""
# Write your MySQL query statement below
update salary set sex = if(sex = 'm','f','m')

"""