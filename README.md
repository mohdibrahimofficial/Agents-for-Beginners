# 🧠 Agents for Beginners

Welcome to **Agents for Beginners** — a simple, no-hype repository for learning how to build basic AI agents using **pure Python**.

This project is inspired by and made possible thanks to this wonderful tutorial:  
👉 [Thank you for this amazing guide!](https://www.youtube.com/watch?v=bZzyPscbtI8)

---

## 📦 Repository Structure

### 🔰 Beginner

Designed for those just starting out. Each folder here introduces foundational agent concepts:

- **`basic`**: The simplest agent examples to get started.
- **`structured_outputs`**: Learn how agents can return structured information.
- **`retrieval`**: Integrating search and knowledge retrieval into agents.
- **`tools`**: How agents can use tools (like calculators or APIs).

### ⚙️ Workflow Patterns

For exploring more advanced agent workflows:

- **`prompt_chaining`**: Learn how to chain prompts for complex tasks.
- **`routing`**: Direct tasks to the appropriate agent or module.
- **`parallelization`**: Running agent tasks concurrently.
- **`orchestra`**: Coordinating multiple agents in a structured pipeline.

---

## ⚙️ Requirements

To run this project, you'll need:

- **Python 3.9+**
- An **OpenAI** or **Azure OpenAI** API key

---

## 🚀 Getting Started

Follow these steps to set up the project:

```bash
1. Clone the Repository
git clone https://github.com/mohdibrahimofficial/Agents-for-Beginners.git
cd Agents-for-Beginners
```
2. Set Up Environment Variables
```bash
Rename .env.example to .env and add your OpenAI/Azure OpenAI API key inside it.
```
3. Create and Activate a Virtual Environment
```bash
python -m venv venv

# Activate it
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```
4. Install Requirements
```bash
pip install -r requirements.txt
```