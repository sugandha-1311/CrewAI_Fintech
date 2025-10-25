# Objectives and Scope of Work - FinTechAI Research & Analysis Platform

## Objectives

The primary objective of this project is to develop a multi-agent AI system that automates comprehensive financial research and analysis workflows. The system leverages CrewAI (Assignment 1) and Google ADK (Assignment 2) frameworks to demonstrate collaborative problem-solving among specialized AI agents in the financial technology domain.

The system addresses the critical need for automated, thorough financial analysis by replacing traditional time-consuming manual research processes. Through coordinated agent collaboration, it gathers market data, analyzes financial metrics, assesses risks, validates information accuracy, and generates structured investment reports. The platform serves investors, financial analysts, and researchers who require quick, comprehensive, and validated financial intelligence.

Secondary objectives include demonstrating advanced agentic behaviors such as parallel task execution, context sharing, tool integration, and hallucination mitigation. The system also showcases practical applications of modern AI frameworks in real-world financial scenarios, bridging the gap between academic agent research and production-ready systems.

## Scope of Work

### Assignment 1 - CrewAI Implementation

**Phase 1: Agent Design & Architecture**
- Design and implement 6+ specialized agents:
  - **Company Researcher**: Gathers company information, background, and business model
  - **Market Analyst**: Researches market trends, competitor analysis, and industry position
  - **Financial Calculator**: Processes financial metrics and performs calculations
  - **Risk Assessor**: Evaluates investment risks and compliance issues
  - **Report Compiler**: Synthesizes all information into structured reports
  - **Quality Validator**: Reviews outputs for accuracy and completeness
- Define clear role-specific prompts for each agent
- Establish information flow and dependencies between agents

**Phase 2: Workflow Implementation**
- Implement sequential execution for dependent tasks (e.g., researcher → calculator → compiler)
- Configure parallel execution for independent tasks (e.g., company research and market analysis simultaneously)
- Enable context sharing mechanism for intermediate outputs
- Integrate at least two external tools: web search API for real-time data and financial calculation libraries

**Phase 3: Output & Validation**
- Generate structured outputs in Markdown format with tables
- Include validation mechanism to ensure output quality
- Create sample test cases with companies like Tesla, Apple, Microsoft

### Assignment 2 - Google ADK Implementation

**Phase 1: Feature Extensions**
- Implement memory/context persistence across execution steps
- Add custom financial data parser tool alongside existing tools
- Configure parallel task execution with dependencies
- Integrate hallucination mitigation through validator agent checking facts against multiple sources

**Phase 2: Monitoring & Logging**
- Implement execution flow tracking and logging
- Create intermediate output monitoring system
- Add error tracking and debugging capabilities
- Generate execution reports for transparency

**Phase 3: Evaluation & Comparison**
- Produce comparative analysis between CrewAI and ADK implementations
- Document workflow differences, coding effort, and system robustness
- Generate structured outputs in JSON format with monitoring data

**Deliverables:** Complete implementations for both assignments, workflow diagrams, sample outputs, and comparative analysis document.
