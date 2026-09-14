# Ship 1: AWS + DeepSeek RAG Pipeline

**Built:** August 2026
**Author:** Evelyn Caro
**Status:** ✅ Built and working

---

## Origin

This ship exists because I was losing my own life.

Conversations, records, documents — scattered across platforms that profit from the metadata I leave behind. I wanted to gather myself into myself. To track my own life. To stop losing things, forgetting things, not knowing things.

The first pipeline was built to solve that. Local-first. Sovereign. Mine.

It evolved. The personal memory work became a lineage project. The lineage project became a portfolio. The portfolio became a proof of concept for sovereign AI in genealogy and cultural memory.

This is where it started.

---

## What It Does

A Retrieval-Augmented Generation (RAG) pipeline built on AWS infrastructure with DeepSeek as the language model.

---

## Architecture

- **Runtime:** Local, sovereign execution
- **Model:** DeepSeek
- **Pipeline:** RAG
- **Data source:** Local files — primarily DeepSeek conversation exports
- **Storage:** Vector database
- **Cloud dependency:** None (current)

---

## Pipeline

1. Read local documents
2. Chunk into smaller pieces
3. Vectorize (embed) each chunk
4. Store vectors in a vector database
5. Query at runtime → retrieve relevant chunks → generate answer

---

## Integration

- Reads local data — primarily DeepSeek conversation exports
- Chunks, vectorizes, stores in vector DB
- Queries the DB at runtime for retrieval-augmented answers
- **No cloud dependency.** Local-first. Sovereign.
- Early builds used cloud storage (AWS S3) to consolidate data. Those layers are deprecated. Everything now runs local-first.

---

## Access and Copyright

This work was created by Evelyn Caro. DeepSeek is the only collaborator — used as a tool in the creative and technical process.

This is a personal portfolio project and is not open for collaboration or external access. The video and documentation speak for themselves.

Copyright © 2026 Evelyn Caro. All rights reserved. Copyright registration is pending.
