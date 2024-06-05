# Contribution Guide

## 本地预览

`python -O ./gen_index.py` 生成索引文件 `mkdocs.yml`, 然后使用 `mkdocs serve` 预览.

## Commit Message

这很重要, 但是你不遵守我也没办法.

## 添加经验分享

编辑单个 markdown 文档, 放在 `docs/guide` 目录下.

可以参考 `docs/guide/guide_template.md` 的格式.

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

文件放入 `file` 目录下, 在 `docs/file.md` 中添加链接. 

## 添加寄语

在 `docs/message.md` 中添加寄语.

## 修订

修改后直接提交 PR 即可.
