# 可离线运行的微型学习 Lab

> **这些是教学基线，不是生产系统或真实 AI 模型。** Python 标准库即可运行，使用完全合成数据；机器测试通过只证明示例代码行为，不证明本人已经掌握。

| Lab | 你会理解什么 | 对应知识节点 | 测试与下一步 |
|---|---|---|---|
| [RAG 证据与权限](rag_evidence/README.md) | 检索范围、旧版、引用、拒答的边界 | AI03 AI04 AI11 ENG06 | 6 条规则基线测试，再独立替换真实 BM25/向量检索 |
| [Agent 审批幂等](agent_approval/README.md) | 审批不等于执行、重复消息不是重复写入 | AI05 AI06 AI08 ENG07 | 7 条状态与负例测试，再改持久事务/重启 |
| [产品指标与单位成本](product_metrics/README.md) | 有效分母、虚假完成、失败成本、零分母 | DATA01 BIZ02 AI13 | 5 条计算测试，再扩展留存/A-B |

```bash
python -m unittest discover -s labs -p 'test_*.py' -v
python tools/learning_router.py scenario rag-knowledge-assistant
python tools/learning_router.py route ENG06
```

完成一次 Lab 后，必须回到自己的 [学习任务卡](../docs/learning/task-contract.md)：你为何进入、前测是什么、哪里失败、关 AI 的陌生题如何通过，下一次复测是什么。不因 Lab 示例自动升级 Engineering/Human/User/Commercial 状态。
