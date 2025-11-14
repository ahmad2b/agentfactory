---
title: "How Your AI Reads the World: Built-In Tools in Action"
chapter: 2
lesson: 3
estimated_time: "20-25 minutes"
learning_objectives:
  - "Understand how AI tools extend beyond text to access files, the web, and real-time information"
  - "Recognize when and why AI needs to use specific tools (files vs. web vs. search)"
  - "Apply tools in natural dialogue without memorizing commands"
  - "Identify what data you're sharing and privacy implications of web-based tools"
  - "Combine multiple tools to answer complex business questions"
---

## The Collaboration Shift: AI Becomes Your Research Partner

Let's start with a simple experiment. Open your Gemini CLI and ask:

```
What is the current temperature in San Francisco?
```

Here's what happens when you run this:

```
> What is the current temperature in San Francisco?

🔍 Searching the web...

The current temperature in San Francisco is approximately 62°F (17°C) with partly
cloudy skies. Conditions vary by neighborhood, with coastal areas typically cooler.

Sources:
- weather.com (retrieved 2024-01-14)
- National Weather Service
```

Notice something important: You didn't tell Gemini HOW to get this information. You didn't type a command like `/search-web` or configure APIs. You just asked naturally, and Gemini knew it needed current data, so it automatically used its web search tool.

This is the shift we're exploring today. Your AI doesn't just respond from memory—it actively reaches out to find fresh information, read files, and access the world beyond its training data. The key difference from traditional software: **you don't memorize commands. You ask naturally.**

This lesson shows you what tools your AI has available, when it uses them, and what's happening behind the scenes. By the end, you'll understand how to work with AI tools safely and effectively.

---

## The Three Tools: When Gemini Reaches Beyond Its Training Data

Your AI has three ways to get information beyond what it learned during training. Let's see each in action.

---

## Tool 1: Web Search — Finding Current Information Across the Web

**When to use:** You need current information but don't know which specific website has it.

Ask Gemini:

```
What is the current stock price of Tesla?
```

**What you'll see:**
```
> What is the current stock price of Tesla?

🔍 Searching the web...

Tesla (TSLA) is currently trading at $242.84, up 2.3% today. The stock opened
at $238.12 and has a 52-week range of $138.80 - $299.29.

Market cap: $769 billion
P/E ratio: 76.45
Volume: 89.2M shares

Sources:
- Yahoo Finance (retrieved 2024-01-14, 14:23 UTC)
- NASDAQ real-time data
```

**What happened:** Gemini searched multiple sources, synthesized the answer, and cited where it got the data.

**Watch for:** `🔍 Searching the web...` indicator

---

## Tool 2: Web Fetching — Reading Specific Websites

**When to use:** You know exactly which website has the information you need.

Ask Gemini:

```
Fetch the Stripe pricing page and summarize their main pricing tiers
```

**What you'll see:**
```
> Fetch the Stripe pricing page and summarize their main pricing tiers

🌐 Fetching https://stripe.com/pricing...

Based on Stripe's pricing page, here are the main tiers:

**Integrated Pricing (Pay-as-you-go)**
- 2.9% + $0.30 per successful card charge
- No monthly fees
- Best for: Startups and small businesses

**Custom Pricing**
- Volume discounts available
- Contact sales for rates
- Best for: High-volume businesses

Additional services:
- Stripe Billing: Subscription management
- Stripe Terminal: In-person payments (different rates)
- International cards: +1.5% fee

Source: stripe.com/pricing (retrieved 2024-01-14)
```

**What happened:** Gemini visited the specific URL, read the page, extracted pricing info, and organized it.

**Watch for:** `🌐 Fetching https://...` indicator

**Difference from web search:**
- **Web Search** (Tool 1): "Find me current Tesla stock price" → AI searches to find the answer
- **Web Fetch** (Tool 2): "Read Stripe's pricing page" → AI reads the specific page you named

---

## Tool 3: File Reading — Analyzing Your Local Data

**When to use:** You have data in a file on your computer and want insights from it.

Create a file called `sales.txt`:

```
Q1: $45,000
Q2: $52,000
Q3: $48,000
Q4: $61,000
```

Ask Gemini:

```
Read sales.txt and tell me which quarter had the highest revenue
```

**What you'll see:**
```
> Read sales.txt and tell me which quarter had the highest revenue

📄 Reading file: sales.txt...

Based on the data in sales.txt, Q4 had the highest revenue at $61,000.

Breakdown:
- Q1: $45,000
- Q2: $52,000
- Q3: $48,000
- Q4: $61,000 ← Highest

Q4 exceeded Q1 by 35.6%, showing strong year-end performance.
```

**What happened:** Gemini read your local file, analyzed the data, and gave you insights.

**Watch for:** `📄 Reading file:` indicator

**What files can Gemini read?**
- ✅ Text files (.txt, .md)
- ✅ CSV files (spreadsheet data)
- ✅ JSON files (structured data)
- ✅ Code files (.py, .js, etc.)

#### 💬 AI Colearning Prompt
> "When Gemini reads a CSV file, what's actually happening behind the scenes? How does it convert rows and columns into understanding that answers business questions?"

---

## Tool 4: Shell Integration — AI-Assisted Terminal Commands

**When to use:** You need to run terminal commands but don't remember the exact syntax, or you want AI to suggest the best approach.

### The AI-Native Way: Ask First, Run Second

**Step 1:** Ask Gemini for the command

In Gemini CLI, ask:

```
I need to find all Excel files modified in the last month. What command should I use?
```

**What you'll see:**
```
> I need to find all Excel files modified in the last month. What command should I use?

To find all Excel files modified in the last 30 days, use this command:

find . -name "*.xlsx" -mtime -30 -type f

Breaking it down:
- find .           → Search in current directory and subdirectories
- -name "*.xlsx"   → Match files ending in .xlsx
- -mtime -30       → Modified within last 30 days
- -type f          → Only files (not directories)

This searches recursively. If you want to search a specific folder instead of
the current one, replace . with the folder path.
```

**Step 2:** Run the command using Shell Mode

Press `!` to enter shell mode in Gemini CLI, then run the command:

```
!find . -name "*.xlsx" -mtime -30 -type f
```

Press `ESC` to exit shell mode and return to Gemini.

---

### Alternative: Direct Shell Commands (When You Know the Command)

If you already know the command you want to run, you can execute it directly in shell mode without asking Gemini first:

1. Press `!` to enter shell mode
2. Type your command: `ls -la`
3. Press `Enter` to execute
4. Press `ESC` to return to Gemini

**When to ask AI first:**
- ✅ You're unsure of the exact syntax
- ✅ You want the safest/best approach
- ✅ You need the command explained before running it
- ✅ Complex tasks (multiple steps, flags, conditions)

**When to run directly:**
- ✅ You know the command and just need quick execution
- ✅ Simple commands like `ls`, `pwd`, `cd`
- ✅ You've run this specific command before

#### 🎓 Expert Insight
> In AI-native development, you don't memorize terminal commands. You ask your AI partner for the right command, understand what it does, then execute. The skill isn't memorization—it's knowing how to describe what you want accomplished and validating the AI's suggestion before running it.

---

## How Tools Work Together

Tools don't work in isolation—Gemini combines them automatically based on your question. Here's what that looks like:

**You ask one question:**
```
Compare Notion and Coda pricing, then tell me which is better for a 20-person startup
```

**Behind the scenes, Gemini automatically:**
1. 🌐 Fetches Notion pricing page
2. 🌐 Fetches Coda pricing page
3. Analyzes both datasets
4. Applies your constraint (20-person startup)
5. Provides recommendation with reasoning

**You see:**
```
> Compare Notion and Coda pricing...

🌐 Fetching https://notion.so/pricing...
🌐 Fetching https://coda.io/pricing...

[Comparison table with both pricing structures]

For a 20-person startup, Coda's Team plan ($10/user = $200/month) offers better
value than Notion's Team plan ($15/user = $300/month) if you need advanced
automations. However, if you prioritize databases and wikis, Notion provides
more robust features at that tier.

Recommendation: Start with Coda to save $1,200/year, migrate to Notion if you
outgrow Coda's database features.

Sources: notion.so/pricing, coda.io/pricing (retrieved 2024-01-14)
```

**The key:** You asked naturally. Gemini orchestrated multiple tools. You got actionable intelligence.

---

## Understanding Errors and Data Privacy

### When Something Goes Wrong: The AI-Native Approach

You'll encounter error messages. Instead of memorizing error codes, **ask your AI to explain and fix them.**

**Example:** You get this error:
```
ERROR: File not found: sales.txt
```

**Ask Gemini:**
```
I got this error: "File not found: sales.txt". What does this mean and how do I fix it?
```

**Gemini will explain:**
- The file doesn't exist in the current directory
- Show you how to check where you are (`pwd`)
- Suggest how to find the file or create it
- Explain the next steps

**Common tool indicators you'll see:**
- ✅ `🔍 Searching...` or `🌐 Fetching...` → Normal, tool is working
- ✅ `Sources: [URLs]` → Good! You can verify the data
- ⚠️ `ERROR:` → Something failed, ask AI to explain
- ⚠️ `Rate limited` → You're requesting too fast, wait a moment

**The pattern:** Don't troubleshoot alone. Copy the error, paste it to Gemini, ask what happened and how to fix it.

---

### 🔐 Privacy & Data Safety: Critical Rules

When tools access data, you need to understand what's being shared:

**What Stays Private:**
- ✅ **File reading** → Your files stay on your computer, only you and Gemini see them
- ✅ Gemini processes data temporarily, doesn't permanently store your file contents

**What Goes to the Web:**
- ⚠️ **Web search/fetch** → Your queries may be logged (like Google searches)
- ⚠️ **Shell commands** → Execute on your computer but Gemini sees the commands

**Never Ask AI to Access:**
- 🚫 Files with passwords, API keys, or secrets
- 🚫 Personal Identifiable Information (PII): SSN, medical records, financial data
- 🚫 Private account pages (email, bank, social media logged-in views)
- 🚫 Customer data (GDPR/CCPA violations)
- 🚫 Confidential business documents

**Safe to Use:**
- ✅ Public websites (pricing pages, documentation, news)
- ✅ Your own files with test/anonymized data
- ✅ General searches ("industry trends 2024" not "my company's confidential strategy")

**Rule of thumb:** If you wouldn't share it in a public coffee shop, don't share it with AI.

#### 🤝 Practice Exercise
> **Ask your AI**: "What are the privacy risks when I ask you to fetch a pricing page from a competitor's website? What data is shared and what stays private?"

**Expected outcome:** Your AI will explain what happens during web fetching, what the website sees (a request, but not your identity), and how to stay safe.

---

## Try With AI: Your First Multi-Tool Workflow

Now that you've seen each tool individually, try this complete workflow combining all three tools.

### Real-World Scenario: Product Pricing Research

You're launching a new SaaS product and need to research competitor pricing. Here's a complete workflow:

**Step 1: Search for Market Overview**
```
Search for SaaS pricing trends in project management tools for 2024
```

Watch for: `🔍 Searching...` — Gemini finds industry trends across multiple sources

---

**Step 2: Fetch Specific Competitor Data**
```
Fetch Monday.com's pricing page and summarize their tiers and features
```

Watch for: `🌐 Fetching...` — Gemini reads the specific pricing page

---

**Step 3: Compare with Another Competitor**
```
Now fetch Asana's pricing and create a comparison table with Monday.com
```

Watch for: Second `🌐 Fetching...` then synthesis of both datasets

---

**Step 4: Analyze Your Own Data**

Create a file called `our_costs.txt`:
```
Development: $8,000/month
Hosting: $1,200/month
Support: $3,500/month
Total: $12,700/month
```

Then ask:
```
Read our_costs.txt. Based on our monthly costs and the competitor pricing you found, what should our pricing strategy be to achieve 40% profit margin?
```

Watch for: `📄 Reading file...` then strategic analysis combining all data

---

**Step 5: Get Strategic Recommendation**
```
Based on everything we've researched, what pricing tier structure would you recommend and why?
```

Watch for: Synthesis of all previous data (no new tool use, pure analysis)


