# Lab：RAG 的来源/版本/权限与拒答

> 对应 AI03/AI04/AI11/ENG06。**这个案例是规则检索最小基线，不是 BM25/向量检索，也不调用真实 LLM。** 输入全是合成英文短文本，方便在没有模型 API/外部服务时先学证据与权限的因果边界。

## 理论为什么学

RAG 并不等于把向量库里的任何文本交给模型。用户每次请求都需要正确的数据**授权范围**、当前有效版本、检索匹配规则和可以追溯的引用；无证据就应该拒答或升级人工。实际产品中还要单独测检索覆盖、答案真实性和引用支持。

## 执行

```bash
python -m unittest labs.rag_evidence.test_baseline -v
python -m unittest discover -s labs -p "test_*.py" -v
```

本 Lab 已提供规则匹配的 6 条确定性单测：正确当前引用、旧版过滤、跨租户拒绝、空输入拒绝、用户试图越权、同文档新版本。

## 你需要自行做的事

1. 不看答案，画“查询→租户权限→活动版本过滤→检索→证据判断→展示”的因果链。
2. 在一个**新生成的合成文档**中加入语义近似但是关键词不相同的问题，证明规则匹配的局限；记住当前 baseline 不是 BM25。
3. 实现并测量真正 BM25/embedding/RAG 的召回后，比较相同金标集下哪些错误被解决、哪些安全边界仍必须由数据层拦截。
4. 关闭 AI 实现两个陌生测试：数据撤销后仍有缓存、用户 B 查询用户 A 的凭证。记录固定版本和断言。

## 通过标准

机器跑通仅证实示例可运行；本人能独立重现越权、旧版本拒绝、无证据拒答和至少一个语义匹配局限，才有待人工评审的学习证据。官方来源：[OpenAI Eval](https://developers.openai.com/api/docs/guides/evaluation-best-practices) / [NIST](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)。上线必须再过 [生产门禁](../../docs/launch/production-readiness.md)。
