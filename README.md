# Ship 1 — DeepSeek RAG Pipeline

**A RAG pipeline that AWS lost and a MacBook Air rebuilt.**

Ship 1 is the first working retrieval-augmented generation pipeline in A Mirror of My Becoming™. It was originally built on AWS SageMaker. It was lost when the SageMaker instance was lost — the EBS volume corrupted, no AMI, no snapshot, no recovery path through the AWS CLI or the AWS Management Console. It was rebuilt locally from the author's archive, on consumer hardware, and made sovereign: the pipeline now lives on disk the author owns, in code the author controls, and in a form that can be rebuilt from the same sources every time.

**Built:** August 2026 (AWS SageMaker). Rebuilt locally in August 2026.
**Author:** Evelyn Caro
**Status:** Built and working
**Part of A Mirror of My Becoming™** — fleet index: [a-mirror-of-my-becoming-rag-pipelines](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-pipelines)

---

## What it does

Reads documents from local disk. Chunks them into segments. Embeds each chunk through a local Ollama embedding model. Writes the chunks and their embeddings into a local Chroma vector store. Answers queries by retrieving the top relevant chunks and passing them to a local LLM for generation.

Nothing leaves the machine. No cloud account. No API key. No telemetry.

---

## The loss — AWS by name

Ship 1 was originally built on **AWS SageMaker**. It was lost when:

| What happened | What it cost |
|---|---|
| The SageMaker instance was terminated | The notebook ran on it |
| The EBS volume corrupted | The notebook was stored on it |
| No AMI was created | No image to relaunch from |
| No snapshot was taken | No point-in-time restore available |
| CLI recovery attempts failed | No path back through the AWS CLI |
| Console recovery attempts failed | No path back through the AWS Management Console |
| **Net result** | **The pipeline was gone** |

**AWS publishes durability, redundancy, and shared-responsibility guarantees for exactly this class of workload.** The service is named AWS SageMaker. The underlying storage is named Amazon EBS. Both are marketed on the promise that data stored on them will survive infrastructure events. **That promise did not hold for this pipeline.** Whether the cause was user error, missing guidance, or an unaddressed gap in the recovery workflow, the fact is: **the pipeline was lost, and AWS's documented recovery paths were exhausted with no path back to the notebook.**

This is a receipt about a platform's published claims and the difference between those claims and what happened.

The lesson is not that AWS is uniquely bad. **The lesson is that cloud dependency is a preservation risk.** When the pipeline lives on a machine you do not own, you do not own the pipeline. When that machine is gone, the pipeline is gone. **The vendor's marketing claims about durability are not a backup strategy. They are a promise about infrastructure. The pipeline is the customer's problem.**

---

## The rebuild

Ship 1 was rebuilt locally from the author's archive — the same sources the pipeline had been built from in the first place. The rebuild runs on an 8 GB Intel MacBook Air with no cloud account, no vendor API, and no cost per query.

The rebuild was cleaner than the original. Not because the code was better, but because the same pipeline built under a sovereign constraint — **recoverable from sources every time** — is worth more than a pipeline that only runs on someone else's hardware.

This is the shape of the fleet. Every ship that follows is built the same way. Every ship can be rebuilt the same way.

---

## Requirements

The notebook names its own environment. Read the top of `Ship1_DeepSeek_RAG_v2_Agentic_executed.ipynb` before running. It lists the Python packages, the Ollama models, and the paths it expects.

**Setup:** [SETUP.md](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-pipelines/blob/main/SETUP.md) — three ways to point the pipeline at your own corpus.

---

## Quickstart

    # 1. Read the top of the notebook. Install what it names.
    # 2. Point the pipeline at a folder of documents (see SETUP.md).
    # 3. Run the notebook.
    #
    # The pipeline reads, chunks, embeds locally, and writes to a
    # local Chroma vector store. No cloud. No API key.

---

## Where the receipts live

Ship 1 is part of the group covered by **[Case Study: DeepSeek — The Benchmark](https://qaevelyn.github.io/white-papers/deepseek-case-study/)** — the paper written in August 2026 documenting the era in which Ships 1–4 were built. The suspension addendum of that paper describes the events of late September 2026, when the DeepSeek platform suspended the account and the pipelines continued running because they did not depend on the platform.

The story of the ingestion stack that feeds the pipelines is in **[The Cache Is Not the Corpus](https://qaevelyn.github.io/white-papers/the-cache-is-not-the-corpus/)**.

A dedicated case study on Ship 1 — the AWS loss and the local rebuild — is in the pipeline.

---

## The fleet

Ship 1 of the A Mirror of My Becoming™ RAG pipelines fleet. The fleet index is [here](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-pipelines).

- **Ship 1** — this repo — DeepSeek RAG, standard, rebuilt local after AWS lost it
- **[Ship 2](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship2-ibm-granite-agentic)** — IBM Granite Agentic RAG
- **[Ship 3](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship3-ibm-granite)** — IBM Granite RAG, cross-platform
- **[Ship 4](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship4-ibm-granite-agentic)** — IBM Granite Agentic RAG, cross-platform
- **[Ship 5](https://github.com/qaevelyn/a-mirror-of-my-becoming-rag-ship5-ibm-granite-agentic-evidenceflow)** — IBM Granite Agentic RAG with EvidenceFlow

**[Suite: Ingestion Tools](https://github.com/qaevelyn/a-mirror-of-my-becoming-suite-ingestion-tools)** — the tooling that gets documents into the vector store this ship reads from.

**[A Mirror of My Becoming™](https://github.com/qaevelyn/a-mirror-of-my-becoming)** — the parent index for the entire practice.

---

## License

Ship 1 is dual-licensed:

- **AGPL-3.0** — free to use, modify, and redistribute under the terms of the license. Full text in [LICENSE](LICENSE).
- **Commercial license** — available for organizations that need to use the code without the AGPL-3.0 obligations. Contact the author for pricing.

Free does not mean free to exploit. If you build a product on this work, the author expects to be paid.

---

## Author

**Evelyn Caro** — Sovereign AI Builder.

**[qaevelyn.github.io](https://qaevelyn.github.io)** · Commercial licensing: **evelyn.caro.cloud@gmail.com**

---

© 2026 Evelyn Caro. All rights reserved.
