# FinTechAI Research & Analysis Platform
## Multi-Agent Financial Intelligence System

This project implements a comprehensive multi-agent system for automated financial research and investment analysis using CrewAI (Assignment 1) and a Google ADK-inspired architecture (Assignment 2).

---

## Project Overview

**Domain**: Financial Technology (FinTech)  
**Objective**: Automate financial research through collaborative multi-agent workflows  
**Use Case**: Generate comprehensive investment analysis reports with company research, market analysis, financial metrics, risk assessment, and structured recommendations

### Key Features

- **6+ Specialized Agents** working collaboratively
- **Parallel Execution** for independent research tasks
- **Sequential Coordination** for dependent analysis steps
- **External Tool Integration** (web search, financial calculators, data parsers)
- **Structured Output** (Markdown for CrewAI, JSON for ADK)
- **Memory & Monitoring** (ADK implementation)
- **Fact Checking & Validation** to prevent hallucination

---

## System Architecture

### Agents

1. **Company Researcher**: Gathers company background, products, business model
2. **Market Analyst**: Researches market trends, competitors, industry position
3. **Financial Calculator**: Computes financial metrics and performance indicators
4. **Risk Assessor**: Evaluates investment risks and compliance issues
5. **Report Compiler**: Synthesizes research into structured reports
6. **Quality Validator** (CrewAI) / **Fact Checker** (ADK): Validates outputs

### Tools Used

- **DuckDuckGo Search**: Web research for real-time data
- **Financial Calculator**: Custom metrics computation
- **Custom Data Parser** (ADK): Financial data parsing and extraction

---

## Project Structure

```
.
├── fintech_crewai.py    # CrewAI implementation
├── fintech_adk.py       # ADK implementation
├── requirements.txt                 # Python dependencies
├── OBJECTIVES_AND_SCOPE.md         # Project objectives and scope
├── EXPECTED_OUTCOME.md             # Expected deliverables
├── WORKFLOW_DIAGRAM.md             # Agent workflows and diagrams
├── COMPARATIVE_ANALYSIS.md         # CrewAI vs ADK comparison
├── README.md                       # This file
├── .env                            # Environment variables (create this)
├── execution.log                   # ADK execution logs (generated)
└── outputs/                        # Generated reports
    ├── assignment1_output_*.md     # CrewAI reports
    └── assignment2_output_*.json   # ADK reports
```

---

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- Groq API key

### 2. Installation

```bash
# Clone or download the project
cd crewai_fintech_lab1

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configuration

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

For this project, the API key is already provided in the code.

### 4. Running the Programs

#### Assignment 1: CrewAI Implementation

```bash
python fintech_crewai.py
```

This will:
- Execute the multi-agent workflow
- Generate Markdown report for "Tesla Inc" (default)
- Save output to `assignment1_output_Tesla_Inc.md`

#### Assignment 2: ADK Implementation

```bash
python fintech_adk.py
```

This will:
- Execute enhanced workflow with monitoring
- Generate JSON report for "Apple Inc" (default)
- Save output to `assignment2_output_Apple_Inc.json`
- Create execution logs in `execution.log`

---

## Customization

### Change Company to Analyze

Edit the `company_name` variable in the main function:

```python
# In fintech_crewai.py or fintech_adk.py
company_name = "Your Company Name Here"
```

### Add New Agents

#### CrewAI (Assignment 1):

```python
new_agent = Agent(
    role="Your Agent Role",
    goal="Agent goal description",
    backstory="Agent backstory",
    verbose=True,
    allow_delegation=False,
    llm=llm,
    tools=[your_tools]
)
```

#### ADK (Assignment 2):

```python
new_agent = EnhancedAgent(
    role="Your Agent Role",
    goal="Agent goal description",
    backstory="Agent backstory",
    tools=[your_tools]
)
```

---

## Workflow Diagrams

See `WORKFLOW_DIAGRAM.md` for detailed:
- Agent coordination flowcharts
- Task dependency graphs
- Execution sequence diagrams
- Comparison of CrewAI vs ADK workflows

---

## Output Examples

### CrewAI Output (Markdown)

```markdown
# Investment Analysis Report: Tesla Inc

## Executive Summary
[Brief overview of findings]

## Company Overview
[Company background, products, business model]

## Market Analysis
[Industry trends, competitive landscape]

## Financial Analysis
[Financial metrics, performance indicators]

## Risk Assessment
[Identified risks and mitigation strategies]

## Investment Recommendation
[Buy/Hold/Sell recommendation]
```

### ADK Output (JSON)

```json
{
  "company_name": "Apple Inc",
  "timestamp": "2024-01-15T10:30:00",
  "report": "{...structured report...}",
  "validation": "{...validation results...}",
  "execution_logs": [
    {
      "timestamp": "2024-01-15T10:30:05",
      "agent": "Company Researcher",
      "task": "Research company background",
      "execution_time": 5.23,
      "errors": []
    }
  ],
  "context_summary": {
    "sections_completed": [...],
    "tools_used": ["web_search", "financial_parser"],
    "parallel_executions": 1,
    "total_execution_time": 45.67
  }
}
```

---

## Comparative Analysis

See `COMPARATIVE_ANALYSIS.md` for detailed comparison covering:
- Workflow design differences
- Coding effort and complexity
- System robustness and reliability
- Feature completeness
- Practical recommendations

---

## Key Differences: CrewAI vs ADK

| Feature | CrewAI | ADK |
|---------|--------|-----|
| **Output Format** | Markdown | JSON + Logs |
| **Memory** | Session-based | Persistent |
| **Monitoring** | Basic verbose | Advanced logging |
| **Validation** | Single validator | Multi-layer validation |
| **Error Tracking** | Basic | Comprehensive |
| **Development** | Faster (250 lines) | More complex (400 lines) |
| **Control** | Framework-managed | Full customization |

---

## Requirements Met

### Assignment 1 (CrewAI)
✅ 6+ specialized agents  
✅ Sequential + parallel execution  
✅ Role-specific prompts  
✅ Context sharing between agents  
✅ 2+ external tools (web search, calculator)  
✅ Structured Markdown output  

### Assignment 2 (ADK)
✅ Memory persistence across steps  
✅ 3+ tools (2 external + 1 custom)  
✅ Parallel task execution  
✅ Hallucination mitigation (Fact Checker)  
✅ Structured JSON output  
✅ Task monitoring & logging  
✅ Comparative analysis document  

---

## Troubleshooting

### Common Issues

1. **API Key Error**
   - Ensure `.env` file exists with correct `GROQ_API_KEY`
   - Or modify code to include API key directly

2. **Import Errors**
   - Run: `pip install -r requirements.txt`
   - Ensure virtual environment is activated

3. **Slow Execution**
   - Normal for comprehensive analysis (2-5 minutes)
   - ADK execution may take longer due to detailed logging

4. **Search Tool Errors**
   - DuckDuckGo search may fail intermittently
   - System will attempt to proceed without search results

---

## Future Enhancements

- Add more financial data sources (Yahoo Finance, Alpha Vantage APIs)
- Implement caching for repeated queries
- Add visualization tools for financial charts
- Support batch processing for multiple companies
- Add web interface for interactive analysis

---

## Contact & Support

For questions or issues:
1. Review the documentation files
2. Check execution logs (`execution.log` for ADK)
3. Review workflow diagrams in `WORKFLOW_DIAGRAM.md`

---

## License

This project is for educational purposes. Feel free to use and modify for learning.

---

**Project Name**: FinTechAI Research & Analysis Platform  
**Domain**: Financial Technology  
**Created**: 2024  
**Framework**: CrewAI & Google ADK-inspired
