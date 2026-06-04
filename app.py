import sys
import gradio as gr

sys.stdout.reconfigure(encoding="utf-8")

from generate import ask


def handle_query(question: str):
    if not question.strip():
        return "", ""
    result = ask(question)
    sources = "\n".join(f"• {s}" for s in result["sources"])
    return result["answer"], sources


UW_PURPLE = "#362161"
UW_GOLD = "#A8915B"
UW_GOLD_BRIGHT = "#e8d5a3"

css = f"""
    body, .gradio-container {{ background-color: {UW_PURPLE} !important; }}
    h1, h2, h3, p, label, .label-wrap span {{ color: {UW_GOLD_BRIGHT} !important; }}
    .gr-button-primary {{
        background-color: {UW_GOLD} !important;
        color: {UW_PURPLE} !important;
        font-weight: bold !important;
        border: none !important;
    }}
    .gr-button-primary:hover {{
        background-color: {UW_GOLD_BRIGHT} !important;
    }}
    textarea, input[type="text"] {{
        background-color: #3a2266 !important;
        color: {UW_GOLD_BRIGHT} !important;
        border: 1px solid {UW_GOLD} !important;
    }}
    .block, .form {{ background-color: #3a2266 !important; border-color: {UW_GOLD} !important; }}
    .example-set button {{
        background-color: #3a2266 !important;
        color: {UW_GOLD_BRIGHT} !important;
        border: 1px solid {UW_GOLD} !important;
    }}
    footer, .built-with {{ display: none !important; }}
    #settings-btn {{ display: none !important; }}
"""

with gr.Blocks(title="Unofficial Guide to UW Seattle") as demo:
    gr.Markdown("# 🐾 Unofficial Guide to UW Seattle")
    gr.Markdown(
        "Ask anything about UW Seattle — dorms, dining, classes, costs, things to do. "
        "Answers are sourced from real Reddit threads and official UW documents."
    )

    with gr.Row():
        inp = gr.Textbox(
            label="Your question",
            placeholder="e.g. What dorm is best for meeting people?",
            lines=2,
            scale=4,
        )
        btn = gr.Button("Ask", variant="primary", scale=1)

    answer_box = gr.Textbox(label="Answer", lines=8, interactive=False)
    sources_box = gr.Textbox(label="Retrieved from", lines=4, interactive=False)

    btn.click(handle_query, inputs=inp, outputs=[answer_box, sources_box])
    inp.submit(handle_query, inputs=inp, outputs=[answer_box, sources_box])

demo.launch(css=css)
