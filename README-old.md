# Ship 1: AWS + DeepSeek RAG Pipeline

## Status
✅ Built and working

## Architecture
- **Cloud:** AWS
- **LLM:** DeepSeek
- **Components:**
  - RAG pipeline
  - S3 storage
  - Lambda functions
  - Agents

## Infrastructure
- **Account ID:** 922981236361
- **Region:** us-east-2
- **S3 Bucket:** mirror-raw-files-922981236361
- **Lambda Pipeline:** mirror-pipeline-automation
- **Agents:**
  - mirror-agent (WIGV3KVGBT)
  - mirror-pipeline-agent (HRWHZXEQKI)

## Credits
- Remaining: $159.65
- Expiration: 2027-06-03

## Integration
- Connects to Mirror project data in S3
- Uses DeepSeek for generation
- Triggers on new documents
- Moves data through bronze → silver → gold layers
