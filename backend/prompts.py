def create_adaptive_prompt(extracted_text, weak_areas):
    # Inject user history to make the learning experience "adaptive"
    weak_topics = ", ".join([item['topic'] for item in weak_areas])
    return f"""
    You are an expert tutor. 
    Notes: {extracted_text}
    The student is weak in: {weak_topics}. 
    Please generate a simplified explanation and 3 quiz questions focused on these weak areas.
    """
