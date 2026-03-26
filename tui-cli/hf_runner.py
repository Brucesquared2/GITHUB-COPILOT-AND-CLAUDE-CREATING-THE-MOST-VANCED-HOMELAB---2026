def run_huggingface_model():
    try:
        from transformers import pipeline
        clf = pipeline("sentiment-analysis")
        out = clf("AI will change everything.")
        return f"HuggingFace Output: {out}"
    except Exception as e:
        return f"[HuggingFace Error]: {e}"
