# Grounded AI Coffee Barista ☕

A grounded AI recommendation agent built with **Google ADK, Gemini, Streamlit, and Google Cloud Run**.

This project explores a practical GenAI problem:

> How can an AI agent provide useful recommendations while staying grounded in a real data source instead of inventing unavailable products?

The result is an AI Barista that retrieves menu information before generating recommendations.

---

## Problem

Large language models can sometimes produce confident but incorrect answers.

For business applications, this can create trust issues.

This project reduces that risk by grounding the AI agent in a real coffee menu and instructing it to recommend only items available in the retrieved data.

---

## What the Agent Can Do

- Recommend drinks and pastries based on customer preferences
- Handle dairy-free and allergen-related requests
- Avoid recommending unavailable products
- Suggest valid alternatives from the menu
- Maintain conversation history during a browser session
- Generate responses grounded in retrieved menu data

---

## Grounding in Action

**User:**  
`Recommend something strong and warm.`

**Agent:**  
Recommends **Espresso Solo**, which exists in the menu and matches the strong + hot preference.

**User:**  
`Do you have a matcha frappuccino?`

**Agent:**  
Explains that the item is not available and suggests an existing menu option instead.

**User:**  
`I'm lactose intolerant, what can I get?`

**Agent:**  
Uses the menu's dairy-free tags and allergen information to recommend suitable options.

This demonstrates **grounding, hallucination control, and context-aware recommendations**.

---

## Screenshots

### Grounded Recommendation

![Grounded Recommendation](screenshots/%E2%98%95%20Coffee%20Shop%20-%20Barista%20Bot.png)

### Dietary Recommendation

![Dietary Recommendation](screenshots/%E2%98%95%20Coffee%20Shop%20-%20Barista%20Bot%202.png)

### Cloud Run Deployment

![Cloud Run Deployment](screenshots/GenAI%20Productivity%E2%80%A6%20%E2%80%93%20Google%20Cloud%20console.png)

---

## Architecture

```text
User
  ↓
Streamlit Interface
  ↓
Google ADK Agent
  ↓
get_menu() Retrieval Tool
  ↓
menu.json
  ↓
Retrieved Menu Context
  ↓
Gemini
  ↓
Grounded Response
