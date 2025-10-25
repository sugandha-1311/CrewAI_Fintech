# Environment Setup

## Required Environment Variables

Create a `.env` file in the project root with the following:

```
GROQ_API_KEY=your_groq_api_key_here
```

## How to Get a Groq API Key

1. Go to https://console.groq.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key to your `.env` file

## Important Security Note

- Never commit your `.env` file to Git
- The `.gitignore` file is configured to exclude `.env`
- Always use environment variables for sensitive data
