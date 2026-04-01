def export_history_as_txt(history):
    lines = []
    lines.append("Student Learning Assistant - Exported History")
    lines.append("=" * 50)

    for item in history:
        lines.append(f"Timestamp: {item.get('timestamp', '')}")
        lines.append(f"Feature: {item.get('feature', '')}")
        lines.append(f"Input: {item.get('input', '')}")
        lines.append(f"Output: {item.get('output', '')}")
        lines.append("-" * 50)

    return "\n".join(lines)