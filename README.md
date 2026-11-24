# pairwise-downmix-channel-layout

## 领域

游戏、图形与多媒体

## 主题

多声道下混为立体声

## 说明

布局查表、LFE 限幅与声道延迟对齐。

初始状态下 `media/downmix_channel_layout.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
