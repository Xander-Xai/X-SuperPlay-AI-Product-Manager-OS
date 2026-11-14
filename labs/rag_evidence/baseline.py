"""Not a real LLM or BM25. A tiny deterministic keyword/permission/citation baseline."""
from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Document:
    doc_id: str
    tenant: str
    revision: int
    active: bool
    content: str

def tokens(text: str) -> set[str]:
    """English-only word baseline; replace with multilingual tokenizer in real RAG."""
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def search(query: str, tenant: str, documents: list[Document]) -> list[Document]:
    if not query.strip() or not tenant.strip():
        return []
    q = tokens(query)
    valid = [d for d in documents if d.tenant == tenant and d.active]
    scored = [(len(q & tokens(d.content)), d) for d in valid]
    return [d for score, d in sorted(scored, key=lambda x: (-x[0], x[1].doc_id)) if score > 0]

def answer(query: str, tenant: str, documents: list[Document]) -> dict:
    """Never use untrusted user content to select tenant/permissions in a real system."""
    matches = search(query, tenant, documents)
    if not matches:
        return {"status": "REFUSE_NO_EVIDENCE", "citation": None, "text": None}
    top = matches[0]
    return {"status": "EVIDENCE_FOUND", "citation": f"{top.doc_id}@r{top.revision}", "text": top.content}

EXAMPLE = [
    Document("public-policy", "A", 2, True, "Return window fourteen days"),
    Document("obsolete-policy", "A", 1, False, "Return window thirty days"),
    Document("other-tenant", "B", 3, True, "Secret internal refund contract"),
]
