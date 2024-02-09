# py_word

Python 快速（查询/整理）单词，数据库基于有道词典。

## 功能

- 输入查词
- 查询输入单词的相关内容
- 批量录入单词到生词本

## 使用

#### Windows

在 CMD 中运行，并授予管理员权限。

### 参数

```bash
key_1 + [*vars]
```

|       ``[*vars]``       |            功能介绍            |
| :---------------------: | :----------------------------: |
|                        |    查询输入单词的词性及释义    |
|         ``-a``         | 查询输入单词的相关内容（详细） |
|         ``-b``         |    将单词相关内容写入单词本    |
| ``filename.txt`` ``-b`` |      批量添加单词到单词本      |

### 生词本

生词本是一个文件名为 ``filename.kirisame.pyword.json``的数据文件，默认存放在 ``./json``目录下。

## 示例

### 样例输入

```bash
contradictory -a
```

### 样例输出

```
adj. 相互矛盾的，对立的；好反驳的，爱争辩的; n. 矛盾命题

与单词contradictory相关的内容：
1:[contradictory with]与......矛盾：表示某事物与另一事物之间存在不一致或相互抵触的关系。

2:[contradictory information]矛盾信息

3:[contradictory evidence]矛盾性证明

4:[contradictory premises]矛盾前提：指在逻辑推理或论证中，存在相互冲突或矛盾的前提条件。
```

## 源信息

```python
# -*- coding: utf-8 -*-
# @name   : py_word/app.py
# @author : fly6022
# @date   : 2024/2/9
# @Email  : i@fly6022.fun
# @version: 2.0.0
# @license: BSD-3-Clause
```
