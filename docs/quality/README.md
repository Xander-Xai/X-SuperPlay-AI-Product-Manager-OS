# 产品经理课程审计与一致性中心

- [当期完整覆盖审计](coverage-audit-20261114.md)：目标范围、补充、残余风险。
- [18 领域机器矩阵](coverage-matrix.json)：每个知识节点至少在一个领域，不允许孤儿节点。
- [术语统一公约](terminology-contract.md)：PM/PO/项目经理、AC/DoD/DoR、POC/MVP/Pilot/Production、四风险及事实等级。
- [权威知识目录](../atlas/knowledge-catalog.json) 和 [来源元数据](../../resources/authorities.json)：唯一主索引，可复核领域、依赖、别名。

```bash
python tools/validate_repo.py
python tools/learning_router.py validate
python -m unittest discover -s tools -p 'test_*.py' -v
python -m unittest discover -s labs -p 'test_*.py' -v
```

**Content Gate ≠ Engineering / Human / User / Commercial Gate**。机器不能证明真实产品商业化成功、学员独立掌握或法规合规。
