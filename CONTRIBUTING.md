# Contribution Guide

## 本地预览

`python -O ./gen_index.py` 生成索引文件 `mkdocs.yml`, 然后使用 `mkdocs serve` 预览.\

## Commit Message

这很重要, 但是你不遵守我也没办法.

## 添加经验分享

编辑单个 markdown 文档, 放在 `docs/guide` 目录下.

可以参考 `docs/guide/guide_template.md` 的格式.

提交的文件开头应该包含一份个人介绍, 包括一些个人信息 (**必须包含参加高考的年份**), 以及对自己的学习经过和成绩的介绍, 作为读者判断这份文章是否适合自己阅读的依据, 你可以参考 `docs/guide/guide_hanoist.md` 的自我介绍部分. 审核的时候这部分不合要求会被打回修改, 其他部分除极端情况不作任何干涉.

### 文档语法

文档开头需要有如下字段:

```
---
title: 标题
date: 2024-06-11 12:34:56
author: someone
author_nickname: 无名氏
---
```

`author` 会被作为链接的路径, 请限制为英文字符, 数字, `-` 和 `_`.

`author_nickname` 会被作为作者名放在文章开头的 note box 内.

`date` 会被作为文章的发布日期, 同样会放在 note box 内.

`title` 会被作为文章标题显示在侧边栏.

文档中每个一级标题会被作为单独的一页, 请使用 `#` 作为一级标题, 井号后面加空格.

其后面的二级标题, 三级标题等会被放在同一个页面中, 直到遇到下一个一级标题.

使用 `{section}` 和 `{section end}` 来标记一个小节, 即侧边栏可以展开的部分.

```markdown
{section}
# 在这里写小节标题, 类似"一级标题"的格式

# 在小节里面新建一页

这里写内容

{section end}
```

小节可以嵌套.

## 添加文件

文件放入 `docs/file` 目录下, 对应的学科的文件夹中.

- `docs/file/Chinese`
- `docs/file/Math`
- `docs/file/English`
- `docs/file/Physics`
- `docs/file/Chemistry`
- `docs/file/Biology`
- `docs/file/History`
- `docs/file/Geography`
- `docs/file/Politics`
- `docs/file/Others`

若暂时没有对应的学科文件夹, 请自行创建, 名称应如上所示.

## 添加寄语

在 `docs/message.md` 中添加寄语.

## 修订

修改后直接提交 PR 即可.

## 更多信息

> 本站点已经有自己的参与者微信群了, 需要咨询任何问题或寻求帮助请加微信: Eliyou2005.

我不推荐使用即时通讯工具, 这隐含了一种"要求对方立刻回复"的压力, 尽量使用邮件或者 issue. -- Asta

[Give Asta Feedback](mailto:astinita@shanghaitech.edu.cn)
