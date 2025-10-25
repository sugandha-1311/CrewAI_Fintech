# Workflow Diagram - FinTechAI Research Platform

## Assignment 1: CrewAI Workflow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    FinTechAI Research Workflow                           │
│                        (CrewAI Implementation)                           │
└─────────────────────────────────────────────────────────────────────────┘

INPUT: Company Name (e.g., "Tesla Inc")
   │
   │
   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                              TASK LAYER                                  │
└─────────────────────────────────────────────────────────────────────────┘

   ┌───────────────────┐              ┌───────────────────┐
   │  Task 1: Company  │              │  Task 2: Market   │
   │   Research        │  ─PARALLEL─▶ │   Analysis        │
   │                   │              │                   │
   └─────────┬─────────┘              └─────────┬─────────┘
             │                                   │
             │ Context: Company Info             │ Context: Market Data
             │                                   │
             └───────────────┬───────────────────┘
                             │
                             ▼
                    ┌───────────────────┐
                    │  Task 3: Financial│
                    │   Calculations    │
                    └─────────┬─────────┘
                              │
                              │ Context: Financial Metrics
                              │
                              ▼
                    ┌───────────────────┐
                    │  Task 4: Risk     │
                    │   Assessment      │
                    └─────────┬─────────┘
                              │
                              │ Context: Risk Analysis
                              │
                              ▼
                    ┌───────────────────┐
                    │  Task 5: Report   │
                    │   Compilation     │
                    └─────────┬─────────┘
                              │
                              │ Context: Full Report
                              │
                              ▼
                    ┌───────────────────┐
                    │  Task 6: Quality  │
                    │   Validation      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  Final Report     │
                    │  (Markdown)       │
                    └───────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                              AGENT LAYER                                 │
└─────────────────────────────────────────────────────────────────────────┘

┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ 1. Company   │  │ 2. Market    │  │ 3. Financial │  │ 4. Risk      │
│  Researcher  │  │  Analyst     │  │  Calculator  │  │  Assessor    │
│              │  │              │  │              │  │              │
│ Tools: Search│  │ Tools: Search│  │ Tools: None  │  │ Tools: None  │
└──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘

┌──────────────┐  ┌──────────────┐
│ 5. Report    │  │ 6. Quality   │
│  Compiler    │  │  Validator   │
│              │  │              │
│ Tools: None  │  │ Tools: None  │
└──────────────┘  └──────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                         EXTERNAL TOOLS                                   │
└─────────────────────────────────────────────────────────────────────────┘

    ┌──────────────────┐          ┌──────────────────┐
    │ DuckDuckGo Search│          │ Financial Calc   │
    │ (Web Research)   │          │ Functions        │
    └──────────────────┘          └──────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                       EXECUTION FLOW                                     │
└─────────────────────────────────────────────────────────────────────────┘

Sequential Execution:
   Task 1/2 (Parallel) → Task 3 → Task 4 → Task 5 → Task 6

Context Sharing:
   - Each task passes its output as context to dependent tasks
   - Final task receives aggregated context from all previous tasks

Output Format:
   - Markdown structured report
   - Tables for financial metrics
   - Professional formatting
```

## Assignment 2: Google ADK Workflow (Enhanced)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                FinTechAI Research Workflow (Enhanced)                    │
│                     (Google ADK Implementation)                          │
└─────────────────────────────────────────────────────────────────────────┘

INPUT: Company Name
   │
   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      MEMORY & CONTEXT STORE                              │
│  - Persistent context across steps                                      │
│  - Execution history tracking                                           │
└─────────────────────────────────────────────────────────────────────────┘
   │
   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      TASK EXECUTION LAYER                                │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────┐     ┌─────────────────┐
│ Task 1: Research│     │ Task 2: Market  │
│ (with memory)   │◄───▶│ (with memory)   │
└────────┬────────┘     └────────┬────────┘
         │                       │
         └───────────┬───────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │ Task 3: Calculate     │
         │ (Memory + Context)    │
         └───────────┬───────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │ Task 4: Risk Analysis │
         │ (Memory + Context)    │
         └───────────┬───────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │ Task 5: Compile       │
         │ (Memory + Context)    │
         └───────────┬───────────┘
                     │
                     ▼
         ┌───────────────────────┐
         │ Task 6: Validate      │
         │ + Fact Check          │
         └───────────┬───────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                       MONITORING & LOGGING                               │
│  - Step-by-step execution logs                                          │
│  - Intermediate output tracking                                         │
│  - Error tracking and debugging                                         │
└─────────────────────────────────────────────────────────────────────────┘
   │
   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      OUTPUT & VALIDATION                                 │
└─────────────────────────────────────────────────────────────────────────┘

   ┌─────────────────────┐    ┌─────────────────────┐
   │ Structured Report   │    │ Execution Log       │
   │ (JSON format)       │    │ (Monitoring data)   │
   └─────────────────────┘    └─────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                      ENHANCED FEATURES                                   │
└─────────────────────────────────────────────────────────────────────────┘

✓ Memory: Persistent context across steps
✓ Tool Integration: Web search + Custom parser + Financial calculator
✓ Parallel Execution: Independent tasks run in parallel
✓ Hallucination Mitigation: Validator checks facts against sources
✓ Monitoring: Full execution tracking and logging
✓ Structured Output: JSON with embedded logs

NEW AGENTS IN ADK:
- Memory Manager (maintains context)
- Logging Agent (tracks execution)
- Fact Checker (prevents hallucination)
```

## Key Differences

| Feature | CrewAI | Google ADK |
|---------|--------|------------|
| Output Format | Markdown | JSON + Logs |
| Memory | Session-based | Persistent |
| Monitoring | Basic | Advanced logging |
| Validation | Single validator | Multi-layer validation |
| Tool Count | 2 external | 3+ (2 external + 1 custom) |
| Error Handling | Basic | Comprehensive |
