## Work Flow To Trello Tool

### 用途 

目前的工序主要使用MarkDown编写，最终要发布到Trello上方便其他人领卡，所以开发了这个python的插件用于将mark down 的工序发布到Trello

### 安装

```
pip install toTrello==0.0.3
```



### 配置

需要在Home 下创建文件`.trello_tool.json`

内容如下

```
{
    "key": "",
    "token": "",
    "file_base_uri": "",
    "stay_stuck_name": "",
    "template_card_list_name": "",
    "template_card_name": "",
    "broad_id": ""
}
```

`key` 和`token` 为trello 的开发者序列码访问 https://trello.com/app-key 生成

`file_base_uri` 为 存放工序的文件夹

`stay_stuck_name` 为要把card发布到的泳道名称

`template_card_list_name` `template_card_name` 为要复制的卡模板卡所属的泳道和卡片名称

`broad_id`为trello board的id， 在board的url上可以看到

例如

```
https://trello.com/b/XXXXXXXX/%E4%B8%89%E7%9C%81%E5%90%BE%E8%BA%AB
```

XXXXXXXX为这个board的id

### 使用

#### Markdown格式的工序编写

为了能识别，markdown格式的工序必须具备特定格式才会被处理

工序中使用 `######`分隔,第一个分隔符之前的为该卡的简单说明,之后才是工序的内容，之后每个工序使用`>` 启示，`>` 标记的内容都会被标记为工序的check list 内容

Step的内容也会作为checklist的item

#### 调用命令

文件存放格式如下，其中i7 i8 i9 为迭代名称，工序文件以期望放到trello上的card名命名

```
WorkFlow/
├─i9
| ├─VO-257.md
| ├─VO-734.md
| ├─VO-811.md
| ├─VO-871.md
├─i8
| └VO-807.md
├─i7
| ├─VO-581.md

```



如果我想把VO-811发布到trello 则执行命令

```
toTrello i9 VO-811
```

如果我期望将i9的所有卡都发布到trello 则执行命令

```
toTrello i9
```









 
