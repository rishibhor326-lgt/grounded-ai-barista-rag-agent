# Grounded AI Coffee Barista ☕

A grounded AI recommendation agent built with **Google ADK, Gemini, Streamlit, and Google Cloud Run**.

The goal of this project was to understand how an AI agent can generate useful recommendations while staying grounded in a real data source instead of inventing unavailable products.

## Problem

Generative AI models can sometimes provide confident but incorrect recommendations.

For a real business application, this can create trust issues.

This project addresses that by connecting the AI agent to a real coffee menu and instructing it to recommend only items available in the retrieved data.

## What the Agent Can Do

- Recommend drinks and pastries based on customer preferences
- Handle dairy-free and allergen-related requests
- Avoid recommending products that are not available
- Suggest valid alternatives from the menu
- Maintain conversation history during the user session

## Example

**User:**  
`Do you have a## Screenshots

### Grounded Recommendation
![Grounded Recommendation](screenshots/grounded-recommendation.png)

### Dietary Recommendation
![Dietary Recommendation](screenshots/dietary-recommendation.png)

### Cloud Run Deployment
![Cloud Run Deployment](screenshots/cloud-run-deployment.png) matcha frappuccino?`

**Agent:**  
Explains that the product is not available and recommends an existing menu item instead.

This demonstrates **grounding and hallucination control**.

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
Gemini
  ↓
Grounded Response
