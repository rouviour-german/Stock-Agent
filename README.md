# 🚀 StockAgent — The AI That Thinks Like a Hedge Fund

> **"We didn't build a trading bot. We built a virtual Wall Street."**

[![arXiv](https://img.shields.io/badge/arXiv-2407.18957-b31b1b.svg?style=flat-square)](https://arxiv.org/pdf/2407.18957)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=flat-square&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](LICENSE)

---

## 🧠 What Is StockAgent?

**StockAgent** is a research-grade, multi-agent AI system that simulates a **fully functional stock market** — where every trader is powered by a Large Language Model (LLM).

Imagine 50 AI investors, each with a unique personality —*Conservative*, *Aggressive*, *Balanced*, or *Growth-Oriented*— making real-time decisions about buying, selling, borrowing, and forecasting. No human input. No pre-scripted behavior. Pure emergent market dynamics driven by GPT-4 or Gemini.

This is not a backtest. This is a **living simulation**.

> 📄 Research Paper: [When AI Meets Finance — arXiv:2407.18957](https://arxiv.org/pdf/2407.18957)

---

## 🌐 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     STOCKAGENT WORLD                        │
│                                                             │
│  ┌──────────────┐   ┌──────────────┐   ┌────────────────┐  │
│  │  AGENT POOL  │   │  SECRETARY   │   │  STOCK ENGINE  │  │
│  │  50 LLM      │◄──►  (Validator) │   │  Price Update  │  │
│  │  Investors   │   │  JSON Parser │   │  Deal Engine   │  │
│  └──────┬───────┘   └──────────────┘   └───────┬────────┘  │
│         │                                       │           │
│  ┌──────▼───────────────────────────────────────▼────────┐  │
│  │              SIMULATION ORCHESTRATOR                  │  │
│  │  Initial → Trading → Post-Trading → Special Events    │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 4-Phase Simulation Cycle
| Phase | Description |
|-------|-------------|
| 🟢 **Initial Phase** | Agents are initialized with random portfolios, cash, and debt |
| 📈 **Trading Phase** | 3 sessions/day — agents buy, sell, or hold based on LLM reasoning |
| 📊 **Post-Trading Phase** | Financial reports, forum messages, price updates |
| ⚡ **Special Events Phase** | Random macro events (rate cuts, policy shifts) shake the market |

---

## ✨ Key Features

- 🤖 **Multi-Agent LLM Trading** — 50 autonomous AI agents with distinct investor personalities
- 🏦 **Realistic Credit System** — Agents take loans (1/2/3 month), pay interest, and go bankrupt
- 📰 **Information Ecosystem** — Daily forum discussions, quarterly earnings reports, macro events
- 🔥 **Emergent Market Behavior** — Price discovery through real bid/ask matching
- 🛡️ **Zero Data Leakage** — Simulation runs forward only; no future data injected
- 🔌 **Dual LLM Support** — Plug in GPT-4, GPT-3.5, Gemini Pro, or any compatible model
- 📉 **Bankruptcy Mechanics** — Agents liquidate positions and exit the market when insolvent
- 📋 **Full Audit Trail** — Every trade, loan, and decision logged to Excel + console

---

## ⚡ Quickstart

### 1. Set Up the Environment

```bash
# Create isolated Python environment
conda create --name stockagent python=3.9
conda activate stockagent

# Install PromptCoder (required dependency)
git clone https://github.com/dhh1995/PromptCoder
cd PromptCoder
pip install -e .
cd ..

# Clone and install StockAgent
git clone <This Github Project>
cd Stockagent
pip install -r requirements.txt
```

### 2. Configure Your API Keys

**Using OpenAI (GPT-4 / GPT-3.5):**
```bash
# Windows PowerShell
$env:OPENAI_API_KEY = "your-openai-api-key"

# Linux / macOS
export OPENAI_API_KEY="your-openai-api-key"
```

**Using Google Gemini:**
```bash
# Windows PowerShell
$env:GOOGLE_API_KEY = "your-google-api-key"

# Linux / macOS
export GOOGLE_API_KEY="your-google-api-key"
```

> ⚠️ **Security Note:** Never hardcode API keys in `util.py`. Always use environment variables or a `.env` file.

### 3. Launch the Simulation

```bash
# Default: Gemini Pro (264 trading days, 50 agents)
python main.py

# With GPT-4
python main.py --model gpt-4

# With GPT-3.5 Turbo
python main.py --model gpt-3.5-turbo

# With Gemini Pro
python main.py --model gemini-pro
```

---

## ⚙️ Configuration (`util.py`)

You can customize the simulation parameters to run shorter experiments or stress-test different market conditions.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `AGENTS_NUM` | `50` | Number of AI traders in the market |
| `TOTAL_DATE` | `264` | Total trading days (~1 full year) |
| `TOTAL_SESSION` | `3` | Trading sessions per day |
| `STOCK_A_INITIAL_PRICE` | `30` | Starting price of Stock A |
| `STOCK_B_INITIAL_PRICE` | `40` | Starting price of Stock B |
| `MAX_INITIAL_PROPERTY` | `5,000,000` | Max starting wealth per agent (¥) |
| `MIN_INITIAL_PROPERTY` | `100,000` | Min starting wealth per agent (¥) |
| `LOAN_RATE` | `[2.7%, 3.0%, 3.3%]` | Interest rates by loan term |

### Special Market Events

StockAgent ships with two pre-configured macro shocks:

| Event | Day | Description |
|-------|-----|-------------|
| 🏛️ **Reserve Ratio Cut** | Day 78 | Government cuts reserve requirement → interest rates drop |
| 📈 **Rate Hike** | Day 144 | Government raises interest rates → tightening credit |

---

## 🧬 Agent Personalities

Each agent is randomly assigned one of 4 trading personalities that influence their LLM prompts:

| Personality | Behavior |
|------------|----------|
| 🛡️ **Conservative** | Risk-averse, prefers cash, avoids heavy leverage |
| ⚔️ **Aggressive** | High-risk, max leverage, chases momentum |
| ⚖️ **Balanced** | Diversified approach, moderate debt levels |
| 🌱 **Growth-Oriented** | Focus on long-term value and earnings reports |

---

## 📁 Project Structure

```
StockAgent/
│
├── main.py             # 🎯 Simulation orchestrator — start here
├── agent.py            # 🤖 Agent class — LLM decision-making engine
├── secretary.py        # 🔍 Response validator — parses & validates LLM JSON
├── stock.py            # 📈 Stock class — price tracking & financial reports
├── util.py             # ⚙️  Global config — parameters, events, constants
├── record.py           # 📋 Data recorder — Excel output for all trades/agents
│
├── prompt/
│   └── agent_prompt.py # 💬 All LLM prompt templates (buy/sell/loan/forum)
│
├── log/
│   └── custom_logger.py # 📝 Colored console + file logging
│
├── fig/                # 📊 Architecture diagrams & workflow figures
└── requirements.txt    # 📦 Python dependencies
```

---

## 📊 Research Insights

StockAgent has been used to study:

- 🔬 **How macro policy changes** (rate cuts, hikes) propagate through AI-driven markets
- 🧪 **How different LLM models** (GPT-4 vs Gemini) differ in trading behavior
- 💡 **How investor personality** affects portfolio outcomes over 264 trading days
- 🌊 **How information spreads** — forum messages, earnings reports → price discovery
- 📉 **Bankruptcy cascades** — what happens when leverage meets a rate shock

---

## 📦 Dependencies

```
openai==1.13.3        # GPT access
google-generativeai   # Gemini access
pandas==1.3.5         # Data handling & Excel output
tiktoken==0.5.1       # Token counting for GPT
requests==2.31.0      # HTTP client
colorama==0.4.4       # Colored terminal output
protobuf==3.20.3      # Protocol buffer support
```

---

## 📖 Citation

If StockAgent contributes to your research, please cite the original paper:

```bibtex
@article{zhang2024ai,
  title     = {When AI Meets Finance (StockAgent): Large Language Model-based 
               Stock Trading in Simulated Real-world Environments},
  author    = {Zhang, Chong and Liu, Xinyi and Jin, Mingyu and Zhang, Zhongmou 
               and Li, Lingyao and Wang, Zhengting and Hua, Wenyue and Shu, Dong 
               and Zhu, Suiyuan and Jin, Xiaobo and others},
  journal   = {arXiv preprint arXiv:2407.18957},
  year      = {2024}
}
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## ⭐ Star History

If this project helped your research or gave you ideas, drop a ⭐ — it genuinely helps.

---

<p align="center">
  <b>Built at the intersection of AI × Finance × Simulation</b><br/>
  <i>StockAgent — Where Large Language Models Meet the Market</i>
</p>

---

---

---

## Author & Contact

- **GitHub:** [@rouviour-german](https://github.com/rouviour-german)
- **Email:** [rouviourgermanmeetings@gmail.com](mailto:rouviourgermanmeetings@gmail.com)
- **Profile:** https://github.com/rouviour-german

