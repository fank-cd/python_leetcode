# coding:utf-8
# 组合两个表

# 表1: Person
#
# +-------------+---------+
# | 列名 | 类型 |
# +-------------+---------+
# | PersonId | int |
# | FirstName | varchar |
# | LastName | varchar |
# +-------------+---------+
# PersonId
# 是上表主键
#
# 表2: Address
#
# +-------------+---------+
# | 列名 | 类型 |
# +-------------+---------+
# | AddressId | int |
# | PersonId | int |
# | City | varchar |
# | State | varchar |
# +-------------+---------+
# AddressId
# 是上表主键
#
# 编写一个
# SQL
# 查询，满足条件：无论
# person
# 是否有地址信息，都需要基于上述两表提供
# person
# 的以下信息：
#
#
#
# FirstName, LastName, City, State
#

# SQL
# 主要是left join的问题
# LEFT OUTER JOIN 接受左边的所有表，注意 这是一个外部连接
"""
# Write your MySQL query statement below
SELECT FirstName, LastName, City, State FROM Person LEFT OUTER JOIN Address on Person.PersonId = Address.PersonId

"""