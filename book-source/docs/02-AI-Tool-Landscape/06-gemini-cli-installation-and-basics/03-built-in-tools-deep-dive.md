---
sidebar_position: 3
title: "What Gemini Can Do: Built-In Tools in Action"
cefr_level: A2
proficiency: Beginner
teaching_stage: 2
stage_name: "AI Collaboration"
stage_description: "Students actively use AI tools and understand their capabilities"
cognitive_load:
  concepts_count: 7
  a2_compliant: true
  scaffolding_level: "Heavy"
learning_objectives:
  - id: LO1
    description: "Identify the four built-in tools Gemini uses (Google Search, File Operations, Shell, Web Fetch)"
    bloom_level: "Remember"
  - id: LO2
    description: "Recognize visual indicators showing which tool Gemini is using"
    bloom_level: "Understand"
  - id: LO3
    description: "Explain when Gemini chooses each tool based on query context"
    bloom_level: "Understand"
  - id: LO4
    description: "Apply tools by crafting queries that trigger appropriate tool usage"
    bloom_level: "Apply"
  - id: LO5
    description: "Analyze tool output to verify Gemini used correct tool for the task"
    bloom_level: "Analyze"
  - id: LO6
    description: "Practice using tools through realistic developer scenarios"
    bloom_level: "Apply"
  - id: LO7
    description: "Evaluate when to use Gemini's tools vs manual methods for development tasks"
    bloom_level: "Evaluate"
digcomp_mapping:
  - objective_id: LO1
    competency_area: "1. Information and Data Literacy"
    competency: "1.1 Browsing, searching and filtering data, information and digital content"
  - objective_id: LO2
    competency_area: "1. Information and Data Literacy"
    competency: "1.2 Evaluating data, information and digital content"
  - objective_id: LO3
    competency_area: "5. Problem Solving"
    competency: "5.2 Identifying needs and technological responses"
  - objective_id: LO4
    competency_area: "3. Digital Content Creation"
    competency: "3.4 Programming"
  - objective_id: LO5
    competency_area: "1. Information and Data Literacy"
    competency: "1.2 Evaluating data, information and digital content"
  - objective_id: LO6
    competency_area: "3. Digital Content Creation"
    competency: "3.4 Programming"
  - objective_id: LO7
    competency_area: "5. Problem Solving"
    competency: "5.1 Solving technical problems"
---

# What Gemini Can Do: Built-In Tools in Action

You're building a web application and need to check the latest React documentation for server components. You could:
- Open a browser
- Search Google
- Navigate through docs
- Find the right section
- Read and synthesize information

Or you could just ask Gemini:

```
What are the new features in React 19?
```

Within seconds, Gemini searches the web, finds official sources, and gives you a clear answer with citations. **This is the power of built-in tools** - your AI doesn't just answer from memory, it actively reaches out to get current information, read your files, and execute commands.

In this lesson, you'll learn what Gemini can actually do for you as a developer.

---

## Tools Activate Automatically

Here's the key insight that changes everything: **You don't invoke tools manually.** You ask naturally, and Gemini decides which tool to use.

When you ask Gemini a question, it analyzes what you need:
- Current information from the web? → Google Search tool activates
- Read a file in your project? → File operations tool activates
- Run a terminal command? → Shell integration activates
- Fetch a specific webpage? → Web fetch tool activates

You'll know a tool is active when you see visual indicators:
- 🔍 **Searching the web...**
- 📁 **Reading file...**
- ⚡ **Running command...**
- 🌐 **Fetching webpage...**

Let's see each tool in action.

---

## Tool 1: Google Search — Getting Current Information

**When Gemini uses this**: You need current information from across the web, and you don't know which specific site has it.

### Example: Checking Latest Framework Versions

You ask Gemini:

```
What's the latest stable version of Node.js?
```

**What you'll see:**

```
> What's the latest stable version of Node.js?

🔍 Searching the web...

The latest stable version of Node.js is 20.11.0 (LTS), released January 2025.

Key features in this release:
- Performance improvements for module loading (up to 15% faster)
- Updated V8 engine to version 11.8
- Security patches for CVE-2024-27980 and CVE-2024-27982
- Improved support for ES modules

The next LTS release (version 22) is planned for April 2025.

Sources:
- nodejs.org (official release page)
- GitHub nodejs/node releases
```

**What happened**: Gemini recognized you needed current version information (not in its training data), activated Google Search, found official sources, and synthesized the answer.

### When Google Search Activates

Gemini uses Google Search when you ask about:
- **Current versions**: "What's the latest TypeScript version?"
- **Recent events**: "What breaking changes were in Python 3.13?"
- **Live data**: "What's the current best practice for React state management?"
- **Comparisons**: "Compare Next.js vs Remix for 2025"
- **Trends**: "What are developers saying about Bun.js adoption?"

---

## Tool 2: File Operations — Reading Your Project Files

**When Gemini uses this**: You need Gemini to read or analyze files in your current project.

### Example: Analyzing Your Dependencies

You ask Gemini:

```
Read my package.json and list my dependencies
```

**What you'll see:**

```
> Read my package.json and list my dependencies

📁 Reading package.json...

Your project has 8 dependencies:

**Production Dependencies:**
- react: ^18.2.0
- react-dom: ^18.2.0
- next: ^14.0.4
- axios: ^1.6.2

**Development Dependencies:**
- typescript: ^5.3.3
- eslint: ^8.56.0
- @types/react: ^18.2.47
- @types/node: ^20.10.6

You're using React 18 with Next.js 14. Would you like me to check if there
are any security vulnerabilities in these versions?
```

**What happened**: Gemini accessed your project's package.json file, parsed the JSON structure, categorized dependencies, and offered a helpful follow-up.

### Example: Understanding Configuration Files

You ask Gemini:

```
Read my .eslintrc.json and explain what rules are enabled
```

**What you'll see:**

```
> Read my .eslintrc.json and explain what rules are enabled

📁 Reading .eslintrc.json...

Your ESLint configuration has these rules enabled:

**Strict Rules:**
- no-unused-vars: Error (prevents unused variables)
- no-console: Warning (alerts on console.log statements)
- eqeqeq: Error (requires === instead of ==)

**TypeScript Rules:**
- @typescript-eslint/no-explicit-any: Error (prevents using 'any' type)
- @typescript-eslint/explicit-function-return-type: Warning

**React Rules:**
- react/prop-types: Off (disabled because you're using TypeScript)
- react-hooks/rules-of-hooks: Error (enforces Hook rules)

This is a fairly strict configuration focused on type safety and avoiding common bugs.
```

**What happened**: Gemini read your configuration file, interpreted the rules, and explained them in plain language.

### When File Operations Activate

Gemini reads files when you ask about:
- **Configuration**: "Show me my .env variables"
- **Code analysis**: "Read main.py and suggest improvements"
- **Documentation**: "Analyze my README.md and suggest additions"
- **Data files**: "Read data.json and count how many users we have"
- **Logs**: "Check error.log and tell me what's failing"

---

## Tool 3: Shell Integration — Running Terminal Commands

**When Gemini uses this**: You need to execute terminal commands and get the results.

### Example: Checking Your Environment

You ask Gemini:

```
Check what Git branch I'm currently on
```

**What you'll see:**

```
> Check what Git branch I'm currently on

⚡ Running: git branch --show-current

You're currently on the 'feature/user-authentication' branch.

Would you like me to:
- Show you the status of uncommitted changes?
- List recent commits on this branch?
- Compare this branch to main?
```

**What happened**: Gemini executed the `git branch --show-current` command, captured the output, and offered relevant next steps.

### Example: Checking Versions

You ask Gemini:

```
What Node.js and npm versions am I running?
```

**What you'll see:**

```
> What Node.js and npm versions am I running?

⚡ Running: node --version
⚡ Running: npm --version

You're running:
- Node.js: v20.10.0
- npm: v10.2.3

Both are up-to-date! Node.js 20.10.0 is the current LTS release.
```

**What happened**: Gemini ran both version check commands, compared against current releases (using Google Search), and confirmed your setup is current.

### When Shell Integration Activates

Gemini runs commands when you ask about:
- **System info**: "What's my current directory?"
- **Git operations**: "Show me the last 5 commits"
- **File listings**: "List all .ts files in the src folder"
- **Process checking**: "Is the development server running?"
- **Testing**: "Run npm test and show me the results"

---

## Tool 4: Web Fetch — Retrieving Specific Pages

**When Gemini uses this**: You know the exact URL and want Gemini to fetch and analyze that specific page.

### Example: Getting API Documentation

You ask Gemini:

```
Fetch the Stripe API docs for payment intents and show me a basic example
```

**What you'll see:**

```
> Fetch the Stripe API docs for payment intents and show me a basic example

🌐 Fetching https://stripe.com/docs/api/payment_intents...

Here's how to create a Payment Intent with Stripe:

**Basic Example (Node.js):**

const stripe = require('stripe')('sk_test_...');

const paymentIntent = await stripe.paymentIntents.create({
  amount: 2000,  // $20.00 in cents
  currency: 'usd',
  payment_method_types: ['card'],
  description: 'Software subscription'
});

**Key Parameters:**
- amount: Integer in smallest currency unit (cents for USD)
- currency: Three-letter ISO code ('usd', 'eur', etc.)
- payment_method_types: Array of allowed payment methods

**Next Steps:**
1. Send paymentIntent.client_secret to your frontend
2. Use Stripe.js to complete payment with the client secret
3. Listen for payment_intent.succeeded webhook event

Source: Stripe API Documentation (retrieved January 2025)
```

**What happened**: Gemini fetched the specific Stripe documentation page, extracted the relevant section on Payment Intents, and provided a clear example with explanation.

### Example: Checking Service Pricing

You ask Gemini:

```
Fetch the Vercel pricing page and summarize the free tier
```

**What you'll see:**

```
> Fetch the Vercel pricing page and summarize the free tier

🌐 Fetching https://vercel.com/pricing...

Vercel's Free (Hobby) tier includes:

**Deployments:**
- Unlimited deployments
- Automatic HTTPS and SSL certificates
- Preview deployments for every Git push
- Edge Network (global CDN)

**Resources:**
- 100 GB bandwidth per month
- 6,000 build execution minutes per month
- Serverless functions: 100 GB-hours per month
- Edge functions: 100,000 invocations per month

**Features:**
- Custom domains (unlimited)
- Automatic CI/CD from Git
- Web Analytics (basic)
- DDoS mitigation

**Limitations:**
- 1 concurrent build at a time
- Community support only
- No team collaboration features

Perfect for personal projects, prototyping, and learning. Upgrade to Pro ($20/month)
for team features and higher limits.
```

**What happened**: Gemini fetched the Vercel pricing page, extracted free tier details, organized them clearly, and provided upgrade context.

### When Web Fetch Activates

Gemini fetches specific pages when you ask about:
- **Documentation**: "Get the FastAPI authentication docs"
- **Pricing**: "Fetch AWS S3 pricing and explain storage costs"
- **Release notes**: "Get the Python 3.13 release notes from python.org"
- **Changelogs**: "Fetch the Next.js 14 changelog"
- **Specific guides**: "Get the React Router tutorial from their docs"

---

## How Gemini Decides Which Tool to Use

Understanding the decision logic helps you craft better queries:

| Your Need | Tool Gemini Uses | Example Query |
|-----------|------------------|---------------|
| Latest version/current info | 🔍 Google Search | "What's new in Python 3.13?" |
| Read project files | 📁 File Operations | "Show my .env variables" |
| Check system state | ⚡ Shell Integration | "What's my current directory?" |
| Specific documentation | 🌐 Web Fetch | "Get FastAPI docs for authentication" |
| Compare multiple sources | 🔍 Google Search | "Compare React vs Vue in 2025" |
| Analyze your code | 📁 File Operations | "Read app.py and suggest improvements" |
| Git operations | ⚡ Shell Integration | "Show uncommitted changes" |
| API reference | 🌐 Web Fetch | "Fetch OpenAI API pricing from their site" |

**The Pattern**:
- **Broad/current/comparative** → Google Search
- **Your project files** → File Operations
- **Commands to execute** → Shell Integration
- **Exact URL to retrieve** → Web Fetch

---

## Recognizing When Tools Are Active

As you use Gemini, watch for these indicators:

### Visual Indicators

**Status messages appear before results:**
```
🔍 Searching the web...
📁 Reading package.json...
⚡ Running: git status
🌐 Fetching https://docs.python.org/3.13/...
```

### Source Citations

When Gemini uses tools, it cites sources:
```
Sources:
- nodejs.org (official release page)
- GitHub nodejs/node releases
- Retrieved: January 17, 2025
```

### Structured Output

Tool responses often have clear structure:
```
Your project has 8 dependencies:

Production Dependencies:
- react: ^18.2.0
- next: ^14.0.4

Development Dependencies:
- typescript: ^5.3.3
```

### Command Echo

Shell integration shows the exact command run:
```
⚡ Running: node --version

v20.10.0
```

**Why this matters**: Knowing which tool activated helps you verify Gemini did what you expected and learn when each tool is appropriate.

---

## Real-World Developer Scenarios

Here's how tools work together in actual development workflows:

### Scenario 1: Starting a New Project

**You**: "Create a new Next.js project called 'my-store' and show me the generated file structure"

**Gemini**:
```
⚡ Running: npx create-next-app@latest my-store

✓ Next.js project 'my-store' created successfully!

📁 Reading my-store directory...

Your project structure:
my-store/
├── app/
│   ├── page.tsx (home page)
│   ├── layout.tsx (root layout)
│   └── globals.css
├── public/ (static assets)
├── package.json
├── next.config.js
├── tsconfig.json
└── README.md

The project is using:
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS (configured)
- ESLint

Ready to start! Run 'cd my-store && npm run dev' to launch the dev server.
```

**Tools used**: Shell (create project), File Operations (read structure), Google Search (verify Next.js version)

---

### Scenario 2: Debugging an Error

**You**: "Read my error.log file and tell me what's causing the crash"

**Gemini**:
```
📁 Reading error.log...

I found the issue! Your application is crashing because of this error:

Error: Cannot find module 'dotenv'
at Function.Module._resolveFilename (node:internal/modules/cjs/loader:1039:15)

**Root Cause**:
You're trying to use environment variables with dotenv, but the package isn't installed.

**Fix**:
⚡ Running: npm list dotenv

dotenv is not installed.

**Solution**:
Run: npm install dotenv

Then make sure your code has:
require('dotenv').config();  // CommonJS
// or
import 'dotenv/config';      // ES modules

Would you like me to check if dotenv is in your package.json?
```

**Tools used**: File Operations (read log), Shell (check package), Google Search (verify current dotenv usage patterns)

---

### Scenario 3: Researching Best Practices

**You**: "What are the best practices for React Server Components in 2025?"

**Gemini**:
```
🔍 Searching the web...

Current best practices for React Server Components (2025):

**1. Data Fetching**
- Fetch data directly in Server Components (no useEffect needed)
- Use async/await at component level
- Cache data with React's built-in cache() function

**2. Component Boundaries**
- Server Components by default
- Add 'use client' only when you need:
  - Event handlers (onClick, onChange)
  - Browser APIs (localStorage, window)
  - React hooks (useState, useEffect)

**3. Performance**
- Keep Server Components at the tree root
- Pass Server Components as props to Client Components
- Avoid passing large objects from Server to Client

**4. Patterns to Avoid**
- ❌ Don't fetch data in Client Components if Server Components can do it
- ❌ Don't serialize functions from Server to Client
- ❌ Don't use Server Components inside Client Components (composition is fine)

**Example (Correct)**:
// app/page.tsx (Server Component)
async function Page() {
  const data = await fetch('https://api.example.com/data');
  return <ClientComponent data={data} />;
}

// components/ClientComponent.tsx
'use client';
export function ClientComponent({ data }) {
  const [state, setState] = useState(data);
  // Client-side interactivity here
}

Sources:
- React.dev official documentation
- Next.js 14 documentation
- Vercel blog posts (January 2025)
```

**Tools used**: Google Search (current best practices), Web Fetch (React official docs)

---

### Scenario 4: Checking Your Setup

**You**: "Check my Node.js, npm, and Git versions, then tell me if I need to update anything"

**Gemini**:
```
⚡ Running: node --version
⚡ Running: npm --version
⚡ Running: git --version

Your current versions:
- Node.js: v20.10.0
- npm: v10.2.3
- Git: v2.43.0

🔍 Checking latest releases...

**Status**: ✅ All up-to-date!

- Node.js 20.10.0 is the current LTS release (supported until April 2026)
- npm 10.2.3 is the latest stable version
- Git 2.43.0 is current (released December 2024)

No updates needed. Your development environment is current!
```

**Tools used**: Shell (check versions), Google Search (verify latest releases)

---

### Scenario 5: Understanding API Documentation

**You**: "Fetch the Stripe webhook documentation and explain how to verify webhook signatures"

**Gemini**:
```
🌐 Fetching https://stripe.com/docs/webhooks/signatures...

Here's how to verify Stripe webhook signatures:

**Why Verification Matters**:
Ensures webhook requests actually come from Stripe (not attackers).

**Step-by-Step Verification (Node.js)**:

1. **Get your webhook signing secret** from Stripe Dashboard:
   - Go to Developers → Webhooks
   - Click your endpoint
   - Copy "Signing secret" (starts with whsec_...)

2. **Install Stripe SDK**:
npm install stripe

3. **Verify signature in your webhook handler**:

const stripe = require('stripe')('sk_test_...');

app.post('/webhook', express.raw({type: 'application/json'}), (req, res) => {
  const sig = req.headers['stripe-signature'];
  const endpointSecret = 'whsec_...';  // Your signing secret

  let event;

  try {
    event = stripe.webhooks.constructEvent(req.body, sig, endpointSecret);
  } catch (err) {
    console.log('⚠️ Webhook signature verification failed:', err.message);
    return res.sendStatus(400);
  }

  // Handle verified event
  switch (event.type) {
    case 'payment_intent.succeeded':
      const paymentIntent = event.data.object;
      console.log('💰 Payment succeeded:', paymentIntent.id);
      break;
    default:
      console.log(`Unhandled event type ${event.type}`);
  }

  res.sendStatus(200);
});

**Important**:
- Use express.raw() middleware (not express.json())
- Stripe needs the raw request body to verify signature
- Store endpointSecret in environment variables (.env file)

**Testing Locally**:
Use Stripe CLI to forward webhooks:
stripe listen --forward-to localhost:3000/webhook

Source: Stripe Webhooks Documentation (stripe.com/docs/webhooks)
```

**Tools used**: Web Fetch (Stripe docs), Google Search (current best practices)

---

## Try With AI

Now practice using Gemini's tools with these exercises. Use your preferred AI companion (Gemini CLI or Claude Code) - the prompts work with any tool.

### Prompt 1: Practice Google Search

```
What are the new features in the latest TypeScript version released in 2025?
```

**Expected outcome**: You'll see 🔍 indicator, Gemini searches the web, returns current TypeScript features with version number and sources.

**What to observe**: Notice how Gemini cites multiple sources and synthesizes information from official TypeScript docs and release notes.

---

### Prompt 2: Practice File Operations

```
Read my package.json file and suggest 3 improvements to make my project more maintainable
```

**Expected outcome**: You'll see 📁 indicator, Gemini reads your package.json, analyzes dependencies, scripts, and configuration, then provides specific suggestions based on actual content.

**What to observe**: Gemini references actual values from your file (specific dependencies, versions, scripts) - not generic advice.

---

### Prompt 3: Practice Shell Integration

```
Show me the last 5 git commits in my repository with their commit messages and dates
```

**Expected outcome**: You'll see ⚡ indicator, Gemini runs `git log` command, displays formatted commit history with hashes, messages, authors, and dates.

**What to observe**: Gemini shows the exact command it ran and formats the output in a readable way.

---

### Prompt 4: Practice Web Fetch

```
Fetch the official Python documentation page for asyncio and explain the basic event loop concept
```

**Expected outcome**: You'll see 🌐 indicator, Gemini retrieves docs.python.org page, extracts asyncio event loop explanation, and provides code examples.

**What to observe**: Gemini cites the specific documentation URL and explains concepts in beginner-friendly language while staying accurate to the official docs.

---

### Bonus Challenge: Combine Multiple Tools

```
Check what Node.js version I'm running, then search for the latest LTS version, and tell me if I should upgrade
```

**Expected outcome**: Gemini will use:
1. ⚡ Shell Integration (check your version)
2. 🔍 Google Search (find latest LTS)
3. Analysis (compare and recommend)

**What to observe**: Watch how Gemini chains tools together to answer a complex question that requires both local system info and current web data.

---

## Key Takeaways

You've learned that Gemini CLI has four built-in tools that activate automatically:

1. **🔍 Google Search** - Current information from across the web
2. **📁 File Operations** - Reading and analyzing your project files
3. **⚡ Shell Integration** - Running terminal commands and capturing output
4. **🌐 Web Fetch** - Retrieving specific webpage content

**The Power**: You ask naturally, Gemini decides which tool to use.

**The Skill**: Recognizing when tools are active (visual indicators, citations, command echo) and understanding when each tool is appropriate.

**Next Steps**: In Lesson 4, you'll learn how Gemini manages conversation context so it remembers what you're working on across multiple questions.
