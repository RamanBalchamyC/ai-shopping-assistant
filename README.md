# 🛒 AI Shopping Assistant

An AI-powered shopping agent that lets you search products by text or image, check ratings, and place orders, all through a simple chat interface.

🔗 **Live demo:** https://r-srcgen-ai-engineer10-project-shopping-agentapp-viyzba.streamlit.app/

<!-- Add a screenshot or GIF of the app here -->
<!-- ![App screenshot](docs/screenshot.png) -->

---

## ✨ Features

- **Search by keyword:** find products by name, description or category
- **Smart filters:** filter by maximum price, organic status and minimum rating
- **Search by image:** upload a product photo, and a vision model identifies it and finds similar items in the store
- **Product ratings:** fetches the average rating and review count for each product
- **Checkout:** places an order and saves it to the database, but only after the user explicitly confirms
- **Conversational:** remembers the chat, so you can say "order the second one" after seeing results

---

## ⚙️ How It Works

```
User (text or image)
        ↓
LangChain Agent (Groq LLM)
        ↓
Decides which tool to call
        ↓
┌──────────────────┬──────────────┬──────────┬────────────────────────┐
│ search_products  │ get_rating   │ checkout │ describe_product_image │
│ (SQLite)         │ (Reviews API)│ (SQLite) │ (Vision model)         │
└──────────────────┴──────────────┴──────────┴────────────────────────┘
        ↓
LLM combines results
        ↓
Response in Streamlit chat UI
```

**Text search flow:** search products → get ratings → filter → show a numbered list → wait for confirmation → checkout

**Image search flow:** analyze image → extract product type and organic status → search products → continue as above

---

## 🧰 Tech Stack

| Layer | Tools |
|---|---|
| Agent framework | LangChain (`create_agent`) |
| LLM and vision | Groq (Qwen) |
| Database | SQLite |
| UI | Streamlit |
| Deployment | Streamlit Community Cloud |
| Package manager | uv |

---

## 📁 Project Structure

```
src/gen_ai_engineer/10_project_shopping_agent/
├── app.py              # Streamlit chat UI
├── shopping_agent.py   # Agent, tools and system prompt
├── reviews_api.py      # Product rating lookup
└── store.db            # SQLite database (products and orders)
```

---

## 🚀 Getting Started

**1. Clone the repo**

```bash
git clone https://github.com/RamanBalchamyC/ai-shopping-assistant.git
cd ai-shopping-assistant
```

**2. Install dependencies**

```bash
uv sync
```

**3. Add your API key**

Create a `.env` file in the project folder:

```
GROQ_API_KEY=your_groq_api_key_here
```

You can get a free key from [Groq Console](https://console.groq.com/keys).

**4. Run the app**

```bash
uv run streamlit run src/gen_ai_engineer/10_project_shopping_agent/app.py
```

---

## 💬 Example Prompts

- `I want organic honey under $15 with 4+ rating`
- `Show me organic oils with 4.5+ rating and less than $20`
- `Order the first one`
- Upload a product photo in the sidebar and click **Find similar products**

---

## 🙏 Acknowledgements

Built as part of the [Agentic AI Crash Course](https://www.youtube.com/watch?v=D74el9mvNak) by [Codebasics](https://codebasics.io/) (Dhaval Patel).