# 从这个站点是哪里来的到你应该干什么

[This might be useful - Missing Semester](https://missing-semester-cn.github.io/)

## TL; DR

这个页面是给急着去玩，又有些时候想为了其他人写点啥，但不知道该怎么办才能把自己的东西糊到这个页面上的人准备的。

如果你认为你 **有自学能力**，那么下面的内容对你完全无意义，搜索 & 问 AI 比读下面的内容快多了。

## 站点是从哪里来的

### 分析一下这个项目的目录

`.github/workflows` 里面是 Github Actions 的配置文件，用来自动化构建这个站点。

`docs` 里面是所有的 Markdown 和其他文件，这些文件会被转换成 HTML 放到站点上。

`mkdocs_base.yaml` 是 MkDocs 的部分配置，完整配置会在 Github Actions 里面生成。

`gen_index.py` 是一个 Python 脚本，用来生成 `mkdocs.yaml`。

`gen_file_list.py` 是一个 Python 脚本，用来生成 `docs/file.md`。

### 从 Markdown 到浏览器

Markdown 是一种轻量级标记语言，其本身不决定具体的显示效果，其优点是可以轻松转换为 HTML，易于阅读和编写。

MkDocs 是基于 Python 的一个静态站点生成工具，可以将 Markdown 文件转换为 HTML 文件，并且生成一个静态站点。

MkDocs Material 是 MkDocs 的一个主题，提供了一些额外的功能，比如更好的页面效果，搜索功能等。

Github Actions 是 Github 提供的一个 CI (**C**ontinuous **I**ntegration，持续集成)/CD (**C**ontinuous **D**eployment，持续部署) 工具，可以在代码提交后自动运行一些脚本。

总结下来，你是这么看到这个网页的：

1. 作者编写了 Markdown 文件，放到了 `docs` 目录下。
2. 在 `mkdocs_base.yaml` 中配置了 MkDocs 的一些基本配置。
3. Markdown 文件被提交到 Github 仓库。
4. Github Actions 自动运行了 `.github/workflows/ci.yml` 指定的流程
    - 安装 Python 环境，安装 MkDocs 和 MkDocs Material
    - 运行 `gen_index.py` 生成 `mkdocs.yaml`，其中制定了网站目录结构和对应哪个 Markdown 文件
    - 运行 `gen_file_list.py` 生成 `docs/file.md`
    - 运行 MkDocs 构建站点，此时 Markdown 文件被转换为 HTML 文件
    - 将构建好的站点推送到 Github Pages
5. 你在浏览器中输入了网站地址(中间可能涉及一些 CNAME 和其他计算机网络相关内容, 自行了解)，浏览器请求 Github Pages 上的 HTML & CSS & JS，渲染成你看到的屏幕上的内容。

## 我的想法该如何变成站点上的内容

### Git

https://git-scm.com/downloads

Git 是一个版本控制工具，可以帮助你管理你的代码，跟踪你的修改，协作开发等。

在安装后，你会发现你多了一个应用图标 Git Bash，打开后你会看到一个命令行界面。

输入 `git config --global user.name "Name"`，把 `Name` 替换成你的名字，设置提交代码时的作者。

输入 `git config --global user.email "Email"`，把 `Email` 替换成你的邮箱，设置提交代码时的邮箱。

### Github

为了向托管在 Github 上的仓库提交代码，你需要一个 Github 账号。

在这之后，打开 https://github.com/24OI/24OI-whk-guide，点击右上角的 Fork，将这个仓库 Fork 到你的账号下。

打开你 Fork 的仓库，点击右上角的 Code，复制 Clone -> HTTPS 的地址。

在 Git Bash 中通过 `cd` 指令选择合适的路径（或者直接在某个文件夹下右键在当前目录打开 Git Bash），输入 `git clone URL` 把 `URL` 替换成你刚刚复制的地址，下载这个仓库。

### VSCode (推荐)

https://code.visualstudio.com/

VS Code 有很好的 Git 集成，可以帮助你更轻松的查看修改情况，提交代码等。

### 本地部署，查看效果

本地打开仓库，按照 `CONTRIBUTING.md` 的指引，修改或添加你的内容。

在完成修改后，如果你想要查看你的修改效果，需要安装 Python.

https://www.python.org/downloads/

在安装时一定要选择 **添加到环境变量** 和 **安装 pip**。

在仓库根目录下运行 `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt` 安装依赖。

在仓库根目录下运行 `python .\gen_index.py` 生成 `mkdocs.yaml`。

在仓库根目录下运行 `python .\gen_file_list.py` 生成 `docs/file.md`。

在仓库根目录下运行 `python -m mkdocs serve` 启动 MkDocs 本地服务器，根据命令行提示访问那个地址查看效果。

### 上传到 Github，提交 PR

在完成修改后，你需要提交你的修改到 Github。

首先，你需要在 Git Bash 中输入 `git add .`，将你的修改添加到暂存区。

然后，你需要在 Git Bash 中输入 `git commit -m "Your message"`，将你的修改提交到本地仓库，`Your message` 替换成你的提交信息。

最后，你需要在 Git Bash 中输入 `git push`，将你的修改推送到 Github。

（或者直接使用 VS Code/Github Desktop 的 GUI 操作）

在你推送完成后，你可以在你 Fork 的仓库页面上看到一个棕色信息框提示你有修改可以合并到此仓库，点击绿色按钮 `Compare & pull request`，填写 PR 的信息，提交 PR。

等待 PR 被 Review，Review 后可能会有一些修改，根据 Reviewer 的意见修改后，你的 PR 将会被合并。

## FAQ

Q：我访问不了你提到的某个网站

A：我不好说，但是请自己解决访问外网问题

------

Q：`git clone` 速度太慢了。

A：自行搜索 Git 代理

------

Q：你的分割页面语法太蠢/不适合我/我能改进

A：在 Github 上提交一个 Issue 或者 PR

------

Q：我在我的 git 仓库里面犯了一个错误，我该怎么办？

A：最简单的方式——另存一份你要修改的部分，删掉本地的仓库，重新 clone 一份，然后把你的修改复制进去。

其他情况基本都可以问 AI
