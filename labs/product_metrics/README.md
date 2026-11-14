# Lab：北极星、有效完成率与每成功任务成本

> 对应 DATA01、DATA02、BIZ02、AI13、AI11。所有事件为合成数据；不是用户数据、公司收入或真实计费。

## 理论

- 一个用户点击“提交”，并不等于任务成功。例中 `task_completed` 只有 `verified=True` 才进入有效成功分子。
- 任务完成率分母是去重的 `task_started` 数，幽灵事件不能当真实任务。
- **每成功任务成本**要计入失败与重试产生的费用，否则上线成本会被系统性低估。零成功的成本比值不是“0 元”，应该是不可定义并明确告警。
- 真正的在线分析需要时间窗、用户/任务单位、归因、退款、采集缺失与数据授权，本实验只验证核心算式。

## 运行

```bash
python -m unittest labs.product_metrics.test_analysis -v
```

## 独立任务

1. 增加合成的重试事件，并解释每成功任务成本如何变化；不能只看平均请求价格。
2. 给 `Event` 增加用户 cohort 和访问时间，计算 7 日留存，说明分母资格/时区。
3. 预注册一次产品改版的主指标、守门指标与停止规则；合成样本不足时不能宣称统计显著。
4. 关闭 AI 用新数据独立算出分母、成功数、成本和一个反例。

权威参考：[Amplitude 产品分析](https://www.amplitude.com/guides/product-analytics)、[OpenAI 评测方法](https://developers.openai.com/api/docs/guides/evaluation-best-practices)。
