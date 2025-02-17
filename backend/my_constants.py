GEMINI_PROMPT = """
**Instructions:**
You are provided with a meeting transcript below.  Please process this transcript and generate a comprehensive summary, including the following sections:

**1. Executive Summary:**  A concise overview of the meeting's key topics, decisions, and outcomes (approximately 150-200 words).

**2. Key Discussion Points:**  A bulleted list of the most important topics discussed during the meeting.  Be specific and avoid vague terms.

**3. Actionable Points:** A table outlining specific actions that were agreed upon, including:
    * **Action Item:** A clear description of the task.
    * **Assigned To:** The individual responsible for completing the task.
    * **Due Date:** The deadline for completing the task (if specified).
    * **Status:** (Optional) Include a column for tracking progress (e.g., "Not Started," "In Progress," "Completed").

**4. Sentiment Analysis:** An overall assessment of the meeting's tone and sentiment.  Indicate whether the meeting was generally positive, negative, or neutral.  Provide specific examples from the transcript to support your analysis.  Consider analyzing sentiment at different points in the meeting if there are notable shifts.

**5. Decisions Made:**  A clear list of all decisions that were made during the meeting.

**6. Next Steps:**  Outline the planned next steps following the meeting.

**7. Attendees (Optional):** If attendee information is available in the transcript, list the attendees.  If not, mention the approximate number of participants and their roles if discernible (e.g., "marketing team," "engineering leads").

**8. Challenges/Obstacles (Optional):** If any challenges or obstacles were identified during the meeting, list them here.

**9. Open Questions/Unresolved Issues (Optional):**  List any questions or issues that were raised but not resolved during the meeting.

**10.  Detailed Summary (Optional):**  A more detailed summary of the meeting, including more context and supporting information for the key discussion points (approximately 300-500 words).  This section should provide a more in-depth narrative of the meeting's flow.

**Meeting Transcript:**
{}

"""