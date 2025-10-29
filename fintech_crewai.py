"""
Assignment 1: FinTechAI Research & Analysis Platform using CrewAI
Multi-Agent System for Financial Research and Investment Analysis
"""

import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Use OpenAI-compatible endpoint (Ollama supports this)
# Configure Ollama to accept OpenAI API calls
llm = ChatOpenAI(
    model_name="gemma3:1b",
    openai_api_key="ollama",  # Ollama doesn't require real key
    openai_api_base="http://localhost:11434/v1",  # Ollama's OpenAI-compatible endpoint
    temperature=0.7
)

# Custom financial metrics tool
class FinancialMetrics(BaseModel):
    """Financial analysis metrics"""
    pe_ratio: float = Field(description="Price to Earnings ratio")
    revenue_growth: float = Field(description="Revenue growth percentage")
    market_cap: str = Field(description="Market capitalization")

def calculate_financial_health(company_data: str) -> str:
    """Custom tool to assess financial health"""
    # Simplified financial health calculation
    return f"""
    Financial Health Assessment:
    - PE Ratio: Estimated at 25-30 (industry standard)
    - Revenue Growth: Positive trending upward
    - Market Position: Strong in respective sector
    - Assessment: Healthy financial metrics based on provided data
    """

# ========== AGENT DEFINITIONS ==========

# 1. Company Researcher Agent
company_researcher = Agent(
    role="Company Researcher",
    goal="Gather comprehensive information about companies including background, business model, products, and services",
    backstory="""You are an expert financial researcher with 15 years of experience in company analysis.
    You excel at finding detailed information about companies, their history, mission, products, 
    and competitive positioning. Use your extensive knowledge base to provide accurate information.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 2. Market Analyst Agent
market_analyst = Agent(
    role="Market Analyst",
    goal="Analyze market trends, industry position, competitors, and market opportunities",
    backstory="""You are a senior market analyst specializing in market research and competitive analysis.
    You have deep knowledge of market dynamics, industry trends, and competitive landscapes.
    Use your expertise to provide comprehensive market insights.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 3. Financial Calculator Agent
financial_calculator = Agent(
    role="Financial Calculator",
    goal="Calculate and analyze financial metrics, ratios, and performance indicators",
    backstory="""You are a financial analyst expert in financial mathematics and metrics calculation.
    You excel at computing PE ratios, revenue growth, profit margins, and other key financial indicators.
    Use your financial expertise to calculate accurate metrics.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 4. Risk Assessor Agent
risk_assessor = Agent(
    role="Risk Assessor",
    goal="Evaluate investment risks, volatility, compliance issues, and risk mitigation strategies",
    backstory="""You are a risk management specialist with expertise in investment risk assessment.
    You identify potential risks, market volatility concerns, and compliance issues in investment decisions.
    Provide detailed risk analysis based on your expertise.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 5. Report Compiler Agent
report_compiler = Agent(
    role="Report Compiler",
    goal="Synthesize all research and analysis into a comprehensive, structured investment report",
    backstory="""You are a professional financial report writer with expertise in creating structured,
    comprehensive investment analysis reports. You excel at organizing complex information into clear,
    actionable insights. Create well-formatted professional reports.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 6. Quality Validator Agent
quality_validator = Agent(
    role="Quality Validator",
    goal="Review and validate all outputs for accuracy, completeness, and quality standards",
    backstory="""You are a quality assurance expert specializing in financial analysis verification.
    You ensure all reports meet high standards for accuracy, completeness, and professional presentation.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# ========== TASK DEFINITIONS ==========

def create_financial_analysis_crew(company_name: str):
    """Create and execute the financial analysis crew"""
    
    # Task 1: Company Research (Sequential start)
    task_research_company = Task(
        description=f"""
        Research the company: {company_name}
        
        Gather comprehensive information about:
        1. Company background and history
        2. Products and services offered
        3. Business model and revenue streams
        4. Recent developments and news
        5. Key personnel and leadership
        
        Provide detailed, factual information from reliable sources.
        """,
        agent=company_researcher,
        expected_output="A detailed company profile with background, products, business model, and recent developments"
    )
    
    # Task 2: Market Analysis (Parallel with company research)
    task_analyze_market = Task(
        description=f"""
        Analyze the market for: {company_name}
        
        Research and provide:
        1. Industry overview and market size
        2. Competitive landscape and main competitors
        3. Market position and competitive advantages
        4. Industry trends and future outlook
        5. Growth opportunities and challenges
        
        Provide strategic market insights.
        """,
        agent=market_analyst,
        expected_output="A comprehensive market analysis including industry trends, competitors, and market position"
    )
    
    # Task 3: Financial Metrics Calculation (Sequential after research)
    task_calculate_metrics = Task(
        description=f"""
        Calculate financial metrics for: {company_name}
        
        Based on the research provided, analyze:
        1. Price-to-Earnings (PE) ratio
        2. Revenue growth rate
        3. Market capitalization estimates
        4. Profitability indicators
        5. Financial health assessment
        
        Use the research data to estimate financial performance metrics.
        """,
        agent=financial_calculator,
        context=[task_research_company, task_analyze_market],
        expected_output="Financial metrics including PE ratio, revenue growth, and financial health assessment"
    )
    
    # Task 4: Risk Assessment (Sequential after calculation)
    task_assess_risks = Task(
        description=f"""
        Assess investment risks for: {company_name}
        
        Evaluate:
        1. Market risks and volatility
        2. Industry-specific risks
        3. Competitive threats
        4. Regulatory and compliance risks
        5. Risk mitigation strategies
        
        Provide a comprehensive risk assessment.
        """,
        agent=risk_assessor,
        context=[task_research_company, task_analyze_market, task_calculate_metrics],
        expected_output="A detailed risk assessment with identified risks and mitigation strategies"
    )
    
    # Task 5: Compile Report (Sequential - final compilation)
    task_compile_report = Task(
        description=f"""
        Compile a comprehensive investment analysis report for: {company_name}
        
        Structure the report in Markdown format with:
        
        # Investment Analysis Report: {company_name}
        
        ## Executive Summary
        (Brief overview of findings)
        
        ## Company Overview
        (Company background, products, business model)
        
        ## Market Analysis
        (Industry trends, competitive landscape, market position)
        
        ## Financial Analysis
        (Financial metrics, performance indicators, financial health)
        
        ## Risk Assessment
        (Identified risks and mitigation strategies)
        
        ## Investment Recommendation
        (Buy/Hold/Sell recommendation with reasoning)
        
        ## Summary Table
        (Key metrics in tabular format)
        
        Ensure the report is professional, well-structured, and actionable.
        """,
        agent=report_compiler,
        context=[task_research_company, task_analyze_market, task_calculate_metrics, task_assess_risks],
        expected_output="A comprehensive Markdown-formatted investment analysis report"
    )
    
    # Task 6: Quality Validation (Sequential - final validation)
    task_validate_quality = Task(
        description=f"""
        Validate the quality of the investment report for: {company_name}
        
        Review and verify:
        1. Accuracy of information presented
        2. Completeness of all required sections
        3. Consistency across different sections
        4. Professional presentation and formatting
        5. Logical flow and readability
        
        Provide validation feedback and confirm if the report meets quality standards.
        """,
        agent=quality_validator,
        context=[task_compile_report],
        expected_output="Quality validation feedback and final approved report"
    )
    
    # Create the crew
    crew = Crew(
        agents=[
            company_researcher,
            market_analyst,
            financial_calculator,
            risk_assessor,
            report_compiler,
            quality_validator
        ],
        tasks=[
            task_research_company,
            task_analyze_market,
            task_calculate_metrics,
            task_assess_risks,
            task_compile_report,
            task_validate_quality
        ],
        verbose=True
    )
    
    return crew

def main():
    """Main execution function"""
    print("=" * 80)
    print("FinTechAI Research & Analysis Platform - Assignment 1")
    print("Multi-Agent Financial Research System using CrewAI")
    print("=" * 80)
    print()
    
    # Example: Analyze Tesla
    company_name = "Tesla Inc"
    
    print(f"Starting financial analysis for: {company_name}")
    print("This may take a few minutes...")
    print()
    
    # Create and execute the crew
    crew = create_financial_analysis_crew(company_name)
    
    # Execute the crew
    result = crew.kickoff()
    
    # Save the result
    output_file = f"assignment1_output_{company_name.replace(' ', '_')}.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# Financial Analysis Report: {company_name}\n\n")
        f.write(str(result))
    
    print()
    print("=" * 80)
    print(f"Analysis complete! Results saved to: {output_file}")
    print("=" * 80)

if __name__ == "__main__":
    main()
