# Reactive LLM Opinion Model
This model tests **Mesa 4.0 Signals** for LLM agent triggers.

### Why this matters
To make Mesa-LLM production-ready, we must reduce unnecessary LLM API calls. 
This model proves that agents can remain "idle" until a specific signal is emitted, 
drastically cutting costs and latency.

### Learnings & Friction
- Hallucination: Most LLMs still try to use `self.model.schedule.add()`.
- Solution: My GSoC project will provide the `llms.txt` context to stop this.